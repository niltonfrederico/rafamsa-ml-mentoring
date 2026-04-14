# Aula 07: Clustering & Descoberta de Estilos de Escrita

## Objetivo da Aula

Introdução ao aprendizado não-supervisionado com K-Means e Clusterização Hierárquica. Sem rótulos, o algoritmo descobre
agrupamentos naturais nos dados de escrita. O aluno aprende a determinar o número ideal de clusters e a interpretar o
que cada grupo representa.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Distinguir aprendizado supervisionado de não-supervisionado
- Aplicar K-Means e entender o algoritmo de atribuição/centroide
- Usar a curva do cotovelo (Elbow Method) para escolher o número de clusters
- Aplicar Clusterização Hierárquica e interpretar dendrogramas
- Visualizar clusters em 2D usando PCA para redução de dimensionalidade
- Interpretar o significado dos clusters no contexto de estilos de escrita

______________________________________________________________________

## Algoritmos

### K-Means

Particiona os dados em `k` grupos, minimizando a distância intra-cluster. Cada ponto pertence ao cluster cujo centroide
é mais próximo.

**Intuição:** como separar amostras de escrita de diferentes escritores sem saber quem é quem — o algoritmo descobre
grupos naturais baseado apenas nas features.

**Parâmetros chave:**

- `n_clusters`: número de grupos (escolhido com a curva do cotovelo)
- `init='k-means++'`: inicialização inteligente de centroides (evita mínimos locais ruins)
- `n_init`: número de reinicializações para encontrar a melhor solução

### Clusterização Hierárquica (Agglomerative)

Começa com cada ponto em seu próprio cluster e vai fundindo os mais próximos iterativamente. Produz um dendrograma
mostrando a hierarquia completa de fusões.

**Parâmetros chave:**

- `linkage`: critério de fusão (`ward`, `complete`, `average`) — `ward` minimiza variância intra-cluster
- `n_clusters`: número final de grupos (ou cortar o dendrograma em uma altura)

______________________________________________________________________

## Dataset: Amostras de Escrita sem Rótulos

- **Origem:** Gerado sinteticamente em aula (mesmo conjunto da Aula 05, mas removendo os rótulos de escritor)
- **Tamanho:** ~600 amostras
- **Features:** features de escrita (pressão, tamanho, inclinação, velocidade, regularidade)
- **Target:** nenhum — aprendizado não-supervisionado
- **Objetivo:** descobrir se os clusters encontrados correspondem a escritores distintos

______________________________________________________________________

## Conceitos-Chave

- **Aprendizado não-supervisionado:** descobrir estrutura nos dados sem rótulos
- **Inertia (WCSS):** soma das distâncias quadráticas de cada ponto ao seu centroide — menor = melhor
- **Elbow Method:** plotar inertia vs. k e procurar o "cotovelo" onde a melhora marginal diminui
- **Dendrograma:** representação hierárquica completa das fusões — permite escolher k visualmente
- **Silhouette score:** métrica de qualidade dos clusters (mede coesão interna vs. separação externa)
- **PCA como ferramenta de visualização:** reduzir para 2D para plotar clusters interpretáveis

______________________________________________________________________

## Resultados Esperados

- Curva do cotovelo sugere k=5–6 (correspondendo aos 6 escritores do dataset)
- Clusterização hierárquica com `ward` deve recuperar grupos similares ao K-Means
- Visualização PCA mostrará clusters razoavelmente separados, com alguma sobreposição

______________________________________________________________________

## Tarefa

1. **Experimentar** com k=3, 5, 6, 8 e comparar a visualização PCA e o silhouette score
1. **Avaliar** usando os rótulos reais (que foram escondidos): os clusters descobertos correspondem aos escritores?
1. **Reflexão:** em que contextos de análise forense você usaria clustering em vez de classificação supervisionada?

______________________________________________________________________

## Dependências (Aula 07)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `KMeans`, `AgglomerativeClustering`, `PCA`, `silhouette_score` | |
`scipy` | `dendrogram`, `linkage` — visualização hierárquica | | `numpy` | Manipulação de arrays | | `matplotlib` |
Curva do cotovelo, dendrograma, scatter plot de clusters | | `seaborn` | Visualização de distribuição por cluster | |
`pandas` | Análise dos clusters |
