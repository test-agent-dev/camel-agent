"""DBAgent module."""

from camel.agents import ChatAgent
from ..config import config

class DBAgent(ChatAgent):
    """Expert agent responsible for database tasks."""

    def __init__(self, model=None):
        if model is None:
            model = config.get_model_for_agent("DBAgent")
        super().__init__(system_message="DBAgent", model=model)

    def handle_request(self, request: str) -> str:
        """Handle database-related requests."""
        print(f"[DBAgent] Handling request: {request}")
        return f"DB handled: {request}"
