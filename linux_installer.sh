#!/bin/bash

# 🔥 LINUX BRUTAL DESTROYER - ONE COMMAND INSTALLER 🔥
# Ultimate installation and execution script

echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo "💀💀💀    LINUX BRUTAL DESTROYER INSTALLER    💀💀💀"
echo "🐧 OPTIMIZED FOR AMD EPYC PROCESSORS 🐧"
echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${CYAN}[SUCCESS]${NC} $1"
}

# Check if running as root for maximum power
if [[ $EUID -eq 0 ]]; then
    print_success "Running as root - MAXIMUM POWER UNLOCKED! 🚀"
else
    print_warning "Not running as root - some optimizations may be limited"
fi

# Detect Linux distribution
print_status "Detecting Linux distribution..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
    DISTRO=$ID
    print_success "Detected: $OS"
else
    print_error "Cannot detect Linux distribution"
    DISTRO="unknown"
fi

# Update system packages
print_status "Updating system packages..."
case $DISTRO in
    ubuntu|debian)
        apt update -y && apt upgrade -y
        INSTALL_CMD="apt install -y"
        ;;
    centos|rhel|fedora)
        if command -v dnf &> /dev/null; then
            dnf update -y
            INSTALL_CMD="dnf install -y"
        else
            yum update -y
            INSTALL_CMD="yum install -y"
        fi
        ;;
    arch|manjaro)
        pacman -Syu --noconfirm
        INSTALL_CMD="pacman -S --noconfirm"
        ;;
    *)
        print_warning "Unknown distribution, trying generic commands..."
        INSTALL_CMD="apt install -y"
        ;;
esac

# Install essential system packages
print_status "Installing essential system packages..."
case $DISTRO in
    ubuntu|debian)
        $INSTALL_CMD python3 python3-pip python3-dev build-essential curl wget git htop
        $INSTALL_CMD libssl-dev libffi-dev python3-setuptools
        ;;
    centos|rhel|fedora)
        $INSTALL_CMD python3 python3-pip python3-devel gcc gcc-c++ curl wget git htop
        $INSTALL_CMD openssl-devel libffi-devel python3-setuptools
        ;;
    arch|manjaro)
        $INSTALL_CMD python python-pip base-devel curl wget git htop
        $INSTALL_CMD openssl libffi python-setuptools
        ;;
esac

# Ensure pip is up to date
print_status "Updating pip..."
python3 -m pip install --upgrade pip

# Install Python packages
print_status "Installing Python dependencies..."
python3 -m pip install --upgrade \
    requests \
    asyncio \
    aiohttp \
    psutil \
    urllib3 \
    certifi \
    charset-normalizer \
    idna \
    multidict \
    yarl \
    aiosignal \
    frozenlist \
    attrs

# System optimizations for maximum performance
print_status "Applying Linux system optimizations..."

# Increase file descriptor limits
echo "* soft nofile 1048576" >> /etc/security/limits.conf 2>/dev/null || true
echo "* hard nofile 1048576" >> /etc/security/limits.conf 2>/dev/null || true
echo "root soft nofile 1048576" >> /etc/security/limits.conf 2>/dev/null || true
echo "root hard nofile 1048576" >> /etc/security/limits.conf 2>/dev/null || true

# Optimize network settings
sysctl -w net.core.somaxconn=65535 2>/dev/null || true
sysctl -w net.core.netdev_max_backlog=5000 2>/dev/null || true
sysctl -w net.ipv4.tcp_max_syn_backlog=65535 2>/dev/null || true
sysctl -w net.ipv4.tcp_fin_timeout=10 2>/dev/null || true
sysctl -w net.ipv4.tcp_tw_reuse=1 2>/dev/null || true
sysctl -w net.ipv4.ip_local_port_range="1024 65535" 2>/dev/null || true

# Create working directory
WORK_DIR="/tmp/brutal_destroyer"
mkdir -p $WORK_DIR
cd $WORK_DIR

print_status "Working directory: $WORK_DIR"

# Download the script from GitHub
print_status "Downloading BRUTAL DESTROYER from GitHub..."
GITHUB_URL="https://raw.githubusercontent.com/blackangiliq/server_distroyer/main/load_tester.py"

if curl -L -o brutal_destroyer.py "$GITHUB_URL"; then
    print_success "Successfully downloaded brutal_destroyer.py"
else
    print_error "Failed to download from GitHub, trying wget..."
    if wget -O brutal_destroyer.py "$GITHUB_URL"; then
        print_success "Successfully downloaded with wget"
    else
        print_error "Failed to download the script!"
        exit 1
    fi
fi

# Verify the file was downloaded
if [ ! -f "brutal_destroyer.py" ]; then
    print_error "Script file not found after download!"
    exit 1
fi

# Make the script executable
chmod +x brutal_destroyer.py

# Display system information
print_status "System Information:"
echo "🖥️  Hostname: $(hostname)"
echo "🐧 OS: $(uname -o)"
echo "🔧 Kernel: $(uname -r)"
echo "💻 Architecture: $(uname -m)"
echo "🧮 CPU Cores: $(nproc)"
echo "💾 Memory: $(free -h | grep '^Mem:' | awk '{print $2}')"
echo "💿 Disk Space: $(df -h / | tail -1 | awk '{print $4}') available"

# Check if running with sufficient privileges
print_status "Checking system privileges..."
if [[ $EUID -eq 0 ]]; then
    print_success "ROOT ACCESS - Maximum destruction power available! 💀"
else
    print_warning "Limited privileges - run with sudo for maximum power!"
fi

# Final system check
print_status "Performing final system checks..."
python3 -c "import sys; print(f'Python version: {sys.version}')"
python3 -c "import requests, aiohttp, psutil; print('All required modules available ✅')"

print_success "🔥 INSTALLATION COMPLETE! 🔥"
echo ""
echo "🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀"
echo "💀💀💀    LAUNCHING BRUTAL DESTROYER    💀💀💀"
echo "🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀"
echo ""
print_warning "Press Ctrl+C to stop the destruction at any time"
echo ""

# Launch the destroyer
sleep 2
python3 brutal_destroyer.py

# Cleanup
print_status "Cleaning up temporary files..."
cd /
rm -rf $WORK_DIR

print_success "🧹 Cleanup complete!"
echo ""
echo "💀💀💀 BRUTAL DESTRUCTION SESSION ENDED 💀💀💀" 
