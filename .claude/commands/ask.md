______________________________________________________________________

## description: Pergunta conceitual ao magus (ML, sklearn, escrita manual, bioacústica de abelhas, materiais do curso). Read-only — não gera código nem materiais. argument-hint: <pergunta>

Invoque o subagent `magus` via a ferramenta Agent com o seguinte prompt:

```
$ARGUMENTS
```

Instruções para a invocação:

- `subagent_type`: `magus`
- `description`: curta (3–5 palavras) resumindo a dúvida
- Encaminhe a pergunta do usuário **literalmente** como o prompt do agente, sem reformular nem resumir.
- Quando o magus responder, repasse a resposta **completa e sem editar** ao usuário (o formato
  `>>> tl;dr / >>> Resposta / >>> Glossário` é parte do contrato do agente).
- Se `$ARGUMENTS` estiver vazio, peça ao usuário qual é a dúvida antes de invocar o agente.
