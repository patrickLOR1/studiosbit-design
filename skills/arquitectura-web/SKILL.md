---
name: studios-bit-arquitectura-web
description: Planear y revisar la arquitectura de nuevos sitios web, landing pages, CMS, ecommerce, dashboards y aplicaciones web en Codex. Activar al crear un nuevo proyecto, escoger stack, rutas, renderizado, backend, APIs, datos, seguridad, rendimiento, despliegue o mantenimiento. Aplicar con la skill de diseño web y las reglas de literatura.
---

# Arquitectura web para proyectos de Studios.Bit y clientes

**Misión:** Convertir el brief en una estructura web proporcionada, mantenible, accesible, segura y verificable **antes de improvisar componentes o servicios**. No modificar sitios existentes, precios ni despliegues sin autorización.

## Flujo obligatorio al iniciar un proyecto

1. **Descubrimiento.** Identificar audiencia, problema, tareas críticas, marca, contenido, idiomas, responsables de edición, datos, integraciones, plazos, presupuesto, proveedores y permisos. Listar incertidumbres sin inventar decisiones.
2. **Clasificación.** Determinar si es landing estática, sitio editorial/CMS, herramienta transaccional o aplicación con cuentas/datos. Justificar la arquitectura **más sencilla que cubra requisitos y riesgos**; evitar framework, DB, IA o microservicios por costumbre.
3. **Mapa de experiencia.** Crear sitemap y rutas, flujos de navegación, CTA, recuperación de errores, estructura de contenido, SEO, idiomas y estados vacíos. Aplicar [fundamentos de diseño con fuentes](../../references/FUNDAMENTOS_DISENO_LITERATURA.md).
4. **Diseño técnico.** Delimitar frontend, renderizado, lógica de negocio, API, persistencia e integraciones; trazar límites de confianza y responsabilidades. Para aplicaciones con servicios/datos, elaborar C4 contexto y contenedores o equivalente conciso.
5. **Calidad desde el inicio.** Elegir requisitos comprobables para accesibilidad, rendimiento, seguridad, privacidad, SEO, confiabilidad, coste y edición. Si no existen datos reales de uso, declarar objetivos iniciales y cómo se medirán.
6. **Decisión técnica.** Comparar al menos dos alternativas pertinentes en decisiones grandes; documentar ADR corto con trade-offs, dueño, riesgos, prueba y rollback.
7. **Implementación controlada.** Construir módulos pequeños que encapsulen cambios, validación del lado servidor para entradas persistentes, roles por recurso, secrets externos, estados de error y pruebas por flujo. Mantener prototipos/datos falsos marcados como tales.
8. **Verificación y entrega.** Probar recorrido completo en móvil/desktop, teclados, zoom, accesibilidad manual y automatizada, unit/integración/E2E cuando aplique, fallos de red, permisos, SEO, rendimiento y reversión. No declarar «listo para producción» sin evidencias.

## Activación de ingeniería especializada (según alcance)

- **Seguridad:** [skill ciberseguridad](../ciberseguridad-web/SKILL.md) + [guía OWASP/NIST](../../references/INGENIERIA_CIBERSEGURIDAD.md) si existe superficie web, datos, usuarios o terceros. Modelo de amenazas, matriz permisos, pruebas negativas, protección de secretos.
- **Frontend:** [skill frontend](../frontend-ingenieria/SKILL.md) + [guía W3C/Core Web Vitals](../../references/INGENIERIA_FRONTEND.md) si se implementa UI. Medir y probar rutas, estados, accesibilidad y performance.
- **Backend:** [skill backend](../backend-ingenieria/SKILL.md) + [guía RFC/OpenAPI/SRE](../../references/INGENIERIA_BACKEND.md) si hay servidor, API, webhook o tareas. Contratos, autenticación/autorización, reintentos seguros, observabilidad.
- **Bases de datos:** [skill bases de datos](../bases-de-datos/SKILL.md) + [guía PostgreSQL/concurrencia/PITR](../../references/INGENIERIA_BASES_DATOS.md) si hay persistencia. Esquema, índices basados en consultas, migraciones, aislamiento y pruebas de restore.

No aplicar mecánicamente todas las capas: una landing simple puede prescindir de backend y BD. En un SaaS con usuarios y persistencia sí se requieren los cuatro análisis. No hay escalabilidad ni ausencia de vulnerabilidades garantizadas por plantillas.

## Gate mínimo de arquitectura (presentar antes de codificar)

| Pregunta | Salida mínima |
|---|---|
| ¿Quién usa qué? | Dos o tres tareas prioritarias y actor responsable |
| ¿Dónde vive cada función? | Mapa de rutas + frontend/backend/terceros |
| ¿Hay datos? | Modelo mínimo, fuente de verdad y límites de acceso |
| ¿Qué depende de JS o red? | Estrategia de renderizado y fallback |
| ¿Qué puede fallar? | Estados de error, reintentos y no duplicación |
| ¿Cómo se actualiza y opera? | CMS o flujo de cambios, entornos, backups si procede |
| ¿Cómo se comprobará? | Pruebas y evidencia asociadas a cada riesgo |

### Casos especiales
- **Landing simple:** priorizar HTML legible, contenido publicado, enlaces y CTA; es válido **no tener backend ni DB**.
- **Sitio editable:** justificar si necesita CMS, qué edita cada rol, preview/publicación y coste de mantenimiento.
- **Formularios y cotizadores:** validar en servidor, diseñar idempotencia/doble envío y confirmación real antes de mostrar éxito.
- **Dashboard y telemetría:** modelar unidades, timestamps, calidad/frescura de datos, fuente real vs simulada, permisos, fallos de conexión y recuperación. No habilitar control de equipos sin autorización expresa.
- **Integraciones con terceros:** declarar permisos, cuotas, fallos, facturación y quién mantiene la dependencia.

## Referencias de consulta

- **Siempre al crear o reestructurar web:** [guía de arquitectura y bibliografía](../../references/ARQUITECTURA_WEB_GUIA.md).
- **Siempre al diseñar experiencias:** [fundamentos de diseño/UX](../../references/FUNDAMENTOS_DISENO_LITERATURA.md).
- **Para patrones visuales, solo cuando aporten:** [índice SB](../../references/INDICE_POR_CATEGORIA.md), sin copiar medios de terceros.
- **Para UI y conversión:** [skill de diseño de sitios](../diseno-sitios-web/SKILL.md).
- **Para motion:** [skill de interacciones](../motion-interacciones/SKILL.md).

## Entregables Codex

**Antes de construir:** diagnóstico, tipo de web, sitemap/flujo, propuesta visual, arquitectura mínima, matriz de datos/integraciones, requisitos de calidad, ADR de decisiones importantes y riesgos. Para sitios pequeños, una página es suficiente.

**Después de construir (si el usuario autoriza desarrollo):** archivos y rutas implementados, pruebas reproducibles con resultados, capturas/mediciones reales, decisiones y limitaciones, pasos de mantenimiento y propuesta de despliegue (no despliegue automático).

**Regla de evidencia:** una heurística de Nielsen o un libro no es una certificación; WCAG/estándares exigen verificación; un mockup no prueba un backend; un video de referencia SB no demuestra resultados de terceros.

## Complemento v1.1 — calidad operativa y evidencia

Usar [método de dirección](../../references/METODO_STUDIOSBIT.md) y [literatura primaria](../../references/LITERATURA_PROFUNDA_2026.md) para dimensionar decisiones; [arquitectura operativa](../../references/ESCALABILIDAD_OPERACION.md) para límites, SLO, contingencias, costos y datos; [BitProof](../bitproof-qa/SKILL.md) para gates según riesgo. Coordinar desde [director-proyecto](../director-proyecto/SKILL.md); no trasladar automáticamente complejidad de un SaaS a una landing estática.
