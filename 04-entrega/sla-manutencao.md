# SLA de Manutenção — template

> Anexado ao contrato de continuidade (Anexo I da manutenção). Preencher os `{{ }}`, revisar com advogado junto do contrato (pendência P4). Operado pelo [estágio 09](../02-jornada-do-cliente/09-manutencao.md).

## 1. Escopo coberto

- Monitoramento dos agentes em produção listados: {{LISTA_AGENTES}}
- Correção de defeitos e ajuste fino de comportamento
- Pequenas evoluções: até **{{HORAS_MES}}h/mês** somadas (não cumulativas); acima disso, mini-ciclo cotado à parte
- Continuidade do acesso à plataforma de capacitação para {{N_USUARIOS}} usuários (inclui onboarding de novos colaboradores)
- Relatório mensal de impacto + ritual trimestral com a diretoria

**Fora do escopo:** novos agentes (mini-ciclo) · mudanças de infraestrutura do cliente · incidentes causados por alteração não comunicada nos sistemas integrados · suporte a usuário final fora da plataforma.

## 2. Severidades e tempos

| Sev. | Definição | Primeira resposta | Solução-alvo |
|---|---|---|---|
| **S1** | Agente parado ou produzindo saída errada com impacto operacional | {{4h úteis}} | {{1 dia útil}} (workaround) · {{3 dias}} (definitiva) |
| **S2** | Degradação parcial (lentidão, falhas intermitentes, aprovações travadas) | {{8h úteis}} | {{3 dias úteis}} |
| **S3** | Incômodo sem impacto operacional; dúvidas; ajustes estéticos | {{1 dia útil}} | {{10 dias úteis}} ou próximo ciclo |
| **Incidente de dados** | Qualquer suspeita envolvendo dados pessoais | **imediata ao tomar ciência** | conforme Cláusula 9.7 do contrato (Art. 48 LGPD) |

**Janela de suporte:** dias úteis, {{9h–18h}} (horário de Brasília). Canal de abertura: {{e-mail dedicado / canal do projeto}} — WhatsApp **não** abre chamado ([política de comunicação](../05-interno/comunicacao.md)).

## 3. Relatório mensal

O relatório mensal segue o modelo Word canônico: [`../08-materiais/modelos/relatorio-mensal-modelo.docx`](../08-materiais/modelos/relatorio-mensal-modelo.docx) — com a tabela **projetado vs. realizado** sempre presente. Processo de emissão no [estágio 09](../02-jornada-do-cliente/09-manutencao.md).

## 4. Condições

- Vigência: 12 meses, renovação automática salvo aviso de 30 dias
- Valor: {{PRECO_MANUTENCAO}}/mês · reajuste anual IPCA · fatura mensal
- Suspensão por inadimplência > {{30}} dias (agentes seguem rodando; suporte e evolução pausam)
- Revisão de volumes: se execuções/usuários crescerem >{{50}}% sobre o contratado, as Partes repactuam
