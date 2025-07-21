"""Simple AI-Society implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from camel.agents import ChatAgent


@dataclass
class AISociety:
    """Container for multiple agents participating in a society."""

    agents: List[ChatAgent]


def run_society(society: AISociety, request: str, turns: int = 1) -> List[str]:
    """Run a simple round-robin conversation among agents."""
    history: List[str] = []
    msg = request
    for _ in range(turns):
        for agent in society.agents:
            if hasattr(agent, "handle_request"):
                msg = agent.handle_request(msg)
                history.append(msg)
    return history
