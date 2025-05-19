class Tool:
    """Simple representation of a tool callable by the agent."""
    def __init__(self, name, func, description=""):
        self.name = name
        self.func = func
        self.description = description

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)
