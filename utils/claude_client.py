import os
import time
from anthropic import Anthropic, RateLimitError, APIStatusError
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Global usage log for this run
usage_log = []

def run_agent(system_prompt: str, user_message: str, use_search: bool = True, max_tokens: int = 800, agent_name: str = "agent") -> str:
    
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

            # Track token usage
            usage_log.append({
                "agent": agent_name,
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens
            })

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