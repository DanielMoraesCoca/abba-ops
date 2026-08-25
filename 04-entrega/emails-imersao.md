# E-mails da Imersão — do contrato ao campo

Sequência pós-assinatura que carrega o [Protocolo de Imersão](protocolo-de-imersao.md). Continua a numeração da [sequência comercial](../03-comercial/emails-follow-up.md) (que termina no e-mail 5, pós-assinatura): estes são os e-mails operacionais da entrega, não de venda.

Regra de estilo: e-mail que vai ao cliente é texto publicado — frases curtas, zero jargão interno, **sem travessão**. Campos `{{...}}` preenchidos antes de enviar, sempre.

---

## E-mail 1 — Convocação do patrocinador (D-7)

**Para:** patrocinador · **Quando:** no dia da assinatura ou D-7, o que vier primeiro · **Objetivo:** ponto focal + participantes + janelas

> **Assunto:** Avaliação {{NOME_EMPRESA}}: três definições para começarmos bem
>
> {{NOME_PATROCINADOR}}, obrigado pela confiança. Para o cronograma de {{N_SEMANAS}} semanas valer, precisamos de três definições suas até {{DATA_D_MINUS_5}}:
>
> 1. **Ponto focal:** uma pessoa do seu time que agenda as salas e cobra as pendências internas. É o papel mais importante do projeto do lado de vocês.
> 2. **Participantes:** nomes, cargos, áreas e e-mails de quem vamos ouvir. Segue anexo o mapa de entrevistas com os perfis e durações. A agenda ideal fecha antes do kickoff.
> 3. **Janelas de entrevista:** os dias das semanas {{SEMANA_1}} e {{SEMANA_2}} em que as agendas estarão mais livres.
>
> Em paralelo, enviaremos hoje a lista de documentos. Ela separa o que precisamos antes do primeiro dia de campo do que pode chegar depois. Nada dela exige preparação especial: são relatórios que a empresa já tem.
>
> Qualquer dúvida, me chama. O kickoff está marcado para {{DATA_KICKOFF}}.

---

## E-mail 2 — Pedido de documentos (D-7)

**Para:** ponto focal, cópia ao patrocinador · **Quando:** D-7 · **Anexo:** Pacote de Imersão gerado por `abba kickoff <eng> --output` (a [checklist](checklist-documentos-assessment.md) filtrada pelo setor)

> **Assunto:** Avaliação {{NOME_EMPRESA}}: lista de documentos (10 min de leitura)
>
> {{NOME_PONTO_FOCAL}}, segue a lista de documentos da avaliação, em duas partes:
>
> **Parte A, antes do campo** (até {{DATA_D_MINUS_2}}): são os itens que destravam o primeiro dia. Sem eles a análise começa no escuro e o cronograma desliza.
>
> **Parte B, ao longo do projeto** (até 30 dias): afinam a análise, mas não seguram nada. Chegando, entram.
>
> Três avisos que simplificam sua vida:
>
> 1. **Formato não importa.** PDF, Excel, foto de quadro, gravação de áudio: nós processamos. Apresentações em PowerPoint, por favor exportar em PDF.
> 2. **Agregado serve, nominal não.** Onde a lista pede "por área", não precisamos de nomes nem valores individuais. Se for mais fácil exportar o relatório inteiro, prefira a versão agregada: é deliberado, por proteção de dados.
> 3. **Não enviem** folha de pagamento nominal, dados de saúde ou dados de clientes finais identificados. A lista anexa explica o porquê de cada item.
>
> Como enviar: {{CANAL_DE_ENVIO}}. Cada documento que chega é confirmado por nós no canal do projeto.

---

## E-mail 3 — Lembrete de pendências (D-3)

**Para:** ponto focal · **Quando:** D-3, somente se itens da Parte A estiverem faltando

> **Assunto:** Avaliação {{NOME_EMPRESA}}: {{N_PENDENTES}} itens para destravar o campo
>
> {{NOME_PONTO_FOCAL}}, faltam {{N_DIAS}} dias para o kickoff e estes itens da Parte A ainda não chegaram:
>
> {{LISTA_PENDENTES}}
>
> Sem eles o primeiro dia de campo não rende, e o cronograma que combinamos fica em risco. Se algum item travou por acesso ou dúvida de formato, me liga hoje que resolvemos juntos. Se algum não existir na empresa, também vale saber: ausência de dado é um achado, não um problema.

---

## E-mail 4 — Disparo do pré-trabalho (D0, após o kickoff)

**Para:** todos os participantes, via patrocinador ou com ele em cópia · **Quando:** até 24h após o kickoff

> **Assunto:** {{NOME_EMPRESA}} + ABBA: seu papel na avaliação (10 a 15 min)
>
> Olá! Como o {{NOME_PATROCINADOR}} apresentou no kickoff, estamos conduzindo a avaliação de prontidão para IA da {{NOME_EMPRESA}}. Sua contribuição tem duas partes:
>
> 1. **Pré-trabalho online** ({{DURACAO_PRE_TRABALHO}} min): {{LINK_OU_INSTRUCAO}}. Prazo: {{DATA_LIMITE_PRE_TRABALHO}}.
> 2. **Conversa individual** de {{DURACAO_ENTREVISTA}} min na semana de {{SEMANA_ENTREVISTA}}: o convite de agenda chega pelo {{NOME_PONTO_FOCAL}}.
>
> Duas garantias: não existe resposta errada (queremos o retrato real, não o ideal), e nada do que você disser aparece no relatório com seu nome. Os achados são apresentados por padrão e por área, nunca por pessoa.

---

## E-mail 5 — Devolução de dado que não devíamos receber (quando ocorrer)

**Para:** ponto focal · **Quando:** no mesmo dia do recebimento · **Referência:** [checklist, seção "não pedir / não receber"](checklist-documentos-assessment.md#não-pedir--não-receber)

> **Assunto:** Avaliação {{NOME_EMPRESA}}: sobre o arquivo {{NOME_ARQUIVO}}
>
> {{NOME_PONTO_FOCAL}}, recebemos o arquivo {{NOME_ARQUIVO}}. Ele contém {{TIPO_DE_DADO}}, que está fora do que a avaliação precisa, então não vamos usar: o arquivo foi apagado dos nossos sistemas hoje e não entrou na análise.
>
> No lugar dele, o que serve é: {{VERSAO_QUE_SERVE}} (por exemplo, a mesma planilha agregada por área, sem nomes).
>
> Isso não é burocracia nossa: é o mesmo cuidado com dados que a avaliação vai recomendar para a operação de vocês. Qualquer dúvida sobre o que enviar, me chama antes que eu prefiro explicar duas vezes a receber uma vez o que não devo.

---

## E-mail 6 — Escalada de pré-trabalho ao patrocinador (semana 1, se necessário)

**Para:** patrocinador · **Quando:** meio da semana 1, se a adesão ao pré-trabalho estiver abaixo de {{LIMIAR}}%

> **Assunto:** Avaliação {{NOME_EMPRESA}}: adesão ao pré-trabalho em {{PERCENTUAL}}%
>
> {{NOME_PATROCINADOR}}, retrato de hoje: {{N_RESPONDERAM}} de {{N_TOTAL}} participantes completaram o pré-trabalho. A pontuação de prontidão reserva 40 dos 100 pontos para essa participação, e nós reportamos o número real, sem maquiagem.
>
> Um empurrão seu resolve: uma mensagem sua no canal do projeto costuma valer mais que três lembretes nossos. Se preferir, mando o rascunho.
>
> Lista de quem falta, se quiser cobrar direto: {{LISTA_FALTANTES_POR_AREA}} (por área, sem expor ninguém no grupo).
