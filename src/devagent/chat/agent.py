"""ChatAgent module for interactive conversations."""

from camel.agents import ChatAgent as CamelChatAgent
from ..config import config

class ChatAgent(CamelChatAgent):
    """Interactive chat agent for user communication."""

    def __init__(self, system_message: str = "ChatAgent", model=None):
        if model is None:
            model = config.get_model_for_agent("ChatAgent")
        super().__init__(system_message=system_message, model=model)
