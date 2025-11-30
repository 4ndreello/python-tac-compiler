# Compilador com Análise Semântica e Otimização

Implementação educacional de compilador em Python com pipeline completo de compilação: análise léxica, parsing, análise semântica, geração de código intermediário e otimização.

## Visão Geral

Este projeto implementa um compilador simplificado para uma linguagem similar a C, demonstrando técnicas clássicas de construção de compiladores incluindo validação semântica, geração de código de três endereços e múltiplos passes de otimização.

## Funcionalidades

### Análise Semântica
- Detecção de variáveis não declaradas
- Detecção de redeclaração de variáveis
- Gerenciamento de tabela de símbolos
- Verificação de tipos

### Geração de Código Intermediário
- Representação em Three-Address Code (TAC)
- Geração automática de variáveis temporárias
- Linearização de expressões da AST

### Otimizações
- Propagação de constantes (Constant Propagation)
- Dobramento de constantes (Constant Folding)
- Eliminação de código morto (Dead Code Elimination - DCE)
- Iteração de ponto fixo até convergência

## Arquitetura

```
Código Fonte → Lexer → Tokens → Parser → AST → Analisador Semântico 
    → Gerador IR → TAC → Otimizador → TAC Otimizado
```

### Estrutura do Projeto

```
projeto-compiladores/
├── src/                      # Código fonte
│   ├── frontend/            # Componentes de front-end
│   │   ├── lexer.py        # Analisador léxico
│   │   ├── parser.py       # Analisador sintático
│   │   └── ast_nodes.py    # Definições dos nós da AST
│   ├── analysis/           # Análise semântica
│   │   └── semantic.py     # Analisador semântico
│   ├── ir/                 # Representação intermediária
│   │   └── ir_generator.py # Gerador de código IR
│   ├── optimization/       # Otimização de código
│   │   └── optimizer.py    # Motor de otimização
│   └── main.py             # Ponto de entrada
├── tests/                  # Suite de testes
│   ├── test_compiler.py    # Testes de integração
│   └── test_semantic_errors.py
├── examples/               # Exemplos e demos
│   └── demo_comparison.py
├── docs/                   # Documentação
│   ├── trabalho2.txt       # Especificação do trabalho
│   ├── QUICK_REFERENCE.md  # Guia de referência rápida
│   ├── STRUCTURE.md        # Estrutura do projeto
│   └── VALIDACAO.md        # Documentação de validação
├── run_tests.py           # Executor de testes
├── run_semantic_tests.py  # Executor de testes semânticos
└── run_demo.py            # Executor de demo
```

## Instalação

### Requisitos
- Python 3.8 ou superior

### Configuração
```bash
git clone https://github.com/4ndreello/projeto-compiladores.git
cd projeto-compiladores
```

Nenhuma dependência externa necessária. O projeto usa apenas módulos da biblioteca padrão do Python.

## Uso

### Executar Exemplo Principal
```bash
python3 -m src.main
```

### Executar Suite Completa de Testes
```bash
python3 run_tests.py
```

### Executar Testes de Erro Semântico
```bash
python3 run_semantic_tests.py
```

### Executar Demo de Otimização
```bash
python3 run_demo.py
```

## Exemplo

### Código Fonte de Entrada
```c
int a;
int b;
a = 3 + 2;
b = a * (a - 1);
```

### Tabela de Símbolos
```
a: int
b: int
```

### Código Intermediário Original (TAC)
```
t1 = 3 + 2
a = t1
t2 = a - 1
t3 = a * t2
b = t3
```

### Código Intermediário Otimizado
```
a = 5
b = 20
```

**Resultado**: Redução de 5 instruções para 2 instruções (60% de otimização)

### Processo de Otimização

1. **Constant Folding**: `3 + 2` avaliado em tempo de compilação → `5`
2. **Constant Propagation**: `a = 5` propagado para expressões subsequentes
3. **Avaliação**: `5 - 1` → `4`, depois `5 * 4` → `20`
4. **Dead Code Elimination**: Temporários `t1`, `t2`, `t3` removidos

## Resultados dos Testes

O projeto inclui 8 casos de teste abrangentes:

| Teste | Descrição | Resultado |
|-------|-----------|-----------|
| 1 | Exemplo original | 60% de redução |
| 2 | Propagação de constantes em cadeia | 40% de redução |
| 3 | Múltiplas operações | 75% de redução |
| 4 | Erro de variável não declarada | Detectado |
| 5 | Erro de redeclaração | Detectado |
| 6 | Expressões com parênteses | 50% de redução |
| 7 | Operações de divisão | 50% de redução |
| 8 | Múltiplas variáveis | 50% de redução |

## Detalhes de Implementação

### Análise Léxica
- Tokenização baseada em regex
- Reconhece: `int`, números, identificadores, operadores (`+`, `-`, `*`, `/`), parênteses, ponto-e-vírgula

### Análise Sintática
- Parser recursivo descendente
- Precedência correta de operadores (multiplicação/divisão antes de soma/subtração)
- Suporte completo a parênteses para alterar precedência

### Análise Semântica
- Tabela de símbolos global
- Verificação de declaração antes do uso
- Detecção de redeclaração
- Base para verificação de tipos (atualmente suporta `int`)

### Geração de IR
- Formato de código de três endereços: `resultado = operando1 op operando2`
- Geração automática de temporários (`t1`, `t2`, ...)
- Linearização completa de expressões

### Otimização
- Iteração de ponto fixo: executa passes até não haver mais mudanças
- Propagação de constantes: rastreia valores constantes em dicionário
- Dobramento de constantes: avalia aritmética em tempo de compilação
- Eliminação de código morto: remove temporários e código não utilizado

## Tecnologias

- **Linguagem**: Python 3.8+
- **Paradigma**: Orientado a objetos com dataclasses
- **Bibliotecas**:
  - `re`: Expressões regulares para análise léxica
  - `dataclasses`: Estruturas de dados para AST
  - `typing`: Type hints para documentação do código

## Referências

- "Compilers: Principles, Techniques, and Tools" (Aho, Sethi, Ullman) - Dragon Book
- "Engineering a Compiler" (Cooper & Torczon)
- "Modern Compiler Implementation in ML" (Andrew W. Appel)

## Autores

- Henrique Scudeller de Oliveira
- Gabriel Andreello
- Ricardo Altever Alves Lessa

Projeto educacional para disciplina de Compiladores.
