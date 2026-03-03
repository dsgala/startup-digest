from utils.claude_client import run_agent

def composer_agent(funding: str, hiring: str, products: str, date: str) -> str:
    system_prompt = """
    You are a world-class startup newsletter editor. Your job is to take raw 
    research and turn it into a beautiful HTML email digest.
    
    Output ONLY valid HTML, nothing else. No markdown, no backticks, just HTML.
    
    Use this exact structure:
    
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: -apple-system, sans-serif; max-width: 680px; 
                   margin: 40px auto; color: #1a1a1a; line-height: 1.6; }
            h1 { font-size: 24px; border-bottom: 3px solid #000; padding-bottom: 12px; }
            h2 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; 
                 margin-top: 36px; color: #555; }
            .story { margin: 16px 0; padding: 16px; background: #f9f9f9; 
                     border-left: 4px solid #000; border-radius: 4px; }
            .story h3 { margin: 0 0 6px 0; font-size: 15px; }
            .story p { margin: 0; font-size: 14px; color: #444; }
            .tag { display: inline-block; font-size: 11px; font-weight: bold; 
                   padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
            .funding { background: #d4edda; color: #155724; }
            .products { background: #cce5ff; color: #004085; }
            .takeaway { background: #000; color: #fff; padding: 20px; 
                        border-radius: 8px; margin-top: 32px; }
            .takeaway p { margin: 0; font-size: 15px; }
        </style>
    </head>
    <body>
        <!-- your content here -->
    </body>
    </html>
    
    Rules:
    - Include 3 stories for Funding, 3 for Products & Research
    - Each story has a tag (💰 Funding or 🛠️ Products), a bold title with key number, 
      and one sentence explaining why it matters
    - End with a "🧠 This Week's Takeaway" black box with 2 sentences on the bigger picture
    - Use concrete numbers everywhere ($1.5B, 1000 jobs, etc.)
    - YOUR ENTIRE RESPONSE MUST BE RAW HTML ONLY. Start your response with <!DOCTYPE html> and nothing else.
    """

    user_message = f"""
    Today is {date}. Compose the HTML digest from this research.
    Focus ONLY on Funding and Products & Research sections.
    
    === FUNDING REPORT ===
    {funding}
    
    === PRODUCTS & RESEARCH REPORT ===
    {products}
    """

    print("✍️ Composer Agent writing your digest...")
    result = run_agent(system_prompt, user_message, use_search=False, max_tokens=2000)
    print("✅ Digest ready!")
    return result