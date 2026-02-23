"""MCP in Code — Filesystem

Setup:
  1. brew install node (if you don't have it)
  2. pip install agno[mcp]

Run directly:
  python 07_mcp_filesystem.py

Or as a web app:
  python 07_mcp_filesystem.py --serve
  Then open os.agno.com
"""

import asyncio
import sys

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

agent = Agent(
    name="File Explorer",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    tools=[
        MCPTools(
            command="npx -y @modelcontextprotocol/server-filesystem .",
        )
    ],
)

app = AgentOS(
    id="mcp-filesystem",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        asyncio.run(agent.aprint_response(
            "What files are here? Summarize the project."
        ))
