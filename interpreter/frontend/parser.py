from .lexer import Lexer
from ..intermediate.ast import AST
from ..intermediate.symbol_table import SymbolTable

class Parser:
    _sym_tab = SymbolTable()

    def __init__(self, lexer: Lexer):
        self._lexer = lexer
        self._ast = AST()

    def parse(self) -> None:
        pass

    def get_error_count(self) -> int:
        return 0



