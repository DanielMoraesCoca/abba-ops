"""Flow principal — espinha determinística com inteligência onde importa.

Arquitetura (especificacao-agentes.md §1):
  intake → gate1 (código) → Crew Análise → Crew Desenho (+ descarte de fatais)
  → obrigações/cenários (código) → gate2 (@human_feedback, advogado)
  → Crew Redação → render final + trilha de auditoria.

Regras: memória OFF em tudo; dados do caso SÓ no EstadoCaso (@persist);
teto de gasto por caso; PII direta nunca vai ao provedor (hook de redação).
"""

from __future__ import annotations

import json

from crewai.flow.flow import Flow, listen, or_, router, start
from crewai.flow.human_feedback import human_feedback
from crewai.flow.persistence import persist

from patrimonio_flow import schemas as S
from patrimonio_flow.gates import triagem_red_flags
from patrimonio_flow.tools.obrigacoes import montar_pacote_obrigacoes, projetar_cenarios
from patrimonio_flow.tools.rag_corpus import RagCorpusTool

TETO_USD_POR_CASO = 5.0
MAX_CICLOS_REDESENHO = 2
VERSAO_CORPUS = "corpus-v0"  # TODO(Sprint 1): ler do manifesto do corpus


@persist()
class PatrimonioFlow(Flow[S.EstadoCaso]):

    # ------------------------------------------------------------ infra por caso

    def _rag_tool(self) -> RagCorpusTool:
        # callback registra no estado todo chunk entregue aos agentes —
        # é o que torna o guardrail anti-citação-órfã verificável.
        return RagCorpusTool(on_retrieve=lambda ids: self.state.chunks_recuperados.extend(ids))

    # ------------------------------------------------------------ etapas

    @start()
    def intake(self):
        """Parser determinístico: respostas do questionário → PerfilEstruturado.
        No protótipo, o perfil chega pronto via kickoff(inputs=...)."""
        self.state.versao_corpus = VERSAO_CORPUS
        assert self.state.perfil is not None, "kickoff exige inputs com o PerfilEstruturado"
        return self.state.perfil

    @router(intake)
    def gate1_red_flags(self):
        self.state.red_flags = triagem_red_flags(self.state.perfil)
        return "bloqueado" if self.state.red_flags.bloqueado else "liberado"

    @listen("bloqueado")
    def relatorio_bloqueio(self):
        """Determinístico: relatório do porquê + próximo passo humano. Fim da linha automática."""
        report = self.state.red_flags
        linhas = [f"- [{f.codigo}] {f.explicacao} → {f.proximo_passo_humano} "
                  f"(fundamento: {f.fundamento_doc_id})"
                  for f in report.flags if f.severidade == S.Severidade.DURO]
        return ("CASO BLOQUEADO PARA DESENHO AUTOMÁTICO — encaminhar ao advogado.\n"
                + "\n".join(linhas))

    @listen("liberado")
    def crew_analise(self):
        from patrimonio_flow.crews.analise_crew import AnaliseCrew
        crew = AnaliseCrew(self._rag_tool(), self.state.chunks_recuperados)
        resultado = crew.crew().kickoff(inputs={
            "perfil_json": self.state.perfil.model_dump_json(),
        })
        # tasks sequenciais: tributária, sucessória, jurisdições
        outs = [t.pydantic for t in resultado.tasks_output]
        self.state.analise = S.AnaliseJuridica(
            tributaria=outs[0], sucessoria=outs[1], jurisdicoes=outs[2])
        return self.state.analise

    @listen(crew_analise)
    def crew_desenho(self):
        from patrimonio_flow.crews.desenho_crew import DesenhoCrew
        flags_brandos = [f.codigo for f in self.state.red_flags.flags
                         if f.severidade == S.Severidade.BRANDO]
        while True:
            crew = DesenhoCrew(self._rag_tool(), self.state.chunks_recuperados)
            resultado = crew.crew().kickoff(inputs={
                "analise_json": self.state.analise.model_dump_json(),
                "flags_brandos": json.dumps(flags_brandos),
                "perfil_json": self.state.perfil.model_dump_json(),
                "desenhos_json": "",  # preenchido pelo context da 2ª task em runtime
            })
            desenhos: list[S.DesenhoEstrutura] = resultado.tasks_output[0].pydantic.desenhos
            criticas: list[S.CriticaAdversarial] = resultado.tasks_output[1].pydantic.criticas
            for d, c in zip(desenhos, criticas):
                d.critica = c
            sobreviventes = [d for d in desenhos if not d.descartado]
            if len(sobreviventes) >= 2 or self.state.ciclos_redesenho >= MAX_CICLOS_REDESENHO:
                self.state.desenhos = sobreviventes or desenhos  # nunca lista vazia p/ o advogado
                return self.state.desenhos
            self.state.ciclos_redesenho += 1  # reexecuta com a crítica no contexto

    @listen(crew_desenho)
    def obrigacoes_e_cenarios(self):
        """Determinístico — regra, não julgamento."""
        total_ext_usd = sum(a.ordem_grandeza_brl for a in self.state.perfil.patrimonio.ativos
                            if a.jurisdicao.upper() != "BR") / 5.0  # TODO: câmbio real
        self.state.obrigacoes = [montar_pacote_obrigacoes(d, self.state.perfil, total_ext_usd)
                                 for d in self.state.desenhos]
        self.state.cenarios = [c for d in self.state.desenhos
                               for c in projetar_cenarios(d, self.state.perfil, total_ext_usd)]
        return self.state.obrigacoes

    @human_feedback(
        message="Revise a análise, os desenhos e as obrigações deste caso. Aprovar, rejeitar ou pedir revisão?",
        emit=["aprovado", "rejeitado", "revisar"],
        learn=False,  # NUNCA gravar correções em memória adaptativa (LGPD)
    )
    @listen(or_(obrigacoes_e_cenarios, "revisar"))
    def gate2_advogado(self):
        """Gate humano obrigatório. Protótipo: console; piloto: provider assíncrono
        (HumanFeedbackPending + Flow.from_pending/resume). Histórico completo em
        self.human_feedback_history → trilha de auditoria da minuta."""
        return {
            "desenhos": [d.model_dump() for d in self.state.desenhos],
            "obrigacoes": [o.model_dump() for o in self.state.obrigacoes],
        }

    @listen("rejeitado")
    def caso_rejeitado(self):
        return "Caso rejeitado pelo advogado revisor — encerrado com estado persistido."

    @listen("aprovado")
    def crew_redacao(self):
        from patrimonio_flow.crews.redacao_crew import RedacaoCrew
        resultado = RedacaoCrew().crew().kickoff(inputs={
            "caso_json": self.state.model_dump_json(
                include={"perfil", "red_flags", "analise", "desenhos",
                         "obrigacoes", "cenarios", "versao_corpus"}),
            "feedback": json.dumps(self.state.feedback_advogado),
        })
        self.state.minuta = resultado.tasks_output[0].pydantic
        return self.state.minuta

    @listen(crew_redacao)
    def render_final(self):
        """Determinístico: minuta + trilha (versão do corpus, chunks usados,
        histórico de feedback humano). TODO(Sprint 3): DOCX padrão visual ABBA."""
        m = self.state.minuta
        trilha = (f"\n\n---\nTrilha: corpus {self.state.versao_corpus} · "
                  f"{len(set(self.state.chunks_recuperados))} chunks consultados · "
                  f"custo acumulado US$ {self.state.custo_acumulado_usd:.2f}")
        return m.corpo_markdown + "\n\n" + m.rodape_obrigatorio + trilha


def kickoff_exemplo(perfil: S.PerfilEstruturado) -> str:
    flow = PatrimonioFlow()
    return flow.kickoff(inputs={"perfil": perfil.model_dump()})


# --- Entrypoints padrão do CrewAI (registrados em [project.scripts]) --------
# A API do AMP injeta os inputs em runtime (POST /kickoff {"inputs": {...}});
# estas funções existem para a detecção do projeto e o run local via CLI.

def kickoff():
    """Entrypoint padrão. Sem inputs, o intake falha o assert de propósito —
    um caso sempre chega com PerfilEstruturado via a API do AMP."""
    PatrimonioFlow().kickoff()


def plot():
    """Gera o diagrama do Flow (crewai plot)."""
    PatrimonioFlow().plot()
