# Estrutura da Apresentação - Compiladores

## Slide 1: Título
- **Título:** Análise Semântica e Otimização de Código
- **Integrantes:** [Nome e RA dos Integrantes]
- **Disciplina:** Compiladores

## Slide 2: Introdução à Análise Semântica
- **O que é:** Fase que verifica se a estrutura sintática faz sentido no contexto da linguagem.
- **Objetivo:** Garantir coerência e regras de tipagem.
- **Diferença:**
  - *Sintática:* "A frase está gramaticalmente correta?"
  - *Semântica:* "A frase tem significado válido?"

## Slide 3: Principais Erros Semânticos
- **Variáveis não declaradas:** Uso de identificadores antes da definição.
- **Tipos incompatíveis:** Operações entre tipos inválidos (ex: somar string com int).
- **Escopo incorreto:** Acesso a variáveis fora do seu bloco de validade.
- **Redeclaração:** Declarar a mesma variável duas vezes no mesmo escopo.

## Slide 4: Estruturas de Dados - Tabela de Símbolos
- **Função:** Armazenar informações sobre identificadores (variáveis, funções).
- **Atributos guardados:** Nome, Tipo, Escopo, Endereço de Memória.
- **Uso:** Consultada frequentemente durante a análise semântica e geração de código.

## Slide 5: Geração de Código Intermediário (IR)
- **O que é:** Uma representação agnóstica da máquina alvo, facilitando otimizações.
- **Tipos comuns:**
  1. **Árvores de Sintaxe Abstrata (AST):** Representação hierárquica.
  2. **Código de Três Endereços (TAC):** Sequência linear de instruções simples.

## Slide 6: Código de Três Endereços (TAC)
- **Estrutura:** 
- **Características:**
  - No máximo um operador por instrução.
  - Uso extensivo de variáveis temporárias (, ).
- **Exemplo:**
  *Fonte:* 
  *TAC:*
  

## Slide 7: Otimização de Código - Visão Geral
- **Objetivo:** Melhorar desempenho (tempo/espaço) sem alterar o comportamento do programa.
- **Tipos:**
  - *Local:* Dentro de um bloco básico.
  - *Global:* Em todo o grafo de fluxo do programa.

## Slide 8: Propagação de Constantes
- **Técnica:** Substituir variáveis cujo valor é conhecido em tempo de compilação por esse valor constante.
- **Exemplo:**
  *Antes:*
  
  *Depois:*
  

## Slide 9: Eliminação de Código Morto (Dead Code Elimination)
- **Técnica:** Remover instruções que computam valores nunca utilizados.
- **Exemplo:**
  *Antes:*
  
  *Depois:*
  

## Slide 10: Eliminação de Subexpressões Comuns (CSE)
- **Técnica:** Evitar recalcular a mesma expressão se os valores não mudaram.
- **Exemplo:**
  *Antes:*
  
  *Depois:*
  

## Slide 11: Implementação Prática - Visão Geral
- **Linguagem:** Python
- **Módulos:** Lexer, Parser, SemanticAnalyzer, IRGenerator, Optimizer.
- **Funcionalidades:**
  - Detecção de variáveis não declaradas.
  - Geração de TAC.
  - Otimização (Propagação de Constantes + Dead Code).

## Slide 12: Exemplo Prático - Entrada
- **Código Fonte:**
  

## Slide 13: Exemplo Prático - Resultados
- **Tabela de Símbolos:** , 
- **IR Original:**
  
- **IR Otimizado:**
  

## Slide 14: Conclusão
- A análise semântica garante a integridade lógica.
- O código intermediário desacopla front-end de back-end.
- Otimizações simples reduzem drasticamente a complexidade do código final.
