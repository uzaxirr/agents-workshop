"""Give Your Agent Memory

Run directly:
  python 05_memory.py

Or as a web app:
  python 05_memory.py --serve
  Then open os.agno.com
"""

import sys

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.memory import MemoryManager
from agno.models.anthropic import Claude
from agno.os import AgentOS

db = SqliteDb(db_file="agents.db")

agent = Agent(
    model=Claude(id="claude-sonnet-4-5-20250929"),
    db=db,
    memory_manager=MemoryManager(
        model=Claude(id="claude-sonnet-4-5-20250929"),
        db=db,
    ),
    enable_agentic_memory=True,
    markdown=True,
)

app = AgentOS(
    id="agent-with-memory",
    agents=[agent],
).get_app()

if __name__ == "__main__":
    if "--serve" in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        # Session 1: tell it about yourself
        agent.print_response(
            "I'm interested in AI stocks",
            user_id="uzair",
        )

        # Session 2: it still remembers
        agent.print_response(
            "What stocks should I buy?",
            user_id="uzair",
        )
