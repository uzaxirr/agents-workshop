"""Your First Agent

Run directly:
  python 01_first_agent.py

Or as a web app:
  python 01_first_agent.py --serve
  Then open os.agno.com
"""

import sys

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.os import AgentOS

agent = Agent(
    model=Claude(id="claude-sonnet-4-5-20250929"),
    markdown=True,
)

app = AgentOS(
    id="first-agent",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        agent.print_response("Write a haiku about programming")
