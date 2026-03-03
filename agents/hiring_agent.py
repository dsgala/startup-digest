from utils.claude_client import run_agent

def hiring_agent(date: str) -> str:
    """
    This agent's job: find startup hiring trends, layoffs, and key talent moves.
    """

    system_prompt = """
    You are a startup talent and hiring analyst. Your job is to track:
    - Major layoffs at tech companies or startups
    - Interesting executive hires or departures (C-suite, VP level)
    - Companies that are aggressively hiring and in what roles
    - Any notable talent trends in the startup world
    
    Structure each story as:
    - Company and what happened
    - Scale (how many people, what roles)
    - Why it matters for the startup ecosystem
    
    Be concise. Cover 3-5 stories max. Focus on the last 7 days only.
    """

    user_message = f"""
    Today is {date}. Search for the most recent startup and tech company 
    hiring news, layoffs, executive moves, and talent trends from the past 7 days.
    """

    print("🔍 Hiring Agent searching...")
    result = run_agent(system_prompt, user_message, use_search=True)
    print("✅ Hiring Agent done")

    return result