# Studios.Bit Design — Creative Direction

**Skill independiente para Codex · versión 0.5 · 30 referencias (SB-01 a SB-30)**

Una biblioteca práctica de **dirección creativa, diseño UI/UX, motion design, storytelling, contenido y procesos digitales** de Studios.Bit para proyectos futuros de distintos clientes.

Cada cliente conserva su identidad, su manual de marca, sus objetivos y las condiciones aprobadas. Las referencias sirven para aprender técnicas y criterios, **no** para copiar proyectos de terceros.

## Qué incluye

- `SKILL.md`: reglas de dirección creativa reutilizables y flujo de trabajo en Codex.
- `references/REFERENCIAS.md`: referencias SB-01 a SB-10.
- `references/LOTE_2026-11-06_SB11_SB30.md`: referencias SB-11 a SB-30.
- `references/CONTENIDO_Y_FORMATOS.md`: guiones, estructura y edición para Reels, TikTok, Instagram y Facebook.
- `references/OPORTUNIDADES_SITIO.md`: backlog histórico de la propia web de Studios.Bit (no aplicable automáticamente a clientes).
- `references/CHANGELOG.md`: versiones y criterios de evolución.
- `AGENTS.example.md`: instrucciones opcionales para proyectos de clientes.
- `scripts/install.ps1` y `scripts/update.ps1`: automatización para Windows.

## Instalación global en Codex (Windows / PowerShell)

Abre PowerShell y ejecuta:

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
git clone https://github.com/patrickLOR1/studiosbit-design.git "$HOME/.agents/skills/studios-bit-creative-direction"
```

**La skill está en la raíz del repositorio** (`SKILL.md`), por lo que esa ruta permite que Codex la encuentre sin copiarla a cada proyecto. Si el repositorio ya está clonado, ejecuta:

```powershell
git -C "$HOME/.agents/skills/studios-bit-creative-direction" pull --ff-only
```

También puedes clonar el repositorio en una carpeta temporal y ejecutar `./scripts/install.ps1` desde la carpeta clonada.

**Uso en Codex:** solicita `$studios-bit-creative-direction` y describe el brief, los objetivos, la industria, los recursos disponibles y la marca del cliente. Reinicia una sesión de Codex si la skill no se reconoce inmediatamente.

## Instalación global en macOS / Linux

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/patrickLOR1/studiosbit-design.git ~/.agents/skills/studios-bit-creative-direction
# Para actualizar más adelante:
git -C ~/.agents/skills/studios-bit-creative-direction pull --ff-only
```

## Para un proyecto en particular

Si el proyecto necesita reglas contextuales propias, agrega al `AGENTS.md` del proyecto el bloque de `AGENTS.example.md`. La skill instalada globalmente no sustituye el brief, manual de marca ni los requisitos de ese proyecto.

## Agregar nuevas referencias

1. Usar el siguiente código consecutivo (**SB-31**, **SB-32**, etc.).
2. Registrar fuente, fecha, observación visual verificable y límites del análisis (audio verificado o no).
3. Analizar **dos planos**: diseño/interacción y narrativa/edición del contenido.
4. Proponer adaptación original para clientes, con alternativa de accesibilidad y rendimiento.
5. Actualizar `references/`, `SKILL.md` y `references/CHANGELOG.md`.
6. Hacer `git pull --ff-only` en cada máquina que tenga instalada la skill.

## Contenido de terceros y privacidad

**No se incluyen los 30 videos ni sus fotogramas originales en este repositorio público.** Solo se publica análisis textual transformativo. No subir imágenes, clips, datos privados, identidades de clientes, credenciales ni contenido sin permiso.

La habilidad ayuda a orientar el diseño; no constituye un modelo reentrenado ni garantiza resultados comerciales. Cualquier referencia visual y afirmación de terceros debe verificarse antes de aplicarse en un trabajo real.

**Estado:** documentación reusable; no realiza modificaciones automáticas al sitio web ni a las funciones comerciales de ningún cliente.
