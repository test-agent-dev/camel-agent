from devagent.db.agent import DBAgent


def test_db_handle():
    agent = DBAgent()
    assert "DB handled" in agent.handle_request("test")
