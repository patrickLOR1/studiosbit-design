---
name: studios-bit-backend-ingenieria
description: Diseñar e implementar backend mantenible, APIs, flujos transaccionales, webhooks, colas, observabilidad, fiabilidad y crecimiento de aplicaciones web de Studios.Bit y clientes. Activar si hay servidor, persistencia, autenticación, integraciones o carga concurrente; no exigir backend en landing estática.
---

# Backend y APIs confiables

**Objetivo:** contratos claros, reglas de negocio aisladas, escalado guiado por métricas y errores recuperables; no prometer disponibilidad absoluta.

## Procedimiento
1. **Capacidades y fronteras:** actores, operaciones, dependencias, datos sensibles, objetivos de latencia/tráfico, presupuesto, mantenimiento y contratos. Arquitectura más simple que cubra el caso (evaluar monolito modular antes de microservicios).
2. **Contrato de API:** entradas y salidas validadas en ejecución, permisos server-side por recurso, HTTP semántico (RFC 9110), errores estructurados (RFC 9457 si aplica), esquemas OpenAPI y límites/paginación.
3. **Escrituras seguras:** transacciones y claves de idempotencia donde haya reintentos o doble POST; webhooks verificados; no enviar confirmación antes de commit real.
4. **Fallos:** deadlines/timeout por dependencia, reintentos limitados únicamente si seguros, backoff/jitter, circuitos o colas cuando se justifiquen, manejo explícito de proveedores no disponibles.
5. **Observabilidad:** logs estructurados redactados + correlation IDs, métricas, trazas según escala, SLI/SLO propuestos y alertas útiles. No registrar tokens ni PII sin necesidad.
6. **Pruebas:** contrato, autorización negativa, concurrencia, duplicados, timeout/red, E2E, carga representativa con p95 y errores; health/rollback en entornos aislados.

## Lectura técnica
[Guía de backend con RFC, OpenAPI, AWS Builders' Library, OpenTelemetry y Google SRE](../../references/INGENIERIA_BACKEND.md). Si hay persistencia, activar [bases de datos](../bases-de-datos/SKILL.md); para amenazas [ciberseguridad](../ciberseguridad-web/SKILL.md).

## Entrega
Mapa de endpoints y responsabilidades, contratos/errores, matríz de roles, tests ejecutados, métricas observadas, fallas posibles, ADR de decisiones no reversibles y pasos de despliegue/rollback **sin ejecutar producción por iniciativa propia**.
