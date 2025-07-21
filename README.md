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

## .env format

```
MCP_HOST=localhost
MCP_PORT=8080
MCP_API_KEY=demo-key
STORAGE_URL=remote://project
```

Each agent directory contains a short README describing its responsibilities.
