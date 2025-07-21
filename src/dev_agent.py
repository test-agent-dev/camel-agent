# DevAgent using Camel-AI and MCPToolkit
# This script demonstrates orchestrating multiple expert agents,
# loading configuration from mcp_config.json, creating a project
# skeleton and uploading results using a pluggable StorageService.

import json
import os
import subprocess
from dataclasses import dataclass
from typing import Dict, Any

from camel.agents import ChatAgent
from camel.agents import MCPAgent
from app.toolkit import MCPToolKit as MCPToolkit

@dataclass
class StorageService:
    """Simple storage service placeholder."""

    def upload(self, source: str, destination: str) -> None:
        """Simulate uploading files to a remote location."""
        print(f"[Storage] Uploading {source} -> {destination}")


class BackendAgent(ChatAgent):
    """Expert agent responsible for backend tasks."""

    def __init__(self):
        from camel.models.stub_model import StubModel
        from camel.types.enums import ModelType
        super().__init__(system_message="BackendAgent", model=StubModel(ModelType.STUB))

    def handle_request(self, request: str) -> str:
        print(f"[BackendAgent] Handling request: {request}")
        return f"Backend handled: {request}"


class FrontendAgent(ChatAgent):
    """Expert agent responsible for frontend tasks."""

    def __init__(self):
        from camel.models.stub_model import StubModel
        from camel.types.enums import ModelType
        super().__init__(system_message="FrontendAgent", model=StubModel(ModelType.STUB))

    def handle_request(self, request: str) -> str:
        print(f"[FrontendAgent] Handling request: {request}")
        return f"Frontend handled: {request}"


class DBAgent(ChatAgent):
    """Expert agent responsible for database tasks."""

    def __init__(self):
        from camel.models.stub_model import StubModel
        from camel.types.enums import ModelType
        super().__init__(system_message="DBAgent", model=StubModel(ModelType.STUB))

    def handle_request(self, request: str) -> str:
        print(f"[DBAgent] Handling request: {request}")
        return f"DB handled: {request}"


class DevAgent(ChatAgent):
    """Main development agent orchestrating expert agents."""

    def __init__(self, config_path: str = "mcp_config.json") -> None:
        self.config_path = config_path
        self.toolkit = self._load_mcp_config()
        from camel.models.stub_model import StubModel
        from camel.types.enums import ModelType
        super().__init__(system_message="DevAgent", model=StubModel(ModelType.STUB))
        self.storage = StorageService()
        self.backend = BackendAgent()
        self.frontend = FrontendAgent()
        self.db = DBAgent()

    def _load_mcp_config(self) -> MCPToolkit:
        """Load MCP configuration from JSON file and build a toolkit."""
        with open(self.config_path, "r") as f:
            cfg = json.load(f)

        print(f"[DevAgent] Loaded MCP config: {cfg}")
        server = cfg["servers"][0]
        url = f"http://{server['host']}:{server['port']}"
        return MCPToolkit(url)

    def create_project(self, name: str, architecture: str) -> str:
        """Create a basic project structure."""
        root = os.path.join(os.getcwd(), name)
        os.makedirs(root, exist_ok=True)
        open(os.path.join(root, "__init__.py"), "w").close()
        if architecture == "monolith":
            os.makedirs(os.path.join(root, "app"), exist_ok=True)
            open(os.path.join(root, "app", "main.py"), "w").write(
                "print('Monolith running')\n")
        elif architecture == "microservices":
            for svc in ["service_a", "service_b"]:
                path = os.path.join(root, svc)
                os.makedirs(path, exist_ok=True)
                open(os.path.join(path, "__init__.py"), "w").close()
                open(os.path.join(path, "main.py"), "w").write(
                    f"print('{svc} running')\n")
        elif architecture == "hexagonal":
            for layer in ["domain", "application", "infrastructure"]:
                os.makedirs(os.path.join(root, layer), exist_ok=True)
        else:
            raise ValueError(f"Unknown architecture: {architecture}")
        print(f"[DevAgent] Created {architecture} project at {root}")
        return root

    def delegate(self, request: str) -> Dict[str, str]:
        """Delegate sub tasks to expert agents."""
        result = {
            "backend": self.backend.handle_request(request),
            "frontend": self.frontend.handle_request(request),
            "db": self.db.handle_request(request),
        }
        return result

    def upload_project(self, project_path: str) -> None:
        """Upload project using the storage service."""
        self.storage.upload(project_path, "remote://project")

    def verify(self, project_path: str) -> None:
        """Run a simple verification by compiling Python files."""
        print(f"[DevAgent] Verifying project at {project_path}")
        subprocess.run(["python3", "-m", "py_compile", "-q", project_path], check=False)


def main() -> None:
    agent = DevAgent()
    project = agent.create_project("sample_project", "monolith")
    results = agent.delegate("Implement feature X")
    print("[DevAgent] Delegation results:", results)
    agent.upload_project(project)
    agent.verify(project)
    print("[DevAgent] Done.")


if __name__ == "__main__":
    main()
