from agents.funding_agent import funding_agent
from agents.hiring_agent import hiring_agent
from agents.products_agent import products_agent
from agents.composer_agent import composer_agent
from datetime import date
import time
import os
import subprocess

today = date.today().strftime("%B %d, %Y")
filename_date = date.today().strftime("%Y-%m-%d")

funding = funding_agent(today)
print("⏳ Waiting 90 seconds...")
time.sleep(90)

products = products_agent(today)
print("⏳ Waiting 90 seconds...")
time.sleep(90)

digest_html = composer_agent(funding, "", products, today)

# Save HTML file to Desktop
output_path = os.path.expanduser(f"~/Desktop/startup_digest_{filename_date}.html")
with open(output_path, "w") as f:
    f.write(digest_html)

print(f"\n📁 Digest saved to {output_path}")

# Open in browser automatically
subprocess.run(["open", output_path])

# Send Mac desktop notification
subprocess.run([
    "osascript", "-e",
    f'display notification "Your startup digest is ready — open your Desktop to read it 🚀" with title "Startup Digest {today}"'
])

print("🔔 Desktop notification sent!")