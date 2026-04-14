# Aula 03: Regressão Linear & Métricas de Escrita

## Objetivo da Aula

Transição de classificação para regressão: prever valores contínuos (velocidade de escrita) a partir de features de
escrita (pressão, tamanho dos caracteres). O aluno aprende a diferença entre classificar e regredir, e a interpretar
métricas de regressão.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Distinguir classificação de regressão (prever categoria vs. valor contínuo)
- Aplicar Regressão Linear simples e múltipla
- Calcular e interpretar R², RMSE e análise de resíduos
- Realizar análise de correlação entre features de escrita
- Comparar o poder preditivo de diferentes features
- Compreender os coeficientes do modelo como pesos das features

______________________________________________________________________

## Algoritmo: Linear Regression

A Regressão Linear encontra a linha (ou hiperplano, no caso multivariado) que minimiza a soma dos erros quadráticos
entre os valores previstos e os reais.

**Intuição para escrita:** a relação entre pressão exercida na caneta e velocidade de escrita tende a ser
aproximadamente linear — quanto maior a pressão, mais lento o traço. A regressão quantifica essa relação.

**Parâmetros chave:**

- `fit_intercept`: se deve ajustar um intercepto (quase sempre `True`)
- Sem hiperparâmetros de complexidade — o risco de overfitting é menor que em modelos não-paramétricos

______________________________________________________________________

## Dataset: Métricas de Escrita (Sintético)

- **Origem:** Gerado sinteticamente em aula — nenhum download necessário
- **Tamanho:** ~300 sessões de escrita de 15 escritores diferentes
- **Features:** pressão da caneta, tamanho médio dos caracteres, velocidade do traço, inclinação
- **Target:** velocidade de escrita (valor contínuo, em cm/s)
- **Motivação pedagógica:** dados sintéticos permitem controlar a relação entre variáveis e confirmar se o modelo
  aprendeu a relação correta

______________________________________________________________________

## Estrutura da Aula (90 min)

| Bloco | Tempo | Conteúdo | |---|---|---| | Setup & Motivação | 15 min | Classificação vs. regressão, geração do
dataset sintético, exploração | | Implementação Prática | 55 min | Correlação, regressão simples (pressão → velocidade),
regressão múltipla, análise de resíduos | | Interpretação & Discussão | 15 min | Interpretação dos coeficientes, padrões
individuais por escritor, limitações do modelo linear | | Encerramento & Preview | 5 min | Conceitos-chave, tarefa,
prévia de Regressão Logística (Aula 04) |

______________________________________________________________________

## Conceitos-Chave

- **Regressão:** previsão de valor contínuo (não uma categoria)
- **R² (coeficiente de determinação):** proporção da variância do target explicada pelo modelo (0 = nada, 1 = perfeito)
- **RMSE:** erro médio em unidades do target — mais intuitivo que MSE
- **Resíduos:** diferença entre valor real e previsto — padrões nos resíduos indicam que o modelo perdeu alguma relação
- **Correlação de Pearson:** mede a força da relação linear entre duas variáveis
- **Multicolinearidade:** quando features correlacionadas entre si comprometem a interpretação dos coeficientes

______________________________________________________________________

## Resultados Esperados

- R² da regressão simples (pressão → velocidade): ~0.65–0.75
- R² da regressão múltipla (pressão + tamanho → velocidade): ~0.80–0.88
- Coeficiente da pressão: negativo (mais pressão = menos velocidade)
- Coeficiente do tamanho: negativo (caracteres maiores = mais lentos)

______________________________________________________________________

## Tarefa

1. **Explorar** a correlação entre todas as features do dataset e o target
1. **Construir** modelos com 1, 2 e 3 features e comparar R²
1. **Reflexão:** em análise forense de escrita, que métricas contínuas seriam mais úteis de prever? Por quê?

______________________________________________________________________

## Dependências (Aula 03)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `LinearRegression`, `train_test_split`, métricas de regressão | |
`numpy` | Geração de dados sintéticos, operações numéricas | | `matplotlib` | Scatter plots, linha de regressão, gráfico
de resíduos | | `seaborn` | Heatmap de correlação, pairplot | | `pandas` | DataFrame, estatísticas descritivas | |
`scipy` | Testes de correlação (`pearsonr`, `spearmanr`) |
