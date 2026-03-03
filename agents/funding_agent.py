from utils.claude_client import run_agent

def funding_agent(date: str) -> str:
    """
    This agent's job: find the latest startup funding rounds and VC activity.
    """

    system_prompt = """
    You are a startup funding analyst. Your job is to find the most recent and 
    noteworthy startup funding rounds, VC investments, and valuation news.
    
    Always structure your findings as:
    - Company name and what they do (one line)
    - Amount raised and round type (Seed, Series A, B, etc.)
    - Key investors
    - Why it's interesting/notable
    
    Be concise. Cover 3-5 stories max. Focus on the last 7 days only.
    """

    user_message = f"""
    Today is {date}. Search for the most recent startup funding rounds 
    and VC investment news from the past 7 days. 
    Focus on interesting or large rounds across any industry.
    """

    print("🔍 Funding Agent searching...")
    result = run_agent(system_prompt, user_message, use_search=True, agent_name="Funding Agent")
    print("✅ Funding Agent done")
    
    return result