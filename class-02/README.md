# Aula 02: Árvores de Decisão & Reconhecimento de Letras

## Objetivo da Aula

Aplicar Árvores de Decisão ao reconhecimento de letras (A–Z), com foco em interpretabilidade do modelo e análise de
importância de features. Ao final, o aluno deve entender como uma árvore toma decisões e como detectar overfitting.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Explicar como uma Árvore de Decisão divide o espaço de features
- Treinar uma `DecisionTreeClassifier` e interpretar sua estrutura
- Visualizar e interpretar o gráfico da árvore
- Analisar a importância das features para identificar letras
- Identificar overfitting variando a profundidade da árvore
- Comparar o comportamento de árvores rasas vs. profundas

______________________________________________________________________

## Algoritmo: Decision Tree

A [Árvore de Decisão](../GLOSSARY.md#árvore-de-decisão-decision-tree) aprende regras de divisão do tipo "se feature X > valor, então vai para esquerda" — exatamente como um
fluxograma de decisão. Cada nó divide os dados em grupos mais homogêneos, usando o [índice Gini](../GLOSSARY.md#índice-gini-gini-index) como critério de divisão.

**Intuição para escrita:** é como um perito grafista aplicando regras observáveis: "se a proporção altura/largura é alta
E o número de pixels no quadrante superior esquerdo é baixo, então provavelmente é a letra 'i'".

**Parâmetros chave:**

- `max_depth`: profundidade máxima — controla complexidade e risco de [overfitting](../GLOSSARY.md#overfitting-sobreajuste)
- `criterion`: métrica de impureza ([índice Gini](../GLOSSARY.md#índice-gini-gini-index) ou `entropy`)
- `min_samples_split`: mínimo de amostras para dividir um nó

______________________________________________________________________

## Dataset: Letter Recognition (UCI)

- **Origem:** UCI Machine Learning Repository — via pacote `ucimlrepo`
- **Tamanho:** 20.000 amostras
- **Features:** 16 features estatísticas extraídas de imagens de letras (proporções, momentos, distribuição de pixels)
- **Classes:** 26 (letras A–Z)
- **Acurácia esperada:** ~85–90% com árvore de profundidade moderada

______________________________________________________________________

## Conceitos-Chave

- **[Interpretabilidade](../GLOSSARY.md#interpretabilidade-interpretability):** ao contrário do k-NN, a Árvore de Decisão explica *por que* classificou assim
- **[Importância de features](../GLOSSARY.md#importância-de-features-feature-importance):** quais medidas da escrita são mais discriminativas para identificar letras
- **[Overfitting](../GLOSSARY.md#overfitting-sobreajuste):** uma árvore muito profunda "memoriza" o treino mas falha no teste
- **[Bias-variance tradeoff](../GLOSSARY.md#bias-variance-tradeoff):** profundidade baixa = alto bias; profundidade alta = alta variância
- **Regras de divisão:** cada nó aplica um limiar em uma [feature](../GLOSSARY.md#feature-atributo) para separar classes

______________________________________________________________________

## Resultados Esperados

- Acurácia com profundidade 5: ~75%
- Acurácia com profundidade irrestrita: ~85–88% (treino ~100%)
- Features mais importantes: geralmente proporções de tamanho e distribuição de pixels nos quadrantes
- Letras mais confundidas: pares visualmente similares (D/O, I/J, C/G)

______________________________________________________________________

## Tarefa

1. **Experimentar** com profundidades 2, 5, 10, 20 e plotar a curva de acurácia treino vs. teste
1. **Identificar** as 3 features mais importantes e formular uma hipótese sobre o que elas representam na escrita
1. **Reflexão:** por que a interpretabilidade de uma Árvore de Decisão é valiosa em análise forense de documentos?

______________________________________________________________________

## Dependências (Aula 02)

| Pacote | Uso na aula |
|---|---|
| `scikit-learn` | `DecisionTreeClassifier`, `train_test_split`, `plot_tree`, métricas |
| `ucimlrepo` | Download do dataset Letter Recognition |
| `numpy` | Manipulação de arrays |
| `matplotlib` | Visualização da árvore, curvas de acurácia |
| `seaborn` | [Matriz de confusão](../GLOSSARY.md#matriz-de-confusão-confusion-matrix), gráfico de [importância de features](../GLOSSARY.md#importância-de-features-feature-importance) |
| `pandas` | Exploração do dataset |
