from src.frontend.ast_nodes import Program, Declaration, Assignment, BinaryOp, Number, Variable

class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.analyze(stmt)
        
        elif isinstance(node, Declaration):
            if node.name in self.symbol_table:
                raise SemanticError(f"Variable '{node.name}' already declared")
            self.symbol_table[node.name] = node.var_type
            
        elif isinstance(node, Assignment):
            if node.name not in self.symbol_table:
                raise SemanticError(f"Variable '{node.name}' not declared")
            self.analyze(node.expression)
            
        elif isinstance(node, BinaryOp):
            self.analyze(node.left)
            self.analyze(node.right)
            
        elif isinstance(node, Variable):
            if node.name not in self.symbol_table:
                raise SemanticError(f"Variable '{node.name}' not declared")
