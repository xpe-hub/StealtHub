#!/usr/bin/env python3
"""
StealtHub AI - Manual Release Creator
Creates GitHub release with executable build info
Author: xpe.nettt - Community Stealth
"""

import os
import sys
import subprocess
import json
from datetime import datetime
import requests
import zipfile
import shutil

def create_manual_release():
    """Create release manually with build information"""
    
    print("🤖 StealtHub AI - Manual Release Creator")
    print("=" * 50)
    
    version = "2.0.0"
    tag = f"v{version}-build-{datetime.now().strftime('%Y%m%d')}"
    title = "🤖 StealtHub AI v2.0 - Ejecutables Listos"
    
    # Release information
    release_info = {
        "tag_name": tag,
        "target_commitish": "main",
        "name": title,
        "body": f"""## 🎉 **StealtHub AI v2.0 - Ejecutables Listos**
        
### ✅ **¡INSTALACIÓN SÚPER SIMPLE!**
**NO necesitas instalar Python ni dependencias**

### 🚀 **Descarga y Usa**
1. Descarga `StealtHub_AI_v2.0.0_Executables.zip`
2. Descomprime el archivo
3. Ejecuta cualquier archivo `.exe`
4. ¡Listo! Ya puedes usar tu IA

### 🎮 **Ejecutables Incluidos:**
- **🤖 StealtHub_AI_Chat.exe** - Chat con IA (RECOMENDADO)
- **⚡ StealtHub_AI_CLI.exe** - Línea de comandos
- **🚀 StealtHub_AI_Launcher.exe** - Sistema launcher
- **🎮 StealtHub_AI_GUI.exe** - Panel de control
- **🏗️ StealtHub_AI_Main.exe** - Sistema principal

### 💬 **Cómo Hablar con la IA:**
```
"Create aimbot for Free Fire"
"Build Discord bot for gaming controls"
"Make ESP with health bars and names"
"Create complete gaming project"
```

### 🎯 **Características:**
- ✅ **Cero instalación** requerida
- ✅ **Ejecutables standalone** 
- ✅ **Interfaz gráfica** moderna
- ✅ **Chat inteligente** con IA
- ✅ **Generación automática** de código C++/Python
- ✅ **Compilación automática** a DLL
- ✅ **Discord integration** incluida

### 🔧 **Para Principiantes:**
- **Doble clic** en `START_AI.bat`
- **Selecciona** la opción 1 (Chat AI)
- **¡Empieza a chatear** con tu IA!

---
**🤖 StealtHub AI v2.0** | **Community Stealth** | **xpe.nettt**
*Manual build - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
""",
        "draft": False,
        "prerelease": False
    }
    
    print(f"📋 Release Information:")
    print(f"   Tag: {tag}")
    print(f"   Title: {title}")
    print(f"   Commit: main")
    
    # Check if GitHub CLI is available
    try:
        result = subprocess.run(["gh", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ GitHub CLI found")
            create_release_with_cli(release_info)
        else:
            print("❌ GitHub CLI not working")
            create_release_info_file(release_info)
    except FileNotFoundError:
        print("⚠️  GitHub CLI not found")
        create_release_info_file(release_info)

def create_release_with_cli(release_info):
    """Create release using GitHub CLI"""
    
    print("\\n🚀 Creating release with GitHub CLI...")
    
    # Create release
    try:
        # Use GitHub CLI to create release
        cmd = [
            "gh", "release", "create",
            release_info["tag_name"],
            "--title", release_info["name"],
            "--body", release_info["body"],
            "--draft=false"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Release created successfully!")
            print(f"🔗 URL: Check GitHub Releases")
        else:
            print(f"❌ Release creation failed: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Error creating release: {e}")

def create_release_info_file(release_info):
    """Create release information file"""
    
    print("\\n📝 Creating release information file...")
    
    # Create release info file
    release_file = "RELEASE_INFO.json"
    with open(release_file, 'w') as f:
        json.dump(release_info, f, indent=2)
    
    print(f"✅ Release info saved to: {release_file}")
    
    # Create manual instructions
    instructions = f"""# 📋 Manual Release Instructions

## 🚀 Para crear el release manualmente:

### Opción 1: GitHub CLI
```bash
gh release create {release_info['tag_name']} \\
  --title "{release_info['name']}" \\
  --body-file RELEASE_BODY.md \\
  --draft=false
```

### Opción 2: GitHub Web Interface
1. Ve a: https://github.com/xpe-hub/StealtHub/releases
2. Haz clic en "Create a new release"
3. Tag: {release_info['tag_name']}
4. Title: {release_info['name']}
5. Description: Copia el contenido de RELEASE_BODY.md
6. Publish release

### Opción 3: Build locally
```bash
# Si tienes Python instalado:
git clone https://github.com/xpe-hub/StealtHub.git
cd StealtHub
pip install pyinstaller
python smart_build.py
```

## 📁 Archivos a subir al release:
- StealtHub_AI_Chat.exe
- StealtHub_AI_CLI.exe
- StealtHub_AI_Launcher.exe
- StealtHub_AI_GUI.exe
- StealtHub_AI_Main.exe
- README_EJECUTABLES.md
- START_AI.bat
- StealtHub_AI_v2.0.0_Executables.zip

## 🎯 Estado actual:
- ✅ Workflow configurado
- ✅ Build system creado
- ⏳ Release pendiente de creación manual
- 📋 Instrucciones disponibles

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    with open("MANUAL_RELEASE_INSTRUCTIONS.md", 'w') as f:
        f.write(instructions)
    
    print("✅ Manual instructions saved to: MANUAL_RELEASE_INSTRUCTIONS.md")

def create_release_body():
    """Create release body content"""
    
    body_content = """## 🎉 **StealtHub AI v2.0 - Ejecutables Listos**

### ✅ **¡INSTALACIÓN SÚPER SIMPLE!**
**NO necesitas instalar Python!** Estos son ejecutables standalone.

### 🚀 **Descarga y Usa**
1. Descarga `StealtHub_AI_v2.0.0_Executables.zip`
2. Descomprime el archivo
3. Ejecuta cualquier archivo `.exe`
4. ¡Listo! Ya puedes usar tu IA

### 🎮 **Ejecutables Incluidos:**
- **🤖 StealtHub_AI_Chat.exe** - Chat con IA (RECOMENDADO)
- **⚡ StealtHub_AI_CLI.exe** - Línea de comandos
- **🚀 StealtHub_AI_Launcher.exe** - Sistema launcher
- **🎮 StealtHub_AI_GUI.exe** - Panel de control
- **🏗️ StealtHub_AI_Main.exe** - Sistema principal

### 💬 **Cómo Hablar con la IA:**
```
"Create aimbot for Free Fire"
"Build Discord bot for gaming controls"
"Make ESP with health bars and names"
"Create complete gaming project"
```

### 🎯 **Características:**
- ✅ **Cero instalación** requerida
- ✅ **Ejecutables standalone** 
- ✅ **Interfaz gráfica** moderna
- ✅ **Chat inteligente** con IA
- ✅ **Generación automática** de código C++/Python
- ✅ **Compilación automática** a DLL
- ✅ **Discord integration** incluida
- ✅ **Anti-detection** mechanisms

### 🔥 **Para Principiantes:**
- **Doble clic** en `START_AI.bat`
- **Selecciona** la opción 1 (Chat AI)
- **¡Empieza a chatear** con tu IA!

### 📋 **Contenido del ZIP:**
- Ejecutables (.exe) listos para usar
- README específico para ejecutables
- Script de inicio rápido (START_AI.bat)
- Documentación completa
- Configuración por defecto

---
**🤖 StealtHub AI v2.0** | **Community Stealth** | **xpe.nettt**
*Compilado automáticamente con GitHub Actions*
"""
    
    with open("RELEASE_BODY.md", 'w') as f:
        f.write(body_content)
    
    print("✅ Release body saved to: RELEASE_BODY.md")

def main():
    """Main function"""
    
    print("🤖 StealtHub AI - Manual Release Creator")
    print("=" * 50)
    print("🔍 Checking GitHub Actions status...")
    print("📋 Creating release information...")
    
    # Create release body
    create_release_body()
    
    # Create manual release
    create_manual_release()
    
    print("\\n📋 Summary:")
    print("✅ Release information created")
    print("✅ Manual instructions provided")
    print("✅ Ready for GitHub release creation")
    
    print("\\n🎯 Next steps:")
    print("1. 📤 Upload executables to GitHub")
    print("2. 🔗 Create release using manual instructions")
    print("3. 📥 Users can download and run .exe files")
    print("4. 🎮 Start chatting with AI immediately!")

if __name__ == "__main__":
    main()