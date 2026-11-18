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

## Nuevas referencias SB-42 a SB-54 (18-nov-2026)
- **SB-43,46,48:** evitar diseño IA genérico; seleccionar inspiración por necesidades y verificar licencias de componentes externos.
- **SB-44:** no confundir prototipo animado con flujos reales; cubrir contenido, permisos, errores y estados vacíos.
- **SB-49:** gamificación opcional y honesta, solo para acciones de valor; no forzar rachas ni notificaciones.
- **SB-50:** adaptar el CTA a la intención; comparar formularios y alternativas accesibles antes de cambiar la captación.
- **SB-52:** en tienda, optimizar búsqueda, selección, carrito, IVA/envío y checkout, sin prometer conversiones.
- **SB-53:** video inmersivo con poster, controles, legibilidad, carga progresiva y alternativa inmóvil.
- Fichas completas: [SB-42 a SB-54](../../references/SB42_SB54.md); no copiar interfaces, métricas ni marcas ajenas.

## Refuerzo SB-55 a SB-61 (18-nov-2026)
- **SB-55:** auditoría anti-plantillas por escala, jerarquía, radios, densidad y CTA, con justificación específica para el cliente; no asumir que «menos tarjetas» siempre es mejor.
- **SB-56:** estados de botones, errores y acordeones con microfeedback contenido, sin bloquear controles ni sacrificar accesibilidad.
- **SB-57:** paleta semántica de roles (base, neutro, acento), contrastes y estados; identidad exclusiva del brief.
- **SB-58:** dashboards con unidades, período, fuente y estados de datos, sin números ficticios confundidos con telemetría real.
- **SB-61:** prompts de visualización solo como brief creativo; prototipo funcional y QA siguen siendo obligatorios.
- Fichas: [SB-55 a SB-61](../../references/SB55_SB61.md).

## QA obligatoria
320, 390, 768, 1024 y 1440 px; teclado y foco, form validation, errores, menú, scroll/anclas, reduced-motion, rendimiento móvil LCP/CLS/INP cuando existan datos, SEO técnico, seguridad, TLS y rastreabilidad. Diferenciar emulación de dispositivo real.

## Entrega
Mapa de sitio, wireframe, componentes, propuesta visual, estados ES/EN cuando aplique, CTA y funnel, acceso/guía de CMS, pruebas y límites. Proyectos ficticios rotulados **Proyecto conceptual**.

## Catálogo
Consulta [índice general](../../references/INDICE_POR_CATEGORIA.md), [SB01–10](../../references/REFERENCIAS.md), [SB11–30](../../references/LOTE_2026-11-06_SB11_SB30.md) y [SB31–35](../../references/SB31_SB35.md), [SB36–41](../../references/SB36_SB41.md) y [SB42–54](../../references/SB42_SB54.md) y [SB55–61](../../references/SB55_SB61.md). Prioriza SB-01,03,05,06,07,08,09,10,11,12,13,15,16,17,19,24,29,30,31,33,35.

### Activación con Codex
Cuando pidan "diseñar un sitio", devolver brief asumido, enfoque visual, secciones, patrones SB-xx, wireframe, decisiones de accesibilidad y ejecución comprobable. Jamás reutilizar literalmente el código/diseño del ejemplo.
