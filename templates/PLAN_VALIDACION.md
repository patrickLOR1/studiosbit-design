# Plan BitProof antes de implementar

**Proyecto / ambiente / fecha / responsable:** [pendiente]  
**Clase S/M/A y fundamento:** [pendiente]

## Recorridos de negocio

| ID | Tarea | Inicio → efecto real esperado | Caso negativo | Evidencia planeada | Bloqueante |
|---|---|---|---|---|---|
| UX-01 | | | | | sí |

## Matriz de pruebas por riesgo

| ID | Área | Método (auto/manual/usuario) | Herramienta | Ambiente | Responsable | Bloqueante |
|---|---|---|---|---|---|---|
| UI-01 | responsive y teclado | | | | | sí |
| A11Y-01 | a11y | | | | | sí |
| PERF-01 | rendimiento | | | | | según alcance |
| SEC-01 | dependencias/secretos | | | | | sí |
| SEC-02 | autorización | | | | | si hay cuentas |
| API-01 | errores/reintentos | | | | | si hay API |
| DB-01 | integridad/restore | | | | | si hay BD |
| CMS-01 | editor real | | | | | si hay CMS |
| SEO-01 | indexación | | | | | si es pública |
| OPS-01 | deploy/rollback | | | | | si se publica |

Reglas: `na` solo con justificación; `pending` no es `pass`; todo `pass` necesita prueba realmente ejecutada con fecha y evidencia; no hacer tests destructivos en producción.
