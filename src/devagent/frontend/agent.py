"""FrontendAgent module."""

from camel.agents import ChatAgent
from camel.models.stub_model import StubModel
from camel.types.enums import ModelType

class FrontendAgent(ChatAgent):
    """Expert agent responsible for frontend tasks."""

    def __init__(self):
        super().__init__(system_message="FrontendAgent", model=StubModel(ModelType.STUB))

    def handle_request(self, request: str) -> str:
        """Handle frontend-related requests."""
        print(f"[FrontendAgent] Handling request: {request}")
        return f"Frontend handled: {request}"
