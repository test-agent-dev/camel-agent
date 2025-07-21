import shutil
from pathlib import Path
from camel_agent import CamelAgent


def test_demo_generation(tmp_path: Path):
    config_file = tmp_path / 'config.json'
    config_file.write_text('{"mcp": {"host": "localhost", "port": 9000}, "storage_path": "' + str(tmp_path / 'out') + '"}')
    agent = CamelAgent(str(config_file))
    context = {'project_name': 'proj', 'architecture': 'test'}
    dest = agent.build_project('python_agent', context)
    assert (dest / 'main.py').exists()
