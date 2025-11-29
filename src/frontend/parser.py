from typing import List, Tuple
from .ast_nodes import Program, Declaration, Assignment, BinaryOp, Number, Variable

class Parser:
    def __init__(self, tokens: List[Tuple[str, str]]):
        self.tokens = tokens
        self.pos = 0

    def parse(self) -> Program:
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.statement())
        return Program(statements)

    def statement(self):
        if self.check('INT'):
            return self.declaration()
        else:
            return self.assignment()

    def declaration(self):
        self.consume('INT')
        name = self.consume('ID')[1]
        self.consume('SEMI')
        return Declaration('int', name)

    def assignment(self):
        name = self.consume('ID')[1]
        self.consume('EQUALS')
        expr = self.expression()
        self.consume('SEMI')
        return Assignment(name, expr)

    def expression(self):
        node = self.term()
        while self.check('PLUS') or self.check('MINUS'):
            op = self.advance()[1]
            right = self.term()
            node = BinaryOp(node, op, right)
        return node

    def term(self):
        node = self.factor()
        while self.check('STAR') or self.check('SLASH'):
            op = self.advance()[1]
            right = self.factor()
            node = BinaryOp(node, op, right)
        return node

    def factor(self):
        if self.check('NUMBER'):
            return Number(int(self.advance()[1]))
        elif self.check('ID'):
            return Variable(self.advance()[1])
        elif self.check('LPAREN'):
            self.consume('LPAREN')
            expr = self.expression()
            self.consume('RPAREN')
            return expr
        raise SyntaxError(f"Unexpected token: {self.tokens[self.pos]}")

    def check(self, kind):
        return self.pos < len(self.tokens) and self.tokens[self.pos][0] == kind

    def advance(self):
        self.pos += 1
        return self.tokens[self.pos - 1]

    def consume(self, kind):
        if self.check(kind):
            return self.advance()
        raise SyntaxError(f"Expected {kind}, got {self.tokens[self.pos] if self.pos < len(self.tokens) else 'EOF'}")
