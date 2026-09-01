"""O Flow da Sentinela — orquestracao deterministica.

Este arquivo pode importar `crewai`; `core/` nao pode. Toda decisao de negocio mora
em `core/`; aqui mora a sequencia.

    abrir_competencia  -> config do cliente + janela de manifestacao
    coletar            -> adaptador de fonte (sintetico neste marco)
    reconciliar        -> core/reconciliacao (+ creditabilidade). Zero LLM.
    decidir_rota       -> sem_divergencia | rotina | julgamento (M3b)
    montar_dossie      -> core/dossie, sempre RASCUNHO
    submeter_a_humano  -> grava e ENCERRA

**A rota `julgamento` so existe de verdade com classificador.** Ate o M3a ela era
alcancavel no papel e inalcancavel na pratica: nada construia uma divergencia de
classificacao duvidosa. Agora um `classificador` injetado a torna real. Ele e
opcional e **vem desligado por padrao**, porque a tabela de vedacoes ainda nao tem
uma linha conferida (`docs/PENDENCIAS.md`, P2): ligada hoje, ela mandaria todo
credito a julgamento, e a crew que julga so chega no M3b. O padrao vira ligado
quando a tabela for preenchida com o contador.

**O Flow nunca transmite ao Fisco e nunca conclui.** Nao existe ferramenta de
transmissao no projeto, e a manifestacao e ato do contribuinte.

Idempotencia: a chave de execucao e `(cnpj, competencia, hash_das_entradas)`. Mesmas
entradas produzem o mesmo dossie — e o que permite reexecutar uma competencia sem
medo durante a janela.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any

from crewai.flow import Flow, listen, router, start
from pydantic import BaseModel

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

    def impressao(self) -> str:
        """Hash estavel das entradas. Muda a entrada, muda a versao do dossie."""
        payload = json.dumps(
            {
                "origem": self.origem,
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
    hoje: date = date.today()
    config: ConfigCliente | None = None
    janela: JanelaManifestacao | None = None
    fonte: Fonte | None = None
    resultado: ResultadoReconciliacao | None = None
    dossie: Dossie | None = None
    markdown: str = ""
    chave_execucao: str = ""


class SentinelaFlow(Flow[EstadoSentinela]):
    """Confere a apuracao assistida dentro da janela de manifestacao."""

    def __init__(
        self,
        *,
        fonte: Fonte | None = None,
        dir_clientes: Path | None = None,
        classificador: Classificador | None = None,
    ) -> None:
        super().__init__()
        self._fonte = fonte
        self._dir_clientes = dir_clientes
        self._classificador = classificador

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
            f"{self.state.cnpj}:{self.state.competencia}:{self._fonte.impressao()}"
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
