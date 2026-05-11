# Perfil do Usuário

> Atualizado automaticamente pela skill evaluate-user. Consumido por Magus e Lucca no início de cada resposta.

## Conhecimento Demonstrado

- **Python sênior (Staff level, 15+ anos):** domínio profundo da linguagem — typing, padrões, qualidade de código
- Familiaridade com estrutura de projetos, boas práticas de engenharia de software
- Capacidade de julgar qualidade de código Python gerado e identificar problemas
- Papel de **professor/mentor**: precisa não só entender os conceitos, mas ser capaz de repassá-los aos alunos

## Dificuldades Identificadas

- **Machine Learning não é a área principal:** conceitos de ML precisam de explicação — não partir do pressuposto de
  domínio prévio
- Algoritmos, métricas e intuições de ML devem ser explicados de forma que o usuário possa repassar para alunos
  iniciantes
- Ao abordar conceitos de ML, sempre incluir: intuição simples → formulação → aplicação prática

## Preferências

- Explicações que **habilitem o repasse pedagógico**: não basta entender, precisa conseguir ensinar
- Linguagem técnica de Python é natural; linguagem técnica de ML deve ser introduzida com contexto
- Foco em aplicações práticas e exemplos concretos antes de teoria formal
- Nível de detalhe de código: alto (Staff Dev) — não infantilizar explicações de código
- Nível de detalhe de ML: médio-introdutório — construir intuição antes de formalismo matemático
- Prefere documentação em **pt-br** com termos técnicos em inglês (ex: "o dataset", "o overfitting")
- Referência a ferramentas com explicação de propósito: não assumir que o aluno já conhece pipx, Poetry, etc.
- Prefere índice/sumário no início de documentos longos

## Tópicos Trabalhados

- Aula 01 (k-NN) já tem notebook gerado: `class-01/class-01-digit-recognition.ipynb`
- Aula 02 (Decision Tree) gerada: `class-02/class-02-letter-recognition.ipynb` + `class-02/teacher-notes.md`
  - Dataset: UCI Letter Recognition (20.000 amostras, 16 features, 26 classes) via `ucimlrepo`
  - Conceitos cobertos: Gini, max_depth, overfitting, bias-variance tradeoff, feature importance, confusion matrix
- Infraestrutura do projeto documentada: Homebrew + pipx + Poetry + Jupyter Lab
- Glossário de ML iniciado com termos da Aula 01 (`GLOSSARY.md`)
- Usuário solicitou conteúdo da aula sem especificar variações — aceitou o escopo padrão do README sem ajustes
- Separa explicitamente conteúdo para alunos (READMEs, notebooks) de conteúdo para instrutor (teacher-notes) — timebox e
  guias de timing devem ficar apenas nos teacher-notes, não nos materiais voltados ao aluno
- Pensa em estrutura do repositório com cuidado: criou `labs/` para experimentação do aluno, com `.gitignore` protegendo
  o histórico do projeto
- Conhece bem o tooling Python (Poetry entry points, `pyproject.toml`, `package-mode`) — não precisa de explicação sobre
  setup de projeto
