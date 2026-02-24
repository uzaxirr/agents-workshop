"""Your First Agent (OpenAI)

Run directly:
  python 01_first_agent_openai.py

Or as a web app:
  python 01_first_agent_openai.py --serve
  Then open os.agno.com
"""

import sys

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
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
