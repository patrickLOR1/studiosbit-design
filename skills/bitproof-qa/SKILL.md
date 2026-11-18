---
name: studios-bit-bitproof-qa
description: Diseñar, ejecutar y auditar las puertas de calidad BitProof de Studios.Bit para sitios y aplicaciones en Codex. Activar al preparar un PR, preview, lanzamiento, entrega a cliente, revisión de seguridad, SEO, accesibilidad, rendimiento o regresiones; clasificar pruebas por riesgo y generar evidencia verificable de lo ejecutado, lo pendiente y lo bloqueante.
---

# BitProof — evidencia antes de promesas

No afirmar «listo», «AA», «seguro», «rápido» o «sin errores» sin indicar **alcance, método, entorno, fecha y resultados**. BitProof es una metodología interna, **no** una certificación externa ni un producto SaaS operativo.

## Triage de riesgo

1. Leer [matriz, severidad y gates](../../references/BITPROOF_GATES.md) y [método](../../references/METODO_STUDIOSBIT.md).
2. Clasificar el proyecto: `S` público simple; `M` integraciones/CMS; `A` cuentas, multi-tenant, pagos, datos sensibles o impacto físico. Explicar excepciones.
3. Enumerar flujos críticos reales y controles aplicables. Una prueba irrelevante se marca `na` con justificación; nunca se simula como `pass`.
4. Para cada prueba registrar identificador, área, ejecución (`auto`, `manual`, `usuario`, `tercero`), resultado (`pass`, `fail`, `pending`, `na`), evidencia, fecha, entorno y autor. Resultado sin archivo/URL/traza o observación reproducible **no es pass**.
5. Marcar críticos de seguridad, pérdida de datos, pagos, flujo de contacto y barreras accesibles como bloqueantes cuando aplican. No eliminar gates para lograr verde.

## Cobertura mínima según contexto

| Área | Evidencia preferida | Límite que debe aclararse |
|---|---|---|
| Negocio y UX | Prueba de tarea real, claridad de CTA, contenido validado | Heurísticas no sustituyen usuarios |
| Frontend | Playwright Chromium/Firefox/WebKit donde aplique, formularios, responsive, errores | Emulación no prueba Safari/iPhone físico |
| Accesibilidad | `axe` + teclado + zoom/reflow + lector + revisión humana WCAG 2.2 | Herramienta automática no certifica AA |
| Rendimiento | Lighthouse CI en laboratorio + CWV de campo p75 móvil/escritorio si hay datos | Score de laboratorio no es INP de campo |
| Seguridad | Dependencias/secret scan, matriz de permisos, casos negativos, cookies y CSP | Scanners no son pentest independiente |
| Backend | Contratos, fallos, latencia, duplicados, webhooks, aislamiento | Un 200 no demuestra efecto real |
| Datos | Integridad/migración, permisos, restore en entorno seguro | Backup sin restore probado no es recuperación |
| SEO/medición | indexabilidad, texto, canonical/hreflang según caso, eventos reales | No se garantiza indexación ni leads |
| Operación | Preview/QA separado, logs redactados, owner y rollback ensayado | Deploy exitoso no prueba el servicio |

## Operativa

- Usar [plan de validación](../../templates/PLAN_VALIDACION.md) **antes** de desarrollar y [reporte de evidencias](../../templates/RELEASE_EVIDENCIAS.md) al cerrar.
- Si el proyecto integra `scripts/bitproof_gate.py`, correrlo contra un registro JSON creado con esquema de `templates/bitproof-evidencia.example.json`; el script verifica **completitud documental**, no ejecuta Playwright, axe ni auditorías por sí mismo.
- Para automatización por proyecto, consultar [recetas CI](../../references/BITPROOF_GATES.md) y docs oficiales de Playwright, axe, Lighthouse CI y GitHub. No copiar versiones de dependencias a ciegas; fijar versiones y comprobar licencias/seguridad.
- Separar `auto`, `manual`, `usuario` y `tercero`. Registrar incidencias, dueño y fecha de corrección. Si no se ejecutó, escribir `pending`.
- Aplicar revisión final humana en preview y aceptación del cliente. Autoridad de publicar sigue con el dueño del proyecto.

## Salida Codex

Una tabla de gates por riesgo (bloqueantes vs deseables), evidencias enlazadas, problemas abiertos y recomendación `GO`, `NO-GO` o `GO condicionado` con riesgos aceptados **por persona autorizada**. Nunca convertir un `pending` crítico en `pass` automáticamente.
