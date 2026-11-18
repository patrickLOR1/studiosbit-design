# BitProof — pruebas reproducibles y puertas de entrega

**Definición:** BitProof es un **marco interno de evidencias** para desarrollo y QA. No sustituye un pentest, una auditoría de accesibilidad formal ni una certificación. El flujo verifica una afirmación concreta con un archivo/URL/traza y una persona responsable.

## Índice
1. Trazabilidad y estados
2. Matriz de gates por riesgo
3. Recetas automatizadas por proyecto
4. Revisiones humanas
5. Release y reporte
6. Limitaciones

## 1. Evidencia auditable

Un gate completo especifica:

```
id | área | flujo/requisito | nivel de riesgo | entorno | método
   | resultado (pass|fail|pending|na) | ruta a evidencia real
   | fecha ISO 8601 | responsable | nota/limitación
```

- `pass` requiere ejecución real, resultado observable y evidencia navegable/archivo preservado.
- `fail` significa problema confirmado, con ticket, causa conocida si está, responsable y prioridad.
- `pending` significa no probado; no convertirlo en «sin hallazgos».
- `na` requiere razón específica del proyecto; no se permite para evitar un bloqueo aplicable.
- `blocker=true` significa que no se declara `GO` si está `fail` o `pending`.

Usar [ejemplo de registro JSON](../templates/bitproof-evidencia.example.json), [reporte](../templates/RELEASE_EVIDENCIAS.md) y validador `scripts/bitproof_gate.py` (solo estructura/evidencia, no ejecución de pruebas). La decisión final de aceptar riesgos es humana y autorizada.

## 2. Gates obligatorios según perfil

| Gate | S público | M integrado/CMS | A crítico | Ejemplo de evidencia |
|---|---|---|---|---|
| `UX-01` oferta/CTA/flujo completo | Sí | Sí | Sí | Test de tarea y captura de confirmación real |
| `UI-01` responsive, teclado, zoom y estados | Sí | Sí | Sí | Pruebas y capturas por breakpoint |
| `A11Y-01` revisión automatizada + manual | Sí | Sí | Sí | axe + teclado/lector según alcance |
| `PERF-01` rendimiento lab y presupuesto | Sí | Sí | Sí | Lighthouse CI y archivos de medición |
| `SEO-01` indexación/canonical | Si hay páginas públicas indexables | Igual | Si aplica | HTML/headers/Search Console |
| `SEC-01` secretos/dependencias/config | Sí | Sí | Sí | SCA/secret scan y revisión de config |
| `SEC-02` acceso por recurso/tenant | No aplica si no hay cuentas | Si hay cuentas | Sí | Test 401/403/IDOR y roles |
| `API-01` errores/reintentos/doble efecto | Si hay endpoint | Sí | Sí | Integración/red caída/duplicado |
| `DB-01` integridad/migración/restore | Si hay persistencia | Si hay persistencia | Sí | Restore aislado, constraints, revisión |
| `CMS-01` cliente edita/publica/revierte | Si hay CMS | Si hay CMS | Si hay CMS | Test realizado por editor |
| `OPS-01` rollback/observabilidad | Proporcional | Sí | Sí | Runbook, smoke, responsable |
| `PRIV-01` datos/consentimiento | Si hay cookies/datos | Sí | Sí | Mapa datos, comprobación de tags |

La tabla es una **política Studios.Bit** que debe adaptarse por brief, contrato y exposición. En un sitio puramente estático, los gates de BD/API se registran `na` con justificación real. Si hay pagos o control de equipos, agregar requisitos específicos independientes, no reducirlos a esta lista.

## 3. Recetas para proyectos reales (no están ejecutadas por este repositorio)

### E2E con Playwright

1. En el repositorio del proyecto instalar `@playwright/test` en versión fijada; crear config y tests de las rutas críticas con `baseURL` de ambiente QA.
2. Incluir Chromium, Firefox y WebKit si el proyecto/coste lo justifica; no llamar «Safari físico» a WebKit Linux de CI.
3. Probar navegación y teclado, CTA/cotización, validación, error de red, duplicados y estados de carga. Usar fixtures sintéticos.
4. En CI conservar traza en fallo, capturas y resultado. No usar credenciales de producción.

Fuente: [Playwright CI](https://playwright.dev/docs/ci), [buenas prácticas](https://playwright.dev/docs/best-practices).

### Accesibilidad con axe + humanos

1. Integrar `@axe-core/playwright` donde sea apropiado; ejecución de rutas/estados con roles correctos.
2. Test manual de navegación solo teclado (Tab, Shift+Tab, Enter, Escape), foco, 200% zoom, texto y errores. Incluir lector de pantalla cuando haya capacidad.
3. Registrar criterio aplicable WCAG 2.2 y no dar conformidad total por un scan limpio.

Fuentes: [Playwright accesibilidad](https://playwright.dev/docs/accessibility-testing), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WCAG-EM 2.0](https://www.w3.org/TR/WCAG-EM/).

### Rendimiento con Lighthouse CI + campo

1. Medir baseline en preview comparable; Lighthouse CI produce análisis reproducible pero tiene variabilidad de laboratorio.
2. Establecer budgets por página y por tercero después de una línea base; no insertar thresholds inventados en cada proyecto.
3. La métrica **INP** requiere observación apropiada, preferentemente de campo; Lighthouse no reemplaza datos de usuarios.
4. Con datos de campo, evaluar p75 LCP/INP/CLS en móvil y escritorio. Si no hay muestra, indicar `sin muestra`, no `0 ms`.

Fuentes: [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md), [web.dev Vitals](https://web.dev/articles/vitals).

### Seguridad, backend y datos

1. SCA, secret scanning, lockfile y revisión de permisos en PR. No imprimir secretos en reportes.
2. Test de identidad, roles y acceso cruzado para cada endpoint protegido; revisión contra OWASP ASVS aplicable.
3. Fallos externos: timeouts, retry, webhook duplicado, limitación de uso, respuesta 401/403/429/5xx según contrato.
4. BD: constraints, test concurrencia, migración en QA y ensayo restore con datos sintéticos. Nunca ensayar pérdida de datos en prod.

Fuentes: [OWASP ASVS](https://asvs.owasp.org/), [OWASP API Top 10](https://api-security.owasp.org/editions/2023/en/0x11-t10/), [Postgres restore](https://www.postgresql.org/docs/current/backup.html), [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use).

### Ejemplo de CI por proyecto (adaptar; NO es workflow instalado aquí)

```yaml
# Integrar en el repositorio del cliente tras validar scripts y versiones.
# Jobs separados: lint/typecheck → unit/integration → E2E → axe → lighthouse
# → SCA/secret scan → revisión humana preview → aprobación de publicación.
# Un error de red o un runner inestable se informa; no se silencia el test.
```

La biblioteca misma sí tiene un workflow **únicamente para validar sus Markdown/skills y tests de scripts**. Ese workflow no mide LCP, frontend, seguridad de clientes ni consulta sistemas externos.

## 4. Pruebas humanas no delegables a un scanner

- Usuario explica la oferta, encuentra la acción y completa la tarea sin ayuda.
- Persona con teclado encuentra el foco y puede navegar/deshacer estados.
- Usuario con tecnología de asistencia, si se reclutó, termina tarea; documentar contexto.
- Cliente editor completa cambio y revisión en preview sin ayuda verbal.
- Persona responsable confirma que logos, imágenes, música, nombres, precios, IVA, legales y consentimientos están autorizados.
- Product owner verifica reporte de defectos y confirma riesgo residual.

## 5. Semáforo de release

| Decisión | Condición |
|---|---|
| `NO-GO` | Algún bloqueante aplicable está `fail`, `pending` o carece de evidencia; o faltan permisos explícitos |
| `GO condicionado` | Bloqueantes comprobados; quedan issues no críticos aceptados por responsable con plan y fecha |
| `GO técnico` | Bloqueantes comprobados y aceptados; tests ejecutados y evidenciados; falta aún autorización de despliegue |

**Importante:** `GO técnico` nunca equivale a publicación autorizada. Si no hay medición de campo aún, se puede reportar «lab aprobado; campo pendiente» sin fingir cumplimiento completo.

## 6. Excepciones con fecha y responsable

Si una condición no se puede probar por falta de equipo físico, acceso o volumen, registrar:

`riesgo / por qué no fue posible / qué se probó en su lugar / riesgo residual / quién lo acepta / fecha límite`.

Una excepción de seguridad crítica no se acepta automáticamente por presión de calendario. La revisión humana debe determinar alternativa viable.
