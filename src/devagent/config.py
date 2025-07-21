"""Configuration loader using python-dotenv."""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    """Application settings loaded from `.env`."""

    MCP_HOST: str = os.getenv("MCP_HOST", "localhost")
    MCP_PORT: int = int(os.getenv("MCP_PORT", "8080"))
    MCP_API_KEY: str = os.getenv("MCP_API_KEY", "demo-key")
    STORAGE_URL: str = os.getenv("STORAGE_URL", "remote://project")

settings = Settings()
