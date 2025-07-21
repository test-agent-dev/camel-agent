from devagent.dev.agent import DevAgent


def test_delegate():
    agent = DevAgent()
    result = agent.delegate("test")
    assert all("handled" in v for v in result.values())
