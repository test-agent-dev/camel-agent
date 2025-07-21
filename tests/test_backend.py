from devagent.backend.agent import BackendAgent


def test_backend_handle():
    agent = BackendAgent()
    assert "Backend handled" in agent.handle_request("test")
