"""BackendAgent module."""

from camel.agents import ChatAgent
from ..config import config

class BackendAgent(ChatAgent):
    """Expert agent responsible for backend tasks."""

    def __init__(self, model=None):
        if model is None:
            model = config.get_model_for_agent("BackendAgent")
        super().__init__(system_message="BackendAgent", model=model)

    def handle_request(self, request: str) -> str:
        """Handle backend-related requests."""
        print(f"[BackendAgent] Handling request: {request}")
        return f"Backend handled: {request}"
