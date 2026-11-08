# Uso de las skills independientes en Codex

## Repositorio y selección
La biblioteca se mantiene en `https://github.com/patrickLOR1/studiosbit-design`.
Las skills están separadas en `skills/<nombre>/SKILL.md`; la existencia del repositorio **no** significa que Codex las descubra en todos los proyectos automáticamente.

## Instalación por proyecto
En el repositorio del cliente (o de la agencia) crea `.agents/skills/` y copia allí **solo las carpetas de las skills necesarias**, conservando el archivo `SKILL.md` de cada una.

**Importante:** cada skill enlaza a las fichas compartidas bajo `../../references/`. Cuando copies skills fuera de esta biblioteca, copia también la carpeta `references/` al mismo nivel que `skills/`, o cambia los enlaces hacia la versión instalada. No dejes referencias rotas.

Ejemplo PowerShell desde la carpeta del proyecto, con la biblioteca descargada en una carpeta local:

```powershell
New-Item -ItemType Directory -Force .agents/skills | Out-Null
Copy-Item -Recurse -Force ../studiosbit-design/skills/* .agents/skills/
Copy-Item -Recurse -Force ../studiosbit-design/references .agents/references
```

En este ejemplo las rutas internas de las skills apuntan a `.agents/references`, porque cada `SKILL.md` vive dos niveles por debajo de `.agents`. En proyectos con otra disposición, ajusta las rutas.

Añade en el AGENTS.md del proyecto:
```md
Para dirección creativa usa .agents/skills/diseno-sitios-web/SKILL.md (web),
.agents/skills/diseno-videos/SKILL.md (audiovisual), o la skill correspondiente.
Respetar siempre el brief y la marca del cliente. No copiar obras de referencia.
```

## Método
1. Leer brief y restricciones.
2. Elegir una skill por entregable principal y como máximo otra complementaria.
3. Consultar índice y fichas SB pertinentes.
4. Presentar dirección y guion/prototipo, con justificación y riesgos.
5. Implementar dentro del proyecto del cliente tras autorización.
6. Pasar QA; entregar evidencias y enlaces verificables.

## Material audiovisual privado
Los MP4 compartidos están **fuera** del repositorio público. Para analizar un fragmento que no esté disponible localmente, pedirlo al dueño o usar la ficha descriptiva, sin suponer detalles de audio o métricas.
