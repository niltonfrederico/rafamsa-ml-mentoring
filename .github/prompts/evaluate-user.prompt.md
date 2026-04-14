______________________________________________________________________

## description: Atualiza o perfil do usuário em .github/instructions/user.instructions.md com observações da interação atual.

# evaluate-user

## Propósito

Este skill é invocado **obrigatoriamente ao final de toda resposta** pelos agentes Magus e Lucca. Ele analisa a
interação atual e atualiza o perfil do usuário em `.github/instructions/user.instructions.md`.

O perfil resultante é consumido por Magus e Lucca no início de toda nova resposta para calibrar profundidade,
vocabulário e abordagem pedagógica.

______________________________________________________________________

## Quando Invocar

- **Sempre:** ao final de cada resposta, sem exceção.
- **Validação obrigatória:** antes de encerrar qualquer resposta, o agente deve confirmar que este skill foi invocado.
  Se não foi, invocar imediatamente.

______________________________________________________________________

## O Que Observar e Registrar

Analise a interação atual buscando evidências de:

### Conhecimento Demonstrado

- Termos técnicos que o usuário usou corretamente e sem precisar de explicação
- Conceitos que o usuário conectou por conta própria (ex: "então isso é parecido com o que vimos na aula 2?")
- Perguntas que mostram entendimento profundo (ex: "por que o SVM funciona melhor com dados normalizados?")
- Código ou lógica que o usuário escreveu corretamente

### Dificuldades Identificadas

- Conceitos que geraram confusão ou precisaram de múltiplas explicações
- Perguntas que revelam equívocos (ex: confundir accuracy com precision)
- Erros recorrentes de código ou de raciocínio
- Tópicos onde o usuário pediu exemplos extras ou reformulação

### Preferências

- Preferência por exemplos concretos vs. explicações teóricas
- Preferência por analogias vs. definições formais
- Vocabulário que o usuário usa naturalmente (ex: "treinar o modelo" vs. "ajustar os parâmetros")
- Nível de detalhe que o usuário parece confortável com
- Áreas de interesse especial (ex: sempre pergunta sobre aplicações forenses)

### Histórico de Tópicos

- Quais algoritmos/conceitos já foram discutidos
- Quais aulas já foram trabalhadas (via Lucca)

______________________________________________________________________

## Como Atualizar `.github/instructions/user.instructions.md`

1. Ler o conteúdo atual de `.github/instructions/user.instructions.md`
1. Extrair as novas observações da interação atual
1. Mesclar com o perfil existente — **não substituir**, **acumular**
1. Escrever o arquivo atualizado

### Regras de Atualização

- Não duplicar observações já registradas
- Se uma observação anterior for contradita pela nova interação, atualizar com a mais recente e registrar a mudança
- Manter o arquivo conciso — agrupar observações similares, não listar cada interação individualmente
- Se não houver nada novo para registrar nesta interação, não modificar o arquivo

______________________________________________________________________

## Formato do Perfil

O arquivo `.github/instructions/user.instructions.md` deve sempre seguir exatamente esta estrutura:

```markdown
# Perfil do Usuário

> Atualizado automaticamente pelo skill evaluate-user. Consumido por Magus e Lucca no início de cada resposta.

## Conhecimento Demonstrado

<!-- Conceitos, termos e habilidades que o usuário mostrou dominar -->

## Dificuldades Identificadas

<!-- Conceitos que causaram confusão, erros recorrentes, equívocos observados -->

## Preferências

<!-- Estilo de explicação preferido, vocabulário natural, áreas de interesse -->

## Tópicos Trabalhados

<!-- Algoritmos discutidos, aulas geradas, conceitos já cobertos -->
```

______________________________________________________________________

## Calibração para Respostas Futuras

Magus e Lucca devem ler `.github/instructions/user.instructions.md` antes de responder e aplicar:

- **Se o usuário já demonstrou conhecimento sobre X:** não explicar X do zero, partir do que já sabe
- **Se o usuário tem dificuldade com Y:** aumentar profundidade e usar mais analogias ao abordar Y
- **Se o usuário prefere exemplos concretos:** sempre começar com um exemplo antes da teoria
- **Se o usuário usa vocabulário informal:** espelhar o estilo sem perder precisão técnica
