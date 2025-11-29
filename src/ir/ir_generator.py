from src.frontend.ast_nodes import Program, Declaration, Assignment, BinaryOp, Number, Variable

class IRGenerator:
    """Gerador de código intermediário em formato TAC (Three-Address Code)."""

    def __init__(self):
        self.instructions = []
        self.temp_counter = 1

    def new_temp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp

    def generate(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.generate(stmt)
        
        elif isinstance(node, Declaration):
            pass
            
        elif isinstance(node, Assignment):
            result = self.generate(node.expression)
            self.instructions.append(('ASSIGN', result, None, node.name))
            
        elif isinstance(node, BinaryOp):
            left = self.generate(node.left)
            right = self.generate(node.right)
            temp = self.new_temp()
            op_map = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}
            self.instructions.append((op_map[node.op], left, right, temp))
            return temp
            
        elif isinstance(node, Number):
            return str(node.value)
            
        elif isinstance(node, Variable):
            return node.name

    def get_code(self):
        return self.instructions
