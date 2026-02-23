"""Slide 7: See It in Action — AgentOS"""

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.os import AgentOS

# Same agent as before
agent = Agent(
    model=Claude(id="claude-sonnet-4-5-20250929"),
    markdown=True,
)

# Wrap it in AgentOS
app = AgentOS(
    id="my-first-agent",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
