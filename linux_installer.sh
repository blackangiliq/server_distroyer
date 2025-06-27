#!/bin/bash

# 🔥 FAST LINUX BRUTAL DESTROYER INSTALLER 🔥
# Quick installation and execution - No delays!

echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo "💀💀💀    FAST LINUX BRUTAL DESTROYER    💀💀💀"
echo "🚀 QUICK SETUP - NO DELAYS! 🚀"
echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

print_status() { echo -e "${GREEN}[INFO]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }
print_success() { echo -e "${CYAN}[SUCCESS]${NC} $1"; }

# Quick Python check
print_status "Checking Python installation..."
if command -v python3 &> /dev/null; then
    print_success "Python3 found: $(python3 --version)"
else
    print_status "Installing Python3 (quick install)..."
    # Quick install without updates
    sudo apt install -y python3 python3-pip 2>/dev/null || \
    sudo yum install -y python3 python3-pip 2>/dev/null || \
    sudo dnf install -y python3 python3-pip 2>/dev/null || \
    sudo pacman -S --noconfirm python python-pip 2>/dev/null
fi

# Quick pip check
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    print_success "Pip found and ready"
else
    print_error "Pip not found, trying quick install..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py --user && rm get-pip.py
fi

# Quick dependency check and install
print_status "Checking Python dependencies..."
python3 -c "import requests, aiohttp, psutil" 2>/dev/null && {
    print_success "All dependencies already installed!"
} || {
    print_status "Installing missing dependencies (quick install)..."
    python3 -m pip install --user --no-warn-script-location requests aiohttp psutil asyncio urllib3 2>/dev/null || \
    pip3 install --user --no-warn-script-location requests aiohttp psutil asyncio urllib3 2>/dev/null || \
    pip install --user --no-warn-script-location requests aiohttp psutil asyncio urllib3 2>/dev/null
}

# Quick system optimizations (only fast ones)
print_status "Applying quick system optimizations..."
ulimit -n 65536 2>/dev/null || true
sudo sysctl -w net.core.somaxconn=65535 2>/dev/null || true
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535" 2>/dev/null || true

# Create temp directory
WORK_DIR="/tmp/brutal_destroyer_$(date +%s)"
mkdir -p $WORK_DIR
cd $WORK_DIR

# Quick download
print_status "Downloading BRUTAL DESTROYER..."
GITHUB_URL="https://raw.githubusercontent.com/blackangiliq/server_distroyer/main/load_tester.py"

if curl -fsSL "$GITHUB_URL" -o brutal_destroyer.py; then
    print_success "Download complete!"
elif wget -q -O brutal_destroyer.py "$GITHUB_URL"; then
    print_success "Download complete (wget)!"
else
    print_error "Download failed!"
    exit 1
fi

# Verify download
if [ ! -f "brutal_destroyer.py" ] || [ ! -s "brutal_destroyer.py" ]; then
    print_error "Downloaded file is empty or missing!"
    exit 1
fi

# Quick system info
print_status "System: $(uname -s) | CPU Cores: $(nproc) | Arch: $(uname -m)"

# Final dependency verification
print_status "Final check..."
python3 -c "import requests, aiohttp, psutil; print('✅ All modules ready')" || {
    print_error "Dependencies missing, trying emergency install..."
    python3 -m pip install --break-system-packages requests aiohttp psutil 2>/dev/null || true
}

print_success "🔥 SETUP COMPLETE - LAUNCHING DESTROYER! 🔥"
echo ""
echo "💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀"
echo "🚀    BRUTAL DESTRUCTION STARTING NOW    🚀"
echo "💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀"
echo ""
print_warning "Press Ctrl+C to stop"
echo ""

# Launch immediately
sleep 1
python3 brutal_destroyer.py

# Quick cleanup
cd / && rm -rf $WORK_DIR
print_success "🧹 Session ended!" 
