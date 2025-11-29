# VALIDAO DO TRABALHO - Anlise Semntica e Gerao/Otimizao de Cdigo Intermedirio

## Checklist dos Requisitos

### Parte Prtica 

#### 1. Anlise Semntica 
- [x] **Detectar erros de tipo e variveis no declaradas**
 - Implementado em `src/semantic.py`
 - Testa variveis no declaradas antes do uso
 - Exemplo: `Variable 'b' not declared`
 
- [x] **Detectar redeclarao de variveis**
 - Verifica duplicatas na tabela de smbolos
 - Exemplo: `Variable 'x' already declared`
 
- [x] **Montar tabela de smbolos**
 - Estrutura: `{nome_variavel: tipo}`
 - Exemplo: `a: int, b: int`

#### 2. Gerao de Cdigo Intermedirio (TAC) 
- [x] **Cdigo de trs endereos**
 - Implementado em `src/ir_generator.py`
 - Formato: `resultado = operando1 operador operando2`
 
- [x] **Exemplo do trabalho funciona corretamente:**
 ```
 Entrada:
 a = 3 + 2;
 b = a * (a - 1);
 
 Sada TAC:
 t1 = 3 + 2
 a = t1
 t2 = a - 1
 t3 = a * t2
 b = t3
 ```

#### 3. Implementao de Otimizaes 
- [x] **Propagao de constantes**
 - Substitui variveis por valores conhecidos
 - `a = 5` usa `5` em vez de `a` nas expresses seguintes
 
- [x] **Dobramento de constantes (Constant Folding)**
 - Calcula expresses constantes em tempo de compilao
 - `3 + 2` `5`
 - `5 * 4` `20`
 
- [x] **Eliminao de cdigo morto (DCE)**
 - Remove temporrios no utilizados
 - Remove `t1`, `t2`, `t3` quando no so mais necessrios

#### 4. Sada Esperada 
- [x] **Impresso da tabela de smbolos**
 ```
 === Tabela de Simbolos ===
 a: int
 b: int
 ```

- [x] **Cdigo intermedirio original**
 ```
 --- Codigo Intermediario Original ---
 t1 = 3 + 2
 a = t1
 t2 = a - 1
 t3 = a * t2
 b = t3
 ```

- [x] **Cdigo intermedirio otimizado**
 ```
 --- Codigo Intermediario Otimizado ---
 a = 5
 b = 20
 ```

## Testes Realizados

### Teste 1: Exemplo Original do Trabalho
```python
int a;
int b;
a = 3 + 2;
b = a * (a - 1);
```
**Resultado:** 5 instrues 2 instrues (60% de reduo)

### Teste 2: Propagao em Cadeia
```python
int x;
int y;
int z;
x = 10;
y = x + 5;
z = y * 2;
```
**Resultado:** 5 instrues 3 instrues (40% de reduo)

### Teste 3: Expresso Complexa
```python
int result;
result = 2 + 3 * 4 - 1;
```
**Resultado:** 4 instrues 1 instruo (75% de reduo)

### Teste 4: Deteco de Erro - Varivel No Declarada
```python
int a;
a = b + 1; // b no foi declarado
```
**Resultado:** Erro Semntico: Variable 'b' not declared

### Teste 5: Deteco de Erro - Redeclarao
```python
int x;
int x; // x j foi declarado
```
**Resultado:** Erro Semntico: Variable 'x' already declared

### Teste 6: Expresses com Parnteses
```python
int a;
int b;
int c;
a = 5;
b = 3;
c = (a + b) * (a - b);
```
**Resultado:** 6 instrues 3 instrues (50% de reduo)

### Teste 7: Operaes de Diviso
```python
int x;
int y;
x = 100 / 10;
y = x / 2;
```
**Resultado:** 4 instrues 2 instrues (50% de reduo)

### Teste 8: Mltiplas Variveis
```python
int a;
int b;
int c;
int d;
a = 1 + 2;
b = 3 + 4;
c = a + b;
d = c * 2;
```
**Resultado:** 8 instrues 4 instrues (50% de reduo)

## Estatsticas Gerais

- **Total de testes executados:** 8
- **Testes bem-sucedidos:** 8 (100%)
- **Erros detectados corretamente:** 
- **Reduo mdia de cdigo:** ~55%

## Otimizaes Validadas

### 1. Constant Folding (Dobramento de Constantes) 
**Exemplo:**
```
ANTES: t1 = 3 + 2
DEPOIS: t1 = 5
```

### 2. Constant Propagation (Propagao de Constantes) 
**Exemplo:**
```
ANTES: 
 a = 5
 t2 = a - 1
DEPOIS:
 a = 5
 t2 = 5 - 1 (que vira t2 = 4)
```

### 3. Dead Code Elimination (Eliminao de Cdigo Morto) 
**Exemplo:**
```
ANTES:
 t1 = 3 + 2
 a = t1
 t2 = a - 1
 t3 = a * t2
 b = t3

DEPOIS:
 a = 5
 b = 20
 (t1, t2, t3 removidos - cdigo morto)
```

## Estrutura do Cdigo

```
src/
 ast_nodes.py Ns da AST bem definidos
 lexer.py Anlise lxica funcionando
 parser.py Parser recursivo descendente
 semantic.py Anlise semntica completa
 ir_generator.py Gerao de TAC correta
 optimizer.py Otimizaes implementadas
 main.py Programa principal

Testes:
 test_compiler.py Suite completa de testes
 test_semantic_errors.py Validao de erros
 demo_comparison.py Comparao visual
```

## CONCLUSO

**TODOS OS REQUISITOS DO TRABALHO FORAM IMPLEMENTADOS E VALIDADOS COM SUCESSO!**

### Requisitos Atendidos:
1. Anlise Semntica completa
2. Gerao de Cdigo de Trs Endereos (TAC)
3. Otimizaes implementadas (mnimo 2, implementamos 3)
4. Tabela de smbolos funcionando
5. Deteco de erros semnticos
6. Sada formatada conforme especificao

### Como Executar:
```bash
# Exemplo principal
python3 -m src.main

# Todos os testes
python3 test_compiler.py

# Testes de erro
python3 test_semantic_errors.py

# Comparao visual
python3 demo_comparison.py
```

### Tecnologias Utilizadas:
- Python 3
- Estruturas de dados nativas
- Pattern matching e visitor pattern para AST
- Algoritmo de ponto fixo para otimizaes

---
**Status:** PRONTO PARA ENTREGA
**Data de Validao:** 2025-11-29
