# 🚀 StealtHub AI - Release Script
# Automated release creation with GitHub Actions
# Author: xpe.nettt - Community Stealth

import os
import sys
import subprocess
import json
from datetime import datetime

def run_command(cmd):
    """Ejecuta comando y retorna resultado"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def get_version():
    """Obtiene versión actual del proyecto"""
    version = "2.0.0"
    
    # Intenta obtener versión de git tags
    success, stdout, stderr = run_command("git describe --tags --abbrev=0 2>/dev/null")
    if success and stdout.strip():
        version = stdout.strip().lstrip('v')
    
    # Intenta obtener versión de archivos de configuración
    if os.path.exists("stealth_hub_cli.py"):
        try:
            with open("stealth_hub_cli.py", "r") as f:
                content = f.read()
                if "VERSION" in content:
                    import re
                    match = re.search(r'VERSION\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        version = match.group(1)
        except:
            pass
    
    return version

def create_release():
    """Crea release con GitHub CLI"""
    version = get_version()
    tag = f"v{version}"
    
    print(f"🚀 Creando release {tag}...")
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("stealth_hub_cli.py"):
        print("❌ Error: No se encontró stealth_hub_cli.py")
        print("   Ejecuta este script desde el directorio raíz del proyecto")
        return False
    
    # Verificar que hay cambios para commitear
    success, stdout, stderr = run_command("git status --porcelain")
    if success and stdout.strip():
        print("📝 Commitando cambios pendientes...")
        run_command("git add .")
        run_command('git commit -m "🤖 StealtHub AI v{} - Pre-release update"'.format(version))
    
    # Crear tag
    print(f"🏷️  Creando tag {tag}...")
    run_command(f"git tag -a {tag} -m '🤖 StealtHub AI v{version} - Release'")
    
    # Push tag (esto triggerará el workflow de release)
    print("📤 Enviando tag a GitHub...")
    success, stdout, stderr = run_command(f"git push origin {tag}")
    
    if success:
        print(f"✅ Release {tag} creado exitosamente!")
        print(f"🔗 GitHub Actions se ejecutará automáticamente")
        print(f"📦 Revisa los artifacts en: https://github.com/xpe-hub/StealtHub/actions")
        return True
    else:
        print(f"❌ Error al enviar tag: {stderr}")
        return False

def check_github_cli():
    """Verifica si GitHub CLI está instalado"""
    success, stdout, stderr = run_command("gh --version")
    return success

def main():
    print("🤖 StealtHub AI - Release Manager")
    print("=" * 40)
    
    # Verificar que estamos en un repo de git
    if not os.path.exists(".git"):
        print("❌ Error: Este directorio no es un repositorio Git")
        return 1
    
    # Verificar GitHub CLI (opcional)
    if not check_github_cli():
        print("⚠️  GitHub CLI no está instalado")
        print("   Instalar con: https://cli.github.com/")
        print("   Continuando sin GitHub CLI...")
    
    # Mostrar información de versión
    version = get_version()
    print(f"📋 Versión actual: {version}")
    
    # Confirmar acción
    print(f"\n🎯 Esto creará:")
    print(f"   • Tag: v{version}")
    print(f"   • Commit con cambios pendientes")
    print(f"   • Trigger de GitHub Actions workflow")
    
    response = input("\n¿Continuar? (y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("❌ Operación cancelada")
        return 0
    
    # Crear release
    success = create_release()
    
    if success:
        print("\n🎉 ¡Release creado exitosamente!")
        print("\n📊 Próximos pasos:")
        print("   1. Monitorea GitHub Actions: https://github.com/xpe-hub/StealtHub/actions")
        print("   2. Revisa los artifacts generados")
        print("   3. Verifica la documentación")
        print("   4. Testa los ejecutables generados")
        return 0
    else:
        print("\n💥 Error al crear release")
        return 1

if __name__ == "__main__":
    sys.exit(main())