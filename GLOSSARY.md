# Glossário de Machine Learning

> Termos técnicos introduzidos ao longo do curso, organizados por aula. Atualizado a cada nova aula ministrada.

______________________________________________________________________

## Índice

- [Aula 01 — k-NN & Reconhecimento de Dígitos](#aula-01--k-nn--reconhecimento-de-dígitos)
- [Aula 02 — Árvores de Decisão & Reconhecimento de Letras](#aula-02--árvores-de-decisão--reconhecimento-de-letras)

______________________________________________________________________

## Aula 01 — k-NN & Reconhecimento de Dígitos

______________________________________________________________________

### Acurácia *(Accuracy)*

**Definição:** Porcentagem de predições corretas em relação ao total de exemplos avaliados.

**Fórmula:**

$$\\text{Acurácia} = \\frac{\\text{número de predições corretas}}{\\text{total de exemplos}}$$

**Exemplo prático:** Se o modelo classificou 970 dígitos corretamente em um conjunto de 1.000 imagens, a acurácia é 97%.

**Atenção:** A acurácia pode ser enganosa quando as classes são muito desbalanceadas (ex: 990 exemplos de uma classe e
10 de outra). Nesse caso, um modelo que sempre chuta a classe majoritária já teria 99% de acurácia sem aprender nada.

______________________________________________________________________

### Algoritmo de ML *(ML Algorithm)*

**Definição:** Uma procedure computacional que aprende padrões a partir de dados e usa esses padrões para fazer
predições ou decisões sobre novos dados.

**Analogia:** É como uma receita — define os passos para transformar dados de entrada em uma saída útil (classificação,
valor previsto, agrupamento etc.).

______________________________________________________________________

### Aprendizado Supervisionado *(Supervised Learning)*

**Definição:** Modalidade de Machine Learning onde o modelo aprende a partir de exemplos **rotulados** — ou seja, pares
(entrada, saída esperada). O modelo ajusta seus parâmetros para minimizar o erro entre suas predições e os rótulos
corretos.

**Exemplo no curso:** No dataset `digits`, cada imagem (entrada) já tem o dígito correto anotado (rótulo). O modelo
aprende associando imagens a dígitos.

**Contraste:** No aprendizado não-supervisionado (Aula 07), não há rótulos — o modelo descobre estrutura nos dados por
conta própria.

______________________________________________________________________

### Classificação *(Classification)*

**Definição:** Tarefa de ML que consiste em prever a **categoria** (classe) à qual um exemplo pertence, dentre um
conjunto finito de categorias possíveis.

**Exemplo prático:** Dado uma imagem de dígito manuscrito, classificar se é 0, 1, 2, ..., ou 9.

**Contraste com Regressão:** A classificação prevê categorias discretas; a regressão (Aula 03) prevê valores numéricos
contínuos.

______________________________________________________________________

### Conjunto de Teste *(Test Set)*

**Definição:** Subconjunto dos dados **nunca visto pelo modelo durante o treino**, usado exclusivamente para avaliar a
performance final.

**Por que é importante:** Avaliar no mesmo conjunto usado para treinar daria uma estimativa otimista e enganosa — seria
como dar as respostas da prova para o aluno estudar e depois usar a mesma prova.

**Convenção no curso:** 20% dos dados (`test_size=0.2`) são separados para teste.

______________________________________________________________________

### Conjunto de Treino *(Training Set)*

**Definição:** Subconjunto dos dados usado para **treinar o modelo** — é a partir desses exemplos que o algoritmo
aprende os padrões.

**Convenção no curso:** 80% dos dados são usados para treino.

______________________________________________________________________

### Dataset

**Definição:** Conjunto de dados estruturado usado para treinar e avaliar modelos de ML. Geralmente organizado em linhas
(exemplos/amostras) e colunas (features/atributos).

**Componentes principais:**

- **X (features/atributos):** as entradas — o que o modelo recebe para fazer a predição
- **y (rótulos/target):** as saídas esperadas — o que o modelo deve aprender a prever

______________________________________________________________________

### Distância Euclidiana *(Euclidean Distance)*

**Definição:** A medida de distância "em linha reta" entre dois pontos no espaço de features. É a métrica padrão usada
pelo k-NN.

**Fórmula para dois pontos $a$ e $b$ com $n$ features:**

$$d(a, b) = \\sqrt{\\sum\_{i=1}^{n}(a_i - b_i)^2}$$

**Intuição:** É a régua do mundo real transportada para espaços com muitas dimensões. Dois dígitos com pixels similares
têm distância euclidiana pequena.

______________________________________________________________________

### Feature (Atributo)

**Definição:** Uma característica mensurável de um exemplo, usada como entrada para o modelo. No dataset `digits`, cada
pixel da imagem 8×8 é uma feature — resultando em 64 features por imagem.

**Analogia para escrita:** features podem ser pressão da caneta, ângulo de inclinação, largura dos traços, proporção
altura/largura dos caracteres.

______________________________________________________________________

### Generalização *(Generalization)*

**Definição:** Capacidade do modelo de fazer predições corretas em dados **novos e não vistos**, e não apenas nos dados
de treino. Um bom modelo generaliza — não memoriza.

______________________________________________________________________

### Hiperparâmetro *(Hyperparameter)*

**Definição:** Configuração do modelo definida **antes** do treino, pelo praticante — ao contrário dos parâmetros, que
são aprendidos durante o treino.

**Exemplo:** No k-NN, o número de vizinhos `k` é um hiperparâmetro. Você escolhe `k=5` antes de treinar; o modelo não
aprende esse valor.

**Contraste com parâmetro:** Em modelos como Regressão Linear (Aula 03), os coeficientes da equação são parâmetros —
eles são aprendidos a partir dos dados.

______________________________________________________________________

### k-NN / k-Nearest Neighbors (k Vizinhos Mais Próximos)

**Definição:** Algoritmo de classificação que, para um novo exemplo, encontra os `k` exemplos de treino mais próximos
(no espaço de features) e classifica pelo voto majoritário entre esses vizinhos.

**Intuição:** "Diga-me com quem você se parece e eu te direi quem você é." Um dígito desconhecido é classificado com
base nos dígitos mais parecidos que o modelo já viu.

**Parâmetros chave:**

- `n_neighbors` (`k`): quantidade de vizinhos consultados
  - `k` pequeno → modelo mais sensível, maior risco de overfitting
  - `k` grande → modelo mais estável, risco de underfitting
- `metric`: forma de medir "parecido" (padrão: distância euclidiana)

**No curso:** usado na Aula 01 para classificar dígitos manuscritos (0–9) com acurácia esperada de 95–98%.

______________________________________________________________________

### Matriz de Confusão *(Confusion Matrix)*

**Definição:** Tabela que mostra, para cada combinação de classe real × classe prevista, quantos exemplos o modelo
classificou corretamente ou confundiu. A diagonal principal representa as predições corretas; o restante são os erros.

**Como ler:**

- Linha = classe real
- Coluna = classe prevista
- Valor na célula (i, j) = quantas vezes o modelo disse "j" quando era "i"

**Por que é útil:** A acurácia diz "quantos o modelo acertou"; a matriz de confusão diz "onde o modelo errou e com o
quê". No contexto de dígitos, ela revela pares que o modelo confunde (ex: 4 e 9 se parecem visualmente).

______________________________________________________________________

### Modelo *(Model)*

**Definição:** A estrutura matemática resultante do processo de treino. Um modelo aprendeu a mapear entradas (features)
para saídas (predições) a partir dos dados de treino.

**Metáfora:** O modelo é o "produto final" do aprendizado — como um especialista após anos de experiência. O algoritmo é
o método de aprendizado; o modelo é o conhecimento adquirido.

______________________________________________________________________

### Overfitting (Sobreajuste)

**Definição:** Fenômeno onde o modelo aprende os dados de treino com precisão excessiva — incluindo ruídos e
particularidades irrelevantes — e perde a capacidade de generalizar para novos dados.

**Sintoma:** Acurácia muito alta no treino, acurácia significativamente menor no teste.

**Causa comum no k-NN:** `k=1` — o modelo "memoriza" cada exemplo de treino e classifica novos exemplos pelo vizinho
mais próximo exato, sem suavizar o ruído.

**Contraste:** Underfitting é o oposto — modelo muito simples que não captura nem os padrões reais dos dados.

______________________________________________________________________

### Pipeline de ML

**Definição:** Sequência padronizada de etapas para construir e avaliar um modelo: preparação de dados → treino →
predição → avaliação.

**Padrão usado no curso:**

```python
# 1. Preparar os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Treinar o modelo
model = AlgoritmoEscolhido(parametros)
model.fit(X_train, y_train)

# 3. Prever e avaliar
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```

______________________________________________________________________

### `random_state`

**Definição:** Parâmetro que controla a semente do gerador de números aleatórios usado por operações estocásticas
(divisão de dados, inicialização de modelos, etc.). Fixar `random_state=42` garante que os resultados sejam
**reprodutíveis** — qualquer pessoa que rodar o mesmo código obtém os mesmos resultados.

**Por que 42?** É uma convenção da comunidade — qualquer inteiro funciona, mas 42 ficou popular como referência ao *Guia
do Mochileiro das Galáxias*.

______________________________________________________________________

### `train_test_split`

**Definição:** Função do scikit-learn que divide os dados em conjuntos de treino e teste de forma aleatória e
estratificada.

**Uso típico:**

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

**Parâmetros principais:**

- `test_size=0.2` → 20% para teste, 80% para treino
- `random_state=42` → reprodutibilidade
- `stratify=y` → mantém a proporção de classes em ambos os conjuntos (recomendado quando as classes são desbalanceadas)

______________________________________________________________________

### Underfitting (Subajuste)

**Definição:** Fenômeno oposto ao overfitting — o modelo é simples demais para capturar os padrões reais dos dados,
resultando em baixa performance tanto no treino quanto no teste.

**Causa comum no k-NN:** `k` muito alto — o modelo suaviza tanto as fronteiras de decisão que perde informação
discriminativa.

______________________________________________________________________

## Aula 02 — Árvores de Decisão & Reconhecimento de Letras

______________________________________________________________________

### Árvore de Decisão *(Decision Tree)*

**Definição:** Algoritmo de classificação que aprende regras binárias explícitas a partir dos dados, formando uma
estrutura de árvore. Cada nó representa uma pergunta sobre uma feature ("feature X > limiar?"); as folhas representam a
classe prevista.

**Intuição:** É como um fluxograma de decisão — o modelo aprende quais perguntas fazer e em que ordem para identificar
melhor cada classe. Ao contrário do k-NN, a árvore é **interpretável**: dá para ler as regras aprendidas.

**Parâmetros chave:**

- `max_depth`: profundidade máxima — principal controle de complexidade
- `criterion`: métrica de impureza para escolher as divisões (`'gini'` ou `'entropy'`)
- `min_samples_split`: número mínimo de amostras para dividir um nó

**No curso:** usado na Aula 02 para reconhecer letras A–Z com o dataset UCI Letter Recognition.

______________________________________________________________________

### Bias-Variance Tradeoff

**Definição:** Dilema fundamental em ML entre dois tipos de erro:

- **Bias (viés):** erro causado por suposições excessivamente simples — modelo incapaz de capturar os padrões reais
  (underfitting)
- **Variância:** erro causado por sensibilidade excessiva ao conjunto de treino — modelo que memoriza ruído
  (overfitting)

**Equilíbrio:** modelos com alta complexidade (ex: árvore profunda) têm baixo bias mas alta variância. Modelos simples
(ex: árvore rasa) têm alto bias mas baixa variância. O objetivo é encontrar o ponto onde o erro total no conjunto de
teste é mínimo.

**Evidência prática:** A curva treino vs. teste por `max_depth` mostra visualmente esse tradeoff — o pico da acurácia
no teste marca o equilíbrio ideal.

______________________________________________________________________

### Importância de Features *(Feature Importance)*

**Definição:** Métrica que quantifica o quanto cada feature contribuiu para a aprendizagem do modelo. Em Árvores de
Decisão, é calculada como a média ponderada das reduções de impureza (Gini) que a feature causou em todos os nós da
árvore, normalizada para somar 1.

**Interpretação:** Features com alta importância são as que o modelo mais usou para separar as classes — equivale a
identificar quais características da escrita são mais discriminativas para distinguir letras ou pessoas.

**Atenção:** Features correlacionadas tendem a "dividir" a importância entre si. Importância não implica causalidade —
uma feature pode ser importante por correlação espúria. Para estimativas mais robustas, usar Random Forest (Aula 05).

______________________________________________________________________

### Interpretabilidade *(Interpretability)*

**Definição:** Capacidade de um modelo de ML de explicar *como* chegou a uma predição de forma compreensível para
humanos. Um modelo interpretável permite auditar as decisões, identificar erros sistemáticos e justificar resultados
em contextos de alto risco.

**Por que importa:** Em aplicações forenses (análise de documentos suspeitos), um perito precisa justificar sua
conclusão em tribunal. Um modelo que apenas retorna "é a letra X" não é suficiente — é preciso evidência rastreável.

**Escala de interpretabilidade:**

- **Alta:** Árvores de Decisão, Regressão Linear/Logística (regras e coeficientes explícitos)
- **Baixa:** k-NN, Redes Neurais (caixa-preta — difícil de explicar por que classificou assim)

______________________________________________________________________

### Índice Gini *(Gini Index)*

**Definição:** Medida de impureza de um nó em uma Árvore de Decisão. Um nó puro (todos os exemplos da mesma classe)
tem Gini = 0. Um nó com classes uniformemente distribuídas tem Gini ≈ 0,5 (máxima impureza para classificação binária).

**Fórmula:**

$$G = 1 - \sum_{i=1}^{C} p_i^2$$

onde $p_i$ é a proporção de amostras da classe $i$ no nó e $C$ é o número de classes.

**Como é usado:** A cada divisão, a árvore escolhe a feature e o limiar que **minimiza o Gini ponderado** dos dois nós
filhos — ou seja, que resulta nos grupos mais puros.

**Alternativa:** A entropia (critério `'entropy'`) mede o mesmo conceito via teoria da informação, com resultado
prático quase idêntico ao Gini na maioria dos datasets.

______________________________________________________________________

*Glossário atualizado na Aula 02. Novos termos serão adicionados a cada aula.*
