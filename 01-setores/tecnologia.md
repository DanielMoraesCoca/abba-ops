# Setor Tecnologia

**Missão:** manter as ferramentas proprietárias e o stack de construção confiáveis, seguros e prontos para cliente.
**Dono:** Pedro · suplente: Daniel (matriz no [README](README.md))

## Ferramentas e stack

| Ativo | Papel no negócio | Estado (2026-07) |
|---|---|---|
| `assessment-brain` (ferramenta própria) | Avaliação em 25 dimensões + scout (degustação) | Funcional; validado em dados sintéticos; certificação com dados reais pendente |
| `abba-portal` (ferramenta própria) | Plataforma de capacitação | Funcional; autenticação interina; vídeos Foundation pendentes |
| CrewAI (stack externa) | Construção dos agentes de cliente (estágio 07) + acesso dos membros nível Arquiteto | Conta/via de contratação a definir (Enterprise vs. self-host) |
| Repo `ABBA` (legado) | Origem da empresa; ativos reutilizáveis (padrões de aprovação humana, integrações) | Não é ferramenta de entrega — não prometer nada baseado nele |

Mapa completo de lacunas: [jornada × ferramentas](../06-ferramentas/mapa-jornada-ferramentas.md).

## Responsabilidades

- Infra e credenciais: chaves de API, ambientes (Vercel/Supabase/Render), backups, domínio (P2)
- Segurança e LGPD técnica: acesso, criptografia, trilhas de auditoria, ciclo de vida de dados (`abba forget` no assessment-brain; fluxos DPO no portal)
- Prontidão para engajamento: antes de cada kickoff, checklist de setup do cliente (tenant, contas, engajamento criado)
- Evolução: priorizar débito técnico que bloqueia negócio (autenticação do portal, contratação/setup do CrewAI) sobre feature nova
- Custos de ferramenta: monitorar gasto de API por engajamento (alimenta a [planilha de precificação](../03-comercial/precificacao-planilha.md))

## Checklist semanal

- [ ] Algum sistema fora do ar ou degradado?
- [ ] Backups do banco de cada ferramenta verificados?
- [ ] Gasto de API da semana dentro do esperado?
- [ ] Alguma pendência técnica bloqueando um estágio de cliente ativo?
- [ ] Riscos técnicos do [registro](../05-interno/registro-de-riscos.md) mudaram de status?

## Regra de ouro
**Nada de dado real de cliente em ambiente de teste; nada de decisão destrutiva fora dos caminhos sancionados** (deleção só pelo `abba forget` / fluxo DPO). As ferramentas nunca aparecem para o cliente pelos nomes internos ([nomenclatura](../00-identidade/marca-e-nomenclatura.md)).
