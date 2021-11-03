import socket
import ssl
from typing import Any, BinaryIO, List, Pattern, Tuple, overload

_LongResp = Tuple[bytes, List[bytes], int]

class error_proto(Exception): ...

POP3_PORT: int
POP3_SSL_PORT: int
CR: bytes
LF: bytes
CRLF: bytes

_list = list  # conflicts with a method named "list"

class POP3:
    encoding: str
    host: str
    port: int
    sock: socket.socket
    file: BinaryIO
    welcome: bytes
    def __init__(self, host: str, port: int = ..., timeout: float = ...) -> None: ...
    def getwelcome(self) -> bytes: ...
    def set_debuglevel(self, level: int) -> None: ...
    def user(self, user: str) -> bytes: ...
    def pass_(self, pswd: str) -> bytes: ...
    def stat(self) -> tuple[int, int]: ...
    def list(self, which: Any | None = ...) -> _LongResp: ...
    def retr(self, which: Any) -> _LongResp: ...
    def dele(self, which: Any) -> bytes: ...
    def noop(self) -> bytes: ...
    def rset(self) -> bytes: ...
    def quit(self) -> bytes: ...
    def close(self) -> None: ...
    def rpop(self, user: str) -> bytes: ...
    timestamp: Pattern[str]
    def apop(self, user: str, password: str) -> bytes: ...
    def top(self, which: Any, howmuch: int) -> _LongResp: ...
    @overload
    def uidl(self) -> _LongResp: ...
    @overload
    def uidl(self, which: Any) -> bytes: ...
    def utf8(self) -> bytes: ...
    def capa(self) -> dict[str, _list[str]]: ...
    def stls(self, context: ssl.SSLContext | None = ...) -> bytes: ...

class POP3_SSL(POP3):
    def __init__(
        self,
        host: str,
        port: int = ...,
        keyfile: str | None = ...,
        certfile: str | None = ...,
        timeout: float = ...,
        context: ssl.SSLContext | None = ...,
    ) -> None: ...
    # "context" is actually the last argument, but that breaks LSP and it doesn't really matter because all the arguments are ignored
    def stls(self, context: Any = ..., keyfile: Any = ..., certfile: Any = ...) -> bytes: ...
