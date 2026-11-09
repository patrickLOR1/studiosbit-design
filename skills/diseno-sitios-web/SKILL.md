---
name: studios-bit-diseno-sitios-web
description: Dirección y producción de landing pages, sitios corporativos, UI/UX, CMS, responsive y conversión basada en referencias SB de Studios.Bit, con identidad propia para cada cliente.
---

# Estudios web — Skill de diseño de sitios

**Ámbito:** brief → arquitectura de información → jerarquía, wireframes → UI → prototipo → desarrollo → QA. Esta skill es para nuevos proyectos, **no** autoriza editar la landing de Studios.Bit.

## Inicio
Pregunta qué vende el cliente, a quién, qué debe entenderse en tres segundos, cuál es la acción principal, qué contenidos/activos tiene y cómo mantendrá la web. Elegir stack según contexto, no por moda.

## Diseño
- Objetivo comercial y CTA primero; una promesa concreta por sección, textos legibles y evidencias reales.
- Dirección de arte por cliente: tipografía, contraste, colores, fotografía, estados y sistema de componentes propio.
- Hero editorial, bento, galería narrativa, escenas, scroll storytelling o 3D **solo si sirven al mensaje y están justificados**.
- Móvil no es una reducción del desktop: ordenar contenido, nav, objetivos táctiles y formularios por prioridad.
- Si el cliente necesita autogestión, proponer CMS con roles claros, campos simples, preview editorial, mantenimiento y capacitación. No prometer paneles avanzados sin construirlos.

## Nuevos patrones SB-36 / SB-38 / SB-39 / SB-40 / SB-41 (9-nov-2026)
- **SB-36, narrativa editorial:** seleccionar solo un recurso dominante (gran titular, 3D o tarjetas); orden de lectura y CTA antes del efecto; escenas reversibles y navegación disponible.
- **SB-38, CMS de autogestión:** definir campos editables, roles mínimos, permisos, preview, publicación, rollback y guía de uso; probar el flujo de cliente antes de ofrecerlo.
- **SB-39, dirección de arte:** entregar 2–3 territorios de composición, tipografía y color **originales**, contrastados contra el brief, no clonar visuales de terceros.
- **SB-40, experimentación responsable:** instrumentación con consentimiento, hipótesis y KPI, test A/B con asignación estable, guardrails, revisión humana y rollback; **no** activar personalización ni IA en producción sin autorización.
- **SB-41, recorridos de integración:** además de QA visual, probar los flujos completos UI → backend → DB y sus fallas; para CMS, login → editar → preview → publicar → comprobar y revertir.
- Para cada patrón, pedir evidencia: capturas en breakpoints, resultados de pruebas, incidencias y límites **verificados**, nunca inventados.
- Fichas: [SB-36 a SB-41](../../references/SB36_SB41.md).

## QA obligatoria
320, 390, 768, 1024 y 1440 px; teclado y foco, form validation, errores, menú, scroll/anclas, reduced-motion, rendimiento móvil LCP/CLS/INP cuando existan datos, SEO técnico, seguridad, TLS y rastreabilidad. Diferenciar emulación de dispositivo real.

## Entrega
Mapa de sitio, wireframe, componentes, propuesta visual, estados ES/EN cuando aplique, CTA y funnel, acceso/guía de CMS, pruebas y límites. Proyectos ficticios rotulados **Proyecto conceptual**.

## Catálogo
Consulta [índice general](../../references/INDICE_POR_CATEGORIA.md), [SB01–10](../../references/REFERENCIAS.md), [SB11–30](../../references/LOTE_2026-11-06_SB11_SB30.md) y [SB31–35](../../references/SB31_SB35.md). Prioriza SB-01,03,05,06,07,08,09,10,11,12,13,15,16,17,19,24,29,30,31,33,35.

### Activación con Codex
Cuando pidan "diseñar un sitio", devolver brief asumido, enfoque visual, secciones, patrones SB-xx, wireframe, decisiones de accesibilidad y ejecución comprobable. Jamás reutilizar literalmente el código/diseño del ejemplo.
