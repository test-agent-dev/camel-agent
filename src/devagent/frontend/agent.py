"""FrontendAgent module."""

from camel.agents import ChatAgent
from ..config import config

class FrontendAgent(ChatAgent):
    """Expert agent responsible for frontend tasks."""

    def __init__(self, model=None):
        if model is None:
            model = config.get_model_for_agent("FrontendAgent")
        super().__init__(system_message="FrontendAgent", model=model)

    def handle_request(self, request: str) -> str:
        """Handle frontend-related requests."""
        print(f"[FrontendAgent] Handling request: {request}")
        return f"Frontend handled: {request}"
