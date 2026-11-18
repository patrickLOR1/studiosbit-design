# Uso de las skills independientes en Codex

## Repositorio y selección
La biblioteca se mantiene en `https://github.com/patrickLOR1/studiosbit-design`.
Las skills están separadas en `skills/<nombre>/SKILL.md`; la existencia del repositorio **no** significa que Codex las descubra en todos los proyectos automáticamente.

## Inicio recomendado v1.1

Para un proyecto nuevo empezar por **director-proyecto**, **arquitectura-web**, **diseno-sitios-web** y **bitproof-qa**; sumar frontend/seguridad según superficie y backend/BD solo cuando existan. Consultar [método](../references/METODO_STUDIOSBIT.md), [literatura](../references/LITERATURA_PROFUNDA_2026.md), [gates](../references/BITPROOF_GATES.md), [video](../references/VIDEO_INTERACCION_SIGNATURE.md) y [entrega CMS](../references/CMS_HANDOFF.md) por pertinencia.

**Instalador seguro** (ejecutar desde la biblioteca; primero vista previa, luego copiar):

    python3 scripts/bootstrap_codex.py --list
    python3 scripts/bootstrap_codex.py --target /ruta/al/proyecto --dry-run
    python3 scripts/bootstrap_codex.py --target /ruta/al/proyecto

El instalador **no sobreescribe** carpetas existentes, copia las referencias y plantillas necesarias para mantener los enlaces relativos y no crea/despliega apps. Si ya existe .agents/references, parar y conciliar manualmente versiones. Para instalar solo habilidades de video/branding:

    python3 scripts/bootstrap_codex.py --target /ruta/al/proyecto --skills director-proyecto diseno-videos identidad-visual

Después, añadir el enrutamiento al AGENTS.md del proyecto. No asumir que Codex descubre habilidades fuera de rutas configuradas. La identidad y el brief son distintos por cliente.

## Selección inicial para proyectos nuevos
- Si el trabajo es **web** (landing, CMS, cotizador, dashboard o aplicación), cargar **director de proyecto + arquitectura web + diseño de sitios + BitProof** antes de codificar.
- Al implementar UI, cargar **frontend**; al manejar usuarios, integraciones o datos, cargar **ciberseguridad**; si hay endpoints o jobs, **backend**; si existe almacenamiento persistente, **bases de datos**. Una landing estática no necesita backend/DB artificiales.
- Consultar los cuatro manuales de `references/INGENIERIA_*.md`, según lo que realmente exista, y exigir gates específicos (acceso, rendimiento, contratos, migraciones/restore).
- Leer referencias/FUNDAMENTOS_DISENO_LITERATURA.md y references/ARQUITECTURA_WEB_GUIA.md; escoger estándares y criterios adecuados al contexto.
- Para tareas exclusivamente de video, branding o redes, usar la skill respectiva sin exigir un proyecto de arquitectura.

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
Para proyectos web nuevos, activar juntas .agents/skills/arquitectura-web/SKILL.md
 y .agents/skills/diseno-sitios-web/SKILL.md. Antes de implementar, leer
 .agents/references/FUNDAMENTOS_DISENO_LITERATURA.md y
 .agents/references/ARQUITECTURA_WEB_GUIA.md, y presentar sitemap, arquitectura
 proporcional, datos e integraciones, seguridad, requisitos y plan de QA.
 Activar frontend-ingenieria para UI, ciberseguridad-web si hay superficie web
 y datos, backend-ingenieria para servidores y bases-de-datos para persistencia.
 Consultar .agents/references/INGENIERIA_*.md según el caso; no inventar servicios.
 Para video/branding usar la skill pertinente. Respetar el brief y la marca.
 No copiar obras ni desplegar sin permiso.
```

## Método
1. Leer brief y restricciones.
2. Elegir una skill principal y otras técnicas pertinentes por componente/riesgo; el límite de una complementaria aplica a referencias creativas, no omite seguridad ni QA.
3. Consultar índice y fichas SB pertinentes.
4. Presentar dirección y guion/prototipo, con justificación y riesgos.
5. Implementar dentro del proyecto del cliente tras autorización.
6. Pasar QA; entregar evidencias y enlaces verificables.

## Material audiovisual privado
Los MP4 compartidos están **fuera** del repositorio público. Para analizar un fragmento que no esté disponible localmente, pedirlo al dueño o usar la ficha descriptiva, sin suponer detalles de audio o métricas.
