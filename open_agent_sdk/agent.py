class Agent:
    """Simple agent that can execute registered tools."""
    def __init__(self, name):
        self.name = name
        self.tools = {}

    def register_tool(self, tool):
        self.tools[tool.name] = tool

    def run(self):
        print(f"Agent {self.name} started. Available tools:")
        for name, tool in self.tools.items():
            print(f"- {name}: {tool.description}")
        while True:
            command = input("Enter tool name (or 'quit'): ")
            if command == 'quit':
                print("Goodbye!")
                break
            if command in self.tools:
                params = input("Enter comma-separated parameters: ")
                args = [p.strip() for p in params.split(',') if p.strip()]
                result = self.tools[command].run(*args)
                print(f"Result: {result}")
            else:
                print("Unknown tool.")
