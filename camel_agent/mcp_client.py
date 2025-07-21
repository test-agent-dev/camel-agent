import socket
from typing import Optional

class MCPClient:
    """Simple TCP client to communicate with an MCP server."""

    def __init__(self, host: str, port: int, timeout: float = 5.0) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock: Optional[socket.socket] = None

    def connect(self) -> None:
        self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)

    def send(self, data: str) -> None:
        if not self.sock:
            raise RuntimeError("Client not connected")
        self.sock.sendall(data.encode('utf-8'))

    def receive(self, bufsize: int = 4096) -> str:
        if not self.sock:
            raise RuntimeError("Client not connected")
        return self.sock.recv(bufsize).decode('utf-8')

    def close(self) -> None:
        if self.sock:
            try:
                self.sock.close()
            finally:
                self.sock = None
