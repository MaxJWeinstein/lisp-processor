from ..source import Source
from ..token import Token, TokenType, PARENTHESES

class Parenthesis(Token):
    def extract(self) -> None:
        self._text = self._source.current_char()
        self._value = None
        self._type = TokenType(self._text)
        if self._type not in PARENTHESES:
            self._type = TokenType.INVALID_TOKEN



