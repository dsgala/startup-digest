# 🚀 Startup Intelligence Digest

A multi-agent AI system that automatically aggregates daily startup news into a beautifully formatted HTML digest.

## What it does

Every day, specialized AI agents search the web for the latest startup news and compile it into one clean, readable report covering:
- 💰 **Funding & Investments** — latest funding rounds, VC activity, valuations
- 🛠️ **Products & Research** — new launches, AI breakthroughs, tool announcements

## How it works
```
Orchestrator
    ├── Funding Agent     → searches for funding news
    ├── Products Agent    → searches for product launches
    └── Composer Agent    → compiles everything into HTML digest
```

Each agent is powered by Claude Haiku via the Anthropic API with built-in retry logic for rate limits.

## Setup

1. Clone the repo
2. Create a virtual environment and activate it
```bash
   python3 -m venv env
   source env/bin/activate
```
3. Install dependencies
```bash
   pip install anthropic python-dotenv
```
4. Add your Anthropic API key
```bash
   echo "ANTHROPIC_API_KEY=your_key_here" > .env
```
5. Run the digest
```bash
   python3 main.py
```

## Output

Generates a dated HTML file on your Desktop that opens automatically in your browser, plus a Mac desktop notification.

## Tech stack

- Python 3.10
- Anthropic API (Claude Haiku)
- Web search via Claude's built-in search tool