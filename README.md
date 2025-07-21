# Camel DevAgent Demo

This project showcases a simple multi-agent system built with [Camel-AI](https://github.com/lightaime/camel), providing an interactive chat interface using Typer and Rich.

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file (see `.env.example`):

```bash
cp .env.example .env
```

## Usage

Start an interactive session:

```bash
python -m devagent.main chat
```

Run the health check:

```bash
python -m devagent.main health
```

Start the HTTP server with the health endpoint:

```bash
uvicorn devagent.api:app --reload
```

## .env format

```
DEFAULT_MODEL_PLATFORM_TYPE=STUB
DEFAULT_MODEL_TYPE=STUB
MCP_SERVERS=[{"url": "http://localhost:8080", "api_key": "demo"}]
AGENTS=DevAgent,BackendAgent,FrontendAgent
# platform:model pairs separated by commas
MODELS=stub:stub,openai:gpt-4o-mini,anthropic:claude-instant
# optional JSON mapping of agents to models
AGENT_MODEL_MAP={"DevAgent": "stub:stub", "BackendAgent": "openai:gpt-4o-mini"}
STORAGE_URL=remote://project
```

Add more models by appending to `MODELS`. Agents will automatically
receive the configured model without further code changes thanks to the
`ConfigLoader` utility.

Each agent directory contains a short README describing its responsibilities.
