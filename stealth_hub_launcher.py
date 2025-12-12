#!/usr/bin/env python3
"""
StealtHub AI - Autonomous Launcher
Complete autonomous AI system with chat interface
Author: xpe.nettt - Community Stealth
"""

import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
import threading
import time
from pathlib import Path

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def check_dependencies():
    """Check if all dependencies are installed"""
    required_packages = [
        'tkinter',
        'requests',
        'numpy',
        'PIL',
        'psutil',
        'discord.py'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing dependencies:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n🔧 Installing missing dependencies...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ Dependencies installed successfully!")
        except Exception as e:
            print(f"❌ Failed to install dependencies: {e}")
            return False
    
    return True

def setup_environment():
    """Setup the development environment"""
    print("🔧 Setting up StealtHub AI environment...")
    
    # Create necessary directories
    directories = [
        'config',
        'logs',
        'generated_projects',
        'generated_code',
        'conversations',
        'plugins',
        'build',
        'dist'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created directory: {directory}")
    
    # Create configuration files
    create_config_files()
    
    print("✅ Environment setup complete!")

def create_config_files():
    """Create default configuration files"""
    
    # Main config
    config = {
        "version": "2.0.0",
        "author": "xpe.nettt",
        "community": "Community Stealth",
        "discord_server": "Community Stealth",
        "default_game": "Free Fire",
        "default_emulator": "BlueStacks",
        "features": {
            "aimbot": {
                "enabled": True,
                "fov": 180,
                "smoothness": 2.0,
                "team_check": True,
                "prediction": True
            },
            "esp": {
                "enabled": True,
                "health_bars": True,
                "names": True,
                "distance": True,
                "skeleton": False
            },
            "speedhack": {
                "enabled": True,
                "default_multiplier": 2.0,
                "max_multiplier": 10.0
            },
            "discord_bot": {
                "enabled": False,
                "token": "",
                "prefix": "!",
                "auto_start": False
            }
        },
        "security": {
            "anti_detection": True,
            "random_delays": True,
            "obfuscation": True
        },
        "ui": {
            "theme": "dark",
            "font_size": 12,
            "chat_history": True,
            "auto_save": True
        }
    }
    
    import json
    with open('config/main_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    # Discord config
    discord_config = {
        "bot_token": "",
        "guild_id": "",
        "channels": {
            "gaming_control": "gaming-commands",
            "development": "development-chat",
            "community": "general"
        },
        "commands": {
            "aimbot": {
                "enabled": True,
                "cooldown": 5
            },
            "esp": {
                "enabled": True,
                "cooldown": 5
            },
            "speedhack": {
                "enabled": True,
                "cooldown": 3
            }
        }
    }
    
    with open('config/discord_config.json', 'w') as f:
        json.dump(discord_config, f, indent=2)
    
    # Security config
    security_config = {
        "detection_prevention": {
            "random_delays": {
                "min_delay": 100,
                "max_delay": 1000
            },
            "thread_obfuscation": True,
            "memory_hiding": True,
            "signature_randomization": True
        },
        "stealth_features": {
            "sleep_randomization": True,
            "thread_delays": True,
            "memory_obfuscation": True,
            "pattern_hiding": True
        }
    }
    
    with open('config/security_config.json', 'w') as f:
        json.dump(security_config, f, indent=2)

def show_launcher():
    """Show the main launcher interface"""
    
    class LauncherGUI:
        def __init__(self):
            self.root = tk.Tk()
            self.setup_gui()
            
        def setup_gui(self):
            self.root.title("🤖 StealtHub AI v2.0 - Autonomous Launcher")
            self.root.geometry("500x400")
            self.root.configure(bg='#1e1e1e')
            
            # Header
            header_frame = tk.Frame(self.root, bg='#2d2d2d', height=80)
            header_frame.pack(fill='x', padx=20, pady=10)
            header_frame.pack_propagate(False)
            
            title_label = tk.Label(
                header_frame,
                text="🤖 StealtHub AI v2.0",
                font=('Arial', 18, 'bold'),
                fg='#00ff00',
                bg='#2d2d2d'
            )
            title_label.pack(pady=20)
            
            subtitle_label = tk.Label(
                header_frame,
                text="Autonomous Gaming Development AI System",
                font=('Arial', 10),
                fg='#cccccc',
                bg='#2d2d2d'
            )
            subtitle_label.pack()
            
            # Main buttons
            buttons_frame = tk.Frame(self.root, bg='#1e1e1e')
            buttons_frame.pack(fill='both', expand=True, padx=20, pady=10)
            
            # Chat AI Button
            chat_btn = tk.Button(
                buttons_frame,
                text="💬 Start Chat AI",
                command=self.launch_chat_ai,
                bg='#0099ff',
                fg='white',
                font=('Arial', 12, 'bold'),
                relief='flat',
                bd=5,
                cursor='hand2',
                height=2
            )
            chat_btn.pack(fill='x', pady=5)
            
            # CLI Button
            cli_btn = tk.Button(
                buttons_frame,
                text="⚡ Launch CLI Interface",
                command=self.launch_cli,
                bg='#00aa00',
                fg='white',
                font=('Arial', 12, 'bold'),
                relief='flat',
                bd=5,
                cursor='hand2',
                height=2
            )
            cli_btn.pack(fill='x', pady=5)
            
            # Discord Bot Button
            discord_btn = tk.Button(
                buttons_frame,
                text="🐍 Discord Bot",
                command=self.launch_discord_bot,
                bg='#7289da',
                fg='white',
                font=('Arial', 12, 'bold'),
                relief='flat',
                bd=5,
                cursor='hand2',
                height=2
            )
            discord_btn.pack(fill='x', pady=5)
            
            # GUI Control Panel Button
            gui_btn = tk.Button(
                buttons_frame,
                text="🎮 GUI Control Panel",
                command=self.launch_gui_panel,
                bg='#ff6b6b',
                fg='white',
                font=('Arial', 12, 'bold'),
                relief='flat',
                bd=5,
                cursor='hand2',
                height=2
            )
            gui_btn.pack(fill='x', pady=5)
            
            # Build/Compile Button
            build_btn = tk.Button(
                buttons_frame,
                text="🔨 Build Executables",
                command=self.build_executables,
                bg='#ff9500',
                fg='white',
                font=('Arial', 12, 'bold'),
                relief='flat',
                bd=5,
                cursor='hand2',
                height=2
            )
            build_btn.pack(fill='x', pady=5)
            
            # Exit button
            exit_btn = tk.Button(
                buttons_frame,
                text="❌ Exit",
                command=self.exit_app,
                bg='#666666',
                fg='white',
                font=('Arial', 10),
                relief='flat',
                bd=5,
                cursor='hand2'
            )
            exit_btn.pack(side='bottom', pady=10)
            
        def launch_chat_ai(self):
            """Launch the chat AI interface"""
            try:
                self.root.withdraw()  # Hide launcher
                os.system(f"{sys.executable} stealth_hub_chat.py")
                self.root.deiconify()  # Show launcher again
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch Chat AI: {str(e)}")
                
        def launch_cli(self):
            """Launch the CLI interface"""
            try:
                self.root.withdraw()  # Hide launcher
                os.system(f"{sys.executable} stealth_hub_cli.py")
                self.root.deiconify()  # Show launcher again
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch CLI: {str(e)}")
                
        def launch_discord_bot(self):
            """Launch Discord bot"""
            try:
                self.root.withdraw()  # Hide launcher
                os.system(f"{sys.executable} generated_discord_bot.py")
                self.root.deiconify()  # Show launcher again
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch Discord Bot: {str(e)}")
                
        def launch_gui_panel(self):
            """Launch GUI control panel"""
            try:
                self.root.withdraw()  # Hide launcher
                os.system(f"{sys.executable} gui/control_panel.py")
                self.root.deiconify()  # Show launcher again
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch GUI Panel: {str(e)}")
                
        def build_executables(self):
            """Build all executables"""
            try:
                self.root.withdraw()  # Hide launcher
                os.system(f"{sys.executable} build_all.py")
                self.root.deiconify()  # Show launcher again
            except Exception as e:
                messagebox.showerror("Error", f"Failed to build executables: {str(e)}")
                
        def exit_app(self):
            """Exit the application"""
            if messagebox.askokcancel("Exit", "Are you sure you want to exit StealtHub AI?"):
                self.root.destroy()
                
        def run(self):
            """Run the launcher"""
            self.root.mainloop()
    
    launcher = LauncherGUI()
    launcher.run()

def main():
    """Main entry point"""
    print("🤖 StealtHub AI v2.0 - Autonomous System Launcher")
    print("=" * 50)
    print("👨‍💻 Author: xpe.nettt")
    print("🏠 Community: Community Stealth")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Failed to setup dependencies. Please install manually.")
        input("Press Enter to exit...")
        return
    
    # Setup environment
    setup_environment()
    
    # Show launcher
    show_launcher()

if __name__ == "__main__":
    main()