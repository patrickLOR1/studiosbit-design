# Ingeniería para crecer sin deuda innecesaria — arquitectura, seguridad, backend, datos y operación

**Tesis:** escalabilidad es la capacidad **medida** de cumplir requisitos ante crecimiento y fallos previsibles dentro de límites económicos y operativos. No existe arquitectura «sin problemas». La mejor decisión para los primeros clientes suele ser modularidad, proveedores manejables y una salida clara, no microservicios.

## Índice
1. Objetivos de calidad y presupuesto
2. Topologías por tamaño
3. Seguridad y confianza
4. Backend/operación
5. Base de datos
6. Calidad de despliegue
7. Evolución por umbrales

## 1. Antes del stack: requisitos medibles

Registrar al menos:

- **Carga:** usuarios concurrentes aproximados, lecturas/escrituras por minuto, volumen de datos/medios, picos de campaña, región de audiencia. Si son estimaciones, marcarlas como tales.
- **Tareas:** latencia aceptable para búsqueda, checkout, formulario, CMS; límites de red y offline.
- **Fiabilidad:** qué error se permite, SLI/SLO contextual, ventanas de soporte, propietarios de alerta, `RPO` (pérdida tolerable) y `RTO` (tiempo tolerable de recuperación).
- **Privacidad:** datos personales, residencia, retención, acceso del cliente, consentimiento y borrado según jurisdicción.
- **Costo:** hosting, transferencias, emails, almacenamiento, API, dominios, backups, mantenimiento y excedentes. Estimar presupuesto mensual/base/pico, sin prometer precio estático de proveedores.
- **Operación:** quién despliega, investiga incidentes, responde clientes y renueva servicios. Sin responsable, la tecnología sofisticada aumenta riesgo.

Anotar cada decisión en [ADR](../templates/ADR.md) cuando haya una alternativa material. Fuente: [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html) y [Google SRE SLO](https://sre.google/sre-book/service-level-objectives/).

## 2. Arquitectura recomendada por evolución, no por moda

| Escenario | Inicio probable | Evolución con señal real |
|---|---|---|
| Landing pública | Generación estática, CDN, imágenes optimizadas; formulario mediante servicio aprobado | CMS solo si el dueño necesita editar con frecuencia |
| Sitio editorial | Estático/SSR + CMS con roles/preview y caché | Separar publicación de edición cuando permisos/volumen lo exijan |
| CRM/cotizador/prospectos | Monolito modular + API validada + BD administrada | Cola para email/reintentos, control de duplicados y observabilidad cuando el flujo lo necesite |
| SaaS / dashboard | Monolito modular, autenticar/autorización por objeto, transacciones, caché medida | Asíncrono/particionado/servicios específicos solo tras evidencia de límite |
| Telemetría industrial | Ingesta de lectura con tiempo/unidad/calidad y buffer, canal segregado | Streaming/almacenamiento especializado si frecuencia/retención lo justifican |

**Por qué monolito modular primero:** menos superficies de despliegue, trazabilidad y transacciones simples; aislamiento por dominio todavía permite extraer servicios si un requisito lo obliga. No mezclar capa visual con reglas de negocio, ni SQL de cada componente.

### Fronteras a dibujar

`Cliente → navegador/UI → API/servicio autorizado → BD/almacenamiento → proveedor externo`.

Marcar en cada salto: identidad, validación, cifra, permisos, timeouts, idempotencia, ownership de datos y logs. C4 contexto y contenedores bastan para muchos proyectos; no dibujar doce diagramas triviales.

## 3. Seguridad desde el diseño y cadena de suministro

**Marco actual verificado:** [OWASP Top 10:2025](https://top10.owasp.org/2025/), [ASVS 5.0.0](https://asvs.owasp.org/), [OWASP API Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/), [NIST SSDF 1.1 final](https://csrc.nist.gov/pubs/sp/800/218/final) y [NIST 800-63B-4 final](https://csrc.nist.gov/pubs/sp/800/63/B/4/final) para contexto de autenticación. `SSDF 1.2` sigue en borrador según revisión, no citarlo como norma final.

- Trazar matriz **actor × recurso × acción × tenant**. Autenticación no sustituye autorización. Probar ataques horizontales/verticales por API y por recursos indirectos (descargas, IDs, reportes).
- Validación y permisos en servidor; consultas SQL parametrizadas; respuesta codificada; CSP y cookies adecuadas a amenaza. CSRF, XSS, SSRF, inyección, session fixation y fuerza bruta según superficie.
- Separar QA/prod y secretos. Nunca exponer claves públicas «con demasiados permisos» solo porque son visibles por diseño. Roles mínimos, revocación y rotación.
- Inventariar dependencias directas/transitivas, lockfiles y licencias; revisar riesgo de componentes obsoletos. SBOM/procedencia según sensibilidad; [OWASP SCVS](https://scvs.owasp.org/scvs/using-scvs/).
- Evitar workflows CI privilegiados para código de forks, terceros no fijados y secretos en logs; [GitHub uso seguro](https://docs.github.com/en/actions/reference/security/secure-use).
- Privacidad desde el dato: finalidad, mínima recolección, retención, exportación/borrado, logging redactado y aviso legal validado por propietario/jurisdicción.
- Para proveedores de IA, no enviar PII o materiales de cliente sin permiso, contrato/proveedor y controles de retención adecuados. Revisar prompt injection, confianza de resultados y costos variables si se añaden features de agentes.

## 4. Backend fiable y observable

| Riesgo | Diseño | Prueba |
|---|---|---|
| Doble envío o webhook repetido | Clave idempotente estable, restricción única y transacción | Dos requests iguales generan un efecto de negocio |
| Proveedor lento/caído | Timeout por dependencia, reintento acotado solo seguro, backoff + jitter | Fallo de red no congela UI ni duplica |
| Respuesta incorrecta | Contrato validado, status HTTP semántico y RFC 9457 para error apropiado | Unit/integración + error visible y recuperable |
| Abuso de endpoint | Límites por actor, carga/tamaño y gasto/uso máximos | Peticiones excesivas no agotan recursos críticos |
| Incidente difícil de depurar | Logs redactados, request ID, trazas y métricas de error/latencia | Identificar recorrido sin exposición de secretos |
| Release problemático | Preview, migration plan, feature flag si procede, rollback ensayado | Revertir sin perder datos o bloquear cliente |

Los reintentos y timeouts se calibran por dependencia; no apilar capas de retry que amplifican fallos. Citar [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html), [OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/) y [Google SRE](https://sre.google/sre-book/service-best-practices/).

## 5. Integridad y recuperación de bases de datos

- **Modelo de dominio:** entidades/relaciones, identificadores, fuente de verdad y estado; contraintes DB (`UNIQUE`, `CHECK`, `FK`) y validación de negocio en servidor.
- **Concurrencia:** definir aislamiento, actualizaciones atómicas, bloqueos optimistas/pesimistas si existe conflicto real, manejo de conflicto/reintento y pruebas de escritura simultánea.
- **Consultas:** índices diseñados según filtros/joins/orden real; usar `EXPLAIN (ANALYZE, BUFFERS)` en dataset representativo y analizar plan, sin crear índices sin costo de escritura.
- **Multitenancy:** `tenant_id` consistente y chequeos de aplicación; RLS solo con estrategia y pruebas que cubran privilegios/bypass/roles. Nunca confiar en filtrar tenant solo en UI.
- **Migraciones:** cambios expand/contract para compatibilidad de releases cuando aplique; revisar backfill, bloqueo, rollback y replicas.
- **Backups:** documentar proveedor, retención, cifrado, PITR disponible y ejecución de una **restauración aislada**, verificando consistencia. RPO/RTO acordados con cliente; no atribuir capacidades no revisadas a Neon o a proveedor concreto.

Fuentes: [PostgreSQL, constraints](https://www.postgresql.org/docs/current/ddl-constraints.html), [backup y restore](https://www.postgresql.org/docs/current/backup.html), [PITR](https://www.postgresql.org/docs/current/continuous-archiving.html).

## 6. Operación responsable y CI/CD

- Revisión en PR con status checks; proteger rama principal según nivel de acceso. No dar permisos de escritura a CI por comodidad.
- En cada cambio: tests de sintaxis y unitarios; E2E de tareas críticas; checks seguridad/dependencias; QA a11y/performace; revisión manual con navegador/cliente; salida visible.
- Antes de deployment: snapshot/backup si aplica, migración, test de smoke, alarma/observabilidad, rollback y responsable.
- Definir incidentes: severidad (pérdida de datos, cuenta comprometida, checkout/lead roto, degradación visual), canal, horario, tiempo de respuesta ofrecido realmente y registro postmortem sin culpar.
- No prometer uptime, pentest, respuesta 24/7 ni compliance si no está contratado y verificado.

## 7. Cuándo escalar una capa (señales, no slogans)

| Señal verificada | Evaluación antes de rediseñar |
|---|---|
| LCP/INP pobres de campo | Fotos/video/JS terceros, hidratar menos, caché, CDN |
| API lenta en p95 con carga | Perfilado, consultas, pooling, bloqueo y reintentos |
| BD saturada | Índices, conexiones, consultas, retención, archivado antes de particionar |
| Webhooks perdidos | Retries, dead letter, idempotencia, cola con trazabilidad |
| Edición difícil para cliente | Modelo de contenidos/CMS, capacitación y permisos |
| Costo inesperado | Top consumidores, cuotas, alertas de presupuesto, límites de servicios |
| Escalamiento de equipo | Módulos, contratos, guías, ownership, revisión de código; microservicios solo por frontera real |

**La decisión excepcional es saber cuándo NO agregar complejidad.** Fuente de evaluación: [DORA 2025](https://dora.dev/research/2025/dora-report/) y [Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html).
