# Organização do Projeto

## Estrutura de Diretórios

```
projeto-compiladores/
├── src/                    # Código fonte
│   ├── frontend/          # Frontend: Análise Léxica e Sintática
│   │   ├── __init__.py
│   │   ├── lexer.py       # Tokenização (análise léxica)
│   │   ├── parser.py      # Análise sintática (constrói AST)
│   │   └── ast_nodes.py   # Definições dos nós da AST
│   │
│   ├── analysis/          # Análise Semântica
│   │   ├── __init__.py
│   │   └── semantic.py    # Verificação de tipos e escopo
│   │
│   ├── ir/                # Representação Intermediária
│   │   ├── __init__.py
│   │   └── ir_generator.py # Geração de código de três endereços
│   │
│   ├── optimization/      # Otimização de Código
│   │   ├── __init__.py
│   │   └── optimizer.py   # Propagação de constantes, DCE, etc.
│   │
│   └── main.py            # Ponto de entrada principal
│
├── tests/                 # Suite de Testes
│   ├── __init__.py
│   ├── test_compiler.py   # Testes completos do compilador
│   └── test_semantic_errors.py # Testes de validação semântica
│
├── examples/              # Programas de Exemplo
│   ├── __init__.py
│   └── demo_comparison.py # Demo de comparação lado a lado
│
├── docs/                  # Documentação
│   ├── README.md
│   ├── QUICK_REFERENCE.md
│   ├── STRUCTURE.md
│   ├── VALIDACAO.md
│   ├── slides_content.md
│   └── trabalho2.txt
│
├── run_tests.py           # Script executor de testes
├── run_semantic_tests.py  # Executor de testes semânticos
├── run_demo.py            # Executor de demo
│
├── README.md              # Documentação do projeto
└── LICENSE                # Licença MIT
```

## Organização dos Módulos

### Frontend (src/frontend/)
Lida com os estágios iniciais da compilação:
- **lexer.py**: Converte código fonte em tokens
- **parser.py**: Constrói Árvore Sintática Abstrata a partir dos tokens
- **ast_nodes.py**: Define tipos de nós da AST (Program, Declaration, Assignment, etc.)

### Analysis (src/analysis/)
Realiza verificações semânticas:
- **semantic.py**: Gerenciamento da tabela de símbolos, verificação de tipos e escopo

### IR (src/ir/)
Geração de representação intermediária:
- **ir_generator.py**: Gera código de três endereços (TAC) a partir da AST

### Optimization (src/optimization/)
Passes de otimização de código:
- **optimizer.py**: Propagação de constantes, constant folding, eliminação de código morto

## Executando o Projeto

### Programa Principal
```bash
python3 -m src.main
```

### Todos os Testes
```bash
python3 run_tests.py
```

### Apenas Testes Semânticos
```bash
python3 run_semantic_tests.py
```

### Demo de Comparação
```bash
python3 run_demo.py
```

## Dependências dos Módulos

```
main.py
  ├── frontend.lexer (Lexer)
  ├── frontend.parser (Parser)
  ├── analysis.semantic (SemanticAnalyzer)
  ├── ir.ir_generator (IRGenerator)
  └── optimization.optimizer (Optimizer)

parser.py
  └── frontend.ast_nodes (classes AST)

semantic.py
  └── frontend.ast_nodes (classes AST)

ir_generator.py
  └── frontend.ast_nodes (classes AST)
```

## Propósito dos Arquivos

| Arquivo | Propósito |
|---------|-----------|
| `src/main.py` | Ponto de entrada demonstrando pipeline completo de compilação |
| `src/frontend/lexer.py` | Tokeniza código fonte |
| `src/frontend/parser.py` | Constrói AST a partir de tokens |
| `src/frontend/ast_nodes.py` | Definições de classes dos nós da AST |
| `src/analysis/semantic.py` | Valida regras semânticas |
| `src/ir/ir_generator.py` | Gera código intermediário |
| `src/optimization/optimizer.py` | Otimiza código IR |
| `tests/test_compiler.py` | Testes de compilação completos |
| `tests/test_semantic_errors.py` | Testes de detecção de erros semânticos |
| `examples/demo_comparison.py` | Comparação visual código original vs otimizado |
| `run_tests.py` | Executor conveniente de testes |
| `run_semantic_tests.py` | Executor de testes semânticos |
| `run_demo.py` | Executor de demo |
