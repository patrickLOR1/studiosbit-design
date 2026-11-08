---
name: studios-bit-motion-interacciones
description: Diseño e implementación de motion web, microinteracciones, navegación animada, scroll storytelling y transiciones con enfoque en propósito, accesibilidad y rendimiento.
---

# Motion e interacciones

## Principios
Usa animación para orientar, explicar o dar feedback; evita motion decorativo sin razón. Define disparador, duración, easing, interrupciones, sentido inverso, estados de foco, tactilidad, hover, reduced-motion, impacto JS y fallback sin JavaScript.

## Patrones
- Navegación con indicador suave, cápsula y expansión: debe conservar hit targets y foco.
- Glow y partículas: cursor opcional solo donde tiene sentido; no impedir interacción.
- Escenas de scroll: un único controlador para anclas; no scroll-jacking ni retrasos artificiales.
- Tipografía cinética: mantener legibilidad y accesibilidad.
- Continuidad espacial: contextualizar dónde va el usuario; no sacrificar performance por 3D.
- Microfeedback: controles, sliders, CTA, pasos de cotizador y estados de error.

## Implementación
Preferir CSS transform y opacity; considerar GSAP/ScrollTrigger y Lenis solo cuando la complejidad lo justifique, sincronizando refresh y cleanup. Hacer lazy initialization y pausar trabajo fuera de viewport; medir TBT/INP, CLS y long tasks. Móvil y reduced-motion no son opcionales.

## Catálogo
[Índice](../../references/INDICE_POR_CATEGORIA.md). Patrones prioritarios: SB-01,03,05,06,07,09,10,12,14,18,19,20,24,26,28,31,32,34.

**Interacción segura:** no convertir efectos mostrados por terceros en componentes clonados; construir demostraciones originales y accesibles, con tests.
