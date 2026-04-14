# Aula 09: Avaliação de Modelos & Validação

## Objetivo da Aula

Consolidar as estratégias corretas de avaliação e validação de modelos ML aplicadas ao sistema de reconhecimento de
escrita construído ao longo do curso. O aluno aprende a comparar modelos de forma rigorosa, a entender o trade-off
bias-variância e a escolher o melhor modelo para um problema real.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Aplicar k-fold cross-validation corretamente e interpretar os resultados
- Traçar e interpretar curvas de aprendizado (learning curves)
- Analisar o trade-off bias-variância para cada algoritmo visto no curso
- Usar testes estatísticos simples para comparar modelos com significância
- Evitar os erros mais comuns de avaliação (data leakage, overfitting no conjunto de teste)
- Selecionar o algoritmo mais adequado para identificação de escritores com base em evidências

______________________________________________________________________

## Foco: Avaliação Rigorosa

Esta aula não introduz um novo algoritmo — ela aprofunda como avaliar corretamente todos os algoritmos vistos. A
avaliação honesta é tão importante quanto a escolha do algoritmo.

______________________________________________________________________

## Estratégias de Avaliação

### K-Fold Cross-Validation

Divide os dados em `k` folds, treinando `k` vezes — cada vez com um fold diferente como conjunto de teste. A média dos
scores é uma estimativa mais robusta que um único treino/teste.

**Quando usar:**

- Sempre que o dataset for pequeno o suficiente para que uma única divisão seja instável
- Para comparação justa entre algoritmos

### Stratified K-Fold

Versão do K-Fold que garante que cada fold tem a mesma proporção de classes. Essencial para datasets desbalanceados.

### Learning Curves

Plotar acurácia de treino e validação em função do tamanho do dataset de treino. Revela se o modelo sofre de alto bias
(underfitting) ou alta variância (overfitting).

**Diagnóstico:**

- Treino alto, validação baixa → alta variância → mais dados ou regularização
- Treino e validação ambos baixos → alto bias → modelo mais complexo ou mais features

### Testes Estatísticos (McNemar, Wilcoxon)

Para comparar dois modelos com significância estatística — confirmar que a diferença de performance não é aleatória.

______________________________________________________________________

## Dataset: Consolidação

- **Origem:** Combinação dos datasets usados ao longo do curso
- **Tamanho:** ~1.000 amostras de 6 escritores
- **Features:** features completas de escrita (20 dimensões, após PCA da Aula 08)
- **Classes:** 6 escritores

______________________________________________________________________

## Estrutura da Aula (90 min)

| Bloco | Tempo | Conteúdo | |---|---|---| | Setup & Motivação | 15 min | "Por que nossa avaliação até agora pode ter
sido otimista?" — armadilhas comuns, review do curso | | Implementação Prática | 55 min | Cross-validation comparativa
(k-NN, DT, RF, SVM), learning curves, teste de McNemar, pipeline correto | | Interpretação & Discussão | 15 min | Qual
modelo vence? Com que significância? O que as learning curves revelam sobre cada algoritmo? | | Encerramento & Preview |
5 min | Síntese do curso, próximos passos em ML, recursos recomendados |

______________________________________________________________________

## Conceitos-Chave

- **Data leakage:** quando informação do conjunto de teste "vaza" para o treino — principal fonte de avaliação inflada
- **Pipeline sklearn:** encapsula pré-processamento + modelo para garantir que o escalonamento seja treinado apenas nos
  dados de treino
- **Nested cross-validation:** cross-validation externo para avaliação + interno para seleção de hiperparâmetros — evita
  data leakage em Grid Search
- **Bias-variância tradeoff:** todo modelo equilibra complexidade (risco de overfitting) vs. simplicidade (risco de
  underfitting)
- **Significância estatística:** uma diferença de 1% na acurácia pode ser ruído — testes estatísticos confirmam se é
  real
- **Generalização:** o objetivo final não é acurácia no conjunto de teste histórico, mas em dados reais futuros

______________________________________________________________________

## Comparação Final dos Modelos (Resultados Esperados)

| Modelo | CV Acurácia (média ± std) | Bias | Variância | |---|---|---|---| | k-NN (k=5) | ~87% ± 3% | Baixo | Médio | |
Árvore de Decisão | ~79% ± 5% | Médio | Alto | | Random Forest | ~91% ± 2% | Baixo | Baixo | | SVM (RBF otimizado) |
~93% ± 2% | Baixo | Baixo |

______________________________________________________________________

## Tarefa Final do Curso

1. **Selecionar** o melhor modelo com base na análise cross-validation desta aula
1. **Treinar** o modelo selecionado em todos os dados disponíveis (treino + validação)
1. **Documentar:** um parágrafo justificando a escolha do modelo com base em evidências
1. **Reflexão final:** quais limitações esse sistema de identificação de escritores ainda tem? Que dados adicionais
   melhorariam o desempenho?

______________________________________________________________________

## Dependências (Aula 09)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `cross_val_score`, `StratifiedKFold`, `learning_curve`,
`Pipeline`, `StandardScaler` | | `scipy` | `wilcoxon` para teste estatístico de comparação de modelos | | `numpy` |
Manipulação de arrays, estatísticas | | `matplotlib` | Learning curves, boxplot de cross-validation, comparação de
modelos | | `seaborn` | Visualização de distribuição de scores | | `pandas` | Tabela de resultados comparativos |
