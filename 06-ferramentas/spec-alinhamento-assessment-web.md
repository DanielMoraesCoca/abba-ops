# Spec — Alinhamento do Assessment Web (para execução dev)

> Ticket pronto para o chapéu Tecnologia. Objetivo: o assessment (`assessment.abbaservices.com.br`) vestir a marca da casa, falar a língua oficial e converter para conversa. Contexto na [ficha da avaliação](ferramenta-avaliacao.md). **O site ainda não está aberto ao público** (confirmado 2026-07-24) — este ticket inteiro executa ANTES do lançamento.

## 0. Pré-requisito (bloqueante — risco R16)
- A produção roda mudanças que **não estão** no repo assessment-brain. Antes de tocar em qualquer item abaixo: commitar/sincronizar o estado de produção no repo (branch própria, PR normal). Regra daqui em diante: produção só roda código versionado
- Aproveitar a sincronização para responder as 2 pendências da [ficha](ferramenta-avaliacao.md): qual provedor de busca alimenta o scout + custo real por execução (anotar na planilha de precificação)

## 1. Visual (padrão da [identidade](../00-identidade/identidade-visual.md))
- Paleta: primária `#1B2A4A` (navy) · acento `#C2A35B` (dourado) · neutros `#5A6472`/`#E8E8E8` · fundo branco. Substituir o gradiente teal/verde atual dos cards de recomendação por navy com acento dourado
- Logo: usar a marca-símbolo dourada ([PNG no repo](../08-materiais/marca/abba-logo.png)) no cabeçalho
- Cabeçalho: "ABBA · Análise" (não "ABBA · Assessment")

## 2. Nomes (tabela da [marca](../00-identidade/marca-e-nomenclatura.md))
- "Assessment" → **"Análise ABBA"** em toda a UI e no PDF
- Recomendações do relatório NUNCA inventam produto: mapear para a escada oficial — "Discovery de IA" → **"Avaliação de Prontidão para IA"** · workshops → "Workshop de Descoberta de Shadow AI" · governança → "Sprint LGPD + Governança de IA". Prompt/template do gerador deve citar apenas estes nomes
- Rodapé do PDF: sempre `assessment.abbaservices.com.br` (NUNCA URL de staging — checar build de produção)

## 3. Página final de CTA (nova — copy pronta, usar como está)
> ## Isto foi feito de fora. Imagine com os dados de dentro.
> Esta análise usou apenas informação pública. A **Avaliação de Prontidão para IA** entrevista do conselho à linha de frente, quantifica cada oportunidade em reais e entrega um caminho recomendado de até 3 agentes de IA — em 2 semanas.
> **O próximo passo é gratuito:** apresentamos esta análise ao vivo, em 45 minutos, e mostramos o que a avaliação profunda revelaria no seu caso.
> **comercial@abbaservices.com.br** · abbaservices.com.br
> *ABBA · Consultoria de IA · Confidencial — elaborado exclusivamente com informação pública; não constitui consultoria formal.*

## 4. Gating (decisão estratégica da [coreografia](../03-comercial/coreografia-da-conversao.md))
- **Público (teaser, 5–8 págs):** capa + card de recomendação + resumo executivo + top 3 oportunidades (só títulos e 1 linha) + página de CTA
- **Completo (30–42 págs):** entregue NA apresentação ao vivo — nunca por download direto
- Captura antes do teaser: nome + e-mail corporativo + empresa (mínimo viável de lead-gen)
- Notificação interna: cada análise gerada → e-mail para `comercial@` (lead novo no funil, estágio 01)

## 5. Aceite
- [ ] 1 análise gerada em produção com visual navy/dourado, nomes oficiais, CTA final e rodapé correto
- [ ] Fluxo completo testado: visitante → captura → teaser → e-mail interno recebido
- [ ] PDF de amostra arquivado em `05 Marketing/` e revisado pelos dois sócios
