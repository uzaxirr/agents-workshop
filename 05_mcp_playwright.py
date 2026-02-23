"""MCP in Code — Playwright

Setup:
  1. brew install node
  2. npx @playwright/mcp@latest
  3. pip install agno[mcp]

Run directly:
  python 05_mcp_playwright.py

Or as a web app:
  python 05_mcp_playwright.py --serve
  Then open os.agno.com
"""

import asyncio
import sys

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

agent = Agent(
    name="Browser Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    tools=[
        MCPTools(
            command="npx @playwright/mcp@latest",
            timeout_seconds=30,
        )
    ],
)

app = AgentOS(
    id="mcp-playwright",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        asyncio.run(agent.aprint_response(
            "Go to news.ycombinator.com and get the top post"
        ))
