"""Application configuration loader using python-dotenv.

This module exposes a :class:`ConfigLoader` that reads environment variables,
validates them and provides helper methods to retrieve the correct model for
each agent. Models are created with Camel-AI's ``ModelFactory`` so any
supported backend can be configured without code changes.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

from dotenv import load_dotenv
from camel.models.model_factory import ModelFactory
from camel.types.enums import ModelPlatformType, ModelType


load_dotenv()


def _split_env(value: str) -> List[str]:
    """Return a list from a comma separated environment variable."""
    return [v.strip() for v in value.split(',') if v.strip()]


def _to_platform(value: str) -> ModelPlatformType:
    """Convert a string to ``ModelPlatformType``."""
    return ModelPlatformType[value.replace('-', '_').upper()]


def _to_model(value: str) -> ModelType:
    """Convert a string to ``ModelType``."""
    return ModelType[value.replace('-', '_').upper()]


@dataclass
class ConfigLoader:
    """Centralised configuration loaded from ``.env``."""

    default_platform: ModelPlatformType
    default_model: ModelType
    mcp_servers: List[Dict[str, str]]
    agents: List[str]
    storage_url: str
    models_spec: List[Tuple[ModelPlatformType, ModelType]]
    agent_model_map: Dict[str, Tuple[ModelPlatformType, ModelType]]
    _models: Dict[Tuple[str, str], object]

    def __init__(self) -> None:
        # Basic envs
        self.default_platform = _to_platform(
            os.getenv('DEFAULT_MODEL_PLATFORM_TYPE', 'STUB')
        )
        self.default_model = _to_model(
            os.getenv('DEFAULT_MODEL_TYPE', 'STUB')
        )
        self.mcp_servers = json.loads(
            os.getenv('MCP_SERVERS', '[{"url": "http://localhost:8080", "api_key": "demo"}]')
        )
        self.agents = _split_env(
            os.getenv('AGENTS', 'DevAgent,BackendAgent,FrontendAgent')
        )
        self.storage_url = os.getenv('STORAGE_URL', 'remote://project')

        models_env = os.getenv('MODELS', self.default_model.name.lower())
        self.models_spec = [self._parse_model(item) for item in _split_env(models_env)]

        agent_map_env = os.getenv('AGENT_MODEL_MAP', '{}')
        raw_map = json.loads(agent_map_env)
        self.agent_model_map = {
            name: self._parse_model(spec) for name, spec in raw_map.items()
        }

        # Instantiate models using ModelFactory
        self._models = {}
        for platform, model in self.models_spec:
            key = (platform.name, model.name)
            self._models[key] = ModelFactory.create(platform, model)

    def _parse_model(self, value: str) -> Tuple[ModelPlatformType, ModelType]:
        if ':' in value:
            plat_s, model_s = value.split(':', 1)
            platform = _to_platform(plat_s)
        else:
            model_s = value
            platform = self.default_platform
        model = _to_model(model_s)
        return platform, model

    def get_default_model(self):
        """Return the first configured model instance."""
        platform, model = self.models_spec[0]
        return self._models[(platform.name, model.name)]

    def get_model_for_agent(self, agent_name: str):
        """Return a model instance for a given agent."""
        if agent_name in self.agent_model_map:
            platform, model = self.agent_model_map[agent_name]
        else:
            # fallback: round-robin selection based on agent position
            idx = self.agents.index(agent_name) if agent_name in self.agents else 0
            platform, model = self.models_spec[idx % len(self.models_spec)]
        return self._models[(platform.name, model.name)]


config = ConfigLoader()
