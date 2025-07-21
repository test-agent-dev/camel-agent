# camel-agent

This repository contains a simple example of a development agent built with **Camel-AI**.

The script `src/dev_agent.py` demonstrates:

- Loading `mcp_config.json` and creating an `MCPToolKit` client.
- Orchestrating three expert agents (`BackendAgent`, `FrontendAgent`, `DBAgent`).
- Generating a Python project skeleton.
- Uploading the project using a placeholder storage service.
- Verifying the project by compiling the Python files.

To run the demo:

```bash
python3 src/dev_agent.py
```

The script will print the actions performed by each agent and the verification status.
