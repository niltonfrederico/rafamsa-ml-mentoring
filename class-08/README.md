# Aula 08: Redução de Dimensionalidade & Visualização

## Objetivo da Aula

Aplicar PCA e t-SNE para reduzir a dimensionalidade de features de escrita e criar visualizações que revelem estrutura
nos dados. O aluno entende quando e por que reduzir dimensões — tanto para visualização quanto para pré-processamento de
outros modelos.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Explicar a "maldição da dimensionalidade" e por que ela importa em análise de escrita
- Aplicar PCA e interpretar variância explicada por componente
- Visualizar agrupamentos de escritores em espaço 2D via PCA
- Aplicar t-SNE para visualização não-linear de dados complexos
- Comparar PCA vs. t-SNE: quando usar cada um
- Usar PCA como pré-processamento para acelerar modelos supervisionados

______________________________________________________________________

## Técnicas

### PCA (Principal Component Analysis)

Transforma as features originais em componentes ortogonais que maximizam a variância explicada. É linear, determinístico
e permite reconstrução dos dados.

**Intuição para escrita:** os primeiros componentes do PCA capturam as variações mais importantes da escrita — como se
descobríssemos que "tamanho geral" e "inclinação média" explicam 80% das diferenças entre escritores.

**Parâmetros chave:**

- `n_components`: número de componentes a manter
- `explained_variance_ratio_`: proporção da variância explicada por cada componente

### t-SNE (t-Distributed Stochastic Neighbor Embedding)

Técnica não-linear de redução de dimensionalidade otimizada para visualização 2D/3D. Preserva relações de proximidade
local, revelando clusters e estruturas que PCA não captura.

**Atenção:** t-SNE é estocástico e não-determinístico — resultados variam entre execuções. Não é adequado para
pré-processamento, apenas para visualização.

**Parâmetros chave:**

- `perplexity`: controla o balanço entre vizinhança local e global (típico: 5–50)
- `n_iter`: número de iterações de otimização (mínimo recomendado: 1000)
- `random_state`: para reprodutibilidade

______________________________________________________________________

## Dataset: Features de Alta Dimensão de Múltiplos Escritores

- **Origem:** Gerado sinteticamente em aula — dataset com mais features que os anteriores (20–30 dimensões)
- **Tamanho:** ~600 amostras de 6 escritores
- **Features:** features de escrita em alta dimensão (pressão, velocidade, traços, ângulos em múltiplos segmentos)
- **Classes:** 6 escritores (como referência visual — o modelo não usa os rótulos durante a redução)

______________________________________________________________________

## Conceitos-Chave

- **Maldição da dimensionalidade:** em espaços de alta dimensão, todos os pontos ficam "longe" uns dos outros —
  algoritmos de distância perdem eficácia
- **Variância explicada:** proporção da informação original capturada por cada componente
- **Scree plot:** gráfico de variância explicada por componente — auxilia na escolha de `n_components`
- **Loadings (cargas):** correlação entre cada feature original e cada componente — revela o significado do componente
- **Vizinhança local (t-SNE):** t-SNE preserva quem é próximo de quem, não distâncias absolutas
- **PCA como pré-processamento:** reduzir para 95% da variância antes do SVM ou k-NN pode acelerar sem perder
  performance

______________________________________________________________________

## Resultados Esperados

- PCA: 2–4 componentes capturam 70–85% da variância
- PCA 2D: escritores com estilos muito distintos formam clusters visíveis
- t-SNE 2D: clusters mais definidos que PCA, especialmente para escritores com padrões similares
- PCA como pré-processamento + SVM: performance similar ao SVM com todas as features, em menos tempo

______________________________________________________________________

## Tarefa

1. **Determinar** com quantos componentes PCA o dataset retém 90% da variância
1. **Treinar** um SVM com todas as features e comparar com SVM após PCA (90% variância)
1. **Experimentar** com diferentes valores de `perplexity` no t-SNE (5, 30, 50) e observar o impacto nos clusters
1. **Reflexão:** como a visualização de features de escrita em 2D poderia ajudar um perito a identificar padrões
   forenses?

______________________________________________________________________

## Dependências (Aula 08)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `PCA`, `TSNE`, `SVC`, `Pipeline`, métricas | | `numpy` | Geração
de dados de alta dimensão | | `matplotlib` | Scree plot, scatter plots PCA vs. t-SNE, loadings | | `seaborn` | Heatmap
de correlação entre componentes e features originais | | `pandas` | Análise dos loadings e variância explicada |
