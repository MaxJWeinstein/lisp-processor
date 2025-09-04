from .frontend.source import Source
from .frontend.lexer import Lexer
from .frontend.parser import Parser
from .intermediate.symbol_table import SymbolTable
from .intermediate.ast import AST
from .backend.executor import Executor

from sys import argv, stdin
from io import TextIOWrapper

def main(args: list[str]):
    stream: TextIOWrapper = stdin
    if len(args) == 1:
        filename = args[0]
        stream = open(filename, "r", encoding="utf-8")
    elif len(args) > 1:
        raise ValueError("Given more than one argument")
    source = Source(stream)
    while source.current_char() != Source.EOF:
        while source.current_char() != Source.EOL:
            print(source.current_char(), end='')
            source.next_char()
        print()
        source.next_char()

if __name__ == "__main__":
    main(argv[1:])
