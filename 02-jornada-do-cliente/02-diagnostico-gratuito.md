# Estágio 02 — Degustação Gratuita (Assessment gratuito)

**Dono:** chapéu Comercial · **Prazo-alvo:** geração do Assessment gratuito em **menos de 5 minutos** (32 a 60 páginas, conforme o modelo de profundidade); curadoria e revisão cruzada da faixa **antes** da conversa; apresentação ao vivo em até **5 dias úteis** após o aceite

## O que é
A amostra do método: uma análise da empresa do prospect feita **apenas com informação pública**, usando o scout do assessment-brain + curadoria dos sócios. De graça, com limite honesto declarado. Objetivo: provar competência e converter para a Avaliação de Prontidão paga.

**Corrigido em 2026-08-27 (V4f), depois da leitura de um relatório real:** o
documento tem **31 páginas na profundidade `quick`** (32 a 60 conforme o modelo),
é gerado em **minutos** pelo site `assessment.abbaservices.com.br`, e **não
contém nenhuma cifra em reais**. O "2 páginas com uma faixa em R$" descrevia um
artefato que a ferramenta nunca produziu.

**O que o documento entrega** ([anatomia completa](../03-comercial/assessment-gratuito.md)): recomendação em Situação/Complicação/Resolução · nota de maturidade em IA de 0 a 5 em seis dimensões · sinais recentes datados · desafios rotulados por natureza (fato declarado × hipótese) e por confiança · oportunidades priorizadas com score e piloto-farol nomeado · roadmap em três horizontes · riscos de adoção · e o **ledger de evidências** com id, citação literal e URL de cada fonte. **Não existe faixa em reais.** O que faz o leitor reagir é a nota de maturidade, o piloto-farol e a lista de desconhecidos.

## Entrada
Lead aceitou a degustação na call de descoberta — **ou chegou pelo assessment web** (`assessment.abbaservices.com.br`, no ar). Regra enquanto o gating não é implementado: lead vindo do assessment web JÁ tem o relatório — o T2 vira "apresentação comentada + o que a avaliação profunda revelaria", não a entrega do PDF.

## Checklist

- [ ] Conversa de 45 min com as **5 perguntas de descoberta do [Assessment gratuito](../03-comercial/assessment-gratuito.md)** — as três primeiras são o [teste de alvo](../00-identidade/alvo.md), então a qualificação sai de graça. **Não apresentar nada nessa conversa**
- [ ] Registrar o placar do teste de alvo (0–5) na pasta do lead — lead sem placar não avança de estágio
- [ ] Rodar o scout: `abba scout "NomeEmpresa" --industry X --create` (com provedor de busca real configurado — **nunca** enviar brief marcado como pesquisa sintética)
- [ ] Curadoria dos sócios sobre o brief bruto (1–2h): cortar o que estiver fraco, fortalecer as 2–3 hipóteses mais fortes, adicionar contexto de setor que só humano tem
- [ ] Gerar o Assessment gratuito em `assessment.abbaservices.com.br` e **ler criticamente**: nenhum achado de confiança baixa pode ser apresentado como certeza
- [ ] Revisão cruzada do outro sócio
- [ ] Agendar apresentação de 45 min ([pauta nº 2](../03-comercial/pautas-de-reuniao.md)) — **apresentar ao vivo, não só mandar o PDF** (a conversa é onde a conversão acontece)
- [ ] Enviar o PDF após a apresentação com o [e-mail nº 2](../03-comercial/emails-follow-up.md)
- [ ] Registrar reação e próximos passos na pasta do lead

## Saída
Prospect quer a avaliação paga (ou outro produto) → [03-proposta](03-proposta.md). Esfriou → follow-up agendado em 30/60/90 dias.

## Regras
- Custo-alvo por degustação: < {{CUSTO_MAX}} em API + 3h de sócio — acima disso, só para leads muito qualificados
- A degustação nunca vira consultoria grátis: 1 rodada, sem revisões, sem reunião extra sem próximo passo comercial

## Ferramentas e templates
[Assessment gratuito](../03-comercial/assessment-gratuito.md) · [modelo DOCX](../08-materiais/modelos/analise-abba-modelo.docx) · assessment-brain (`abba scout`) · Drive `01 Comercial/Leads/` · [pauta nº 2](../03-comercial/pautas-de-reuniao.md) · [e-mail nº 2](../03-comercial/emails-follow-up.md)
