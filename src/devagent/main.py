"""Typer CLI entry point for DevAgent."""

import typer
from rich.console import Console

from .dev.agent import DevAgent

console = Console()
app = typer.Typer()

@app.command()
def chat(name: str = "demo", language: str = "python"):
    """Start an interactive chat with the DevAgent."""
    agent = DevAgent()
    console.print("[bold green]DevAgent chat started. Type 'exit' to quit.[/bold green]")
    while True:
        msg = console.input("[cyan]> ")
        if msg.lower() == "exit":
            break
        project = agent.create_project(name, language)
        result = agent.delegate(msg)
        console.print(result)
        agent.upload_project(project)
        agent.verify(project)

@app.command()
def health():
    """Run a simple health check."""
    agent = DevAgent()
    agent.verify("src/devagent/dev/agent.py")
    console.print("[bold green]Health check completed.[/bold green]")

if __name__ == "__main__":
    app()
