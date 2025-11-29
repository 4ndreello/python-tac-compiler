from src.frontend.lexer import Lexer
from src.frontend.parser import Parser
from src.analysis.semantic import SemanticAnalyzer
from src.ir.ir_generator import IRGenerator
from src.optimization.optimizer import Optimizer

def print_ir(instructions, title):
    print(f"--- {title} ---")
    for op, arg1, arg2, result in instructions:
        if op == 'ASSIGN':
            print(f"{result} = {arg1}")
        else:
            symbol = {'ADD': '+', 'SUB': '-', 'MUL': '*', 'DIV': '/'}.get(op, op)
            print(f"{result} = {arg1} {symbol} {arg2}")
    print()

def main():
    source_code = """
    int a;
    int b;
    a = 3 + 2;
    b = a * (a - 1);
    """

    print("=== Original Source ===")
    print(source_code.strip())
    print()

    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    semantic = SemanticAnalyzer()
    semantic.analyze(ast)
    
    print("=== Symbol Table ===")
    for name, type_ in semantic.symbol_table.items():
        print(f"{name}: {type_}")
    print()

    ir_gen = IRGenerator()
    ir_gen.generate(ast)
    original_ir = ir_gen.get_code()

    print_ir(original_ir, "Original Intermediate Code")

    optimizer = Optimizer()
    optimized_ir = optimizer.optimize(original_ir)

    print_ir(optimized_ir, "Optimized Intermediate Code")

if __name__ == "__main__":
    main()
