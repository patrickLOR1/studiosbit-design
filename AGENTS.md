# Instrucciones para Codex — studiosbit-design

Este repositorio es una biblioteca de **conocimiento y skills**, no el sitio productivo de Studios.Bit.

Al recibir un brief, escoge la(s) skill(s) pertinente(s):
- Arquitectura y decisiones transversales: `skills/arquitectura-web/SKILL.md`.
- Ciberseguridad, datos sensibles, acceso, sesiones, secretos y dependencias: `skills/ciberseguridad-web/SKILL.md`.
- Frontend, semántica, estado, rendimiento, responsive y accesibilidad: `skills/frontend-ingenieria/SKILL.md`.
- Backend, contratos API, reintentos, integraciones y observabilidad: `skills/backend-ingenieria/SKILL.md`.
- Bases de datos, migraciones, concurrencia, índices y restauración: `skills/bases-de-datos/SKILL.md`.
- Sitios y UX: `skills/diseno-sitios-web/SKILL.md`.
- Producción y edición audiovisual: `skills/diseno-videos/SKILL.md`.
- Microinteracciones, animación y performance: `skills/motion-interacciones/SKILL.md`.
- Logotipo, identidad y sistemas visuales: `skills/identidad-visual/SKILL.md`.
- Marketing, formatos, distribución y autoridad: `skills/estrategia-contenido/SKILL.md`.

**Regla de inicio para cualquier nuevo proyecto web:** antes de escribir código, usar la skill de arquitectura web y la de diseño de sitios, leer [fundamentos y literatura](references/FUNDAMENTOS_DISENO_LITERATURA.md) y [guía de arquitectura](references/ARQUITECTURA_WEB_GUIA.md), y entregar brief, sitemap, arquitectura proporcional y criterios de aceptación. **Activar además las cuatro skills de ingeniería por componente/riesgo aplicable**: frontend siempre que se programe UI, ciberseguridad si hay superficie web o datos, backend si existe lógica de servidor, bases de datos si hay persistencia. No crear backend/DB para una landing estática por cumplir una plantilla. Consultar [seguridad](references/INGENIERIA_CIBERSEGURIDAD.md), [frontend](references/INGENIERIA_FRONTEND.md), [backend](references/INGENIERIA_BACKEND.md) y [bases de datos](references/INGENIERIA_BASES_DATOS.md) según el sistema. Diferenciar normas verificables (WCAG), heurísticas de autor y ejemplos SB. No copiar una arquitectura de otro cliente ni instalar servicios sin necesidad.

Lee solo las referencias necesarias por problema en `references/INDICE_POR_CATEGORIA.md`. Selecciona hasta 2 patrones SB principales y propón una aplicación **original** con criterios de QA.

- Las referencias son de terceros; nunca atribuyas sus resultados, clientes, código o imágenes a Studios.Bit.
- Al producir trabajo para un cliente, respeta su marca, contrato, accesibilidad, presupuesto y aprobación.
- Los proyectos nuevos deben separar hechos, hipótesis y decisiones; justificar stack, datos, permisos, calidad, coste y QA.
- Exigir gates por riesgo: permiso horizontal/vertical y secretos; UI con teclado/errores y medición; APIs con idempotencia, timeout y observabilidad; DB con constraints, migraciones y restauración ensayada.
- Diferenciar fuentes normativas (RFC/WCAG), guías y propuestas; verificar versiones antes de cada implementación. **No hay arquitectura sin fallos garantizada**. Un prototipo animado no demuestra funcionalidad.
- No cambiar el repositorio `Studios.Bit` (landing) ni ejecutar despliegues a menos que el usuario los solicite expresamente.
- Menciona qué se verificó y qué queda como propuesta. No inventes datos.
