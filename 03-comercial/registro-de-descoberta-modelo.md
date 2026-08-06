# Registro de Descoberta — modelo

> **Camada:** comercial (modelo). O que se preenche e manda ao time de engenharia **no mesmo dia** da reunião conduzida pelo [roteiro de descoberta](roteiro-descoberta-prototipo.md). O que faltar vira pergunta ao ponto focal — **não segunda reunião de descoberta**.
>
> **Regra de confidencialidade:** a instância preenchida (com nome do cliente) vive no **Drive, na pasta do lead — nunca em git**. Este arquivo é só o molde.
>
> **Regra de honestidade interna:** o registro diz o que o cliente disse **e o que não disse**. A seção 8 (checklist) existe para isso — lacuna registrada é lacuna que se fecha; lacuna escondida vira protótipo errado.

---

## 1. A empresa e o caso
Setor, porte, o que a empresa faz, onde opera. **Se mais de um caso foi posto na mesa: registrar todos, dizer qual foi escolhido e por quê** (os demais entram na fila).

## 2. O problema, na voz dele
Citações literais, entre aspas. **O exemplo concreto que a pessoa deu é o coração do registro** — ele vale mais que qualquer paráfrase nossa.

## 3. O objetivo esperado — nas palavras do cliente
Se a pessoa descreveu o que quer ver, transcrever **palavra por palavra**. É o requisito na fonte; toda reformulação nossa perde informação.

## 4. Os fatos que mudam o desenho
Os achados que simplificam ou complicam a engenharia. Os dois mais comuns:
- **Consulta × execução** — a solução recomenda, ou age no sistema? (execução exige integração transacional; consulta não)
- **Tempo real × lote** — precisa responder na hora, ou roda periodicamente? (define arquitetura e custo por execução)

## 5. Os gatilhos
O que dispara uma nova execução, e com que frequência. Lista numerada.

## 6. Criticidade e erro
O erro inaceitável e o tolerável, nas palavras dele. **Daqui nasce a decisão de onde vai a aprovação humana** — e, quando a exigência é de exatidão, a decisão de arquitetura correspondente (o que é cálculo determinístico e auditável × o que é trabalho de modelo).

## 7. Dados
O que existe, em que formato, quem fornece, o que é sensível — **e os riscos de dado que o próprio cliente apontou** (dado velho, dado incompleto, dado que só uma pessoa sabe corrigir).

## 8. Pessoas
Tabela: patrocinador · **quem já faz esse trabalho hoje** (o dono do conhecimento tácito — prioridade de contato) · quem revisa/aprova · ponto focal técnico · quem do nosso lado.

## 9. Checklist dos 12 — o que temos e o que falta
Copiar o checklist do [roteiro](roteiro-descoberta-prototipo.md) e marcar ✅ / ⚠️ / ❌ item a item, com a leitura honesta no fim: em que a reunião foi forte, em que foi fraca, e o que a próxima resolve.

## 10. Desenho preliminar do protótipo
Uma frase de resumo + o fluxo numerado + **o que o protótipo NÃO faz** (dizer isso na proposta evita a expectativa que mata o projeto) + **como será medido** (a régua do GO).

## 11. As perguntas da próxima reunião
Agrupadas por bloco, com destaque para o que mais falta. Inclui sempre o **pedido da amostra com gabarito** (quem monta, até quando).

## 12. Sinais comerciais registrados
Reação a preço, disposição a pagar, urgência, quem ele quer envolver. **Reação a preço vai também para a [planilha de precificação](precificacao-planilha.md) §6** — é o dado que valida a tabela.

## 13. Próximos passos
Tabela: o quê · quem · quando.

---

## Como gerar o PDF do registro

O markdown é o que o time usa; o PDF é para o cliente e para o Drive. Converter com o estilo editorial da casa:

```bash
python3 -c "
import markdown
css = open('style.css').read()
body = markdown.markdown(open('registro.md').read(), extensions=['tables','sane_lists'])
open('registro.html','w').write(f\"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>\")"
soffice --headless --convert-to pdf registro.html
```

Folha de estilo (branco, Cambria/Calibri, dourado sóbrio, filetes) no [padrão editorial](../08-materiais/README.md) §0.

## Ligações

[Roteiro de descoberta](roteiro-descoberta-prototipo.md) · [Cartão de reunião](../08-materiais/modelos/cartao-descoberta-prototipo.pdf) · [Relatório do protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx) (os critérios do bloco 2 viram a seção 2 dele) · [Calculadora de construção](../06-ferramentas/calculadora-construcao.md) (o registro alimenta os 7 fatores)
