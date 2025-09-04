from enum import Enum

from .source import Source

class TokenType(Enum):
    EOF = -1

    L_PAREN = "("
    R_PAREN = ")"
    L_BRACKET = "["
    R_BRACKET = "]"
    L_BRACE = "{"
    R_BRACE = "}"

    STR_QUOTE = "\""
    QUOTE = "'"
    QUASIQUOTE = "`"
    UNQUOTE = ","
    UNQUOTE_SPLICING = ",@"

    DOT = "."

    TRUE = "#t"
    FALSE = "#f"

    SYMBOL = "symbol"
    NUMBER = "number"

    INVALID_TOKEN = None
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value == value:
                return member
        return cls(-1)

PARENTHESES: list[TokenType] = [
    TokenType.L_PAREN, TokenType.R_PAREN,
    TokenType.L_BRACE, TokenType.R_BRACE,
    TokenType.L_BRACKET, TokenType.R_BRACKET
]



class Token():
    def __init__(self, source: Source):
        self._source = source
        self._line_num = source._line_num
        self._position = source._current_pos

        self._type: TokenType = None
        self._text: str = ""
        self._value: object = None

        self.extract()

    def extract(self) -> None:
        self._text = self._source.current_char()
        self._source.next_char()

class EofToken(Token):
    def __init__(self):
        self._type = TokenType.EOF
    def extract(self) -> None:
        pass
