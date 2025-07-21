"""Configuration loader using python-dotenv."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import List, Dict, Any

from dotenv import load_dotenv

load_dotenv()


def _split_env(value: str) -> List[str]:
    """Split a comma separated environment variable."""
    return [v.strip() for v in value.split(",") if v.strip()]


@dataclass
class Settings:
    """Application settings loaded from `.env`."""

    DEFAULT_MODEL_PLATFORM_TYPE: str = os.getenv(
        "DEFAULT_MODEL_PLATFORM_TYPE", "STUB"
    )
    DEFAULT_MODEL_TYPE: str = os.getenv("DEFAULT_MODEL_TYPE", "GPT_4O_MINI")

    MCP_SERVERS: List[Dict[str, Any]] = field(
        default_factory=lambda: json.loads(
            os.getenv(
                "MCP_SERVERS",
                '[{"url": "http://localhost:8080", "api_key": "demo"}]',
            )
        )
    )

    AGENTS: List[str] = field(
        default_factory=lambda: _split_env(
            os.getenv("AGENTS", "DevAgent,BackendAgent,FrontendAgent")
        )
    )
    MODELS: List[str] = field(
        default_factory=lambda: _split_env(
            os.getenv("MODELS", "gpt-4o-mini")
        )
    )

    STORAGE_URL: str = os.getenv("STORAGE_URL", "remote://project")


settings = Settings()
