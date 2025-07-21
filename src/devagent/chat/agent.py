"""ChatAgent module for interactive conversations."""

from camel.agents import ChatAgent as CamelChatAgent
from camel.models.stub_model import StubModel
from camel.types.enums import ModelType

class ChatAgent(CamelChatAgent):
    """Interactive chat agent for user communication."""

    def __init__(self, system_message: str = "ChatAgent"):
        super().__init__(system_message=system_message, model=StubModel(ModelType.STUB))
