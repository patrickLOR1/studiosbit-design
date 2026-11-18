# Ingeniería backend y APIs confiables — guía para Codex

**Revisado: 2026-11-18.** Elecciones tecnológicas específicas requieren verificar versiones de framework/runtime y documentación del proveedor al implementar.

## Fuentes primarias
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — métodos, códigos, caché e idempotencia.
- [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) — esquema común para errores de API.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — documentación y contrato HTTP; **v3.2.1 a 2026-11-18**, verificar al aplicar.
- [AWS Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — problemas de reenvío y claves explícitas.
- [AWS Builders' Library: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — estrategias para fallos transitorios.
- [OpenTelemetry — Signals](https://opentelemetry.io/docs/concepts/signals/) — logs, métricas y trazas.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — SLI/SLO y metas centradas en la experiencia del usuario.
- [The Twelve-Factor App](https://12factor.net/) — configuración externa y procesos según entorno.

## 1. Diseño por capacidades y límites
- Enumerar operaciones, reglas de negocio, fuentes de verdad, actores, dependencias externas, criticidad y presupuesto operativo.
- Empezar por **monolito modular** cuando basta. Separar rutas/controladores, casos de uso/reglas, adaptadores de datos, integraciones y configuración; crear servicios/colas solo si objetivos medidos lo justifican.
- Compartir contratos públicos tipados cuando el stack lo permita, pero **validar entrada en ejecución**: tipos TypeScript no protegen tráfico de red.
- Versionar APIs cuando los consumidores lo requieran; política de compatibilidad y deprecación, paginación con orden estable y límites, timestamps UTC con zona explícita en presentación.

## 2. Contratos HTTP y seguridad
- Definir entrada/salida, validación, autenticación, autorización **por recurso y tenant**, códigos coherentes, paginación, límites, manejo de conflictos y errores sin filtrar internals.
- Usar semántica HTTP real: GET sin efectos solicitados; POST no se asume idempotente; PUT/DELETE idempotentes en efecto solicitado. Para operaciones POST sensibles, clave de idempotencia con alcance, expiración y detección de parámetros divergentes.
- Documentar errores con RFC 9457 si resulta adecuado; nunca exponer trazas, SQL, secretos o detalles internos en respuesta.
- Throttling, límites de payload, timeouts, backpressure, permisos mínimos, firma de webhooks y validación del contenido recibido.

## 3. Fallos y ejecución distribuida
- Definir timeout **por dependencia** y deadline de la operación total. Reintentos solo en errores clasificados transitorios y operaciones seguras para reintento, con límite de intentos y backoff con jitter.
- Evitar tormentas de reintentos en varias capas. Cuando el cliente no sabe si una escritura se aplicó, usar idempotencia/consulta de estado, nunca repetir ciegamente.
- Para jobs: entrega «al menos una vez» cuando aplique → consumidor idempotente, reintentos limitados, cola de fallos, alertas, trazabilidad y re-proceso seguro. No prometer exactly-once mágico.
- Para eventos en tiempo real: tolerar duplicados, orden parcial, desconexiones y backfill; diferenciar timestamp de adquisición, recepción y procesado.
- Diseñar degradación elegante cuando falla correo/CRM/analítica: no perder transacción principal si la dependencia no es esencial.

## 4. Observabilidad y escala
- Mínimo: logs estructurados redactados con correlación ID, métricas de throughput, errores, p50/p95/p99, dependencias, cola/saturación y trazas de rutas críticas. Evitar datos privados y alta cardinalidad accidental.
- Definir 1–3 SLI útiles (ej. tasa de éxito del formulario, latencia p95 de lectura, frescura de telemetría) y **objetivos propuestos** que se ajusten con medición, coste y riesgo; no inventar uptime garantizado.
- Diferenciar escalado por concurrencia, CPU, I/O, latencia DB, bloqueo, proveedor, volumen y costes. Medir cuello de botella primero, luego cache/pool/cola/índice según evidencia.
- Entornos aislados, migración gradual, health checks adecuados, rollback de código y compatibilidad con migraciones, backups + restore, runbook y alertas.

## 5. Gate de pruebas backend
| Ámbito | Evidencia |
|---|---|
| Contrato | OpenAPI/esquemas validados, respuestas y errores reales |
| Identidad | 401/403, roles/tenants, objetos ajenos, rate limits |
| Integridad | Doble POST, reintentos, concurrencia, límites transaccionales |
| Fallos | Timeout DB, proveedor 5xx, webhook duplicado, caída temporal |
| Operación | Logs correlacionados sin secretos, métricas, health y alertas |
| Escala | Prueba de carga proporcional con entorno/volumen descritos, p95/errores/saturación |
| Entrega | CI, pruebas unit/integración/E2E y procedimiento seguro de rollback |

**No equivale a una garantía:** no asegurar cero errores, escalabilidad ilimitada ni uso correcto de un proveedor sin testarlo. Para servicios que controlan hardware/OT, lectura por defecto y revisión específica antes de escribir.
