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
import os
from datetime import date

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

# Estimativa de custo por caso (ordem de grandeza — calibrar no eval com preços
# reais do provedor). Guarda o teto declarado em teto_usd_caso; o Flow aborta ao
# estourar. Mesmo padrão do --max-usd do cérebro.
PRECO_USD_1K_PROMPT = 0.003
PRECO_USD_1K_COMPLETION = 0.015


def estimar_custo_usd(prompt_tokens: int, completion_tokens: int) -> float:
    """Custo estimado em USD a partir de tokens. Pura — testável sem LLM."""
    return (max(prompt_tokens, 0) / 1000.0) * PRECO_USD_1K_PROMPT + \
           (max(completion_tokens, 0) / 1000.0) * PRECO_USD_1K_COMPLETION


@persist()
class PatrimonioFlow(Flow[S.EstadoCaso]):

    # ------------------------------------------------------------ infra por caso

    def _rag_tool(self) -> RagCorpusTool:
        # callback registra no estado todo chunk entregue aos agentes —
        # é o que torna o guardrail anti-citação-órfã verificável.
        # as_of/tenant_id são setados aqui (contexto do caso), NÃO pelo agente:
        # o corpus é filtrado pela data do caso (vigência) e pelo tenant.
        return RagCorpusTool(
            on_retrieve=lambda ids: self.state.chunks_recuperados.extend(ids),
            as_of=self.state.data_caso or None,
            tenant_id=self.state.tenant_id)

    def _cobrar_custo(self, resultado) -> None:
        """Acumula o custo estimado do crew no estado e ABORTA se estourar o teto
        do caso. Guarda de orçamento dentro do Flow (defesa a mais além do BFF)."""
        uso = getattr(resultado, "token_usage", None)
        if uso is None:
            return
        pt = getattr(uso, "prompt_tokens", 0) or 0
        ct = getattr(uso, "completion_tokens", 0) or 0
        self.state.custo_acumulado_usd += estimar_custo_usd(pt, ct)
        if self.state.custo_acumulado_usd > self.state.teto_usd_caso:
            raise RuntimeError(
                f"Teto de custo do caso excedido: "
                f"US$ {self.state.custo_acumulado_usd:.2f} > US$ {self.state.teto_usd_caso:.2f}")

    # ------------------------------------------------------------ etapas

    @start()
    def intake(self):
        """Parser determinístico: respostas do questionário → PerfilEstruturado.
        No protótipo, o perfil chega pronto via kickoff(inputs=...)."""
        self.state.versao_corpus = VERSAO_CORPUS
        # data-de-referência do caso: filtra o corpus por vigência (as_of). Sem
        # data explícita, usa hoje — o caso é sempre avaliado contra a lei vigente.
        if not self.state.data_caso:
            self.state.data_caso = date.today().isoformat()
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
        self._cobrar_custo(resultado)
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
            self._cobrar_custo(resultado)
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
        # marca que o gate humano foi ALCANÇADO — render_final exige isto (o
        # gate é não-burlável: nenhuma minuta sai sem passar por aqui).
        self.state.gate_humano_ok = True
        # o payload de revisão é o mesmo item que a fila assíncrona monta (DRY):
        from patrimonio_flow.hitl import montar_item_revisao
        return montar_item_revisao(self.state)

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
        self._cobrar_custo(resultado)
        self.state.minuta = resultado.tasks_output[0].pydantic
        return self.state.minuta

    @listen(crew_redacao)
    def render_final(self):
        """Determinístico: minuta + trilha (versão do corpus, chunks usados,
        histórico de feedback humano). TODO(Sprint 3): DOCX padrão visual ABBA."""
        # gate não-burlável: nenhuma minuta é renderizada sem o gate humano ter
        # sido alcançado (controle anti-UPL/EOAB). Topologia já garante isto
        # (render_final ← crew_redacao ← "aprovado" ← gate2); a asserção é a trava.
        assert self.state.gate_humano_ok, (
            "Minuta sem gate humano — bloqueado. A saída exige revisão do advogado.")
        from patrimonio_flow.render import minuta_para_docx, trilha_de_auditoria
        m = self.state.minuta
        trilha = trilha_de_auditoria(
            self.state.versao_corpus, len(set(self.state.chunks_recuperados)),
            self.state.custo_acumulado_usd)
        # DOCX opcional: se MINUTA_DIR estiver setado, grava o documento editável.
        # No app (Fase 1) isso é servido ao profissional; sem env, retorna o markdown.
        minuta_dir = os.environ.get("MINUTA_DIR")
        if minuta_dir:
            caminho = os.path.join(minuta_dir, f"{self.state.caso_id or 'minuta'}.docx")
            minuta_para_docx(m, caminho, trilha=trilha)
        return m.corpo_markdown + "\n\n" + m.rodape_obrigatorio + "\n\n---\n" + trilha


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
