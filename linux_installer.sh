#!/bin/bash

# Simple stress test runner
echo "🔥 Installing requirements..."

# Install Python packages
pip3 install requests aiohttp

# Download the script
echo "📥 Downloading script..."
curl -s -L "https://raw.githubusercontent.com/blackangiliq/server_distroyer/main/linux_load_test.py" -o stress_test.py

# Check if download was successful
if [ ! -s stress_test.py ]; then
    echo "❌ Download failed. Checking for local file..."
    if [ -f "brutal_server_stress_test.py" ]; then
        echo "✅ Using local brutal_server_stress_test.py file..."
        cp brutal_server_stress_test.py stress_test.py
    else
        echo "❌ Could not download the script and no local file found."
        exit 1
    fi
fi

# Run the script
echo "🚀 Starting stress test..."
python3 stress_test.py 
