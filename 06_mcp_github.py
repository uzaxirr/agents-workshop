"""MCP in Code — GitHub (Hosted)

Setup:
  1. Create a GitHub PAT: github.com/settings/personal-access-tokens
  2. export GITHUB_TOKEN=github_pat_...
  3. pip install agno[mcp]

Run directly:
  python 06_mcp_github.py

Or as a web app:
  python 06_mcp_github.py --serve
  Then open os.agno.com
"""

import asyncio
import os
import sys

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.mcp import MCPTools, StreamableHTTPClientParams

agent = Agent(
    name="GitHub Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
    tools=[
        MCPTools(
            transport="streamable-http",
            server_params=StreamableHTTPClientParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"},
            ),
        )
    ],
)

app = AgentOS(
    id="mcp-github",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        asyncio.run(agent.aprint_response(
            "List the top 5 open issues on agno-agi/agno"
        ))
