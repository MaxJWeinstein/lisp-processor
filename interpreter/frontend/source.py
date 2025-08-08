from io import TextIOBase

class Source:
    EOL: str = "\n"
    EOF: str = "EOF"

    def __init__(self, stream: TextIOBase):
        self._stream = stream
        self._line: str = ""
        self._line_num: int = 0
        self._current_pos: int = -2

    def current_char(self) -> str:
        if (self._current_pos == -2) or (self._current_pos > len(self._line)):
            self._read_next_line()
            return self.current_char()
        if self._current_pos == len(self._line):
            return EOL
        if self._current_pos == -1:
            return EOF
        return self._line[self._current_pos]

    def next_char(self) -> str:
        self._current_pos += 1
        return self.current_char()

    def peek_char(self) -> str:
        # make sure we've read a line in
        self.current_char()

        pos = self._current_pos + 1
        if pos == 0:
            return EOF
        if pos == len(self._line):
            return EOL

        return self._line[pos]

    def close(self) -> None:
        self._stream.close()


    def _read_next_line(self) -> None:
        self._line = self._stream.readline()
        if self._line == "":
            self._current_pos = -1
        else:
            self._line_num += 1
            self._current_pos = 0
