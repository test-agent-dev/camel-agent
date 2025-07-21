import json
from pathlib import Path
from typing import Any, Dict, Type
import importlib

from .mcp_client import MCPClient

class CamelAgent:
    """Main agent orchestrating expert agents and MCP communication."""

    def __init__(self, config_path: str = 'config.json') -> None:
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        mcp_conf = self.config.get('mcp', {})
        self.mcp_client = MCPClient(mcp_conf.get('host', 'localhost'), mcp_conf.get('port', 9000))
        self.storage_path = Path(self.config.get('storage_path', 'server'))

    def load_expert(self, name: str) -> Any:
        module = importlib.import_module(f'expert_agents.{name}')
        class_name = ''.join(part.capitalize() for part in name.split('_'))
        expert_cls: Type[Any] = getattr(module, class_name)
        return expert_cls()

    def build_project(self, expert: str, context: Dict[str, str]) -> Path:
        expert_agent = self.load_expert(expert)
        dest = self.storage_path / context.get('project_name', 'demo')
        expert_agent.generate_code(context, dest)
        return dest

    def send_to_mcp(self, message: str) -> str:
        self.mcp_client.connect()
        try:
            self.mcp_client.send(message)
            return self.mcp_client.receive()
        finally:
            self.mcp_client.close()
