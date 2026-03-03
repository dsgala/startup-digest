#!/bin/bash

# Activate the virtual environment
source /Users/dharmigala/Desktop/startup_digest/startup_digest_env/bin/activate

# Run the digest
cd /Users/dharmigala/Desktop/startup_digest
python3 main.py

# Send Mac notification when done
osascript -e 'display notification "Your Startup Digest is ready on your Desktop! 🚀" with title "Startup Digest" sound name "Default"'