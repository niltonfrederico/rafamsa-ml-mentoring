# Reconhecimento de Escrita Manual & Identificação de Pessoas — Curso de Mentoria em ML

> Curso prático de Machine Learning com scikit-learn aplicado a análise de escrita manual e identificação de pessoas.
> **9 aulas · 1h30min cada · Python 3.13+**

______________________________________________________________________

## Índice

- [Reconhecimento de Escrita Manual & Identificação de Pessoas — Curso de Mentoria em ML](#reconhecimento-de-escrita-manual--identifica%C3%A7%C3%A3o-de-pessoas--curso-de-mentoria-em-ml)
  - [Índice](#%C3%ADndice)
  - [Visão Geral do Curso](#vis%C3%A3o-geral-do-curso)
    - [Objetivos do Curso](#objetivos-do-curso)
  - [Configuração do Ambiente](#configura%C3%A7%C3%A3o-do-ambiente)
    - [1. Instalar o Homebrew](#1-instalar-o-homebrew)
    - [2. Instalar o pipx via Homebrew](#2-instalar-o-pipx-via-homebrew)
    - [3. Instalar o Poetry via pipx](#3-instalar-o-poetry-via-pipx)
    - [4. Instalar o projeto](#4-instalar-o-projeto)
    - [5. Ativar o ambiente virtual](#5-ativar-o-ambiente-virtual)
      - [No terminal](#no-terminal)
      - [No VS Code](#no-vs-code)
  - [Executando as Aulas](#executando-as-aulas)
    - [Preparando o Lab da Aula](#preparando-o-lab-da-aula)
    - [Iniciando o Jupyter Lab](#iniciando-o-jupyter-lab)
    - [Executando um Notebook](#executando-um-notebook)
  - [Currículo — Sumário das Aulas](#curr%C3%ADculo--sum%C3%A1rio-das-aulas)
  - [Estrutura do Repositório](#estrutura-do-reposit%C3%B3rio)
  - [Agentes de IA](#agentes-de-ia)
  - [Glossário](#gloss%C3%A1rio)

______________________________________________________________________

## Visão Geral do Curso

**Duração:** 9 aulas × 1h30min cada\
**Framework:** scikit-learn\
**Público-alvo:** Estudantes com conhecimento de Python e matemática básica para ML\
**Abordagem:** Prática — cada aula produz um modelo ML completo aplicado à análise de escrita

### Objetivos do Curso

Ao final do curso, o aluno será capaz de:

- Aplicar algoritmos fundamentais de ML a dados de escrita e imagens
- Usar scikit-learn para classificação, regressão, clustering e redução de dimensionalidade
- Escolher o algoritmo certo para cada tipo de problema
- Avaliar a performance de modelos de forma rigorosa e evitar armadilhas comuns
- Construir sistemas capazes de identificar pessoas a partir de padrões de escrita

______________________________________________________________________

## Configuração do Ambiente

### 1. Instalar o Homebrew

**O que é:** O [Homebrew](https://brew.sh) é o gerenciador de pacotes mais popular para macOS e Linux. Ele facilita a
instalação de ferramentas de desenvolvimento sem precisar gerenciar arquivos manualmente ou usar `sudo` de forma
arriscada.

**Por que usamos:** É a forma mais limpa de instalar `pipx` no Ubuntu sem depender dos pacotes do sistema, que costumam
ser desatualizados.

Acesse [brew.sh](https://brew.sh) para instruções completas. No Ubuntu, o comando é:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Após a instalação, adicione o Homebrew ao seu PATH seguindo as instruções exibidas no terminal (geralmente adicionando
duas linhas ao `~/.bashrc` ou `~/.profile`).

Verifique a instalação:

```bash
brew --version
```

______________________________________________________________________

### 2. Instalar o pipx via Homebrew

**O que é:** O [pipx](https://pipx.pypa.io) instala ferramentas de linha de comando Python em ambientes isolados. Cada
ferramenta fica em seu próprio virtualenv, mas continua acessível globalmente no terminal — sem conflitos de
dependências.

**Por que usamos:** Instalar o Poetry diretamente com `pip install poetry` pode causar conflitos com outros pacotes do
sistema. O `pipx` isola o Poetry sem comprometer o Python global.

```bash
brew install pipx
pipx ensurepath
```

Após o `ensurepath`, reinicie o terminal ou execute `source ~/.bashrc` para aplicar as mudanças de PATH.

Verifique a instalação:

```bash
pipx --version
```

______________________________________________________________________

### 3. Instalar o Poetry via pipx

**O que é:** O [Poetry](https://python-poetry.org) é uma ferramenta moderna para gerenciamento de dependências e
ambientes virtuais em Python. Ele lê o `pyproject.toml`, resolve dependências e cria um virtualenv isolado para o
projeto.

**Por que usamos:** Substitui a combinação `pip` + `venv` + `requirements.txt` com uma única ferramenta declarativa.
Garante que todos que trabalham no projeto usem exatamente as mesmas versões de dependências.

```bash
pipx install poetry
```

Verifique a instalação:

```bash
poetry --version
```

______________________________________________________________________

### 4. Instalar o projeto

Com o Poetry instalado, clone o repositório (se ainda não tiver feito) e instale todas as dependências:

```bash
# Na raiz do projeto (onde está o pyproject.toml)
poetry install
```

Isso vai:

1. Criar um virtualenv dedicado para o projeto
1. Instalar todas as dependências declaradas em `pyproject.toml` (numpy, pandas, scikit-learn, jupyter, etc.)
1. Gerar/atualizar o `poetry.lock` com as versões exatas resolvidas

> **Requisito:** Python 3.13 ou superior. Verifique com `python --version`.

______________________________________________________________________

### 5. Ativar o ambiente virtual

#### No terminal

```bash
# Ativar o shell do virtualenv
poetry shell

# Ou executar um comando diretamente sem ativar
poetry run python script.py
```

Para sair do virtualenv ativado:

```bash
exit
```

#### No VS Code

1. Abra a pasta do projeto no VS Code
1. Abra qualquer arquivo `.py` ou `.ipynb`
1. Clique no seletor de interpretador no canto inferior direito (ou use o atalho `Ctrl+Shift+P` → **Python: Select
   Interpreter**)
1. Selecione o interpretador que contém o caminho do virtualenv do Poetry

Para encontrar o caminho do virtualenv caso o VS Code não detecte automaticamente:

```bash
poetry env info --path
```

Copie o caminho retornado e cole no seletor de interpretador do VS Code.

______________________________________________________________________

## Executando as Aulas

### Preparando o Lab da Aula

Antes de começar uma aula, copie o notebook para sua pasta `labs/` pessoal. Isso preserva o notebook original e dá
liberdade para experimentar sem risco de sobrescrever o material do curso:

```bash
poetry run lab <número_da_aula>
```

Exemplos:

```bash
poetry run lab 1    # copia class-01/*.ipynb → class-01/labs/
poetry run lab 02   # copia class-02/*.ipynb → class-02/labs/
```

O arquivo copiado em `labs/` é ignorado pelo git — suas modificações ficam apenas na sua máquina.

### Iniciando o Jupyter Lab

Com o ambiente ativado (`poetry shell`), execute:

```bash
jupyter lab
```

O Jupyter Lab abrirá automaticamente no navegador padrão em `http://localhost:8888`.

Alternativamente, sem ativar o shell:

```bash
poetry run jupyter lab
```

### Executando um Notebook

1. Execute `poetry run lab <número>` para copiar o notebook para `labs/`
1. No Jupyter Lab, navegue até `class-XX/labs/` e abra o arquivo copiado
1. Para executar todas as células em sequência: menu **Run → Run All Cells** (ou `Shift+Enter` célula a célula)
1. As células devem ser executadas **em ordem**, de cima para baixo — nunca pule etapas

> Cada notebook foi construído para rodar do início ao fim sem erros. Se uma célula falhar, execute as anteriores
> primeiro.

______________________________________________________________________

## Currículo — Sumário das Aulas

| # | Tópico | Algoritmo | Aplicação | Dataset | Status | | --- | --- | --- | --- | --- | --- | |
[01](class-01/README.md) | Introdução ao ML & Reconhecimento de Dígitos | k-Nearest Neighbors | Classificação de dígitos
manuscritos | sklearn `digits` | ✅ Concluída | | [02](class-02/README.md) | Árvores de Decisão & Reconhecimento de
Letras | Decision Tree | Reconhecimento de letras A–Z | UCI Letter Recognition | ✅ Concluída | |
[03](class-03/README.md) | Regressão Linear & Métricas de Escrita | Linear Regression | Previsão de velocidade de
escrita | Sintético | 🔜 Próxima | | [03b](class-03b-project-kickoff/README.md) | **Milestone — Kickoff do Projeto de
Pesquisa** | — | Inventário do dataset + primeira inspeção de áudio real + classificação binária | Áudio coletado pelo
Rafael (USP-RP + Alfenas) | 🔜 Pendente | | [04](class-04/README.md) | Regressão Logística & Classificação de Escritores
| Logistic Regression | Classificação binária de escritores | Sintético | 🔜 Pendente | | [05](class-05/README.md) |
Métodos Ensemble & Identificação Multi-Escritor | Random Forest | Identificação multi-classe de escritores | UCI /
Sintético | 🔜 Pendente | | [06](class-06/README.md) | Support Vector Machines & Identificação Avançada | SVM (kernels) |
Identificação com padrões não-lineares | UCI / Sintético | 🔜 Pendente | | [07](class-07/README.md) | Clustering &
Descoberta de Estilos de Escrita | K-Means, Hierárquico | Agrupamento não-supervisionado de estilos | UCI / Sintético |
🔜 Pendente | | [08](class-08/README.md) | Redução de Dimensionalidade & Visualização | PCA, t-SNE | Visualização do
espaço de features | sklearn `digits` | 🔜 Pendente | | [09](class-09/README.md) | Avaliação de Modelos & Validação |
Cross-validation, testes estatísticos | Avaliação rigorosa e comparação de modelos | Todos | 🔜 Pendente |

______________________________________________________________________

## Estrutura do Repositório

```
.
├── pyproject.toml         # Dependências e configuração do projeto
├── README.md              # Este arquivo
├── GLOSSARY.md            # Glossário de termos de ML do curso
├── scripts/
│   └── lab.py             # Comando `poetry run lab <n>` — copia notebook para labs/
├── .github/
│   ├── copilot-instructions.md   # Diretrizes de geração de conteúdo
│   ├── agents/                   # Definições dos agentes Lucca e Magus
│   ├── instructions/             # Perfil do usuário (calibração dos agentes)
│   └── skills/                   # Skills dos agentes (evaluate-user, etc.)
├── class-01/
│   ├── README.md                 # Contrato conceitual da aula
│   ├── class-01-digit-recognition.ipynb
│   └── labs/                     # Área de experimentação do aluno (ignorada pelo git)
├── class-02/ … class-09/
│   ├── README.md                 # Contrato conceitual (notebook gerado pelo Lucca)
│   └── labs/                     # Área de experimentação do aluno (ignorada pelo git)
```

______________________________________________________________________

## Agentes de IA

Este repositório usa dois agentes de IA para suporte ao curso:

| Agente | Propósito | Quando chamar | |---|---|---| | **magus** | Tire dúvidas sobre conceitos, algoritmos, resultados
e ML em geral | "O que é overfitting?", "Por que o SVM funciona melhor com dados normalizados?" | | **lucca** | Geração
de notebooks, exercícios e material didático | "Gerar Aula 02: Árvores de Decisão" |

______________________________________________________________________

## Glossário

Consulte o [GLOSSARY.md](GLOSSARY.md) para definições dos termos técnicos usados no curso.

O glossário é atualizado a cada aula com os novos termos introduzidos.
