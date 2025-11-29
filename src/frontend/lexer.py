import re
from typing import List, Tuple

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Tuple[str, str]] = []
        self.pos = 0

    def tokenize(self) -> List[Tuple[str, str]]:
        token_specs = [
            ('INT', r'\bint\b'),
            ('NUMBER', r'\d+'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('EQUALS', r'='),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('STAR', r'\*'),
            ('SLASH', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('SEMI', r';'),
            ('WS', r'\s+'),
            ('MISMATCH', r'.'),
        ]
        
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
        
        for mo in re.finditer(token_regex, self.source):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'WS':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected character: {value}')
            self.tokens.append((kind, value))
        
        return self.tokens
