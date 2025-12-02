#!/bin/bash
# StealthHub AI v2.0 - Complete Installation Script
# Author: xpe.nettt
# Community: Community Stealth
# Copyright: © 2025 xpe.nettt - Community Stealth

echo "🤖 StealthHub AI v2.0 - Installation Script"
echo "============================================"
echo ""

# Check Python version
python_version=$(python3 --version 2>/dev/null | cut -d' ' -f2 | cut -d'.' -f1,2)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8+ is required. Found: $python_version"
    echo "Please install Python 3.8 or newer and try again."
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo ""
echo "🐍 Creating Python virtual environment..."
python3 -m venv stealth_hub_env
source stealth_hub_env/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo ""
echo "📁 Creating directories..."
mkdir -p data
mkdir -p generated_dlls
mkdir -p logs
mkdir -p config

# Create configuration file
echo ""
echo "⚙️ Creating configuration..."
cat > config/stealth_hub_config.env << EOF
# StealthHub AI Configuration
# Generated on $(date)

# Discord Integration (Optional)
DISCORD_BOT_TOKEN=
DISCORD_CHANNEL_OFFSETS=🔍-offsets-free-fire
DISCORD_CHANNEL_PANELS=🎮-panel-references
DISCORD_CHANNEL_DEVELOPMENT=💻-dev-requests

# AI Engine Settings
AI_VERSION=2.0.0
AI_AUTHOR=xpe.nettt
AI_COMMUNITY=Community Stealth

# Game Settings
TARGET_GAME=Free Fire
TARGET_PLATFORM=BlueStacksMSI

# Database Settings
DATABASE_PATH=data/stealth_hub_analysis.db

# Output Settings
OUTPUT_DIR=generated_dlls
LOG_LEVEL=INFO

# Compilation Settings
COMPILER=visual_studio
COMPILER_PATH=C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat

# Note: Fill in DISCORD_BOT_TOKEN for Discord integration
# To get a bot token, create an application at https://discord.com/developers/applications
# Add the bot to your Community Stealth Discord server with appropriate permissions.
EOF

# Create startup script
echo ""
echo "🚀 Creating startup script..."
cat > start_stealth_hub.sh << 'EOF'
#!/bin/bash
# StealthHub AI v2.0 - Startup Script

echo "🤖 Starting StealthHub AI v2.0..."
echo ""

# Activate virtual environment
source stealth_hub_env/bin/activate

# Load configuration
source config/stealth_hub_config.env

# Start the CLI
python stealth_hub_cli.py "$@"
EOF

chmod +x start_stealth_hub.sh

# Create compilation script for Windows
echo ""
echo "🔨 Creating Windows compilation script..."
cat > compile_dll.bat << 'EOF'
@echo off
REM StealthHub AI v2.0 - DLL Compilation Script for Windows
REM Author: xpe.nettt - Community Stealth

echo 🤖 StealthHub AI v2.0 - DLL Compilation
echo =======================================

REM Check if source file exists
if "%~1"=="" (
    echo ❌ Usage: compile_dll.bat ^<source_file.cpp^>
    echo Example: compile_dll.bat generated_dlls\StealtHub_aimbot_20251203_123000.cpp
    pause
    exit /b 1
)

set SOURCE_FILE=%1
set OUTPUT_NAME=%~n1.dll

echo 📝 Source: %SOURCE_FILE%
echo 🎯 Output: %OUTPUT_NAME%

REM Check for Visual Studio
where cl.exe >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Visual Studio not found or not in PATH
    echo Please run from Developer Command Prompt for Visual Studio
    echo Or install Visual Studio 2017+ with C++ build tools
    pause
    exit /b 1
)

echo 🔨 Compiling %SOURCE_FILE%...
cl /LD %SOURCE_FILE% /Fe:%OUTPUT_NAME% /link user32.dll kernel32.dll d3d9.dll

if %ERRORLEVEL% EQU 0 (
    echo ✅ Compilation successful!
    echo 📁 Output: %OUTPUT_NAME%
) else (
    echo ❌ Compilation failed!
    echo Please check the error messages above
)

pause
EOF

# Create batch file for easy CLI access
echo ""
echo "⚡ Creating quick access scripts..."
cat > stealth_hub.bat << 'EOF'
@echo off
REM StealthHub AI v2.0 - Quick Access for Windows
REM Author: xpe.nettt - Community Stealth

echo 🤖 StealthHub AI v2.0 - Quick Access
echo =====================================

REM Activate virtual environment
call stealth_hub_env\Scripts\activate.bat

REM Run CLI
python stealth_hub_cli.py %*

pause
EOF

# Test installation
echo ""
echo "🧪 Testing installation..."
python3 -c "
import sys
sys.path.append('ai_engine')
try:
    from stealth_hub_ai_engine import StealthHubAI
    print('✅ StealthHub AI Engine loaded successfully')
    
    ai = StealthHubAI()
    stats = ai.get_statistics()
    print(f'✅ Version: {stats[\"version\"]}')
    print(f'✅ Author: {stats[\"author\"]}')
    print(f'✅ Community: {stats[\"community\"]}')
    print('✅ All systems operational!')
except Exception as e:
    print(f'❌ Error loading StealthHub AI: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Installation completed successfully!"
    echo ""
    echo "📚 Quick Start Guide:"
    echo "1. Run: ./start_stealth_hub.sh"
    echo "2. Or: python stealth_hub_cli.py"
    echo "3. Try: python stealth_hub_cli.py --request 'aimbot for Free Fire'"
    echo ""
    echo "📁 Important Files:"
    echo "• config/stealth_hub_config.env - Configuration file"
    echo "• start_stealth_hub.sh - Startup script"
    echo "• stealth_hub.bat - Windows quick access"
    echo "• compile_dll.bat - DLL compilation for Windows"
    echo "• data/ - Database and analysis storage"
    echo "• generated_dlls/ - Generated code output"
    echo ""
    echo "🔗 Community Stealth Discord:"
    echo "• Offsets Channel: 🔍-offsets-free-fire"
    echo "• Panel References: 🎮-panel-references"
    echo "• Development: 💻-dev-requests"
    echo ""
    echo "📖 Next Steps:"
    echo "1. Join Community Stealth Discord"
    echo "2. Get updated offsets for Free Fire"
    echo "3. Start generating DLLs with AI"
    echo ""
else
    echo ""
    echo "❌ Installation failed!"
    echo "Please check the error messages above and try again."
    echo "For support, contact Community Stealth Discord."
    exit 1
fi