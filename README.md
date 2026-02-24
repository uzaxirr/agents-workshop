# AI Agents in Python — Workshop Code

All code snippets from the workshop by **Uzair Ali**.

## Setup

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install agno + your model provider
pip install agno anthropic   # or: pip install agno openai
pip install duckduckgo-search  # for the search tool example
```

For MCP examples:
```bash
pip install agno[mcp]
```

## Running

Every file can be run in two ways:

```bash
# Run directly in terminal
python 01_first_agent.py

# Or as a web app with AgentOS chat UI
python 01_first_agent.py --serve
# Then open os.agno.com
```

## Files

| # | File | What it does |
|---|------|-------------|
| 1 | `01_first_agent.py` | Your first agent — Anthropic (Claude) |
| 1b | `01_first_agent_openai.py` | Same agent — OpenAI (GPT-4o-mini) |
| 1c | `01_first_agent_gemini.py` | Same agent — Google (Gemini) |
| 2 | `02_agentos.py` | Same agent deployed with AgentOS |
| 3 | `03_tools_instructions.py` | DuckDuckGo search with instructions |
| 4 | `04_custom_tool.py` | Write your own tool (weather) |
| 5 | `05_memory.py` | Give your agent memory across sessions |
| 6 | `06_mcp_playwright.py` | MCP: browser automation with Playwright |
| 7 | `07_mcp_filesystem.py` | MCP: explore files on your machine |
| 8 | `08_mcp_github.py` | MCP: GitHub hosted server |
| 9 | `09_calorie_counter.py` | Live demo: calorie counter with AgentOS |

## Links

- [Agno Docs](https://docs.agno.com)
- [Agno GitHub](https://github.com/agno-agi/agno)
- [AgentOS](https://os.agno.com)
