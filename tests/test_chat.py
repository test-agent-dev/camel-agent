from devagent.chat.agent import ChatAgent


def test_chat_initialization():
    agent = ChatAgent()
    assert agent.system_message.content == "ChatAgent"
