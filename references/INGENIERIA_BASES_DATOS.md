# Ingeniería de bases de datos — modelo, rendimiento y recuperación

**Revisado: 2026-11-18.** PostgreSQL se usa aquí como referencia documental concreta; no se impone para todo proyecto. La documentación **current** oficial mostraba PostgreSQL 18 a esta fecha; verificar versión real y soporte del hosting antes de usar sintaxis. Nunca migrar producción sin autorización, respaldo y plan de compatibilidad.

## Fuentes originales
- [PostgreSQL 18: constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — integridad declarativa NOT NULL/CHECK/UNIQUE/FK.
- [PostgreSQL 18: Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — concurrencia y niveles de aislamiento.
- [PostgreSQL 18: Indexes](https://www.postgresql.org/docs/current/indexes.html) y [multicolumn](https://www.postgresql.org/docs/current/indexes-multicolumn.html) — coste/beneficio y orden de columnas.
- [PostgreSQL 18: EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — planes reales, `EXPLAIN (ANALYZE, BUFFERS)` con cautela.
- [PostgreSQL 18: Continuous Archiving / PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) — recuperación temporal.
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — parametrización y separación de credenciales.

## 1. Selección del almacenamiento por necesidades
- **Sin datos persistentes:** no instalar DB. Contenido fijo o archivos editables podrían bastar.
- **Relacional transaccional:** evaluar Postgres/SQL para consistencia, relaciones, reporting y consultas declarativas.
- **Documento/key-value/cache/series temporales:** justificar por patrones de lectura/escritura, volumen, retención, búsqueda, agregación, operación, capacidades del equipo y coste; no sustituir un sistema relacional por moda.
- Definir: entidades, cardinalidad, acceso multi-tenant o no, lectura/escritura, crecimiento, latencia, retención, privacidad, RPO/RTO objetivo, hosting y coste.

## 2. Esquema y consistencia
- Diseñar con tablas y relaciones explicables; nombres coherentes, claves estables, tipos correctos, unidades/timestamps precisos y zonas horarias manejadas conscientemente.
- Implementar integridad en DB mediante NOT NULL, UNIQUE, FK, CHECK donde corresponda. No delegarla solo al frontend/ORM.
- Transacciones para operaciones que deban ser atómicas; establecer política de aislamiento/concurrencia según anomalías reales. Probar carreras de actualización y duplicación.
- Para multi-tenant: modelo explícito de `tenant_id`, permisos **en servidor**, consultas filtradas, y RLS como defensa adicional si se adopta y prueba. Nunca suponer aislamiento por ocultar UI.
- Consultas preparadas/parametrizadas; cuenta de aplicación con permisos mínimos; roles separados para migraciones y backups.

## 3. Migraciones y cambios sin interrupciones evitables
1. Definir DDL en control de versiones, migraciones numeradas y estrategia para despliegues concurrentes.
2. Preferir **expand → migrar/backfill → cambiar lectores/escritores → contract** para cambios incompatibles; compatibilidad durante rolling deploy.
3. Ensayar migración y rollback lógico en base clonada/sintética representativa; estimar tiempo de bloqueo, volumen y posibilidad de reanudar.
4. Datos sensibles: backfill auditable y cambios por lotes, sin exponerlos en logs. Nunca editar producción desde una skill documental.
5. Los rollbacks de esquema no siempre son seguros: plan de restauración/forward-fix, backups consistentes y decisión explícita.

## 4. Rendimiento y capacidad
- Registrar consultas reales importantes, cardinalidad, filtros, orden, paginación, N+1, p95 de latencia y uso de conexiones. Crear índices **para consultas medidas**, no sobre cada columna.
- Comparar planes y estadísticas con EXPLAIN; recordar que `ANALYZE` ejecuta la instrucción y puede alterar datos en operaciones de escritura. Probar sobre datos representativos y entorno seguro.
- Índices compuestos dependen del orden/condiciones. Medir coste de escritura, espacio y mantenimiento. Vigilar pools/conexiones, transacciones largas, bloqueos y consultas costosas.
- Escalar vertical/horizontal, réplicas, particiones o cachés solo después de conocer cuello de botella y consistencia que se necesita. Evitar particionar desde el primer día sin razones.

## 5. Backup, restauración y ciclo de vida
- Diferenciar backup lógico, físico, WAL/PITR y réplica: **una réplica no sustituye backup**.
- Establecer RPO (pérdida máxima admisible) y RTO (tiempo para restaurar) como objetivos; revisar soporte real del proveedor y coste.
- Automatizar backup con retención y cifrado según sensibilidad; alertar fallos; realizar **restauración de prueba** periódica y conservar evidencia. No declarar «tenemos backup» sin comprobar recuperación.
- Controlar retención/borrado/exportación, mínimo privilegio, auditoría, enmascaramiento de fixtures, ambientes separados, coste de almacenamiento y salida del proveedor.

## 6. QA y criterios para una PR
| Gate | Evidencia |
|---|---|
| Modelo | Diagrama/tablas/claves/relaciones + motivo de cada entidad |
| Integridad | Tests NOT NULL, UNIQUE, FK, concurrencia y rollback |
| Seguridad | Roles, aislamiento tenant, queries parametrizadas y secretos ausentes |
| Evolución | Migración up/backfill ensayada, compatibilidad app anterior/nueva |
| Rendimiento | Queries críticas + EXPLAIN/latencias medidos (sin datos privados) |
| Operación | Plan y prueba de backup/restore, RPO/RTO propuestos/verificados |

Documentar incertidumbres (tráfico, tamaño, tasa de escritura); nunca inventar métricas ni garantías de recuperación. No guardar credenciales reales en ejemplos.
