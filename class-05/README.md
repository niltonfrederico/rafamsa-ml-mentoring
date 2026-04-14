# Aula 05: Métodos Ensemble & Random Forest

## Objetivo da Aula

Introduzir aprendizado em ensemble com Random Forest para classificação multi-classe de escritores. O aluno entende por
que combinar múltiplas árvores melhora a performance e aprende a selecionar features relevantes de forma automática.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Explicar o conceito de ensemble learning (combinação de modelos fracos)
- Entender como o Random Forest usa bootstrap sampling e random feature selection
- Treinar um `RandomForestClassifier` para identificação multi-classe de escritores
- Interpretar a importância de features calculada pela floresta
- Aplicar cross-validation para estimativa robusta de performance
- Comparar Random Forest com Árvore de Decisão simples (Aula 02)

______________________________________________________________________

## Algoritmo: Random Forest

O Random Forest treina múltiplas Árvores de Decisão em subsets aleatórios dos dados (bootstrap) e com subsets aleatórios
de features em cada divisão. A predição final é determinada por votação majoritária das árvores.

**Intuição para escrita:** é como consultar vários peritos grafistas independentes — cada um analisa aspectos diferentes
da escrita e o veredicto final é o consenso. A diversidade entre os peritos reduz erros.

**Parâmetros chave:**

- `n_estimators`: número de árvores — mais árvores = mais estável, mas mais lento
- `max_features`: número de features consideradas em cada divisão (controla diversidade)
- `max_depth`: profundidade máxima de cada árvore
- `oob_score=True`: ativa avaliação Out-of-Bag (estimativa gratuita de generalização)

______________________________________________________________________

## Dataset: Amostras de Escrita Multi-Escritor

- **Origem:** Gerado sinteticamente em aula
- **Tamanho:** ~600 amostras de 6 escritores diferentes
- **Features:** 10–15 features de escrita (pressão, tamanho, inclinação, velocidade, regularidade)
- **Classes:** 6 (identificação individual de escritores)
- **Acurácia esperada:** ~88–93% com Random Forest

______________________________________________________________________

## Conceitos-Chave

- **Ensemble learning:** combinar modelos fracos para criar um modelo forte
- **Bootstrap sampling:** treinar cada árvore em um subset aleatório com reposição dos dados
- **Out-of-Bag (OOB) score:** estimativa de generalização sem precisar de conjunto de validação separado
- **Feature importance:** média de quanto cada feature reduz a impureza nas divisões da floresta
- **Cross-validation:** k-fold CV para estimativa mais robusta da performance real
- **Variance reduction:** a diversidade entre árvores reduz a variância do ensemble

______________________________________________________________________

## Resultados Esperados

- Acurácia Random Forest: ~88–93%
- Acurácia Árvore de Decisão simples: ~75–82%
- OOB score: geralmente próximo à acurácia no conjunto de teste
- Features mais importantes: tenderão a ser aquelas com maior variação entre escritores

______________________________________________________________________

## Tarefa

1. **Experimentar** com 10, 50, 100 e 300 árvores — a partir de quantas a acurácia estabiliza?
1. **Seleção de features:** remover as 3 features menos importantes e retreinar. A performance cai muito?
1. **Reflexão:** em identificação forense, quais aspectos da escrita seriam as "features" mais confiáveis para
   distinguir escritores?

______________________________________________________________________

## Dependências (Aula 05)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `RandomForestClassifier`, `DecisionTreeClassifier`,
`cross_val_score`, métricas | | `numpy` | Geração de dados sintéticos, manipulação de arrays | | `matplotlib` | Curva de
OOB error, importância de features, comparação de modelos | | `seaborn` | Matriz de confusão, boxplot de
cross-validation scores | | `pandas` | Análise de importância de features |
