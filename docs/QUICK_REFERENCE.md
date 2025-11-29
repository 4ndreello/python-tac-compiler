# Guia de Referência Rápida

## Estrutura do Projeto

O compilador está organizado em módulos lógicos:

```
src/
├── frontend/       # Análise Léxica & Sintática
├── analysis/       # Análise Semântica
├── ir/            # Representação Intermediária
└── optimization/  # Otimização de Código

tests/             # Todos os testes
examples/          # Programas de demonstração
```

## Comandos Rápidos

### Executar Exemplo Principal
```bash
python3 -m src.main
```

### Executar Todos os Testes
```bash
python3 run_tests.py
```

### Executar Testes Semânticos
```bash
python3 run_semantic_tests.py
```

### Executar Demo de Comparação
```bash
python3 run_demo.py
```

## Visão Geral dos Módulos

### Frontend (Léxico & Sintático)
- `lexer.py` - Tokenização
- `parser.py` - Construção da AST
- `ast_nodes.py` - Definições da AST

### Analysis (Semântico)
- `semantic.py` - Tabela de símbolos, verificação de tipos

### IR (Representação Intermediária)
- `ir_generator.py` - Geração de TAC

### Optimization (Otimização)
- `optimizer.py` - Propagação de constantes, DCE

## Caminhos de Importação

```python
# Frontend
from src.frontend.lexer import Lexer
from src.frontend.parser import Parser
from src.frontend.ast_nodes import Program, Declaration, Assignment

# Analysis
from src.analysis.semantic import SemanticAnalyzer, SemanticError

# IR
from src.ir.ir_generator import IRGenerator

# Optimization
from src.optimization.optimizer import Optimizer
```

## Propósito dos Diretórios

| Diretório | Propósito |
|-----------|-----------|
| `src/frontend/` | Processamento de entrada (lexer, parser, AST) |
| `src/analysis/` | Validação semântica |
| `src/ir/` | Geração de código IR |
| `src/optimization/` | Otimização de código |
| `tests/` | Suite de testes |
| `examples/` | Programas demo |

## Arquivos Principais

| Arquivo | Descrição |
|---------|-----------|
| `src/main.py` | Ponto de entrada |
| `run_tests.py` | Executor de testes |
| `README.md` | Documentação completa |
| `docs/STRUCTURE.md` | Informações detalhadas da estrutura |
| `docs/VALIDACAO.md` | Checklist de validação |
