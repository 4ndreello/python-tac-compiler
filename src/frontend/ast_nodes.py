from dataclasses import dataclass
from typing import Any, List, Optional

@dataclass
class Node:
    pass

@dataclass
class Program(Node):
    statements: List[Node]

@dataclass
class Declaration(Node):
    var_type: str
    name: str

@dataclass
class Assignment(Node):
    name: str
    expression: Node

@dataclass
class BinaryOp(Node):
    left: Node
    op: str
    right: Node

@dataclass
class Number(Node):
    value: int

@dataclass
class Variable(Node):
    name: str
