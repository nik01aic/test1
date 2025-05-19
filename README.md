# Agent SDK Demo

This repository contains a simple demonstration of using an open SDK for building agents.
The included code defines a minimal SDK with tools and an agent that can execute them.

## Running the demo

Run the example application using Python 3:

```bash
python demo_agent.py
```

The agent provides two built-in tools:

- `greet`: prints a greeting for the provided name.
- `add`: adds two numbers together.

When running, type the tool name and provide comma-separated parameters when prompted.
Use `quit` to exit the agent.

## Tests

To run basic unit tests:

```bash
python -m unittest discover -v -s tests
```
