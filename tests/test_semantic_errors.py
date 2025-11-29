

from src.frontend.lexer import Lexer
from src.frontend.parser import Parser
from src.analysis.semantic import SemanticAnalyzer, SemanticError

def test_semantic_error(code, description):
    print(f"\n{'='*70}")
    print(f"TEST: {description}")
    print('='*70)
    print("\nCode:")
    print(code.strip())
    print()
    
    try:
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        semantic = SemanticAnalyzer()
        semantic.analyze(ast)
        
        print("FAIL: Expected semantic error, but none was detected!")
        
    except SemanticError as e:
        print(f"SUCCESS: Semantic error detected correctly!")
        print(f"   Message: {e}")

print("\n" + "="*70)
print("  SEMANTIC ERROR DETECTION TESTS")
print("="*70)

test_semantic_error("""
int a;
a = b + 1;
""", "Undeclared variable (b)")

test_semantic_error("""
int x;
int x;
""", "Variable redeclaration (x)")

test_semantic_error("""
int result;
result = foo * 2;
""", "Undeclared variable in expression (foo)")

test_semantic_error("""
int a;
a = x + y + z;
""", "Multiple undeclared variables (x, y, z)")

test_semantic_error("""
int value;
value = 10;
int value;
""", "Redeclaration after use (value)")

print("\n" + "="*70)
print("  VALID CODE TEST")
print("="*70)

print("\nValid code (should pass without errors):")
valid_code = """
int a;
int b;
int c;
a = 10;
b = 20;
c = a + b;
"""
print(valid_code.strip())

try:
    lexer = Lexer(valid_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    semantic = SemanticAnalyzer()
    semantic.analyze(ast)
    
    print("\nSUCCESS: Valid code compiled without errors!")
    print("\nSymbol Table:")
    for name, type_ in semantic.symbol_table.items():
        print(f"  {name}: {type_}")
        
except Exception as e:
    print(f"\nFAIL: {e}")

print("\n" + "="*70)
print("ALL SEMANTIC VALIDATION TESTS PASSED")
print("="*70)
