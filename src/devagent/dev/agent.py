"""DevAgent orchestrates specialized agents."""

from dataclasses import dataclass
import os
import subprocess

from camel.agents import ChatAgent
from camel.models.stub_model import StubModel
from camel.types.enums import ModelType

from ..backend.agent import BackendAgent
from ..frontend.agent import FrontendAgent
from ..db.agent import DBAgent
from ..chat.agent import ChatAgent as UserChatAgent
from ..config import settings
from ..storage import StorageService
from camel.toolkits import MCPToolkit

@dataclass
class DevAgent(ChatAgent):
    """Main development agent orchestrating expert agents."""

    def __init__(self) -> None:
        server_dict = {f"srv{i}": cfg for i, cfg in enumerate(settings.MCP_SERVERS)}
        self.toolkit = MCPToolkit(config_dict={"mcpServers": server_dict})
        super().__init__(system_message="DevAgent", model=StubModel(ModelType.STUB))
        self.storage = StorageService()
        self.backend = BackendAgent()
        self.frontend = FrontendAgent()
        self.db = DBAgent()
        self.chat = UserChatAgent()

    def create_project(self, name: str, language: str) -> str:
        """Create a hello world project in the given language."""
        ext_map = {"python": "py", "javascript": "js", "java": "java"}
        ext = ext_map.get(language.lower(), "txt")
        root = os.path.join(os.getcwd(), name)
        os.makedirs(root, exist_ok=True)
        path = os.path.join(root, f"main.{ext}")
        with open(path, "w") as f:
            if language.lower() == "python":
                f.write("print('hello world')\n")
            elif language.lower() == "javascript":
                f.write("console.log('hello world');\n")
            elif language.lower() == "java":
                f.write("public class Main { public static void main(String[] args) { System.out.println(\"hello world\"); } }")
            else:
                f.write("hello world\n")
        return root

    def delegate(self, request: str) -> dict:
        """Delegate work to specialized agents."""
        return {
            "backend": self.backend.handle_request(request),
            "frontend": self.frontend.handle_request(request),
            "db": self.db.handle_request(request),
        }

    def upload_project(self, project_path: str) -> None:
        """Upload project using the storage service."""
        self.storage.upload(project_path, settings.STORAGE_URL)

    def verify(self, project_path: str) -> None:
        """Run a simple verification by compiling Python files."""
        subprocess.run(["python3", "-m", "py_compile", project_path], check=False)
