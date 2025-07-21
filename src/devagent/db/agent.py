"""DBAgent module."""

from camel.agents import ChatAgent
from camel.models.stub_model import StubModel
from camel.types.enums import ModelType

class DBAgent(ChatAgent):
    """Expert agent responsible for database tasks."""

    def __init__(self):
        super().__init__(system_message="DBAgent", model=StubModel(ModelType.STUB))

    def handle_request(self, request: str) -> str:
        """Handle database-related requests."""
        print(f"[DBAgent] Handling request: {request}")
        return f"DB handled: {request}"
