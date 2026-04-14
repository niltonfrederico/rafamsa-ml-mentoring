# Aula 06: Support Vector Machines & Identificação Avançada

## Objetivo da Aula

Introduzir Support Vector Machines (SVM) para identificação de escritores com padrões complexos e não-lineares. O aluno
entende o conceito de margem máxima, o kernel trick e como realizar otimização sistemática de hiperparâmetros com Grid
Search.

______________________________________________________________________

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Explicar o conceito de margem máxima e support vectors
- Distinguir fronteiras lineares de não-lineares e quando cada uma se aplica
- Usar kernels (linear, RBF, polinomial) para transformar o espaço de features
- Treinar um `SVC` e otimizar `C` e `gamma` com `GridSearchCV`
- Comparar SVM com Random Forest em termos de performance e custo computacional
- Interpretar a função de decisão do SVM como medida de confiança

______________________________________________________________________

## Algoritmo: Support Vector Machine (SVM)

O SVM encontra a fronteira de decisão que maximiza a margem entre as classes. O kernel trick permite criar fronteiras
não-lineares sem calcular explicitamente as coordenadas em espaços de alta dimensão.

**Intuição para escrita:** o SVM procura os exemplos "mais difíceis" de cada escritor — aqueles mais próximos da
fronteira — e usa apenas eles (os support vectors) para definir a fronteira. É robusto a outliers.

**Kernels:**

- `linear`: fronteira linear — funciona bem quando as classes são linearmente separáveis
- `rbf` (Radial Basis Function): fronteira curva — o mais versátil, bom para dados complexos
- `poly`: fronteira polinomial — captura relações de ordem superior entre features

**Parâmetros chave:**

- `C`: penalização de erros de classificação — alto C = menos regularização = fronteira mais ajustada
- `gamma` (kernels rbf/poly): controla o alcance de influência de cada sample — alto = fronteira mais irregular
- `kernel`: tipo de kernel

______________________________________________________________________

## Dataset: Features de Escrita Multi-Escritor (Complexo)

- **Origem:** Gerado sinteticamente em aula (com mais sobreposição entre classes que na Aula 05)
- **Tamanho:** ~600 amostras de 6 escritores com padrões de escrita sobrepostos
- **Features:** mesmo conjunto da Aula 05, mas com mais variabilidade intra-escritor
- **Classes:** 6 (identificação individual)
- **Acurácia esperada:** ~90–96% com SVM (kernel RBF otimizado)

______________________________________________________________________

## Conceitos-Chave

- **Margem máxima:** o SVM maximiza a distância entre a fronteira de decisão e os exemplos mais próximos de cada classe
- **Support vectors:** os exemplos que "sustentam" a fronteira — os demais não influenciam o modelo
- **Kernel trick:** mapeamento implícito para espaço de alta dimensão sem custo computacional explícito
- **Regularização C:** controla o trade-off entre margem larga e erros de classificação
- **Grid Search + Cross-Validation:** busca sistemática da melhor combinação de hiperparâmetros
- **Escalonamento de features:** crítico para SVM — features em escalas diferentes distorcem a distância

______________________________________________________________________

## Resultados Esperados

- Acurácia SVM linear: ~82–87%
- Acurácia SVM RBF (não otimizado): ~88–92%
- Acurácia SVM RBF (otimizado com Grid Search): ~90–96%
- Acurácia Random Forest (referência da Aula 05): ~88–93%
- Parâmetros ótimos típicos: `C` entre 1–100, `gamma` entre 0.001–0.1

______________________________________________________________________

## Tarefa

1. **Testar** os 3 kernels com parâmetros padrão e comparar acurácias
1. **Executar** Grid Search com grade `C=[0.1, 1, 10, 100]` × `gamma=[0.001, 0.01, 0.1, 1]` e visualizar o heatmap de
   scores
1. **Reflexão:** em que cenário você escolheria SVM sobre Random Forest? E quando escolheria Random Forest sobre SVM?

______________________________________________________________________

## Dependências (Aula 06)

| Pacote | Uso na aula | |---|---| | `scikit-learn` | `SVC`, `GridSearchCV`, `StandardScaler`, `Pipeline`, métricas | |
`numpy` | Geração de dados, manipulação de arrays | | `matplotlib` | Visualização de fronteiras de decisão (2D), heatmap
do Grid Search | | `seaborn` | Matriz de confusão, comparação de kernels | | `pandas` | Organização dos resultados do
Grid Search |
