# Aula 01: Introdução ao ML & Reconhecimento de Dígitos

## Status

✅ **Aula ministrada**

______________________________________________________________________

## Objetivo da Aula

Introdução à classificação em machine learning usando reconhecimento de dígitos manuscritos como caso prático. Ao final
da aula, o aluno deve conseguir treinar, avaliar e interpretar um classificador k-NN aplicado a imagens de dígitos.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Explicar o que é classificação em ML com suas próprias palavras
- Carregar e explorar o dataset `digits` do sklearn
- Implementar divisão treino/teste com `train_test_split`
- Treinar e usar um classificador k-NN (`KNeighborsClassifier`)
- Calcular e interpretar métricas de acurácia e matriz de confusão
- Conectar o reconhecimento de dígitos com o objetivo maior do curso: identificação de pessoas pela escrita

______________________________________________________________________

## Algoritmo: k-Nearest Neighbors (k-NN)

O k-NN classifica um novo exemplo buscando os `k` exemplos de treino mais parecidos (mais próximos no espaço de
features) e votando pela classe majoritária entre eles.

**Intuição para manuscritos:** assim como reconhecemos a escrita de alguém comparando com outras amostras que já vimos,
o k-NN classifica pelo parecido com exemplos conhecidos.

**Parâmetros chave:**

- `n_neighbors` (`k`): número de vizinhos — valores menores = modelo mais sensível, maior risco de [overfitting](../GLOSSARY.md#overfitting-sobreajuste); valores
  maiores = mais estável, risco de [underfitting](../GLOSSARY.md#underfitting-subajuste)
- `metric`: distância usada para medir "parecido" (padrão: Euclidiana)

______________________________________________________________________

## Dataset: Digits (sklearn)

- **Origem:** Built-in do sklearn — nenhum download necessário
- **Tamanho:** 1.797 imagens de dígitos manuscritos (0–9)
- **Features:** 64 pixels (imagem 8×8 achatada para vetor 1D)
- **Classes:** 10 (dígitos de 0 a 9)
- **Acurácia esperada:** 95–98% com k-NN

______________________________________________________________________

## Conceitos-Chave

- **[Classificação](../GLOSSARY.md#classificação-classification):** prever a qual categoria um exemplo pertence
- **Treino/teste:** separar dados para treinar e avaliar o modelo de forma honesta — ver [Conjunto de Treino](../GLOSSARY.md#conjunto-de-treino-training-set) e [Conjunto de Teste](../GLOSSARY.md#conjunto-de-teste-test-set)
- **[Acurácia](../GLOSSARY.md#acurácia-accuracy):** porcentagem de predições corretas
- **[Matriz de confusão](../GLOSSARY.md#matriz-de-confusão-confusion-matrix):** tabela que mostra quais classes o modelo confunde entre si
- **[Overfitting](../GLOSSARY.md#overfitting-sobreajuste):** modelo que "memoriza" o treino mas generaliza mal

______________________________________________________________________

## Resultados Esperados

- Acurácia de classificação: ~95–98%
- Dígitos mais difíceis de distinguir: 8/6, 4/9 (formas visualmente similares)
- Valor ótimo de k para este dataset: geralmente entre 3 e 7

______________________________________________________________________

## Tarefa

1. **Experimenter** com diferentes valores de k (k=1, 3, 5, 7, 15, 21) e plotar a curva de acurácia
1. **Analisar** quais dígitos são mais frequentemente confundidos e formular uma hipótese visual
1. **Reflexão:** como esse problema de classificação de dígitos se conecta com o objetivo de identificar uma pessoa pela
   escrita?

______________________________________________________________________

## Dependências (Aula 01)

Todos os pacotes usados nesta aula estão declarados no `pyproject.toml`:

| Pacote | Uso na aula |
|---|---|
| `scikit-learn` | Dataset `digits`, `KNeighborsClassifier`, `train_test_split`, métricas |
| `numpy` | Manipulação de arrays, reshape de imagens |
| `matplotlib` | Visualização de imagens de dígitos, curvas de acurácia |
| `seaborn` | Heatmap da [matriz de confusão](../GLOSSARY.md#matriz-de-confusão-confusion-matrix) |

______________________________________________________________________

## Arquivos desta Aula

| Arquivo | Descrição |
|---|---|
| `class-01-digit-recognition.ipynb` | Notebook completo da aula — já executado |

______________________________________________________________________

## Conexão com o Curso

Esta aula estabelece os padrões de trabalho que serão usados em todas as aulas seguintes:

- Fluxo sklearn: load → split → fit → predict → evaluate
- Visualização e interpretação de resultados
- Conexão constante com análise de escrita e identificação de pessoas
