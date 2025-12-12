@echo off
echo 🤖 StealtHub AI v2.0 - Quick Installation
echo =======================================
echo.

echo 📦 Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found!

echo.
echo 📦 Installing dependencies...
pip install -r requirements.txt

if %ERRORLEVEL% EQU 0 (
    echo ✅ Installation successful!
    echo.
    echo 🚀 Ready to use! Choose your interface:
    echo.
    echo 🤖 Interactive Chat AI:
    echo    python stealth_hub_chat.py
    echo.
    echo ⚡ CLI Interface:
    echo    python stealth_hub_cli.py
    echo.
    echo 🎮 System Launcher:
    echo    python stealth_hub_launcher.py
    echo.
    echo 💬 Start chatting with the AI right now!
) else (
    echo ❌ Installation failed.
    echo Please check your Python and pip installation.
)

pause
