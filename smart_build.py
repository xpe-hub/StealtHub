#!/usr/bin/env python3
"""
StealtHub AI - Smart Executable Builder
Creates standalone executables without dependencies
Author: xpe.nettt - Community Stealth
"""

import os
import sys
import subprocess
import shutil
import platform
import zipfile
from pathlib import Path
import time
from datetime import datetime

class SmartBuilder:
    """Smart builder that adapts to different environments"""
    
    def __init__(self):
        self.system = platform.system()
        self.is_windows = self.system == "Windows"
        self.is_linux = self.system == "Linux"
        self.is_mac = self.system == "Darwin"
        
        self.build_dir = "build"
        self.dist_dir = "dist"
        self.version = "2.0.0"
        self.author = "xpe.nettt"
        self.community = "Community Stealth"
        
        # Target executables
        self.targets = [
            {
                "name": "StealtHub_AI_Chat",
                "script": "stealth_hub_chat.py",
                "windowed": True,
                "description": "Interactive Chat AI Interface"
            },
            {
                "name": "StealtHub_AI_CLI", 
                "script": "stealth_hub_cli.py",
                "windowed": False,
                "description": "Command Line Interface"
            },
            {
                "name": "StealtHub_AI_Launcher",
                "script": "stealth_hub_launcher.py", 
                "windowed": True,
                "description": "System Launcher"
            },
            {
                "name": "StealtHub_AI_GUI",
                "script": "gui/control_panel.py",
                "windowed": True,
                "description": "GUI Control Panel"
            },
            {
                "name": "StealtHub_AI_Main",
                "script": "main.py",
                "windowed": False,
                "description": "Main System"
            }
        ]
        
    def check_environment(self):
        """Check build environment"""
        print(f"🔍 Environment Check:")
        print(f"   System: {self.system}")
        print(f"   Python: {sys.version}")
        print(f"   Working Dir: {os.getcwd()}")
        
        # Check required files
        missing_files = []
        for target in self.targets:
            if not os.path.exists(target["script"]):
                missing_files.append(target["script"])
                
        if missing_files:
            print(f"❌ Missing files: {missing_files}")
            return False
            
        print("✅ Environment check passed")
        return True
        
    def install_pyinstaller(self):
        """Install PyInstaller"""
        print("📦 Installing PyInstaller...")
        
        try:
            # Try different installation methods
            methods = [
                [sys.executable, "-m", "pip", "install", "pyinstaller"],
                [sys.executable, "-m", "pip3", "install", "pyinstaller"],
                ["pip", "install", "pyinstaller"],
                ["pip3", "install", "pyinstaller"]
            ]
            
            for method in methods:
                try:
                    result = subprocess.run(method, capture_output=True, text=True, timeout=60)
                    if result.returncode == 0:
                        print("✅ PyInstaller installed successfully")
                        return True
                except:
                    continue
                    
            print("⚠️  PyInstaller installation failed, trying to continue...")
            return False
            
        except Exception as e:
            print(f"⚠️  Error installing PyInstaller: {e}")
            return False
            
    def build_executable(self, target):
        """Build a single executable"""
        name = target["name"]
        script = target["script"]
        windowed = target["windowed"]
        description = target["description"]
        
        print(f"🔨 Building {name} ({description})...")
        
        # Create command
        cmd = [
            "pyinstaller",
            "--onefile",
            "--clean",
            "--noconfirm",
            f"--name={name}",
            f"--distpath={self.dist_dir}",
            f"--workpath={self.build_dir}"
        ]
        
        if windowed:
            cmd.append("--windowed")
            
        # Add icon if exists
        icon_path = "resources/stealth_hub_icon.ico"
        if os.path.exists(icon_path):
            cmd.append(f"--icon={icon_path}")
            
        cmd.append(script)
        
        try:
            # Run PyInstaller
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                # Find the executable
                exe_name = f"{name}.exe" if self.is_windows else name
                exe_path = os.path.join(self.dist_dir, exe_name)
                
                if os.path.exists(exe_path):
                    size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                    print(f"✅ {name} built successfully ({size_mb:.1f} MB)")
                    return True
                else:
                    print(f"❌ {name} executable not found")
                    return False
            else:
                print(f"❌ {name} build failed:")
                print(result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ {name} build timeout")
            return False
        except Exception as e:
            print(f"❌ {name} build error: {e}")
            return False
            
    def create_package(self):
        """Create complete package"""
        print("📦 Creating release package...")
        
        package_name = f"StealtHub_AI_v{self.version}_{self.system}_Release"
        package_dir = os.path.join(self.dist_dir, package_name)
        
        # Create package directory
        os.makedirs(package_dir, exist_ok=True)
        
        # Copy executables
        copied_executables = []
        for target in self.targets:
            exe_name = f"{target['name']}.exe" if self.is_windows else target['name']
            exe_path = os.path.join(self.dist_dir, exe_name)
            
            if os.path.exists(exe_path):
                shutil.copy2(exe_path, package_dir)
                copied_executables.append(exe_name)
                print(f"✅ Copied: {exe_name}")
                
        # Copy configuration files
        config_files = [
            "requirements.txt",
            "README.md", 
            "LICENSE",
            "README_FINAL.md"
        ]
        
        for config_file in config_files:
            if os.path.exists(config_file):
                shutil.copy2(config_file, package_dir)
                print(f"✅ Copied: {config_file}")
                
        # Create system-specific documentation
        self.create_system_readme(package_dir, copied_executables)
        
        # Create launcher script
        self.create_launcher_script(package_dir, copied_executables)
        
        # Create ZIP if on Linux (for GitHub Actions)
        if self.is_linux:
            self.create_zip_package(package_dir, package_name)
            
        return package_dir
        
    def create_system_readme(self, package_dir, executables):
        """Create system-specific README"""
        
        if self.is_windows:
            readme_content = f'''# 🤖 StealtHub AI v{self.version} - Windows Executables

## 🚀 Instalación Súper Simple

**¡NO necesitas instalar Python!** Estos son ejecutables standalone.

### 🎯 Cómo usar:

1. **Doble clic** en cualquier archivo .exe
2. **¡Listo!** Ya puedes usar StealtHub AI

### 📱 Ejecutables disponibles:

{chr(10).join(f"- **{exe}** - {self.get_executable_description(exe)}" for exe in executables)}

### 💬 Cómo hablar con la IA:

1. Ejecuta `StealtHub_AI_Chat.exe`
2. En la ventana de chat, escribe:
   - "Create aimbot for Free Fire"
   - "Build Discord bot for gaming"
   - "Make ESP system with health bars"

### 🎮 Ejemplos:

```
🤖 AI: ¡Hola! Soy tu asistente de desarrollo de juegos.
You: "Crea aimbot para Free Fire"
🤖 AI: ✅ ¡Generado! Archivos listos para compilar
You: "Haz bot de Discord" 
🤖 AI: ✅ ¡Bot creado! Código Python completo
```

### ⚡ Inicio Rápido:

1. **Doble clic** en `START_AI.bat`
2. **Selecciona** opción 1 (Chat AI)
3. **¡Empieza a chatear** con tu IA!

---
🤖 **StealtHub AI v{self.version}** | xpe.nettt | Community Stealth
'''
            
        else:  # Linux/Mac
            readme_content = f'''# 🤖 StealtHub AI v{self.version} - {self.system} Executables

## 🚀 Quick Start

1. **Make executable:** `chmod +x *.exe` (Linux) or **Right-click > Properties > Make executable** (Mac)
2. **Run:** `./StealtHub_AI_Chat`
3. **Chat with AI!** Start asking for game development help

### Available Executables:

{chr(10).join(f"- **{exe}** - {self.get_executable_description(exe)}" for exe in executables)}

---
🤖 **StealtHub AI v{self.version}** | xpe.nettt | Community Stealth
'''
            
        with open(os.path.join(package_dir, "README_EXECUTABLES.md"), 'w') as f:
            f.write(readme_content)
            
    def get_executable_description(self, exe_name):
        """Get description for executable"""
        descriptions = {
            "StealtHub_AI_Chat.exe": "Chat Interface con IA (RECOMENDADO)",
            "StealtHub_AI_CLI.exe": "Línea de comandos",
            "StealtHub_AI_Launcher.exe": "Launcher del sistema",
            "StealtHub_AI_GUI.exe": "Panel de control gráfico",
            "StealtHub_AI_Main.exe": "Sistema principal",
            "StealtHub_AI_Chat": "Chat Interface con IA (RECOMMENDED)",
            "StealtHub_AI_CLI": "Command Line Interface",
            "StealtHub_AI_Launcher": "System Launcher", 
            "StealtHub_AI_GUI": "GUI Control Panel",
            "StealtHub_AI_Main": "Main System"
        }
        return descriptions.get(exe_name, "StealtHub AI Component")
        
    def create_launcher_script(self, package_dir, executables):
        """Create launcher script"""
        
        if self.is_windows:
            # Windows batch launcher
            launcher_content = f'''@echo off
echo 🤖 StealtHub AI v{self.version} - Quick Launcher
echo ===========================================
echo.
echo 🎯 Elige tu interfaz preferida:
echo.

options=(
"1. Chat AI (RECOMENDADO) - Interfaz de conversación"
"2. CLI - Línea de comandos" 
"3. Launcher - Sistema completo"
"4. GUI - Panel de control"
)

for /l %%i in (1,1,4) do (
    echo !options[%%i]!
)

echo.
set /p choice="Ingresa tu opción (1-4): "

if "%choice%"=="1" (
    echo 🤖 Iniciando Chat AI...
    start "" "StealtHub_AI_Chat.exe"
) else if "%choice%"=="2" (
    echo ⚡ Iniciando CLI...
    start "" "StealtHub_AI_CLI.exe"
) else if "%choice%"=="3" (
    echo 🚀 Iniciando Launcher...
    start "" "StealtHub_AI_Launcher.exe"
) else if "%choice%"=="4" (
    echo 🎮 Iniciando GUI...
    start "" "StealtHub_AI_GUI.exe"
) else (
    echo ❌ Opción inválida. Usando Chat AI por defecto...
    start "" "StealtHub_AI_Chat.exe"
)

echo.
echo ✅ StealtHub AI iniciado!
echo.
echo 💬 Comandos útiles para la IA:
echo - "Create aimbot for Free Fire"
echo - "Build Discord bot for gaming"
echo - "Make ESP with health bars"
echo - "Create complete project"
echo.
pause
'''
            
            with open(os.path.join(package_dir, "START_AI.bat"), 'w') as f:
                f.write(launcher_content)
                
        else:
            # Linux/Mac shell launcher
            launcher_content = f'''#!/bin/bash
echo "🤖 StealtHub AI v{self.version} - Quick Launcher"
echo "==========================================="
echo ""
echo "🎯 Choose your preferred interface:"
echo ""
echo "1. Chat AI (RECOMMENDED) - Conversation interface"
echo "2. CLI - Command line interface"
echo "3. Launcher - Complete system launcher"
echo "4. GUI - Control panel"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "🤖 Starting Chat AI..."
        ./StealtHub_AI_Chat
        ;;
    2)
        echo "⚡ Starting CLI..."
        ./StealtHub_AI_CLI
        ;;
    3)
        echo "🚀 Starting Launcher..."
        ./StealtHub_AI_Launcher
        ;;
    4)
        echo "🎮 Starting GUI..."
        ./StealtHub_AI_GUI
        ;;
    *)
        echo "❌ Invalid choice. Using Chat AI by default..."
        ./StealtHub_AI_Chat
        ;;
esac

echo ""
echo "✅ StealtHub AI started!"
echo ""
echo "💬 Useful AI commands:"
echo '- "Create aimbot for Free Fire"'
echo '- "Build Discord bot for gaming"'
echo '- "Make ESP with health bars"'
echo '- "Create complete project"'
echo ""
'''
            
            launcher_file = os.path.join(package_dir, "start_ai.sh")
            with open(launcher_file, 'w') as f:
                f.write(launcher_content)
                
            # Make executable
            os.chmod(launcher_file, 0o755)
            
    def create_zip_package(self, package_dir, package_name):
        """Create ZIP package"""
        print("🗂️ Creating ZIP package...")
        
        zip_name = f"{package_name}.zip"
        zip_path = os.path.join(self.dist_dir, zip_name)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(package_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, package_dir)
                    zipf.write(file_path, arcname)
                    
        print(f"✅ ZIP package created: {zip_path}")
        return zip_path
        
    def run_build(self):
        """Run complete build process"""
        print("🔨 Starting Smart Build Process...")
        print("=" * 50)
        
        start_time = time.time()
        
        # Environment check
        if not self.check_environment():
            return False
            
        # Install PyInstaller
        if not self.install_pyinstaller():
            print("⚠️  Continuing without PyInstaller installation")
            
        # Clean previous builds
        print("🧹 Cleaning previous builds...")
        for directory in [self.build_dir, self.dist_dir]:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                
        # Build executables
        successful_builds = 0
        for target in self.targets:
            if self.build_executable(target):
                successful_builds += 1
            time.sleep(1)  # Brief pause between builds
            
        print(f"\\n📊 Build Summary:")
        print(f"✅ Successful builds: {successful_builds}/{len(self.targets)}")
        
        if successful_builds > 0:
            # Create package
            package_dir = self.create_package()
            
            # Calculate build time
            build_time = time.time() - start_time
            
            print(f"\\n🎉 Build Complete!")
            print(f"⏱️  Build time: {build_time:.2f} seconds")
            print(f"📦 Package: {package_dir}")
            
            # List built executables
            print(f"\\n🎯 Built Executables:")
            for target in self.targets:
                exe_name = f"{target['name']}.exe" if self.is_windows else target['name']
                exe_path = os.path.join(self.dist_dir, exe_name)
                if os.path.exists(exe_path):
                    size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                    print(f"   ✅ {exe_name} ({size_mb:.1f} MB)")
                    
            print(f"\\n🚀 Ready for distribution!")
            print(f"💾 Users can download and run directly without Python!")
            
            return True
        else:
            print("❌ No successful builds. Please check errors above.")
            return False

def main():
    """Main entry point"""
    builder = SmartBuilder()
    success = builder.run_build()
    
    if success:
        print("\\n🎯 Next steps:")
        print("1. Test the executables locally")
        print("2. Upload to GitHub to trigger GitHub Actions")
        print("3. Download from GitHub Releases")
        print("4. Users can run directly without Python installation!")
    else:
        print("\\n❌ Build failed. Please check the errors above.")
        
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())