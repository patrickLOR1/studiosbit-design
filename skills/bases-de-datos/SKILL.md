---
name: studios-bit-bases-de-datos
description: Diseñar, implementar y revisar persistencia de datos para sitios, SaaS, cotizadores, CRM, ecommerce, dashboards y telemetría. Activar ante esquemas, SQL, ORM, migraciones, índices, concurrencia, multi-tenant, backups, rendimiento o elección de DB. Sin imponer PostgreSQL ni crear DB para webs estáticas.
---

# Bases de datos seguras, evolutivas y recuperables

**Objetivo:** preservar integridad, seguridad, rendimiento y capacidad real de restauración con complejidad proporcional.

## Flujo
1. **Descubrimiento:** quién escribe/lee; entidades y relaciones; volumen y crecimiento estimado; confidencialidad, retención y borrado; patrones de acceso, disponibilidad y recuperación requerida.
2. **Elección:** justificar SQL/no SQL/archivo/cache/serie temporal; elegir tecnología por transacciones, consultas, operación, hosting y coste; no copiar stack por moda.
3. **Modelo:** tipos, PK/FK, UNIQUE, CHECK, NOT NULL, timestamps/unidades, fuente de verdad; transacciones y comportamiento de concurrencia.
4. **Aislamiento:** credenciales por rol, queries parametrizadas, filtros por recurso y tenant en servidor; evaluar RLS como segunda barrera, no sustituto de autorización.
5. **Evolución:** migraciones versionadas, cambios compatibles expand/backfill/contract, prueba previa con datos sintéticos representativos y rollback/forward-fix. **Nunca migrar producción sin autorización.**
6. **Rendimiento:** consultas críticas, N+1, EXPLAIN/ANALYZE en entorno seguro, índices medidos, pools y límites. La réplica no sustituye backup.
7. **Recuperación:** definir RPO/RTO, retención y proveedor responsable, prueba real de restore y evidencia antes de afirmar protección.
8. **QA:** constraints, carreras y duplicados, permisos de tenant, migración, EXPLAIN, restauración de ensayo y costes.

## Lectura requerida
[Ingeniería de BD con literatura PostgreSQL 18, transacciones, índices, PITR y seguridad](../../references/INGENIERIA_BASES_DATOS.md). Si hay API, leer [backend](../backend-ingenieria/SKILL.md); si hay datos personales o multi-tenant, [ciberseguridad](../ciberseguridad-web/SKILL.md).

## Resultado Codex
Diagrama entidad-relación, DDL y migraciones si autorizadas, matriz de acceso, plan de índices basado en consultas, tests y procedimientos de backup/restore. Separar **propuesto** de **verificado**. Cero secretos o datos de clientes en fixtures públicos.
