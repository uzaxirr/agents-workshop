# Workshop Script: AI Agents in Python

---

## Slide 1 — Title

> Hey everyone, thanks for being here. I'm Uzair. Quick show of hands — how many of you have used ChatGPT or Claude before? Okay, most of you. Now how many of you have tried building something with an LLM in your own code? A few. Cool.
>
> So here's the thing — most people use AI through a chat window. You type, it replies, you copy-paste. That's fine for personal use. But what if you could give that same AI the ability to actually *do* things? Search the web, read your files, call APIs, make decisions — all on its own, inside your own Python code. That's what an agent is. And that's what we're building today.
>
> Here's what we'll cover. First, we'll understand what agents actually are — and aren't. Then we'll build one from scratch — literally 3 lines of code. We'll give it tools so it can search the web, check the weather, browse websites. We'll give it memory so it remembers you across sessions. We'll plug it into real services like GitHub using MCP — the new open standard for connecting AI to anything. And at the end, we'll build a live app together — a calorie counter where you upload a food photo and it gives you the full macro breakdown. All in Python. All running on your machine.
>
> There's a QR code on screen — scan it or go to **is.gd/ns_agents**. That's a GitHub repo with every code snippet from this session. You can follow along, run them later, whatever works for you. Let's get into it.

---

## Slide 2 — What is an Agent? (Concept)

> Let me give you a scenario. Imagine you're a manager and you hire a new assistant. You don't hand them a 200-step checklist for every possible situation. You say, "Here's what I need done, here are the tools you have access to, use your judgment." They figure out the steps themselves. That's exactly what an agent is.
>
> It's software where the LLM controls the execution flow. You're not writing if-else logic for every case — the model decides what to do next. The formula is dead simple: **LLM + tools + instructions**. The LLM is the brain. Tools are its hands. Instructions tell it how to behave. And from there, it analyzes information, makes decisions, and acts autonomously.

---

## Slide 3 — What is an Agent? (Architecture)

> Here's how it looks under the hood. Think about how you process a request at work. Someone sends you a message — that's the input. You think about it, maybe check your notes, look something up, use a tool — and then you respond. Agents work the same way.
>
> Input comes in — text, images, audio, video. The agent processes it and produces output. But the powerful part is what it has access to underneath. **Memory** — like your own brain remembering past conversations. **Knowledge** — like having a filing cabinet of company docs you can search through. And **Tools** — like having your laptop, your phone, your browser — things that let you actually do stuff in the world.

---

## Slide 4 — What is Agno?

> So how do we actually build agents? You could wire everything up from scratch — handle the API calls, tool execution, memory, parsing. People do that. It's painful.
>
> Agno is a lightweight, open-source Python framework that handles all of that for you. Think of it like Flask or FastAPI but for AI agents. It's model-agnostic — works with OpenAI, Anthropic, Google, local models. It comes with 50+ built-in tools, knowledge bases, memory, teams, workflows. And it's fast — agent creation takes about 2 microseconds. No bloated abstractions, no magic. Just clean Python.

---

## Slide 5 — Get Started

> People think setting up AI stuff is complicated. Docker containers, GPU configs, ML pipelines. Not here. Four steps.
>
> **One**: pip install agno. **Two**: install your model provider — anthropic, openai, or google-genai, pick whichever you already have a key for. **Three**: set your API key as an environment variable. **Four**: write 5 lines of Python. That's the entire setup. If you can install a pip package, you can build an agent.

---

## Slide 6 — Your First Agent

> Here it is. Your first agent. Look at this — import Agent, import Claude, create the agent, call print_response. 3 lines of real code.
>
> This is like the "hello world" of AI agents. Except instead of printing a string, you've got a system that can reason, answer complex questions, generate content, explain code — anything you'd do in ChatGPT, but running inside your own Python script. You own it. You control it.

---

## Slide 7 — See It in Action (AgentOS)

> Okay so you've built your agent and it works in the terminal. Now your boss walks over and says "Can I see a demo?" You're not going to show them a terminal window.
>
> Same agent, 3 new lines. Import AgentOS, wrap your agent in it, and you get a FastAPI app. Run it, open **os.agno.com**, and boom — full chat UI. Session management, memory, monitoring, everything. You went from a Python script to a web app in 30 seconds. Zero frontend code. That's the kind of thing that gets people promoted.

---

## Slide 8 — What are Tools?

> Here's a real-world problem. You ask ChatGPT "What's the weather in Tokyo right now?" and it says "I don't have access to real-time data." Frustrating, right? It's smart but it can't *do* anything.
>
> Tools fix that. They're Python functions you give to the agent. Now it *can* check the weather, search the web, query your database, send an email. The agent decides on its own when to call which tool and what arguments to pass. Think of tools as giving someone a phone. Before — they could only think. After — they can call, text, browse, order food. Same brain, way more capability.

---

## Slide 9 — Tools + Instructions in Code

> Say you're building an agent for your marketing team. They want to keep up with what's trending in AI. Two things to add.
>
> First, **tools** — we give it DuckDuckGoTools so it can search the web. Now it has access to live information. Second, **instructions** — "Use tables to display data." That changes how it behaves. Without instructions, it might ramble. With instructions, it's clean and structured. We ask "Top 5 trending AI tools in 2025" and it comes back with a beautiful table — tool names, features, use cases. Tools give capability. Instructions give behavior. Together, they turn a generic LLM into a purpose-built assistant.

---

## Slide 10 — Write Your Own Tool

> What if there's no built-in tool for what you need? Say your company has an internal API for inventory, or you need to check a very specific weather service, or you want to query your own database.
>
> Any Python function becomes a tool. Write the function, add a docstring so the agent knows what it does, and pass it in. Here's a weather example — it hits wttr.in and returns JSON. The agent reads the docstring, understands "oh, this function gets weather for a city," and calls it whenever someone asks about weather. That's the whole pattern. If you can write a Python function, you can build a tool.

---

## Slide 11 — Give Your Agent Memory

> You know how you go to your favorite coffee shop and the barista just knows your order? "The usual?" That's memory. Now imagine going to a coffee shop where every single visit, they ask "Hi, what's your name? What would you like?" — that's what agents without memory feel like.
>
> Without memory, every conversation starts from scratch. The agent forgets you exist. With memory, it remembers facts about you across sessions. SQLite works fine — zero setup, it's just a file. Add a MemoryManager, set `enable_agentic_memory=True`. Now in session 1, you say "I'm interested in AI stocks." Next week, you come back, ask "What should I buy?" — and it already knows your preferences. The agent decides what's worth remembering on its own. Just like that barista.

---

## Slide 12 — What is MCP?

> Okay, so we've built tools, we've written custom tools. But imagine you need your agent to work with GitHub, Slack, your database, Google Docs, Notion — are you going to build a custom tool for each one? That's weeks of work.
>
> MCP — Model Context Protocol — is like an **app store for AI tools**. It's an open standard created by Anthropic. Think of it like USB. Before USB, every device had its own proprietary cable. After USB — one plug, works with everything. MCP is the same idea. Someone builds an MCP server for GitHub. Someone else builds one for Slack. Your agent just plugs in and gets access to all their tools. Without MCP, you build each integration yourself. With MCP, someone else already did it.

---

## Slide 13 — MCP in Code: Playwright

> Here's where it gets fun. Say your job involves checking a competitor's website every morning, pulling the latest pricing, and putting it in a spreadsheet. Boring. Repetitive. Perfect for an agent.
>
> This agent can browse the web like a human — navigate pages, click buttons, fill forms, scrape data. The setup is three commands. In the code, we pass MCPTools with a command — literally the same command you'd type in your terminal to start the Playwright server. One line. Now the agent can browse any website. We're telling it to go to Hacker News and get the top post. But this could be "go to competitor.com and get their pricing page."

---

## Slide 14 — MCP in Code: Filesystem

> Now, Playwright needs Node.js, GitHub needs a token — what if you just want the simplest possible MCP example? Something everyone can run right now?
>
> Filesystem MCP. Zero setup. No accounts. No tokens. You point the agent at a folder on your machine and it can read files, search through them, summarize them. Imagine you just joined a new company, you clone a repo, and you have no idea what's going on. Instead of spending an hour reading through files, you ask the agent "What files are here? Summarize this project." And it reads the README, scans the code, and gives you a clear overview. That's your onboarding buddy in 10 lines of code.

---

## Slide 15 — MCP in Code: GitHub (Advanced)

> Another real scenario — you're a tech lead managing 10 repos. Every morning you check open issues, review PRs, look at CI failures. That's 30 minutes of context-switching before you even start coding.
>
> This agent connects to GitHub's official hosted MCP server. No Docker, no local server running — just your Personal Access Token. Set it up in 6 steps, all on screen. Now the agent can list issues, read PRs, search code, check workflows — anything GitHub can do. You ask "What are the top 5 open issues on our repo?" and it just tells you. Your morning triage goes from 30 minutes to 30 seconds.

---

## Slide 16 — Live Demo Intro

> Alright, enough slides. Let's build something real, right now. We're making a **calorie counter**. Here's the scenario — you're at lunch, you've got a plate of food in front of you, you want to know the calories and macros. You snap a photo, upload it, and the agent breaks it down for you. Food name, calories, protein, carbs, fat — all in a clean table. Let's build it.

---

## Slide 17 — Calorie Counter Code

> Here's the code. It's 15 lines. We use GPT-4o-mini — it's great at vision and costs almost nothing. The instructions are simple: "You're a calorie counting assistant. When someone sends a food image, analyze it, give the food name, estimated calories, and macros in a table."
>
> We wrap it in AgentOS so we get the chat UI — that's where you upload images. Run it with `python calorie_counter.py`, open os.agno.com, and start uploading food photos.
>
> Let me show you live.

*[Live demo: run the agent, upload a food photo, show the results]*

> And that's it. 15 lines of Python, and you've got an app that nutritionists would charge you a subscription for.

---

## Slide 18 — Where to Go Next

> So we went from zero to a working AI agent with tools, memory, MCP, and a live demo — all in Python. But this is really just the starting point. Here's where you can go next.
>
> **Knowledge and RAG** — imagine giving your agent access to your company's entire documentation. A customer support agent that actually knows your product, because it's read every doc.
>
> **Reasoning** — chain-of-thought problem solving. For when the task is complex and the agent needs to think step by step, like debugging code or analyzing a contract.
>
> **Teams** — multiple agents working together. A research agent finds information, a writing agent drafts the report, an editor agent polishes it. Like a real team.
>
> **Workflows** — deterministic pipelines. When you need reliability and control over the exact sequence of steps.
>
> All of this is in the Agno docs and the GitHub repo. Scan the QR codes, star the repo, and keep building.

---

## Slide 19 — Thank You

> And one last thing — if you enjoyed this session and build something cool with agents, I'd love to see it. Follow me on X — **@uzaxirr** — there's a QR code right there. Share what you build, tag me. I share a lot of AI agent content there too, so it's a good way to stay connected. Thank you all, this was fun!
