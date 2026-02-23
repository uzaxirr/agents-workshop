"""Write Your Own Tool

Run directly:
  python 04_custom_tool.py

Or as a web app:
  python 04_custom_tool.py --serve
  Then open os.agno.com
"""

import json
import sys
import urllib.request

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.os import AgentOS


def get_weather(city: str) -> str:
    """Get current weather for a city."""
    url = f"https://wttr.in/{city}?format=j1"
    data = json.loads(urllib.request.urlopen(url).read())
    return json.dumps(data)


agent = Agent(
    model=Claude(id="claude-sonnet-4-5-20250929"),
    tools=[get_weather],
    markdown=True,
)

app = AgentOS(
    id="custom-tool",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        agent.print_response("Weather in Tokyo?")
