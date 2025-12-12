#!/usr/bin/env python3
"""
StealtHub AI - Smart Build System
Builds standalone executables without dependencies
Author: xpe.nettt - Community Stealth

This script has been updated to use the smart builder
for better cross-platform compatibility.
"""

import os
import sys
import subprocess
import time
from datetime import datetime

def run_smart_build():
    """Run the smart build system"""
    print("🤖 StealtHub AI - Smart Build System")
    print("=" * 50)
    print("🔨 Building standalone executables...")
    print("📦 No dependencies required for end users!")
    print()
    
    try:
        # Import and run smart builder
        from smart_build import SmartBuilder
        builder = SmartBuilder()
        return builder.run_build()
        
    except ImportError:
        print("❌ Smart build module not found")
        print("🔄 Falling back to manual build...")
        return manual_build()
    except Exception as e:
        print(f"❌ Smart build error: {e}")
        print("🔄 Trying manual build...")
        return manual_build()

def manual_build():
    """Fallback manual build"""
    print("🔧 Manual Build Mode")
    
    targets = [
        ("StealtHub_AI_Chat", "stealth_hub_chat.py", True),
        ("StealtHub_AI_CLI", "stealth_hub_cli.py", False), 
        ("StealtHub_AI_Launcher", "stealth_hub_launcher.py", True),
        ("StealtHub_AI_GUI", "gui/control_panel.py", True),
        ("StealtHub_AI_Main", "main.py", False)
    ]
    
    successful = 0
    for name, script, windowed in targets:
        print(f"🔨 Building {name}...")
        if os.path.exists(script):
            cmd = [
                "pyinstaller", "--onefile", "--clean", 
                f"--name={name}",
                "--distpath=./dist", "--workpath=./build"
            ]
            if windowed:
                cmd.append("--windowed")
            cmd.append(script)
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    print(f"✅ {name} built successfully")
                    successful += 1
                else:
                    print(f"❌ {name} failed: {result.stderr}")
            except Exception as e:
                print(f"❌ {name} error: {e}")
        else:
            print(f"❌ {name}: {script} not found")
            
    print(f"\\n📊 Manual build results: {successful}/{len(targets)} successful")
    return successful > 0

class StealtHubBuilder:
    """Complete build system for StealtHub AI"""
    
    def __init__(self):
        self.build_dir = "build"
        self.dist_dir = "dist"
        self.src_files = [
            "stealth_hub_chat.py",
            "stealth_hub_cli.py", 
            "stealth_hub_launcher.py",
            "main.py",
            "gui/control_panel.py",
            "ai_engine/stealth_hub_ai_engine.py",
            "ai_engine/ai_dll_generator.py",
            "templates/game_templates.py",
            "offset_manager/freefire_offset_manager.py"
        ]
        self.version = "2.0.0"
        self.author = "xpe.nettt"
        self.community = "Community Stealth"
        
    def clean_build(self):
        """Clean previous build artifacts"""
        print("🧹 Cleaning build directories...")
        
        directories_to_clean = [self.build_dir, self.dist_dir, "__pycache__"]
        for directory in directories_to_clean:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"✅ Removed: {directory}")
        
        # Clean pyinstaller cache
        cache_dirs = ["*.spec", "*.pyc", ".pyc", "__pycache__"]
        for pattern in cache_dirs:
            try:
                for item in Path(".").glob(pattern):
                    if item.is_dir():
                        shutil.rmtree(item)
                    else:
                        item.unlink()
            except:
                pass
        
        print("✅ Build cleanup complete!")
        
    def install_build_dependencies(self):
        """Install build dependencies"""
        print("📦 Installing build dependencies...")
        
        build_packages = [
            "pyinstaller>=5.0.0",
            "cx_Freeze>=6.0.0", 
            "auto-py-to-exe>=2.20.0",
            "nuitka>=1.0.0"
        ]
        
        for package in build_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ Installed: {package}")
            except subprocess.CalledProcessError:
                print(f"⚠️  Failed to install: {package}")
        
        print("✅ Build dependencies ready!")
        
    def build_chat_executable(self):
        """Build chat AI executable"""
        print("🤖 Building Chat AI Executable...")
        
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            "--name", "StealtHub_AI_Chat",
            "--distpath", f"{self.dist_dir}/",
            "--workpath", f"{self.build_dir}/",
            "--specpath", f"{self.build_dir}/",
            "--icon", "resources/stealth_hub_icon.ico",
            "stealth_hub_chat.py"
        ]
        
        try:
            subprocess.check_call(cmd)
            print("✅ Chat AI executable built successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to build Chat AI: {e}")
            return False
            
    def build_cli_executable(self):
        """Build CLI executable"""
        print("⚡ Building CLI Executable...")
        
        cmd = [
            "pyinstaller",
            "--onefile", 
            "--name", "StealtHub_AI_CLI",
            "--distpath", f"{self.dist_dir}/",
            "--workpath", f"{self.build_dir}/",
            "--specpath", f"{self.build_dir}/",
            "stealth_hub_cli.py"
        ]
        
        try:
            subprocess.check_call(cmd)
            print("✅ CLI executable built successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to build CLI: {e}")
            return False
            
    def build_launcher_executable(self):
        """Build launcher executable"""
        print("🚀 Building Launcher Executable...")
        
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            "--name", "StealtHub_AI_Launcher", 
            "--distpath", f"{self.dist_dir}/",
            "--workpath", f"{self.build_dir}/",
            "--specpath", f"{self.build_dir}/",
            "--icon", "resources/stealth_hub_icon.ico",
            "stealth_hub_launcher.py"
        ]
        
        try:
            subprocess.check_call(cmd)
            print("✅ Launcher executable built successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to build Launcher: {e}")
            return False
            
    def build_gui_executable(self):
        """Build GUI control panel executable"""
        print("🎮 Building GUI Control Panel...")
        
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            "--name", "StealtHub_AI_GUI",
            "--distpath", f"{self.dist_dir}/",
            "--workpath", f"{self.build_dir}/", 
            "--specpath", f"{self.build_dir}/",
            "--icon", "resources/stealth_hub_icon.ico",
            "gui/control_panel.py"
        ]
        
        try:
            subprocess.check_call(cmd)
            print("✅ GUI Control Panel built successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to build GUI: {e}")
            return False
            
    def create_package(self):
        """Create complete package"""
        print("📦 Creating Complete Package...")
        
        package_name = f"StealtHub_AI_v{self.version}_Complete"
        package_dir = f"{self.dist_dir}/{package_name}"
        
        # Create package directory
        os.makedirs(package_dir, exist_ok=True)
        
        # Copy executables
        executables = [
            "StealtHub_AI_Chat.exe",
            "StealtHub_AI_CLI.exe", 
            "StealtHub_AI_Launcher.exe",
            "StealtHub_AI_GUI.exe"
        ]
        
        for exe in executables:
            src = f"{self.dist_dir}/{exe}"
            if os.path.exists(src):
                shutil.copy2(src, package_dir)
                print(f"✅ Copied: {exe}")
            else:
                print(f"⚠️  Not found: {exe}")
        
        # Copy source files
        source_dirs = ["ai_engine", "gui", "templates", "offset_manager", "docs", "resources"]
        for dir_name in source_dirs:
            if os.path.exists(dir_name):
                shutil.copytree(dir_name, f"{package_dir}/{dir_name}", dirs_exist_ok=True)
                print(f"✅ Copied directory: {dir_name}")
        
        # Copy configuration files
        config_files = [
            "requirements.txt",
            "README.md",
            "LICENSE",
            "config/"
        ]
        
        for config in config_files:
            if os.path.exists(config):
                if os.path.isfile(config):
                    shutil.copy2(config, package_dir)
                else:
                    shutil.copytree(config, f"{package_dir}/{config}", dirs_exist_ok=True)
                print(f"✅ Copied: {config}")
        
        # Create installation script
        self.create_installer_script(package_dir)
        
        # Create README for package
        self.create_package_readme(package_dir)
        
        print(f"✅ Package created: {package_dir}")
        return package_dir
        
    def create_installer_script(self, package_dir):
        """Create installation script"""
        installer_content = f'''@echo off
echo 🤖 StealtHub AI v{self.version} - Installation Script
echo ==============================================
echo 👨‍💻 Author: {self.author}
echo 🏠 Community: {self.community}
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
    echo ✅ Dependencies installed successfully!
    echo.
    echo 🚀 Installation complete!
    echo.
    echo 📋 Available executables:
    echo • StealtHub_AI_Chat.exe - Interactive Chat AI
    echo • StealtHub_AI_CLI.exe - Command Line Interface  
    echo • StealtHub_AI_Launcher.exe - System Launcher
    echo • StealtHub_AI_GUI.exe - GUI Control Panel
    echo.
    echo 🎮 Ready to use! Double-click any executable to start.
) else (
    echo ❌ Failed to install dependencies.
    echo Please check your Python and pip installation.
)

pause
'''
        
        with open(f"{package_dir}/install.bat", 'w') as f:
            f.write(installer_content)
            
    def create_package_readme(self, package_dir):
        """Create README for the package"""
        readme_content = f'''# 🤖 StealtHub AI v{self.version}

**Autonomous Gaming Development AI System**

> **Author**: {self.author}  
> **Community**: {self.community}  
> **Version**: {self.version}  
> **Release Date**: {datetime.now().strftime('%Y-%m-%d')}  

## 🚀 Quick Start

### 1. Install Dependencies
Double-click `install.bat` to install required Python packages.

### 2. Run StealtHub AI
Choose your preferred interface:

- **🤖 StealtHub_AI_Chat.exe** - Interactive chat AI (RECOMMENDED)
- **⚡ StealtHub_AI_CLI.exe** - Command line interface
- **🚀 StealtHub_AI_Launcher.exe** - System launcher with all options
- **🎮 StealtHub_AI_GUI.exe** - GUI control panel

## 🎮 Features

### 🤖 Chat AI Interface
- Natural language conversation
- Autonomous code generation
- Real-time assistance
- Gaming development guidance

### ⚡ CLI Interface  
- Command-line operations
- Batch processing
- Script automation
- Advanced options

### 🎮 GUI Control Panel
- Visual controls
- Real-time monitoring
- Configuration management
- Status displays

## 🛠️ Available Functions

### Gaming Development
- Aimbot generation (C++ DLLs)
- ESP systems with overlays
- SpeedHack development  
- Recoil control systems
- Anti-detection mechanisms

### Programming & Scripts
- Python automation
- Discord bot creation
- GUI applications
- Memory manipulation tools

### Technical Services
- Code analysis
- Security assessment
- Cross-platform compatibility
- Documentation generation

## 💬 Usage Examples

### Chat AI Commands:
- "Create an aimbot for Free Fire with FOV 180"
- "Generate a Discord bot for gaming controls" 
- "Build a complete ESP system"
- "Make a speedhack with adjustable multiplier"

### CLI Commands:
```bash
StealtHub_AI_CLI.exe --request "aimbot for Free Fire"
StealtHub_AI_CLI.exe --interactive
StealtHub_AI_CLI.exe --stats
```

## 🛡️ Security Features

- Anti-detection mechanisms
- Stealth injection methods
- Memory obfuscation
- Thread randomization
- Signature protection

## 📞 Support

- **Discord**: Community Stealth
- **Email**: xpepaneles@gmail.com  
- **Documentation**: Check the `docs/` directory

## ⚠️ Disclaimer

This software is for educational and research purposes only.
Users are responsible for compliance with applicable laws and terms of service.

## 📄 License

MIT License - See LICENSE file for details.

---

**🤖 StealtHub AI v{self.version} | {self.community} | {self.author}**

*Generated automatically by StealtHub AI Build System*
'''
        
        with open(f"{package_dir}/README.md", 'w') as f:
            f.write(readme_content)
            
    def create_release_archive(self, package_dir):
        """Create release archive"""
        print("🗂️ Creating Release Archive...")
        
        archive_name = f"StealtHub_AI_v{self.version}_Release.zip"
        archive_path = f"{self.dist_dir}/{archive_name}"
        
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(package_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, package_dir)
                    zipf.write(file_path, arcname)
                    
        print(f"✅ Release archive created: {archive_path}")
        return archive_path
        
    def run_build(self):
        """Run complete build process"""
        print("🔨 Starting StealtHub AI Build Process...")
        print("=" * 50)
        
        start_time = time.time()
        
        # Clean previous builds
        self.clean_build()
        
        # Install dependencies
        self.install_build_dependencies()
        
        # Build executables
        builds = [
            ("Chat AI", self.build_chat_executable),
            ("CLI", self.build_cli_executable), 
            ("Launcher", self.build_launcher_executable),
            ("GUI", self.build_gui_executable)
        ]
        
        successful_builds = 0
        for name, build_func in builds:
            if build_func():
                successful_builds += 1
            time.sleep(2)  # Brief pause between builds
        
        print(f"\n📊 Build Summary:")
        print(f"✅ Successful builds: {successful_builds}/{len(builds)}")
        
        if successful_builds > 0:
            # Create package
            package_dir = self.create_package()
            
            # Create release archive
            archive_path = self.create_release_archive(package_dir)
            
            # Calculate build time
            build_time = time.time() - start_time
            
            print(f"\n🎉 Build Complete!")
            print(f"⏱️  Build time: {build_time:.2f} seconds")
            print(f"📦 Package: {package_dir}")
            print(f"🗂️  Archive: {archive_path}")
            print(f"🎯 Ready for distribution!")
            
            return True
        else:
            print("❌ No successful builds. Please check errors above.")
            return False

def main():
    """Main entry point"""
    print("🤖 StealtHub AI - Build System v2.0")
    print("=" * 50)
    print("🎯 Building standalone executables...")
    print("💡 End users won't need Python installation!")
    print()
    
    success = run_smart_build()
    
    if success:
        print("\n🎉 Build completed successfully!")
        print("\n📋 Next steps:")
        print("1. ✅ Executables ready in ./dist/ directory")
        print("2. 📤 Upload to GitHub to trigger CI/CD")
        print("3. 📦 Download from GitHub Releases")
        print("4. 🚀 Users can run .exe files directly!")
        print("\n🎯 Users can now:")
        print("   • Download ZIP from GitHub")
        print("   • Extract and run any .exe")
        print("   • Start chatting with AI immediately")
        print("   • NO Python installation required!")
    else:
        print("\n❌ Build failed. Check errors above.")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())