# Verificador de Contraparte — Fronteira Ética e Legal (leia antes de tudo)

> **Camada:** interno (governança de produto). Este documento existe ANTES da especificação porque, neste produto, a fronteira é o produto. Uma ferramenta de verificação anti-fraude, mal desenhada, vira o oposto: a camada de credibilidade que um golpista usa para enganar a vítima. As regras abaixo não são cláusulas — são o desenho.
>
> Origem: pedido do contato de domínio (2026-08-12) por uma ferramenta que verifique contrapartes "para que não mintam"; leitura dos documentos revelou tipologia de fraude ([alerta](alerta-indicadores-fraude.md)). Travas confirmadas em conversa de sócios (2026-08-12).

---

## As 4 travas (invioláveis)

1. **A ABBA nunca é o dinheiro nem o carimbo.** O produto não põe capital, não paga taxa, não intermedeia fundos, não custodia, não conecta partes para transacionar. Ele lê documentos e consulta fontes públicas. Ponto.
2. **A ferramenta sinaliza RISCO — jamais emite "aprovado/verificado/idôneo".** A saída máxima positiva é *"não encontramos indicadores de risco nas fontes consultadas nesta data"* — com a data, as fontes e o alcance explícitos. Nunca um selo que terceiros possam exibir como validação. Um "aprovado" da ABBA na mão errada financia o golpe seguinte.
3. **Só fontes públicas e oficiais.** Registros empresariais, listas de sanções, diretório SWIFT, WHOIS, mídia. **Nunca** acesso não autorizado a sistemas ("o banco de dados deles"), scraping de dado privado/paywall, engenharia social, ou compra de dado de origem duvidosa.
4. **Humano nomeado assina o veredito.** Como no protótipo patrimonial: a IA levanta e cita; o profissional lê e decide. O relatório é minuta de apoio, não conclusão automática.

## O que é LEGAL (e por quê)

Verificação de contraparte por **fonte pública** é prática padrão e amparada:
- **KYC/KYB/EDD** (Know Your Customer/Business, Enhanced Due Diligence) é exigência regulatória em todo o sistema financeiro; consultar registros, sanções e mídia sobre uma contraparte é o núcleo dela.
- **Base legal LGPD:** prevenção à fraude é hipótese expressa de tratamento — legítimo interesse (art. 7, IX) e proteção ao crédito (art. 7, X); o art. 11, §1º admite tratamento de dado sensível para prevenção à fraude. GDPR: legítimo interesse (art. 6(1)(f)), reconhecido no considerando 47 para prevenção a fraude.
- **Dado público:** informação de registro empresarial, sanções e mídia é pública por natureza; consultá-la para uma finalidade legítima e específica (não ser fraudado) é lícito.

## O que é ILEGAL / fica FORA (linha vermelha)

- **Acesso não autorizado a sistema** — invadir, usar credencial de terceiro, "entrar no servidor deles". Crime (Lei 12.737/2012, "Lei Carolina Dieckmann"; no exterior, CFAA e equivalentes).
- **Scraping de dado pessoal privado/paywall**, ou montar dossiê íntimo além da finalidade de prevenção à fraude (viola minimização e finalidade da LGPD).
- **Dado sensível fora da hipótese** de prevenção à fraude; retenção além do necessário.
- **Qualquer papel na transação suspeita** — verificar é defensivo; facilitar, custodiar ou "monetizar" é participação.

## O teste de finalidade (aplicar a cada uso)

Antes de rodar uma verificação, uma pergunta: *"o resultado disto serve para EU decidir se confio, ou para CONVENCER um terceiro a confiar?"* O primeiro é defesa (legítimo). O segundo é o começo de virar carimbo — recusar.

## Ligações

[Alerta de indicadores](alerta-indicadores-fraude.md) · [Plano do verificador](plano-verificador.md) · [Especificação](especificacao-verificador.md) · Doutrina-mãe: [protocolo de prova](../../../04-entrega/protocolo-de-prova.md) · [posicionamento](../../../00-identidade/posicionamento.md)
