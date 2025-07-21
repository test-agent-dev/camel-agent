from devagent.frontend.agent import FrontendAgent


def test_frontend_handle():
    agent = FrontendAgent()
    assert "Frontend handled" in agent.handle_request("test")
