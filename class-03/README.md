# Aula 03: Regressão Linear & Métricas de Escrita

## Objetivo da Aula

Transição de [classificação](../GLOSSARY.md#classifica%C3%A7%C3%A3o-classification) para
[regressão](../GLOSSARY.md#regress%C3%A3o-regression): prever valores contínuos (velocidade de escrita) a partir de
features de escrita (pressão, tamanho dos caracteres). O aluno aprende a diferença entre classificar e regredir, e a
interpretar métricas de regressão.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Distinguir [classificação](../GLOSSARY.md#classifica%C3%A7%C3%A3o-classification) de
  [regressão](../GLOSSARY.md#regress%C3%A3o-regression) (prever categoria vs. valor contínuo)
- Aplicar [Regressão Linear](../GLOSSARY.md#regress%C3%A3o-linear-linear-regression) simples e múltipla
- Calcular e interpretar [R²](../GLOSSARY.md#r%C2%B2-coeficiente-de-determina%C3%A7%C3%A3o),
  [RMSE](../GLOSSARY.md#rmse-root-mean-squared-error) e [análise de resíduos](../GLOSSARY.md#res%C3%ADduos-residuals)
- Realizar análise de [correlação de Pearson](../GLOSSARY.md#correla%C3%A7%C3%A3o-de-pearson-pearson-correlation) entre
  [features](../GLOSSARY.md#feature-atributo) de escrita
- Comparar o poder preditivo de diferentes features
- Compreender os [coeficientes](../GLOSSARY.md#coeficiente-coefficient) do modelo como pesos das features

______________________________________________________________________

## Algoritmo: Linear Regression

A [Regressão Linear](../GLOSSARY.md#regress%C3%A3o-linear-linear-regression) encontra a linha (ou hiperplano, no caso
multivariado) que minimiza a soma dos erros quadráticos entre os valores previstos e os reais.

**Intuição para escrita:** a relação entre pressão exercida na caneta e velocidade de escrita tende a ser
aproximadamente linear — quanto maior a pressão, mais lento o traço. A regressão quantifica essa relação.

**Parâmetros chave:**

- `fit_intercept`: se deve ajustar um [intercepto](../GLOSSARY.md#intercepto-intercept) (quase sempre `True`)
- Sem [hiperparâmetros](../GLOSSARY.md#hiperpar%C3%A2metro-hyperparameter) de complexidade — o risco de
  [overfitting](../GLOSSARY.md#overfitting-sobreajuste) é menor que em modelos não-paramétricos

______________________________________________________________________

## Dataset: Métricas de Escrita (Sintético)

- **Origem:** Gerado sinteticamente em aula — nenhum download necessário
- **Tamanho:** ~300 sessões de escrita de 15 escritores diferentes
- **Features:** pressão da caneta, tamanho médio dos caracteres, velocidade do traço, inclinação
- **Target:** velocidade de escrita (valor contínuo, em cm/s)
- **Motivação pedagógica:** dados sintéticos permitem controlar a relação entre variáveis e confirmar se o modelo
  aprendeu a relação correta

______________________________________________________________________

## Conceitos-Chave

- **[Regressão](../GLOSSARY.md#regress%C3%A3o-regression):** previsão de valor contínuo (não uma categoria)
- **[R² (coeficiente de determinação)](../GLOSSARY.md#r%C2%B2-coeficiente-de-determina%C3%A7%C3%A3o):** proporção da
  variância do target explicada pelo modelo (0 = nada, 1 = perfeito)
- **[RMSE](../GLOSSARY.md#rmse-root-mean-squared-error):** erro médio em unidades do target — mais intuitivo que MSE
- **[Resíduos](../GLOSSARY.md#res%C3%ADduos-residuals):** diferença entre valor real e previsto — padrões nos resíduos
  indicam que o modelo perdeu alguma relação
- **[Correlação de Pearson](../GLOSSARY.md#correla%C3%A7%C3%A3o-de-pearson-pearson-correlation):** mede a força da
  relação linear entre duas variáveis
- **[Multicolinearidade](../GLOSSARY.md#multicolinearidade-multicollinearity):** quando features correlacionadas entre
  si comprometem a interpretação dos coeficientes

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

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `LinearRegression`,
[`train_test_split`](../GLOSSARY.md#train_test_split), métricas de regressão | | `numpy` | Geração de dados sintéticos,
operações numéricas | | `matplotlib` | Scatter plots, linha de regressão, gráfico de
[resíduos](../GLOSSARY.md#res%C3%ADduos-residuals) | | `seaborn` | Heatmap de
[correlação](../GLOSSARY.md#correla%C3%A7%C3%A3o-de-pearson-pearson-correlation), pairplot | | `pandas` | DataFrame,
estatísticas descritivas | | `scipy` | Testes de correlação (`pearsonr`, `spearmanr`) |
