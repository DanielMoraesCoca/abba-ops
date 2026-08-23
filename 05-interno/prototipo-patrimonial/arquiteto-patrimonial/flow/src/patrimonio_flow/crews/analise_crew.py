"""Crew A — Análise: produz fatos jurídicos citados (nunca estrutura).

Processo sequencial; cada task com output_pydantic + guardrails de função
(anti_citacao_orfa é criado por caso, com os chunks efetivamente recuperados).
"""

from __future__ import annotations

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from patrimonio_flow import schemas as S
from patrimonio_flow.guardrails import make_anti_citacao_orfa, sem_linguagem_de_ocultacao
from patrimonio_flow.tools.rag_corpus import RagCorpusTool

# Ver desenho_crew.py: eleva o teto de completion para as análises citadas
# (tributária/sucessória/jurisdições) não truncarem em casos com muitas fontes.
MAX_TOKENS_SAIDA = 16000


@CrewBase
class AnaliseCrew:
    """Instanciada por caso: recebe a tool (com callback de retrieval) e a lista
    viva de chunks recuperados para o guardrail anti-citação-órfã."""

    agents_config = "config/analise_agents.yaml"
    tasks_config = "config/analise_tasks.yaml"

    def __init__(self, rag_tool: RagCorpusTool, chunks_recuperados: list[str]):
        self.rag_tool = rag_tool
        self.chunks_recuperados = chunks_recuperados

    # -------- agents (temperature=0: etapas extrativas; modelo por etapa: calibrar no eval)

    @agent
    def analista_tributario_br(self) -> Agent:
        return Agent(config=self.agents_config["analista_tributario_br"],
                     tools=[self.rag_tool], temperature=0, memory=False,
                     max_tokens=MAX_TOKENS_SAIDA)

    @agent
    def analista_sucessorio(self) -> Agent:
        return Agent(config=self.agents_config["analista_sucessorio"],
                     tools=[self.rag_tool], temperature=0, memory=False,
                     max_tokens=MAX_TOKENS_SAIDA)

    @agent
    def analista_jurisdicoes(self) -> Agent:
        return Agent(config=self.agents_config["analista_jurisdicoes"],
                     tools=[self.rag_tool], temperature=0, memory=False,
                     max_tokens=MAX_TOKENS_SAIDA)

    # -------- tasks

    def _guardrails(self):
        return [sem_linguagem_de_ocultacao,
                make_anti_citacao_orfa(self.chunks_recuperados, self.rag_tool.textos_entregues)]

    @task
    def task_analise_tributaria(self) -> Task:
        return Task(config=self.tasks_config["task_analise_tributaria"],
                    output_pydantic=S.AnaliseTributaria, guardrails=self._guardrails())

    @task
    def task_analise_sucessoria(self) -> Task:
        return Task(config=self.tasks_config["task_analise_sucessoria"],
                    output_pydantic=S.AnaliseSucessoria, guardrails=self._guardrails())

    @task
    def task_analise_jurisdicoes(self) -> Task:
        return Task(config=self.tasks_config["task_analise_jurisdicoes"],
                    output_pydantic=S.AnaliseJurisdicoes, guardrails=self._guardrails())

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks,
                    process=Process.sequential, memory=False, verbose=True,
                    max_rpm=30)  # rate-limit: defesa a mais de custo (o teto duro é _cobrar_custo)
