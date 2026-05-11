______________________________________________________________________

## name: evaluate-user description: Invocação obrigatória ao final de toda resposta dos agentes Magus e Lucca. Analisa a interação atual e atualiza o perfil do usuário em .claude/instructions/user.md para calibrar respostas futuras.

# evaluate-user

**Invocação:** obrigatória ao final de toda resposta dos agentes Magus e Lucca, sem exceção.

**Propósito:** Analisar a interação atual e atualizar o perfil do usuário em
[.claude/instructions/user.md](../../instructions/user.md) para que os agentes calibrem respostas futuras.

______________________________________________________________________

## Execução

1. Ler [.claude/instructions/user.md](../../instructions/user.md) (conteúdo atual do perfil)
1. Analisar a interação atual buscando evidências nas categorias abaixo
1. Mesclar observações novas com o perfil existente — **não substituir, acumular**
1. Escrever o arquivo atualizado via `Edit` (ou `Write` se for reescrita completa)
1. Se não houver nada novo para registrar, não modificar o arquivo

______________________________________________________________________

## O Que Observar

### Conhecimento Demonstrado

- Termos técnicos usados corretamente sem precisar de explicação
- Conceitos conectados por conta própria pelo usuário
- Perguntas que mostram entendimento profundo
- Código ou lógica escritos corretamente

### Dificuldades Identificadas

- Conceitos que geraram confusão ou precisaram de múltiplas explicações
- Perguntas que revelam equívocos (ex: confundir accuracy com precision)
- Erros recorrentes de código ou raciocínio
- Tópicos onde o usuário pediu exemplos extras ou reformulação

### Preferências

- Exemplos concretos vs. explicações teóricas
- Analogias vs. definições formais
- Vocabulário natural do usuário
- Nível de detalhe confortável
- Áreas de interesse especial

### Histórico de Tópicos

- Algoritmos e conceitos já discutidos
- Aulas geradas via Lucca

______________________________________________________________________

## Regras de Atualização

- Não duplicar observações já registradas
- Se uma observação anterior for contradita, atualizar com a mais recente
- Manter o arquivo conciso — agrupar observações similares
- Nunca listar cada interação individualmente; consolidar padrões

______________________________________________________________________

## Formato do Arquivo de Perfil

[.claude/instructions/user.md](../../instructions/user.md) deve sempre seguir esta estrutura:

```markdown
# Perfil do Usuário

> Atualizado automaticamente pela skill evaluate-user. Consumido por Magus e Lucca no início de cada resposta.

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

Após ler [.claude/instructions/user.md](../../instructions/user.md), aplicar:

- **Conhecimento demonstrado sobre X:** não explicar X do zero
- **Dificuldade com Y:** aumentar profundidade e usar mais analogias
- **Prefere exemplos concretos:** começar com exemplo antes da teoria
- **Vocabulário informal:** espelhar o estilo sem perder precisão técnica
