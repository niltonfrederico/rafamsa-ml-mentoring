---
description: Pergunta conceitual ao magus (ML, sklearn, escrita manual, bioacústica de abelhas, materiais do curso). Read-only — não gera código nem materiais.
argument-hint: <pergunta>
---

# /ask

Forward a conceptual question to the `magus` subagent, augmented with caller identity and any IDE selection context.

## Step 0 — Resolve caller identity (once per project)

1. `Read` the project's auto-memory `MEMORY.md` and look for an entry whose name is `ask-caller-identity`.
1. If found, `Read` the linked file and use the stored value (`aluno` or `mentor`). Skip to Step 1.
1. If not found, ask the user via `AskUserQuestion`:
   - Question: "Você é o aluno (Rafael) ou o mentor (Nilton)?"
   - Header: "Quem pergunta"
   - Options:
     - **Rafael (aluno)** — desc: "Mestrando UNIFAL/MG, projeto de ID acústica de abelhas. R-user, inglês B1."
     - **Nilton (mentor)** — desc: "Staff SWE, sênior em Python. Calibra como mentor que precisa entender e ensinar."
1. Persist the answer as a `user`-type memory:
   - File: `ask_caller_identity.md` in the project memory dir
   - Frontmatter: `name: ask-caller-identity`, `type: user`, descriptive `description:`
   - Body: a single line — `aluno` or `mentor` — plus any reason the user gave
   - Add a pointer line to `MEMORY.md`

## Step 1 — Build the magus prompt

Compose the prompt to send to `magus`, in this order:

1. **Caller identity** (`aluno` or `mentor`, from Step 0)
1. **User's question** (`$ARGUMENTS`), verbatim — do not rephrase or summarize
1. **IDE selection context**, if present in the conversation — pull from the most recent
   `<ide_selection>...</ide_selection>` block, or, lacking that, from the most recent
   `<ide_opened_file>...</ide_opened_file>` block

Format:

```
<operador>aluno|mentor</operador>

<pergunta>
$ARGUMENTS
</pergunta>

<contexto-ide>
Arquivo: <relative path>
Linhas: <range, or "arquivo aberto, sem seleção">

<exact selected snippet, or the opened file's relevant region>
</contexto-ide>
```

If no IDE block is present, **omit** the `<contexto-ide>` tag entirely. Never fabricate selection.

## Step 2 — Invoke

- `subagent_type`: `magus`
- `description`: 3–5 word summary of the question
- Forward the magus's full response **verbatim** to the user. The `>>> tl;dr / >>> Resposta / >>> Glossário` format is
  part of the agent's contract — do not strip or edit.

## Edge cases

- **`$ARGUMENTS` empty AND no IDE context:** ask the user what the question is before invoking the agent.
- **`$ARGUMENTS` empty BUT IDE selection/file present:** treat as "explique este código" and proceed.
