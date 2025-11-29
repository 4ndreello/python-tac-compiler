# Copilot Instructions - Compilador

## Project Overview
Educational compiler in Python implementing a classical compilation pipeline: lexical analysis → parsing → semantic analysis → IR generation → optimization. Processes a C-like language with `int` declarations and arithmetic expressions into optimized Three-Address Code (TAC).

## Architecture & Pipeline

### Compilation Stages (in order)
1. **Lexer** (`src/frontend/lexer.py`) - Regex-based tokenization into tuples `(token_type, value)`
2. **Parser** (`src/frontend/parser.py`) - Recursive descent parser builds AST from tokens
3. **Semantic Analyzer** (`src/analysis/semantic.py`) - Symbol table validation, detects redeclarations/undeclared vars
4. **IR Generator** (`src/ir/ir_generator.py`) - Generates TAC with auto-incrementing temporaries (`t1`, `t2`...)
5. **Optimizer** (`src/optimization/optimizer.py`) - Fixed-point iteration of constant propagation/folding + DCE

### Data Flow
```
Source → Tokens → AST → Validated AST → TAC Instructions → Optimized TAC
         (Lexer)  (Parser) (Semantic)     (IRGenerator)    (Optimizer)
```

### Key Insight: TAC Representation
IR instructions are 4-tuples: `(operation, arg1, arg2, result)`
- Binary ops: `('ADD', '3', '2', 't1')` → `t1 = 3 + 2`
- Assignments: `('ASSIGN', 't1', None, 'a')` → `a = t1`

## Critical Conventions

### AST Node Pattern
All AST nodes in `src/frontend/ast_nodes.py` use `@dataclass` and inherit from `Node`. Visitor-style pattern used across semantic analysis and IR generation:
```python
if isinstance(node, Program):
    for stmt in node.statements:
        self.analyze(stmt)  # or self.generate(stmt)
```

### Module Import Structure
Always use **absolute imports** with `src.` prefix:
```python
from src.frontend.lexer import Lexer
from src.analysis.semantic import SemanticAnalyzer, SemanticError
```
Never use relative imports outside package (`from .lexer import Lexer` only within `src/frontend/`).

### Optimizer Fixed-Point Iteration
`Optimizer.optimize()` runs passes in a loop until no changes occur. Each pass returns `(new_ir, changed_flag)`:
```python
while changed:
    new_ir, folded = self.constant_propagation(current_ir)
    if folded: changed = True; current_ir = new_ir
```
When adding optimizations, follow this `(instructions, bool)` return pattern.

### Constant Propagation State Management
The optimizer maintains a `constants` dict mapping variable names to their constant values. **Critical**: Delete entries when variables receive non-constant values to prevent incorrect propagation:
```python
if result in constants and op != 'ASSIGN':
    del constants[result]  # Variable no longer constant
```

## Developer Workflows

### Running Tests
```bash
python3 run_tests.py                 # Full test suite (8 tests in test_compiler.py)
python3 run_semantic_tests.py        # Semantic error detection only
python3 run_demo.py                  # Visual before/after optimization demo
python3 -m src.main                  # Main example from README
```

### Adding New Test Cases
Tests in `tests/test_compiler.py` follow pattern:
```python
test_code = """
int x;
x = 5 + 3;
"""
compile_and_optimize(test_code, "TEST N: Description")
```
Helper function `compile_and_optimize()` runs full pipeline and prints all stages.

### Extending the Language

**New operators**: 
1. Add token to `Lexer.tokenize()` token_specs
2. Update `Parser.term()` or `Parser.factor()` precedence level
3. Map operator in `IRGenerator.generate()` op_map
4. Handle in `Optimizer.constant_propagation()` arithmetic evaluation

**New types**: 
1. Add token pattern in Lexer
2. Update `Declaration` handling in semantic analyzer
3. Add type checking logic (currently only validates existence, not type compatibility)

## File Locations

| Component | File | Key Classes/Functions |
|-----------|------|----------------------|
| Entry point | `src/main.py` | `main()` |
| Tokenization | `src/frontend/lexer.py` | `Lexer.tokenize()` |
| Parsing | `src/frontend/parser.py` | `Parser.parse()`, precedence methods |
| AST definitions | `src/frontend/ast_nodes.py` | `Program`, `Declaration`, `BinaryOp`, etc. |
| Semantic checks | `src/analysis/semantic.py` | `SemanticAnalyzer.analyze()`, `symbol_table` |
| IR generation | `src/ir/ir_generator.py` | `IRGenerator.generate()`, `new_temp()` |
| Optimization | `src/optimization/optimizer.py` | `constant_propagation()`, `dead_code_elimination()` |

## Common Patterns

### Error Handling
Raise `SemanticError` (custom exception) for semantic issues. Parser raises `SyntaxError` directly. Lexer raises `RuntimeError` for invalid characters.

### Temporary Variable Naming
Auto-increment counter in `IRGenerator.new_temp()` generates `t1`, `t2`, etc. Never reuse temporaries—optimizer handles elimination.

### Symbol Table Structure
Simple `dict[str, str]` mapping variable name → type (currently always `'int'`). No scoping—all variables are global.

## Testing Philosophy
Tests in `test_compiler.py` are **full-pipeline integration tests**, not unit tests. Each test runs: lex → parse → semantic → IR → optimize. Includes both positive tests (optimization effectiveness) and negative tests (semantic error detection in TEST 4 & 5).
