# Content Creation Instructions for ML Classes

## User Profile

Todos os agentes (Magus e Lucca) devem ler [.claude/instructions/user.md](.claude/instructions/user.md) no início de
toda interação e calibrar profundidade, vocabulário e abordagem pedagógica de acordo. Esse arquivo é mantido pela skill
`evaluate-user` e acumula conhecimento sobre o usuário ao longo das sessões.

______________________________________________________________________

## Context

Este curso é um programa hands-on de mentoria em machine learning focado em **Reconhecimento de Escrita Manual &
Identificação de Pessoas** usando scikit-learn. Os alunos têm conhecimento de Python e entendem matemática básica de ML.
Cada aula tem **1 hora e 30 minutos (90 minutos)**.

O curso roda por **9 aulas**. Toda aula entrega um Jupyter notebook completo e funcional que o aluno consegue rodar
top-to-bottom sem erros.

______________________________________________________________________

## Class Structure (90 minutes)

Toda aula deve seguir esta estrutura exatamente:

```
Part 1: Setup & Motivation    — 15 minutes
Part 2: Hands-On Implementation — 55 minutes
Part 3: Interpretation & Discussion — 15 minutes
Part 4: Wrap-up & Preview     —  5 minutes
```

### Part 1: Setup & Motivation (15 min)

- Revisão rápida da aula anterior (o que foi construído, o que foi aprendido)
- Apresentação do problema de escrita manual/análise de documento que esta aula resolve
- Visão geral do dataset: load, inspecionar shape, mostrar amostras de registros/imagens
- Declarar os 2–4 objetivos de aprendizado da aula com clareza

### Part 2: Hands-On Implementation (55 min)

- Coding passo a passo — sem saltos grandes, todo bloco é explicado
- Seguir esta progressão sempre:
  1. Import libraries (com explicação de uma linha pra cada)
  1. Load e exploração de dados (shape, dtypes, sample rows, basic stats)
  1. Implementação simples primeiro — colocar um baseline funcionando
  1. Adicionar complexidade incrementalmente (features, tuning, evaluation)
  1. Avaliar e visualizar resultados
- Incluir no mínimo 3 cells "Try This": mudanças de parâmetro que o aluno deve rodar
- Incluir no mínimo 3 plots (ver Visualization Requirements abaixo)

### Part 3: Interpretation & Discussion (15 min)

- Análise dos resultados: o que funcionou, o que não, por quê
- Identificar padrões de misclassification ou outputs surpreendentes
- Conectar achados a análise de escrita manual real ou aplicações forenses
- Endereçar as misconceptions mais comuns dos alunos pra esse algoritmo
- Incluir 2–3 perguntas "Think About It" (sem código, discussão aberta)

### Part 4: Wrap-up & Preview (5 min)

- Resumo de key concepts (lista de bullets, máximo 5 itens)
- Assignment: um destes:
  - Experiment: modificar um hyperparameter e observar o efeito
  - Explore: aplicar a técnica a um dataset diferente ou subset
  - Reflect: conectar o algoritmo a um cenário do mundo real
- Teaser da próxima aula: uma frase sobre o que vem a seguir

______________________________________________________________________

## Coding Standards

### Python Code Quality

```python
# Every function must have full type annotations
def train_classifier(
    X_train: np.ndarray,
    y_train: np.ndarray,
    n_neighbors: int = 5,
) -> KNeighborsClassifier:
    ...
```

- Type annotations em todos os parâmetros e tipos de retorno
- Um import por linha, caminhos absolutos apenas — nunca `from . import something`
- `random_state=42` em todas as operações estocásticas (train_test_split, classifiers, etc.)
- Nomes de variáveis com contexto de escrita manual:
  - `writer_id`, `pen_pressure`, `stroke_width`, `character_features`
  - `X_train`, `X_test`, `y_train`, `y_test` (convenção padrão de ML)
- Sem código morto, sem blocos comentados, sem TODOs em notebooks entregues

### Standard sklearn Pattern

Sempre seguir esse padrão:

```python
# 1. Prepare data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Train model
model = AlgorithmName(parameters)
model.fit(X_train, y_train)

# 3. Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")

# 4. Interpret in context
# (explanation of what this accuracy means for this handwriting problem)
```

### Error Handling

Incluir verificação de imports e checks de carregamento de dados na primeira cell:

```python
# Verify environment
import importlib
required = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]
for pkg in required:
    assert importlib.util.find_spec(pkg) is not None, f"Missing: {pkg}"
print("Environment OK")
```

______________________________________________________________________

## Visualization Requirements

- Mínimo 3 plots por aula
- Todo plot deve ter:
  - Título
  - Eixos rotulados (com unidades quando aplicável)
  - Legenda quando houver múltiplas séries
  - Uma markdown cell embaixo interpretando o que o aluno deve observar
- Usar `seaborn` pra plots estatísticos/de distribuição
- Usar `matplotlib` pra visualizações customizadas (imagens, confusion matrices, decision boundaries)
- Color scheme: acessível (evitar só red/green — usar a palette colorblind do seaborn)

### Required Plot Types by Class

| Class | Mandatory Plots | |---|---| | 01 — k-NN | Sample digit images, k-value accuracy curve, confusion matrix | | 02
— Decision Tree | Tree visualization, feature importance bar chart, confusion matrix | | 03 — Linear Regression |
Scatter + regression line, residual plot, R² comparison | | 04 — Logistic Regression | Sigmoid curve, confusion matrix,
ROC curve | | 05 — Random Forest | Feature importance, OOB error curve, comparison with single tree | | 06 — SVM |
Decision boundary (2D), kernel comparison, grid search heatmap | | 07 — Clustering | Elbow curve, cluster visualization
(PCA 2D), dendrogram | | 08 — Dimensionality Reduction | Explained variance (PCA), PCA vs t-SNE scatter, component
loadings | | 09 — Model Evaluation | Learning curves, cross-validation box plots, ROC multi-class |

______________________________________________________________________

## Dataset Standards

### Priority Order

1. **sklearn built-in** — sem download, totalmente reproduzível (`load_digits`, `load_iris`, etc.)
1. **Synthetic** — gerado in-notebook com parâmetros documentados
1. **UCI via ucimlrepo** — `from ucimlrepo import fetch_ucirepo`
1. **External download** — fornecer URL direta e checksum

### Data Exploration Template

Toda aula deve incluir esta sequência antes de qualquer step de ML:

```python
print(f"Dataset shape: {X.shape}")
print(f"Classes: {np.unique(y)}")
print(f"Class distribution:\n{pd.Series(y).value_counts()}")
df.describe()
```

______________________________________________________________________

## Engagement Elements

### Required per Class

- **✍️ Handwriting Connection** — markdown cell conectando o algoritmo à análise de escrita manual
- **🔬 Hands-On Exercise** — no mínimo 3 cells "Try This" com mudanças específicas de parâmetro
- **🤔 Think About It** — 2–3 perguntas abertas (sem código)
- **🎯 Challenge (Optional)** — exercício extra pra quem terminar cedo

### "Try This" Cell Format

```python
# ✏️ Try This: Change k from 5 to 1 and observe the effect on accuracy.
# What happens? Why does a smaller k make the model more sensitive to noise?
# model = KNeighborsClassifier(n_neighbors=1)  # Change this line
```

______________________________________________________________________

## Teacher Notes Format

Junto com cada notebook, entregar um `teacher-notes.md` com:

1. **Class Overview** — duração, target audience, objetivo
1. **Pre-Class Checklist** — pacotes a verificar, dados a pré-baixar
1. **Concept Explanations** — cada biblioteca e algoritmo explicado pro instrutor
1. **Timing Guide** — breakdown minuto a minuto pra sessão de 90 minutos
1. **Common Student Questions** — Qs antecipadas com respostas sugeridas
1. **Troubleshooting** — top 5 erros prováveis e soluções
1. **Assignment Details** — outcomes esperados, rubrica se aplicável

______________________________________________________________________

## Request Format for Lucca

Ao solicitar uma aula, usar:

```
Generate Class [X]: [Topic Name]
- Focus areas: [aspectos específicos a enfatizar]
- Dataset preference: [se diferente do default do README]
- Special requirements: [qualquer outra coisa]
```

Exemplo:

```
Generate Class 02: Decision Trees & Letter Recognition
- Focus areas: feature importance visualization, overfitting via depth
- Dataset preference: UCI letter recognition (via ucimlrepo)
- Special requirements: include tree depth comparison (depth=3 vs depth=10)
```

______________________________________________________________________

## Quality Checklist

Antes de entregar qualquer material de aula:

**Content**

- [ ] Todos os learning objectives do README estão endereçados
- [ ] Timing cabe em 90 minutos (testar lendo)
- [ ] Conexão com escrita manual/forense é clara e convincente
- [ ] Nível de dificuldade é apropriado (constrói sobre aulas anteriores)

**Technical**

- [ ] Todas as cells rodam top-to-bottom sem erros
- [ ] `random_state=42` em todas as operações estocásticas
- [ ] Todas as funções têm type annotations
- [ ] Sem dead code ou TODOs
- [ ] No mínimo 3 plots com eixos rotulados, títulos e interpretação

**Pedagogical**

- [ ] No mínimo 3 elementos interativos "Try This"
- [ ] 2–3 perguntas "Think About It"
- [ ] Assignment é específico e acionável
- [ ] Preview da próxima aula incluído

**Glossary**

- [ ] Todos os termos técnicos no `README.md` da aula linkados ao `GLOSSARY.md` via anchors relativos (ex.:
  `[overfitting](../GLOSSARY.md#overfitting-sobreajuste)`)
- [ ] `GLOSSARY.md` atualizado com todo novo termo introduzido nesta aula (na seção `## Aula XX` correta)
- [ ] Índice do glossário no topo do `GLOSSARY.md` inclui a nova seção

______________________________________________________________________

## Agents

- **Lucca** ([.claude/agents/lucca.md](.claude/agents/lucca.md)) — criação de conteúdo (notebooks, exercícios,
  teacher-notes)
- **Magus** ([.claude/agents/magus.md](.claude/agents/magus.md)) — respostas a dúvidas conceituais

## Skills

### evaluate-user

**Path:** [.claude/skills/evaluate-user/SKILL.md](.claude/skills/evaluate-user/SKILL.md)

Invocada **obrigatoriamente ao final de toda resposta** pelos agentes Magus e Lucca. Analisa a interação atual e
atualiza [.claude/instructions/user.md](.claude/instructions/user.md). Ler o `SKILL.md` para instruções completas de
execução.
