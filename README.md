# 🚀 Startup Intelligence Digest

An automated multi-agent AI system that searches the web and compiles the latest startup news into a beautifully formatted HTML digest — delivered to your Desktop 3x a week.

## What it does

Every Monday, Wednesday, and Friday at 9am CST, specialized AI agents search the web and compile a clean, readable report covering:
- 💰 **Funding & Investments** — latest funding rounds, VC activity, valuations
- 🛠️ **Products & Research** — new launches, AI breakthroughs, tool announcements

The digest is saved as a dated HTML file on your Desktop and triggers a Mac desktop notification automatically.

## Architecture
```
Orchestrator
    ├── Funding Agent      → searches for latest funding rounds & VC news
    ├── Products Agent     → searches for product launches & research
    └── Composer Agent     → compiles everything into a formatted HTML digest
```

Each agent is independently prompted, uses Claude's built-in web search, and passes its output to the Composer. The system includes automatic retry logic for API rate limits and server overloads.

## Project Structure
```
startup_digest/
├── .env                        # API key (not tracked)
├── main.py                     # Entry point
├── run_digest.sh               # Shell script for automation
├── agents/
│   ├── funding_agent.py        # Searches funding news
│   ├── products_agent.py       # Searches product & research news
│   ├── composer_agent.py       # Compiles HTML digest
│   └── orchestrator.py
└── utils/
    ├── claude_client.py        # Shared API client with retry logic
    └── cost_tracker.py         # Token usage and cost reporting
```

## Setup

1. Clone the repo
```bash
   git clone https://github.com/dsgala/startup-digest.git
   cd startup-digest
```

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

5. Run manually
```bash
   python3 main.py
```

## Automation (Mac)

To run automatically 3x a week at 9am:
```bash
chmod +x run_digest.sh
export EDITOR=nano
crontab -e
```

Add this line:
```
0 9 * * 1,3,5 /bin/bash /path/to/startup_digest/run_digest.sh
```

## Cost Tracking

The system includes a built-in cost tracker that runs automatically after every digest. After each run you will see a full breakdown of:
- Input and output tokens consumed per agent
- Cost per agent call
- Total cost for the run
- Projected daily, monthly, and yearly cost at your current usage

This makes it easy to monitor your API spending over time and adjust run frequency or prompt length if needed.

## Output

A dated HTML file saved to your Desktop, auto-opened in your browser, with a Mac desktop notification.

## Tech Stack

- Python 3.10
- Anthropic API (Claude Haiku)
- Claude built-in web search tool
- Mac cron + osascript for automation