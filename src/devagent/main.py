"""Typer CLI entry point for DevAgent."""

from __future__ import annotations

import typer
from rich.console import Console

from .dev.agent import DevAgent
from .backend.agent import BackendAgent
from .frontend.agent import FrontendAgent
from .db.agent import DBAgent
from .chat.agent import ChatAgent as UserChatAgent
from .society import AISociety, run_society
from .config import settings
from camel.toolkits import MCPToolkit
import asyncio

console = Console()
app = typer.Typer()

AGENT_MAP = {
    "DevAgent": DevAgent,
    "BackendAgent": BackendAgent,
    "FrontendAgent": FrontendAgent,
    "DBAgent": DBAgent,
    "ChatAgent": UserChatAgent,
}

@app.command()
def chat(task: str = "generate a hello world", turns: int = 1):
    """Start an interactive chat using an AI-Society."""
    agents = [AGENT_MAP[name]() for name in settings.AGENTS if name in AGENT_MAP]
    society = AISociety(agents)
    console.print("[bold green]AI-Society chat started. Type 'exit' to quit.[/bold green]")
    while True:
        msg = console.input("[cyan]> ")
        if msg.lower() == "exit":
            break
        history = run_society(society, msg, turns)
        console.print(history[-1] if history else "no response")

@app.command()
def health():
    """Run a simple health check."""
    society = AISociety([DevAgent()])
    run_society(society, "ping")
    try:
        toolkit = MCPToolkit(config_dict={"mcpServers": settings.MCP_SERVERS})
        console.print(f"Connecting to {len(settings.MCP_SERVERS)} MCP servers...")
        asyncio.run(toolkit.connect())
        asyncio.run(toolkit.disconnect())
    except Exception as exc:
        console.print(f"[red]Health check failed: {exc}[/red]")
        raise typer.Exit(code=1)
    console.print("[bold green]Health check completed.[/bold green]")

if __name__ == "__main__":
    app()
