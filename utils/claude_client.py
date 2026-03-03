import os
import time
from anthropic import Anthropic, RateLimitError, APIStatusError
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_agent(system_prompt: str, user_message: str, use_search: bool = True, max_tokens: int = 800) -> str:
    """
    Core function every agent uses. Handles rate limits and server overloads automatically.
    
    system_prompt: defines the agent's role
    user_message: the actual task
    use_search: whether this agent needs web search
    max_tokens: how long the response can be (composer needs more than search agents)
    """
    
    tools = [{"type": "web_search_20250305", "name": "web_search"}] if use_search else []

    max_retries = 5
    wait_time = 60

    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=max_tokens,
                system=system_prompt,
                tools=tools,
                messages=[{"role": "user", "content": user_message}]
            )

            result = ""
            for block in response.content:
                if hasattr(block, "text"):
                    result += block.text

            return result.strip()

        except RateLimitError:
            if attempt < max_retries - 1:
                print(f"⚠️  Rate limit hit. Waiting {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                wait_time += 30
            else:
                print("❌ Max retries reached on rate limit.")
                raise

        except APIStatusError as e:
            if e.status_code == 529:
                if attempt < max_retries - 1:
                    print(f"⚠️  Servers overloaded. Waiting {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                    wait_time += 30
                else:
                    print("❌ Max retries reached on overload.")
                    raise
            else:
                raise