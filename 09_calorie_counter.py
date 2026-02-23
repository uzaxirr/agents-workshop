"""Live Demo: Calorie Counter Agent

Run:
  python 07_calorie_counter.py

Then open os.agno.com and upload a food photo!
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="""You are a calorie counting assistant.
When a user sends a food image, analyze it and respond with:
- Food name
- Estimated calories
- Protein, carbs, and fat in grams
Be concise. Use a table for the macros.""",
    markdown=True,
)

app = AgentOS(
    id="calorie-counter",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
