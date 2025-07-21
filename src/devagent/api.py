"""FastAPI application exposing a health endpoint."""

from fastapi import FastAPI, Response

from .config import config
from .society import AISociety, run_society
from .dev.agent import DevAgent

app = FastAPI()


@app.get("/health")
async def health() -> Response:
    """Check MCP connectivity and society startup."""
    society = AISociety([DevAgent()])
    run_society(society, "ping")
    # Attempt to create MCPToolkit using config; ignore connection errors.
    from camel.toolkits import MCPToolkit
    try:
        toolkit = MCPToolkit(config_dict={"mcpServers": config.mcp_servers})
        await toolkit.connect()
        await toolkit.disconnect()
    except Exception:
        return Response(status_code=503)
    return Response(content="ok", media_type="text/plain")
