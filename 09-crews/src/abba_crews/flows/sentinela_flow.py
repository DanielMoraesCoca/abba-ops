"""O Flow da Sentinela — orquestracao deterministica.

Este arquivo pode importar `crewai`; `core/` nao pode. Toda decisao de negocio mora
em `core/`; aqui mora a sequencia.

    abrir_competencia       -> config do cliente + janela de manifestacao
    coletar                 -> adaptador de fonte (sintetico neste marco)
    reconciliar_competencia -> core/reconciliacao (+ creditabilidade). Zero LLM.
    decidir_rota            -> sem_divergencia | rotina | julgamento (M3b)
    dossie_conforme         -> core/dossie, sempre RASCUNHO
    dossie_rotina           -> idem, quando ha divergencia estrutural
    julgar                  -> recusa alto ate o M3b

Os dois passos de dossie chamam `_montar`, que grava pelo arquivo e ENCERRA.

> Os nomes acima sao conferidos por `tests/unit/test_promessas.py`: todo nome deste
> bloco tem de existir e ser um passo do Flow. A trava existe porque este bloco ja
> mentiu duas vezes — prometeu `submeter_a_humano` antes de o metodo existir, e depois
> seguiu prometendo `reconciliar` e `montar_dossie`, que nunca existiram.

**A rota `julgamento` so existe de verdade com classificador.** Ate o M3a ela era
alcancavel no papel e inalcancavel na pratica: nada construia uma divergencia de
classificacao duvidosa. Agora um `classificador` injetado a torna real. Ele e
opcional e **vem desligado por padrao**, porque a tabela de vedacoes ainda nao tem
uma linha conferida (`docs/PENDENCIAS.md`, P2): ligada hoje, ela mandaria todo
credito a julgamento, e a crew que julga so chega no M3b. O padrao vira ligado
quando a tabela for preenchida com o contador.

**O Flow nunca transmite ao Fisco e nunca conclui.** Nao existe ferramenta de
transmissao no projeto, e a manifestacao e ato do contribuinte.

Idempotencia: a chave de execucao e `(cnpj, competencia, impressao)`, e a **impressao
inclui a data de referencia**. Reexecutar no mesmo dia devolve o mesmo dossie; rodar
noutro dia gera dossie novo **ao lado**, sem apagar o anterior.

A data entra porque o documento depende dela: dias restantes, data de geracao e ate a
`natureza` (MANIFESTACAO vs. REGISTRO_DE_PERDA) mudam com o calendario. Ate 2026-09-02
ela ficava de fora, e o efeito era o pior possivel — um dossie que dizia "manifeste-se,
faltam 3 dias" era **silenciosamente substituido** por outro dizendo "prazo perdido",
sob a mesma chave, com o anterior destruido.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any

from crewai.flow import Flow, listen, router, start
from pydantic import BaseModel, Field

from abba_crews.core.arquivo import Arquivo, RegistroDossie
from abba_crews.core.calendario import JanelaManifestacao
from abba_crews.core.clientes import ConfigCliente, carregar_por_cnpj
from abba_crews.core.creditabilidade import Classificador
from abba_crews.core.dossie import Dossie, montar, renderizar
from abba_crews.core.modelos import ApuracaoFisco, DocumentoFiscal
from abba_crews.core.reconciliacao import ResultadoReconciliacao, reconciliar


class Fonte(BaseModel):
    """De onde vieram os dados de uma competencia.

    Isolar isto num modelo e o que permite o marco rodar em sintetico agora e apontar
    para a API da Plataforma RTC no M6 sem tocar no Flow.
    """

    model_config = {"frozen": True}

    documentos: tuple[DocumentoFiscal, ...]
    apuracao: ApuracaoFisco
    origem: str = "sintetico"

    def impressao(self, hoje: date) -> str:
        """Hash estavel das entradas **e da data de referencia**.

        `hoje` entra no hash porque o dossie muda com ela. Sem isso a chave prometia
        idempotencia que nao existia e o rerun sobrescrevia o rascunho do dia anterior.
        """
        payload = json.dumps(
            {
                "origem": self.origem,
                "hoje": hoje.isoformat(),
                "documentos": [d.model_dump(mode="json") for d in self.documentos],
                "apuracao": self.apuracao.model_dump(mode="json"),
            },
            sort_keys=True,
            default=str,
        )
        return hashlib.sha256(payload.encode()).hexdigest()[:16]


class EstadoSentinela(BaseModel):
    """Estado da conferencia de uma competencia."""

    cnpj: str = ""
    competencia: str = ""
    hoje: date = Field(default_factory=date.today)
    """`default_factory`, nao `date.today()`: o default do Pydantic e avaliado uma vez,
    na definicao da classe. Num processo longo — que e como o AMP roda — a data
    envelhecia sozinha, e e ela que decide o prazo."""
    config: ConfigCliente | None = None
    janela: JanelaManifestacao | None = None
    fonte: Fonte | None = None
    resultado: ResultadoReconciliacao | None = None
    dossie: Dossie | None = None
    markdown: str = ""
    chave_execucao: str = ""
    registro: RegistroDossie | None = None
    """O dossie guardado, quando ha arquivo. `None` = rodou sem persistir."""


class SentinelaFlow(Flow[EstadoSentinela]):
    """Confere a apuracao assistida dentro da janela de manifestacao."""

    def __init__(
        self,
        *,
        fonte: Fonte | None = None,
        dir_clientes: Path | None = None,
        classificador: Classificador | None = None,
        arquivo: Arquivo | None = None,
    ) -> None:
        super().__init__()
        self._fonte = fonte
        self._dir_clientes = dir_clientes
        self._classificador = classificador
        self._arquivo = arquivo

    @start()
    def abrir_competencia(self, crewai_trigger_payload: dict[str, Any] | None = None) -> None:
        """Recebe o gatilho e monta o contexto. Valida antes de qualquer custo."""
        p = crewai_trigger_payload or {}
        self.state.cnpj = str(p.get("cnpj", "")).strip()
        self.state.competencia = str(p.get("competencia", "")).strip()
        if hoje := p.get("hoje"):
            self.state.hoje = date.fromisoformat(str(hoje))

        faltando = [c for c in ("cnpj", "competencia") if not getattr(self.state, c)]
        if faltando:
            raise ValueError(
                f"gatilho incompleto: falta {', '.join(faltando)}. "
                'Esperado: {"cnpj": "...", "competencia": "AAAA-MM"}'
            )

        self.state.config = carregar_por_cnpj(self.state.cnpj, self._dir_clientes)
        self.state.janela = JanelaManifestacao.para(
            self.state.competencia, entrega_dere=self.state.config.entrega_dere
        )

    @listen(abrir_competencia)
    def coletar(self) -> None:
        """Traz documentos e proposta. Zero LLM.

        No M6 este passo chama a API da Plataforma RTC e a Distribuicao DF-e. Ate la,
        a fonte e injetada — o que mantem o Flow testavel sem rede.
        """
        if self._fonte is None:
            raise NotImplementedError(
                "coleta real chega no M6 (API RTC + Distribuicao DF-e), e depende da "
                "credencial do piloto RTC-CBS. Para rodar agora, injete uma Fonte "
                "sintetica: SentinelaFlow(fonte=...) ou use `abba-crews sentinela --mock`."
            )
        self.state.fonte = self._fonte
        self.state.chave_execucao = (
            f"{self.state.cnpj}:{self.state.competencia}:"
            f"{self._fonte.impressao(self.state.hoje)}"
        )

    @listen(coletar)
    def reconciliar_competencia(self) -> None:
        """O nucleo deterministico. Zero LLM."""
        assert self.state.fonte and self.state.config
        self.state.resultado = reconciliar(
            self.state.fonte.documentos,
            self.state.fonte.apuracao,
            tolerancia_brl=self.state.config.tolerancia_brl,
            classificador=self._classificador,
        )

    @router(reconciliar_competencia)
    def decidir_rota(self) -> str:
        """O roteamento que faz a conta fechar em centenas de CNPJs por mes."""
        assert self.state.resultado
        if self.state.resultado.conforme:
            return "sem_divergencia"
        return "julgamento" if self.state.resultado.requer_julgamento else "rotina"

    @listen("julgamento")
    def julgar(self) -> None:
        """Rota alcancavel desde o M3a, e ainda sem quem a atenda.

        Recusar alto e o comportamento correto: a alternativa seria montar um dossie
        que cala sobre creditos de creditabilidade nao resolvida — exatamente o falso
        positivo fiscal que o produto promete nao cometer.
        """
        assert self.state.resultado
        duvidosas = [d for d in self.state.resultado.divergencias if d.requer_julgamento]
        raise NotImplementedError(
            f"{len(duvidosas)} item(ns) com creditabilidade nao resolvida pela tabela "
            f"de vedacoes. A crew que julga o residuo (cetico + redator) chega no M3b; "
            f"a tabela se preenche com o contador (docs/PENDENCIAS.md, P2). Ate la, "
            f"este produto nao conclui sobre estes itens — e nao vai fingir que conclui."
        )

    @listen("sem_divergencia")
    def dossie_conforme(self) -> None:
        self._montar()

    @listen("rotina")
    def dossie_rotina(self) -> None:
        self._montar()

    def _montar(self) -> None:
        assert self.state.config and self.state.janela and self.state.resultado
        self.state.dossie = montar(
            config=self.state.config,
            janela=self.state.janela,
            resultado=self.state.resultado,
            hoje=self.state.hoje,
        )
        self.state.markdown = renderizar(self.state.dossie)
        self._submeter_a_humano()

    def _submeter_a_humano(self) -> None:
        """Grava e ENCERRA — o passo que a docstring prometia desde o M2 e nao existia.

        O turno do software termina aqui. Nao ha `human_input=True` no meio do Flow:
        o contador tem dezenas de CNPJs e uma janela curta, e nao vai ficar preso a
        um prompt esperando processo. O dossie fica guardado e ele assina no tempo
        dele, por `abba-crews aprovar`.

        Injetado e opcional, como o classificador: a CLI decide onde as coisas caem;
        o Flow e biblioteca. Sem `arquivo`, o dossie sai so pela saida padrao.
        """
        if self._arquivo is None or self.state.dossie is None:
            return
        assert self.state.fonte
        self.state.registro = self._arquivo.guardar(
            self.state.dossie,
            self.state.markdown,
            impressao=self.state.fonte.impressao(self.state.hoje),
            origem=self.state.fonte.origem,
        )
        self._registrar_conferencia()

    def _registrar_conferencia(self) -> None:
        """Enfileira o fato da conferencia para o cerebro (M5). Nao escreve nele.

        So quando ha `engagement_id`: nem todo CNPJ conferido pertence a um trabalho
        registrado, e inventar um seria pior que nao registrar.
        """
        r, d = self.state.registro, self.state.dossie
        if self._arquivo is None or r is None or d is None or not r.engagement_id:
            return
        from abba_crews.core.outbox import Outbox, da_conferencia

        Outbox(self._arquivo).registrar(
            da_conferencia(
                engagement_id=r.engagement_id,
                cnpj=r.cnpj,
                competencia=r.competencia,
                impressao=r.impressao,
                favoravel=d.total_favoravel,
                desfavoravel=d.total_desfavoravel,
                descartado=d.total_descartado,
                itens=d.resultado.itens_conferidos,
            )
        )
