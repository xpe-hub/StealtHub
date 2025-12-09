# 🤖 GitHub Actions - StealtHub AI CI/CD

Este directorio contiene los workflows automatizados para el sistema StealtHub AI.

## 📋 Workflows Disponibles

### 1. 🔍 **Pull Request Checks** (`pr-checks.yml`)
**Se ejecuta en:** Pull requests a `main`

**Qué hace:**
- ✅ Verifica calidad del código con `flake8`
- ✅ Valida formato con `black` e `isort`
- ✅ Pruebas de importación de todos los módulos
- ✅ Escaneo de seguridad con `bandit` y `safety`
- ✅ Reporte automático en los PRs

### 2. 🚀 **CI/CD Completo** (`ci-cd-complete.yml`)
**Se ejecuta en:** Push a `main/develop` y releases

**Qué hace:**
- 🧪 Testing con múltiples versiones de Python (3.8-3.11)
- 🔨 Construcción de ejecutables con PyInstaller
- 📦 Creación de paquetes Python instalables
- 🛡️ Escaneo completo de seguridad
- 📚 Generación de documentación automática
- 🚀 Creación de releases con GitHub
- 📊 Reportes detallados de calidad

## 🚀 Cómo Funciona

### Para Pull Requests:
1. **Crea un PR** → Se ejecutan automáticamente los checks
2. **Revisa los resultados** → Verifica que todo pase
3. **Merge cuando esté listo** → Solo si todos los checks pasan

### Para Releases:
1. **Haz push a `main`** → Se ejecuta el pipeline completo
2. **Revisa los artifacts** → Se generan automáticamente
3. **Crea un release** → O usa el automático
4. **¡Listo!** → GitHub crea el release automáticamente

## 📦 Artifacts Generados

El pipeline genera automáticamente:

- **🤖 Ejecutables CLI**: `stealth_hub_cli`
- **🎮 Ejecutable Principal**: `stealth_hub_main`
- **📦 Paquete Python**: `.whl` y `.tar.gz`
- **🗂️ Release Completo**: `stealth_hub_ai_v2.0.0.zip`
- **📚 Documentación**: Sitio web con MkDocs
- **📊 Reportes**: Seguridad, testing, calidad

## 🛡️ Seguridad

El sistema incluye:
- **🔍 Bandit**: Análisis estático de seguridad
- **⚠️ Safety**: Verificación de vulnerabilidades
- **🔒 CodeQL**: Análisis avanzado de código
- **✅ Quality Gates**: Solo código validado pasa

## 📊 Status Badges

Añade estos badges a tu README:

```markdown
[![CI/CD Pipeline](https://github.com/xpe-hub/StealtHub/actions/workflows/ci-cd-complete.yml/badge.svg)](https://github.com/xpe-hub/StealtHub/actions)
[![Code Quality](https://github.com/xpe-hub/StealtHub/actions/workflows/pr-checks.yml/badge.svg)](https://github.com/xpe-hub/StealtHub/actions)
```

## 🔧 Configuración

### Variables de Entorno (Opcional)
Puedes configurar en GitHub Settings > Secrets:

- `DISCORD_BOT_TOKEN` - Para integración Discord
- `RELEASE_TOKEN` - Token personalizado para releases

### Configuración de Branches
- **`main`**: Producción - Se ejecuta CI/CD completo
- **`develop`**: Desarrollo - Se ejecuta testing
- **`feature/*`**: Features - Solo PR checks

## 📝 Checklist Pre-Deploy

Antes de hacer push a `main`, asegúrate de:

- [ ] ✅ Todos los tests pasan localmente
- [ ] ✅ El código sigue los estándares (`black`, `flake8`)
- [ ] ✅ No hay vulnerabilidades de seguridad
- [ ] ✅ Los imports funcionan correctamente
- [ ] ✅ Has actualizado la versión en los archivos

## 🆘 Troubleshooting

### Si falla el pipeline:

1. **Revisa los logs** en la pestaña Actions de GitHub
2. **Verifica las versiones** de Python en el workflow
3. **Comprueba las dependencias** en `requirements.txt`
4. **Testa localmente** antes de hacer push

### Problemas comunes:

- **Timeout**: Reduce la complejidad de los tests
- **ImportError**: Verifica que todas las dependencias estén en `requirements.txt`
- **Security scan fails**: Resuelve las vulnerabilidades encontradas

## 🎯 Próximos Pasos

1. **Activa los workflows** haciendo commit de estos archivos
2. **Configura las protecciones** de branch para `main`
3. **Añade los badges** al README
4. **Configura los secrets** si necesitas integraciones externas

## 📞 Soporte

Si necesitas ayuda con los workflows:
- 📧 **Email**: xpepaneles@gmail.com
- 💬 **Discord**: Community Stealth
- 🐛 **Issues**: Crea un issue en el repositorio

---

**🤖 Powered by StealtHub AI v2.0 | © 2025 xpe.nettt - Community Stealth**