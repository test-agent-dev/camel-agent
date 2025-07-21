from devagent.society import AISociety, run_society
from devagent.backend.agent import BackendAgent
from devagent.frontend.agent import FrontendAgent

def test_run_society():
    society = AISociety([BackendAgent(), FrontendAgent()])
    history = run_society(society, "do work")
    assert len(history) == 2
