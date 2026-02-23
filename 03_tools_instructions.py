"""Tools + Instructions

Run directly:
  python 03_tools_instructions.py

Or as a web app:
  python 03_tools_instructions.py --serve
  Then open os.agno.com
"""

import sys

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.os import AgentOS
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-5-20250929"),
    tools=[DuckDuckGoTools()],
    instructions="Use tables to display data.",
    markdown=True,
)

app = AgentOS(
    id="tools-instructions",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        agent.print_response("Top 5 trending AI tools in 2025", stream=True)
