# Uso de las skills en Codex y Claude Code

## Repositorio y selección
La biblioteca se mantiene en `https://github.com/patrickLOR1/studiosbit-design`.
Cada skill vive en `skills/studios-bit-<disciplina>/SKILL.md`. El nombre de la carpeta **coincide** con el campo `name` del `SKILL.md`; no lo cambies o el agente no la reconocerá.

| Carpeta | Para qué |
|---|---|
| `studios-bit-diseno-sitios-web` | Landings, sitios, UI/UX, prototipos |
| `studios-bit-diseno-videos` | Reels, TikTok, Shorts, render y QA |
| `studios-bit-motion-interacciones` | Animación web y microinteracciones |
| `studios-bit-identidad-visual` | Logo, paleta, tipografía, dirección de arte |
| `studios-bit-estrategia-contenido` | Plan editorial, copy y captación |

Que el repositorio exista **no** hace que los agentes descubran las skills en otros proyectos: hay que instalarlas en cada proyecto (o una vez a nivel usuario).

## Trabajar dentro de esta biblioteca
- **Codex** lee `AGENTS.md` automáticamente.
- **Claude Code** lee `CLAUDE.md`, que a su vez importa `AGENTS.md`. Ambos siguen las mismas reglas.

## Instalar en otro proyecto

Las skills enlazan a las fichas con rutas `../../references/`. Por eso, junto a la carpeta de skills hay que copiar `references/` **al mismo nivel**:

```
<proyecto>/
  .agents/            (Codex)          .claude/            (Claude Code)
    skills/                              skills/
      studios-bit-diseno-videos/           studios-bit-diseno-videos/
        SKILL.md                             SKILL.md
    references/                          references/
```

### Codex (PowerShell, desde la carpeta del proyecto)
```powershell
New-Item -ItemType Directory -Force .agents/skills | Out-Null
Copy-Item -Recurse -Force ../studiosbit-design/skills/* .agents/skills/
Copy-Item -Recurse -Force ../studiosbit-design/references .agents/references
```

### Claude Code (PowerShell, desde la carpeta del proyecto)
```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse -Force ../studiosbit-design/skills/* .claude/skills/
Copy-Item -Recurse -Force ../studiosbit-design/references .claude/references
```

Para tenerlas en **todos** tus proyectos de Claude Code, copia lo mismo en `~/.claude/skills/` y `~/.claude/references/`.

Copia solo las skills que el proyecto necesite. Si usas otra disposición de carpetas, ajusta los enlaces `../../references/`; no dejes referencias rotas.

### Instrucción para el AGENTS.md / CLAUDE.md del proyecto
```md
Para dirección creativa usa la skill studios-bit-diseno-sitios-web (web),
studios-bit-diseno-videos (audiovisual) o la que corresponda.
Respetar siempre el brief y la marca del cliente. No copiar obras de referencia.
```

## Kit de logos de Studios.Bit
El kit `StudiosBit_Kit_Logos` (PNG/SVG) se comparte entre socios y **no** está en este repositorio público. Para producir piezas de la agencia, colócalo en `brand/StudiosBit_Kit_Logos/` de tu copia local (la carpeta `brand/` está en `.gitignore`). La skill de videos indica qué archivo usar según el fondo.

## Método
1. Leer brief y restricciones.
2. Elegir una skill por entregable principal y como máximo otra complementaria.
3. Consultar índice y fichas SB pertinentes.
4. Presentar dirección y guion/prototipo, con justificación y riesgos.
5. Implementar dentro del proyecto del cliente tras autorización.
6. Pasar QA; entregar evidencias y enlaces verificables.

## Actualizar las skills instaladas
Cuando cambie la biblioteca, vuelve a ejecutar los comandos de copia. Revisa `references/CHANGELOG.md` para saber qué cambió.

## Material audiovisual privado
Los MP4 y fotogramas de referencia están **fuera** del repositorio público. Para analizar un fragmento que no esté disponible localmente, pedirlo al dueño o usar la ficha descriptiva, sin suponer detalles de audio o métricas.
