from open_agent_sdk.agent import Agent
from open_agent_sdk.tool import Tool


def greet(name="world"):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return str(int(a) + int(b))


def main():
    agent = Agent("Demo Agent")
    agent.register_tool(Tool("greet", greet, "Greet a person"))
    agent.register_tool(Tool("add", add_numbers, "Add two numbers"))
    agent.run()


if __name__ == "__main__":
    main()
