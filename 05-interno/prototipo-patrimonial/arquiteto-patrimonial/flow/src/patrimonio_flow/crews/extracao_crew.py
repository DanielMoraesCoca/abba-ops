"""Crew de Extração — documento do cliente → PerfilEstruturado (a porta de entrada).

O "aha" de adoção: em vez de preencher um formulário, o profissional sobe o documento
e o perfil vem estruturado. Duas regras invioláveis aqui:
  1. PII pré-LLM — o texto chega mascarado (nomes/CPF viram placeholders); a extração
     produz um perfil pseudonimizado por natureza (o schema não tem campo de nome/CPF).
  2. Fidelidade — extrai o que está escrito; não infere aceite de transparência nem
     inventa dado ausente. A triagem e a análise são etapas seguintes.
"""

from __future__ import annotations

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from patrimonio_flow import schemas as S


@CrewBase
class ExtracaoCrew:
    agents_config = "config/extracao_agents.yaml"
    tasks_config = "config/extracao_tasks.yaml"

    @agent
    def extrator_perfil(self) -> Agent:
        # temperatura 0: extração é determinística por natureza, não criativa
        return Agent(config=self.agents_config["extrator_perfil"], temperature=0, memory=False)

    @task
    def task_extrair_perfil(self) -> Task:
        return Task(config=self.tasks_config["task_extrair_perfil"],
                    output_pydantic=S.PerfilEstruturado)

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks,
                    process=Process.sequential, memory=False, verbose=True, max_rpm=30)
