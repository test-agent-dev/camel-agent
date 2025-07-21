"""BackendAgent module."""

from camel.agents import ChatAgent
from camel.models.stub_model import StubModel
from camel.types.enums import ModelType

class BackendAgent(ChatAgent):
    """Expert agent responsible for backend tasks."""

    def __init__(self):
        super().__init__(system_message="BackendAgent", model=StubModel(ModelType.STUB))

    def handle_request(self, request: str) -> str:
        """Handle backend-related requests."""
        print(f"[BackendAgent] Handling request: {request}")
        return f"Backend handled: {request}"
