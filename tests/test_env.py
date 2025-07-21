from devagent.config import settings

def test_env_loading():
    assert isinstance(settings.AGENTS, list)
    assert settings.MODELS
