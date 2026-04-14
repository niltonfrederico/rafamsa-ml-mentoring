# Content Creation Instructions for ML Classes

## User Profile

All agents (Magus and Lucca) must read `.github/instructions/user.instructions.md` at the start of every interaction and
calibrate depth, vocabulary, and pedagogical approach accordingly. This file is maintained by the `evaluate-user` skill
and accumulates knowledge about the user across all sessions.

______________________________________________________________________

## Context

This course is a hands-on machine learning mentoring programme focused on **Handwriting Recognition & Person
Identification** using scikit-learn. Students have Python knowledge and understand basic ML mathematics. Each class is
**1 hour and 30 minutes (90 minutes)**.

The course runs for **9 classes**. Every class delivers one complete, working Jupyter notebook that a student can run
top-to-bottom without error.

______________________________________________________________________

## Class Structure (90 minutes)

Every class must follow this structure exactly:

```
Part 1: Setup & Motivation    — 15 minutes
Part 2: Hands-On Implementation — 55 minutes
Part 3: Interpretation & Discussion — 15 minutes
Part 4: Wrap-up & Preview     —  5 minutes
```

### Part 1: Setup & Motivation (15 min)

- Quick review of the previous class (what was built, what was learned)
- Introduce the handwriting/document analysis problem this class solves
- Dataset overview: load, inspect shape, show sample records/images
- State the 2–4 learning objectives for this class clearly

### Part 2: Hands-On Implementation (55 min)

- Step-by-step coding — no large jumps, every block is explained
- Follow this progression every time:
  1. Import libraries (with one-line explanation of each)
  1. Load and explore data (shape, dtypes, sample rows, basic stats)
  1. Simple implementation first — get a baseline working
  1. Add complexity incrementally (features, tuning, evaluation)
  1. Evaluate and visualize results
- Include at least 3 "Try This" cells: parameter changes the student should run
- Include at least 3 plots (see Visualization Requirements below)

### Part 3: Interpretation & Discussion (15 min)

- Analyze the results: what worked, what didn't, why
- Identify misclassification patterns or surprising outputs
- Connect findings to real-world handwriting analysis or forensic applications
- Address the most common student misconceptions for this algorithm
- Include 2–3 "Think About It" questions (no code required, open discussion)

### Part 4: Wrap-up & Preview (5 min)

- Key concepts summary (bullet list, max 5 items)
- Assignment: one of:
  - Experiment: modify a hyperparameter and observe the effect
  - Explore: apply the technique to a different dataset or subset
  - Reflect: connect the algorithm to a real-world scenario
- Next class teaser: one sentence on what comes next

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

- Type annotations on all function parameters and return types
- One import per line, absolute paths only — never `from . import something`
- `random_state=42` on all stochastic operations (train_test_split, classifiers, etc.)
- Meaningful variable names with handwriting context:
  - `writer_id`, `pen_pressure`, `stroke_width`, `character_features`
  - `X_train`, `X_test`, `y_train`, `y_test` (standard ML convention)
- No dead code, no commented-out blocks, no TODO comments in delivered notebooks

### Standard sklearn Pattern

Always follow this pattern:

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

Include import verification and data loading checks in the first cell:

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

- Minimum 3 plots per class
- Every plot must have:
  - Title
  - Labeled axes (with units where applicable)
  - Legend if multiple series
  - A markdown cell below interpreting what the student should observe
- Use `seaborn` for statistical/distribution plots
- Use `matplotlib` for custom visualizations (images, confusion matrices, decision boundaries)
- Color scheme: accessible (avoid red/green only — use seaborn's colorblind palette)

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

1. **sklearn built-in** — no download, fully reproducible (`load_digits`, `load_iris`, etc.)
1. **Synthetic** — generated in-notebook with documented parameters
1. **UCI via ucimlrepo** — `from ucimlrepo import fetch_ucirepo`
1. **External download** — provide direct URL and checksum

### Data Exploration Template

Every class must include this sequence before any ML step:

```python
print(f"Dataset shape: {X.shape}")
print(f"Classes: {np.unique(y)}")
print(f"Class distribution:\n{pd.Series(y).value_counts()}")
df.describe()
```

______________________________________________________________________

## Engagement Elements

### Required per Class

- **✍️ Handwriting Connection** — a markdown cell connecting the algorithm to handwriting analysis
- **🔬 Hands-On Exercise** — at least 3 "Try This" cells with specific parameter changes
- **🤔 Think About It** — 2–3 open discussion questions (no code)
- **🎯 Challenge (Optional)** — extension exercise for students who finish early

### "Try This" Cell Format

```python
# ✏️ Try This: Change k from 5 to 1 and observe the effect on accuracy.
# What happens? Why does a smaller k make the model more sensitive to noise?
# model = KNeighborsClassifier(n_neighbors=1)  # Change this line
```

______________________________________________________________________

## Teacher Notes Format

Alongside each notebook, deliver a `teacher-notes.md` with:

1. **Class Overview** — duration, target audience, goal
1. **Pre-Class Checklist** — packages to verify, any data to pre-download
1. **Concept Explanations** — each library and algorithm explained for the instructor
1. **Timing Guide** — minute-by-minute breakdown for the 90-minute session
1. **Common Student Questions** — anticipated Qs with suggested answers
1. **Troubleshooting** — top 5 likely errors and solutions
1. **Assignment Details** — expected outcomes, grading rubric if applicable

______________________________________________________________________

## Request Format for Lucca

When requesting a class, use:

```
Generate Class [X]: [Topic Name]
- Focus areas: [specific aspects to emphasize]
- Dataset preference: [if different from README default]
- Special requirements: [anything else]
```

Example:

```
Generate Class 02: Decision Trees & Letter Recognition
- Focus areas: feature importance visualization, overfitting via depth
- Dataset preference: UCI letter recognition (via ucimlrepo)
- Special requirements: include tree depth comparison (depth=3 vs depth=10)
```

______________________________________________________________________

## Quality Checklist

Before delivering any class material:

**Content**

- [ ] All learning objectives from the README are addressed
- [ ] Timing fits within 90 minutes (test by reading through)
- [ ] Handwriting/forensic connection is clear and compelling
- [ ] Difficulty level is appropriate (builds on previous classes)

**Technical**

- [ ] All cells run top-to-bottom without errors
- [ ] `random_state=42` on all stochastic operations
- [ ] All functions have type annotations
- [ ] No dead code or TODO comments
- [ ] At least 3 plots with labeled axes, titles, and interpretation

**Pedagogical**

- [ ] At least 3 "Try This" interactive elements
- [ ] 2–3 "Think About It" discussion questions
- [ ] Assignment is specific and actionable
- [ ] Next class preview included

**Glossary**

- [ ] All technical terms in the class `README.md` linked to `GLOSSARY.md` using relative anchors
  (e.g., `[overfitting](../GLOSSARY.md#overfitting-sobreajuste)`)
- [ ] `GLOSSARY.md` updated with every new term introduced in this class (under the correct `## Aula XX` section)
- [ ] Glossary index at the top of `GLOSSARY.md` includes the new section

______________________________________________________________________

## Skills

### evaluate-user

**Path:** `.github/skills/evaluate-user/SKILL.md`

Invocado **obrigatoriamente ao final de toda resposta** pelos agentes Magus e Lucca. Analisa a interação atual e
atualiza `.github/instructions/user.instructions.md`. Ler o `SKILL.md` para instruções completas de execução.
