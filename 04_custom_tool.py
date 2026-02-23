"""Write Your Own Tool

Run directly:
  python 04_custom_tool.py

Or as a web app:
  python 04_custom_tool.py --serve
  Then open os.agno.com
"""

import json
import sys
import urllib.parse
import urllib.request

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.os import AgentOS


def get_weather(city: str) -> str:
    """Get current weather for a city."""
    encoded_city = urllib.parse.quote(city)
    geo = json.loads(urllib.request.urlopen(
        f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_city}&count=1"
    ).read())
    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]
    weather = json.loads(urllib.request.urlopen(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
    ).read())
    return json.dumps({"city": city, "current": weather["current"]})


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
