# camel-agent

This project contains a minimal implementation of a software development agent
written in Python. The agent dynamically loads expert agents for specific
fields, connects to a configurable MCP server using a basic TCP client and saves
generated code in a configurable directory.

## Usage

```bash
python demo.py
```

The demo script shows how to build a simple project using `PythonAgent` and
stores it under the configured `storage_path`.
