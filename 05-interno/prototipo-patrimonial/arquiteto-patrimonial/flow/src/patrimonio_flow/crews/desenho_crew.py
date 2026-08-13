"""Crew B — Desenho: alternativas de estrutura + crítica adversarial.

O Flow (código) descarta desenhos com ataque `fatal` e reexecuta com a crítica
no contexto se restarem menos de 2 desenhos (máx. 2 ciclos) — ver main.py.
"""

from __future__ import annotations

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from patrimonio_flow import schemas as S
from patrimonio_flow.guardrails import make_anti_citacao_orfa, sem_linguagem_de_ocultacao
from patrimonio_flow.tools.rag_corpus import RagCorpusTool


@CrewBase
class DesenhoCrew:
    agents_config = "config/desenho_agents.yaml"
    tasks_config = "config/desenho_tasks.yaml"

    def __init__(self, rag_tool: RagCorpusTool, chunks_recuperados: list[str]):
        self.rag_tool = rag_tool
        self.chunks_recuperados = chunks_recuperados

    @agent
    def arquiteto_estruturas(self) -> Agent:
        # modelo sugerido: classe Sonnet; criatividade controlada
        return Agent(config=self.agents_config["arquiteto_estruturas"],
                     tools=[self.rag_tool], memory=False)

    @agent
    def critico_adversarial(self) -> Agent:
        # é onde mais se paga inteligência — modelo sugerido: classe Sonnet/Opus
        return Agent(config=self.agents_config["critico_adversarial"],
                     tools=[self.rag_tool], memory=False)

    @task
    def task_desenhar_alternativas(self) -> Task:
        return Task(config=self.tasks_config["task_desenhar_alternativas"],
                    output_pydantic=S.ListaDesenhos,
                    guardrails=[sem_linguagem_de_ocultacao,
                                make_anti_citacao_orfa(self.chunks_recuperados,
                                                       self.rag_tool.textos_entregues)])

    @task
    def task_critica_adversarial(self) -> Task:
        return Task(config=self.tasks_config["task_critica_adversarial"],
                    output_pydantic=S.ListaCriticas,
                    guardrails=[sem_linguagem_de_ocultacao])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks,
                    process=Process.sequential, memory=False, verbose=True,
                    max_rpm=30)  # rate-limit: defesa a mais de custo (o teto duro é _cobrar_custo)
