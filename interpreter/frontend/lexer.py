from .source import Source
from .token import Token



class Lexer:
    def __init__(self, source: Source):
        this._source = source
        this._current_token: Token = None

    def current_token(self) -> Token:
        return self._current_token

    def next_token(self) -> Token:
        self._current_token = self._extract_token()
        return self._current_token

    def _extract_token(self) -> Token:
        pass

