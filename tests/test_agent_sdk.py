import unittest
from open_agent_sdk.tool import Tool
from open_agent_sdk.agent import Agent

class TestSDK(unittest.TestCase):
    def test_tool_run(self):
        tool = Tool('greet', lambda name: f'Hello {name}', 'greet tool')
        self.assertEqual(tool.run('Alice'), 'Hello Alice')

    def test_agent_register(self):
        agent = Agent('test')
        tool = Tool('dummy', lambda: 'ok', 'dummy')
        agent.register_tool(tool)
        self.assertIn('dummy', agent.tools)

    def test_root_import(self):
        from open_agent_sdk import Agent as RootAgent, Tool as RootTool
        self.assertIs(RootAgent, Agent)
        self.assertIs(RootTool, Tool)

if __name__ == '__main__':
    unittest.main()
