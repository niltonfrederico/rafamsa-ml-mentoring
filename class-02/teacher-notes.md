# Teacher Notes — Aula 02: Árvores de Decisão & Reconhecimento de Letras

## 1. Visão Geral da Aula

| Item | Detalhe |
|---|---|
| **Duração** | 90 minutos |
| **Público** | Alunos com Python, sem domínio prévio de ML |
| **Algoritmo** | `DecisionTreeClassifier` (scikit-learn) |
| **Dataset** | UCI Letter Recognition — 20.000 amostras, 16 features, 26 classes |
| **Meta pedagógica** | Conectar interpretabilidade do modelo com aplicações forenses reais |

---

## 2. Checklist Pré-Aula

- [ ] Verificar que `ucimlrepo` está instalado: `pip install ucimlrepo`
- [ ] Rodar `fetch_ucirepo(id=59)` pelo menos uma vez antes da aula para popular o cache local
- [ ] Confirmar que o Jupyter Lab abre e executa `import sklearn` sem erro
- [ ] Ter este arquivo de notas aberto em paralelo ao notebook durante a aula

### Instalação do pacote `ucimlrepo`

```bash
pip install ucimlrepo
```

O download do dataset ocorre na primeira execução da célula `fetch_ucirepo(id=59)`. Demora ~5 segundos com boa conexão.
Nas execuções seguintes, usa cache local em `~/.cache/ucimlrepo/`.

---

## 3. Conceitos para o Instrutor

### Árvore de Decisão — Intuição

A árvore cria um fluxograma. Cada nó faz uma pergunta binária sobre uma feature: "feature X > limiar?". O algoritmo
escolhe a feature e o limiar que maximiza a **redução de impureza** — o quanto as duas metades ficam mais "puras" (com
uma classe dominante) após a divisão.

**Analogia para os alunos:** É como um jogo de 20 perguntas, onde o modelo aprendeu quais perguntas são mais eficientes
para identificar cada letra.

### Índice Gini

$$G = 1 - \sum_{i=1}^{C} p_i^2$$

onde $p_i$ é a proporção de amostras da classe $i$ no nó. $G = 0$ → nó puro. $G \approx 0.5$ → máxima impureza
(classes uniformes).

**Não é necessário derivar a fórmula em aula.** Basta que os alunos entendam: Gini mede quão "misturadas" estão as
classes num nó. A árvore quer minimizar o Gini em cada divisão.

### Overfitting em Árvores

Com `max_depth=None`, a árvore cresce até cada folha ter uma única amostra → acurácia de treino = 100%. Isso é
**overfitting puro**: o modelo memorizou o ruído do treino e não generaliza.

O `max_depth` é o regularizador primário. Outros regularizadores úteis: `min_samples_split`, `min_samples_leaf`,
`max_leaf_nodes`.

### Feature Importance

`feature_importances_[i]` = soma ponderada das reduções de Gini que a feature $i$ causou em todos os nós da árvore,
normalizada para somar 1. Intuitivamente: features com alto valor foram "úteis" em muitas divisões.

**Limitação importante:** features correlacionadas entre si tendem a "dividir" a importância. Se duas features forem
quase idênticas, cada uma parecerá menos importante individualmente.

---

## 4. Guia de Timing da Aula

| Minuto | Atividade |
|---|---|
| 0–5 | Revisão da Aula 01 — o que foi k-NN? O que aprendemos? |
| 5–15 | Motivação: de dígitos para letras, por que interpretabilidade importa |
| 15–20 | Células de import e verificação de ambiente |
| 20–30 | Carregamento e exploração do dataset — Plot 1 (distribuição de classes) |
| 30–45 | Baseline (depth irrestrita), sweep de profundidade — Plot 2 (curva treino vs. teste) |
| 45–55 | Modelo com melhor profundidade, classification report |
| 55–65 | Visualização da árvore (plot_tree) + Plot 3 (feature importance) |
| 65–75 | Confusion matrix — identificação de pares problemáticos |
| 75–85 | Try This 1–3 (os alunos executam, observe os resultados) |
| 85–90 | Parte 3: Discussão, Think About It, Tarefa e Preview da Aula 03 |

---

## 5. Perguntas Comuns dos Alunos

**P: "Por que acurácia de treino 100% é ruim?"**
R: Porque indica que o modelo memorizou o treino mas provavelmente não vai funcionar bem em dados novos. Analogia: é
como decorar as respostas de uma prova em vez de aprender o conteúdo — você vai bem nessa prova, mas falha em qualquer
variação das perguntas.

**P: "Qual a diferença entre Gini e Entropy na prática?"**
R: Muito pequena. Gini é computacionalmente mais rápido. Para a maioria dos datasets, a diferença de acurácia é < 0.5%.
Gini é o padrão do sklearn por isso.

**P: "Por que usar `stratify=y` no split?"**
R: Para garantir que as 26 classes estejam representadas proporcionalmente tanto no treino quanto no teste. Sem isso,
por azar, uma classe poderia estar sub-representada no teste, distorcendo a avaliação de acurácia por classe.

**P: "A importância de feature é absoluta ou depende da árvore?"**
R: Depende totalmente da árvore. Muda com `max_depth`, `random_state`, etc. Não é uma propriedade intrínseca do
dataset. Para estimativas mais robustas de importância de feature, usamos Florestas Aleatórias (Aula 05).

**P: "Por que D e O são confundidas se são letras bem diferentes visualmente?"**
R: Porque as 16 features são medidas das *imagens digitalizadas*, não dos glifos como os humanos os percebem. Uma letra
'D' e uma 'O' podem ter centróides e distribuição de pixels muito similares — a diferença que *nós* percebemos (o lado
reto do D) pode não estar capturada eficientemente nessas 16 features.

---

## 6. Troubleshooting

| Erro | Causa Provável | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'ucimlrepo'` | Pacote não instalado | `pip install ucimlrepo` |
| `ConnectionError` no `fetch_ucirepo` | Sem internet ou servidor UCI indisponível | Usar dataset alternativo: `pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data', header=None)` |
| `ValueError: X has N features but DecisionTreeClassifier expects M` | Features de treino e teste inconsistentes (Try This 3) | Verificar que os índices `top_indices` são aplicados em ambos X_train e X_test |
| Plot da árvore em branco ou muito pequeno | `figsize` insuficiente | Aumentar para `(36, 12)` ou reduzir `max_depth` no `plot_tree` |
| Acurácia abaixo de 80% com `best_depth` | Variação aleatória por `random_state` diferente | Normal — usar `random_state=42` como instruído garante reprodutibilidade |

### Dataset offline (fallback)

Se o UCI estiver inacessível, substitua a célula de carregamento por:

```python
import io
import urllib.request

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data"
col_names = ["lettr", "x-box", "y-box", "width", "high", "onpix",
             "x-bar", "y-bar", "x2bar", "y2bar", "xybar",
             "x2ybr", "xy2br", "x-ege", "xegvy", "y-ege", "yegvx"]
df = pd.read_csv(url, header=None, names=col_names)
X_raw = df.drop(columns=["lettr"])
y_raw = df["lettr"]
```

---

## 7. Detalhes da Tarefa

### Opção A — Heatmap de Hiperparâmetros (Experimental)

**Resultado esperado:** acurácia máxima no teste em torno de `max_depth=12–16` e qualquer `criterion`. A heatmap deve
mostrar claramente que profundidades muito baixas (< 5) têm acurácia baixa independentemente do critério, e que `gini`
vs `entropy` fazem pouca diferença.

**Critérios de avaliação:**

- Código funcional que treina os 8 modelos (4 depths × 2 criteria)
- Heatmap com eixos rotulados e título
- Comentário sobre qual combinação maximiza o teste e por que

### Opção B — Reflexão Forense

**Resposta esperada:** O aluno deve identificar que uma Árvore de Decisão pode gerar automaticamente um caminho de
decisão (da raiz até a folha) como "prova" — "a letra foi identificada como X porque: feature A > 3.5 E feature B ≤
7.2 E feature C > 1.0". As limitações incluem: features podem não ter interpretação semântica clara, overfitting pode
tornar regras específicas demais para generalização, e o modelo não captura incerteza (não fornece probabilidades
calibradas).

---

## 8. Conexão entre as Aulas

| Aula | Algoritmo | Contribuição para o Tema |
|---|---|---|
| 01 | k-NN | Baseline de classificação, sem interpretabilidade |
| **02** | **Decision Tree** | **Regras explícitas, feature importance, overfitting** |
| 03 | Linear Regression | Previsão de valores contínuos (pressão de caneta) |
| 05 | Random Forest | Ensemble de árvores — resolve overfitting da Aula 02 |
