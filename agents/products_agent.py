from utils.claude_client import run_agent

def products_agent(date: str) -> str:
    """
    This agent's job: find new product launches, AI research breakthroughs, 
    and interesting startup announcements.
    """

    system_prompt = """
    You are a startup product and research analyst. Your job is to track:
    - New product launches from startups or big tech
    - Interesting AI research papers or breakthroughs
    - New tools, APIs, or platforms developers are excited about
    - Any notable pivots or strategy shifts from known startups
    
    Structure each story as:
    - Company/researchers and what they launched or published
    - What it does in plain English
    - Why the startup ecosystem should care
    
    Be concise. Cover 3-5 stories max. Focus on the last 7 days only.
    """

    user_message = f"""
    Today is {date}. Search for the most recent startup product launches, 
    AI research papers, and notable tech announcements from the past 7 days.
    """

    print("🔍 Products & Research Agent searching...")
    result = run_agent(system_prompt, user_message, use_search=True)
    print("✅ Products & Research Agent done")

    return result