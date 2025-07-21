from devagent.config import config

def test_env_loading():
    assert isinstance(config.agents, list)
    assert config.models_spec
