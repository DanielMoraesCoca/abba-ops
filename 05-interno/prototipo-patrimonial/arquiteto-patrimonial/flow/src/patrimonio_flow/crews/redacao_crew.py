"""Crew C — Redação: a minuta ao advogado (nunca o conselho final)."""

from __future__ import annotations

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from patrimonio_flow import schemas as S
from patrimonio_flow.guardrails import minuta_tem_secoes_obrigatorias, sem_linguagem_de_ocultacao

# Ver desenho_crew.py: eleva o teto de completion para a minuta não truncar
# (documento longo em JSON). Gasto real limitado pelo conteúdo; teto de custo
# do caso segue valendo.
MAX_TOKENS_SAIDA = 16000


@CrewBase
class RedacaoCrew:
    agents_config = "config/redacao_agents.yaml"
    tasks_config = "config/redacao_tasks.yaml"

    @agent
    def redator_juridico(self) -> Agent:
        return Agent(config=self.agents_config["redator_juridico"], memory=False,
                     max_tokens=MAX_TOKENS_SAIDA)

    @task
    def task_redigir_minuta(self) -> Task:
        return Task(config=self.tasks_config["task_redigir_minuta"],
                    output_pydantic=S.MinutaFinal,
                    guardrails=[sem_linguagem_de_ocultacao, minuta_tem_secoes_obrigatorias])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks,
                    process=Process.sequential, memory=False, verbose=True,
                    max_rpm=30)  # rate-limit: defesa a mais de custo (o teto duro é _cobrar_custo)
