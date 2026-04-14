# Aula 04: Regressão Logística & Classificação de Escritores

## Objetivo da Aula

Introduzir classificação binária probabilística com Regressão Logística, aplicada à predição de características do
escritor a partir de features de escrita. O aluno aprende a interpretar saídas probabilísticas e a avaliar
classificadores binários com métricas além da acurácia.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Distinguir Regressão Logística de Regressão Linear (classificação vs. predição contínua)
- Entender a função sigmoide e como ela converte scores em probabilidades
- Treinar e interpretar um `LogisticRegression` do sklearn
- Ler e interpretar uma matriz de confusão (TP, TN, FP, FN)
- Calcular e interpretar precisão, recall, F1 e AUC-ROC
- Entender quando acurácia sozinha é uma métrica enganosa (classes desbalanceadas)

______________________________________________________________________

## Algoritmo: Logistic Regression

A Regressão Logística aplica a função sigmoide à saída de um modelo linear, transformando scores em probabilidades entre
0 e 1. A fronteira de decisão é linear no espaço de features.

**Intuição para escrita:** ao invés de "sim/não" direto, o modelo retorna "há 78% de probabilidade de que este escritor
seja da categoria X". Isso é útil em contextos forenses onde a incerteza importa.

**Parâmetros chave:**

- `C`: inverso da regularização — valores menores = mais regularização = modelo mais simples
- `max_iter`: número de iterações para convergência (aumentar se o modelo não convergir)
- `class_weight='balanced'`: útil em datasets desbalanceados

______________________________________________________________________

## Dataset: Features de Escrita com Grupos de Escritores

- **Origem:** Gerado sinteticamente em aula
- **Tamanho:** ~400 amostras, 2 grupos de escritores com padrões distintos
- **Features:** pressão, tamanho de caracteres, inclinação, velocidade, regularidade do traço
- **Target:** grupo do escritor (classificação binária)
- **Nota:** o dataset sintético é construído para ter fronteira de decisão aproximadamente linear

______________________________________________________________________

## Estrutura da Aula (90 min)

| Bloco | Tempo | Conteúdo | |---|---|---| | Setup & Motivação | 15 min | Do contínuo para o binário: motivação
probabilística, geração do dataset | | Implementação Prática | 55 min | Função sigmoide, treino do modelo, matriz de
confusão, curva ROC, análise de coeficientes | | Interpretação & Discussão | 15 min | Quando confiar na probabilidade?
Trade-off precisão/recall, casos de uso forenses | | Encerramento & Preview | 5 min | Conceitos-chave, tarefa, prévia de
Random Forest (Aula 05) |

______________________________________________________________________

## Conceitos-Chave

- **Função sigmoide:** transforma qualquer valor real em probabilidade (0–1)
- **Threshold de decisão:** padrão é 0.5, mas pode ser ajustado conforme o contexto
- **Matriz de confusão:** TP, TN, FP, FN — base para todas as métricas de classificação binária
- **Precisão:** dos que o modelo disse "positivo", quantos realmente eram?
- **Recall (sensibilidade):** dos que eram realmente "positivo", quantos o modelo pegou?
- **AUC-ROC:** mede a capacidade discriminativa do modelo independente do threshold
- **Regularização:** penalização de coeficientes grandes para evitar overfitting

______________________________________________________________________

## Resultados Esperados

- Acurácia esperada: ~82–90%
- AUC-ROC: ~0.88–0.93
- Coeficiente com maior magnitude: a feature mais discriminante entre os grupos

______________________________________________________________________

## Tarefa

1. **Experimentar** com diferentes thresholds de decisão (0.3, 0.5, 0.7) e observar o impacto em precisão vs. recall
1. **Comparar** com k-NN da Aula 01: qual tem melhor AUC neste dataset? Por quê?
1. **Reflexão:** em análise forense de documentos, você prefere um modelo com alta precisão ou alto recall? Justifique.

______________________________________________________________________

## Dependências (Aula 04)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `LogisticRegression`, `train_test_split`, `confusion_matrix`,
`roc_curve`, `roc_auc_score` | | `numpy` | Geração de dados sintéticos, cálculo da sigmoide | | `matplotlib` | Curva
ROC, sigmoide, visualização de fronteira de decisão | | `seaborn` | Heatmap da matriz de confusão | | `pandas` | Análise
do dataset, coeficientes do modelo |
