---
name: studios-bit-ciberseguridad-web
description: Seguridad y privacidad en sitios, SaaS, APIs, formularios, autenticación, sesiones, integraciones y datos de proyectos Studios.Bit. Activar al revisar amenazas, permisos, secretos, dependencias, despliegue o cualquier flujo con datos y cuentas. Aplicar OWASP ASVS 5.0, Top 10 2025 y NIST SSDF, con evidencia.
---

# Ciberseguridad web verificable

**Objetivo:** reducir y explicar riesgo en diseño, código, integración y operación. No decir «a prueba de hackeos», «certificado» ni «seguro» sin un alcance y evidencia precisos.

## Procedimiento
1. **Inventario y alcance:** saber qué se protege, de quién, dónde vive, quién accede, flujos y datos personales. Confirmar si es pública estática, app con cuentas, multi-tenant, pagos o integración industrial.
2. **Amenazas:** dibujar límites de confianza y matriz actor/recurso/acción/tenant; identificar abuso, inyección, autenticación, XSS, CSRF, SSRF, filtraciones, supply chain y disponibilidad.
3. **Controles de diseño:** permisos server-side deny-by-default, validación en servidor, queries parametrizadas, sesiones/cookies y OAuth actualizados si aplica, secretos por entorno, aislamiento de QA/prod, mitigaciones específicas y logs redactados.
4. **Implementación:** usar componentes y servicios mantenidos, privilegio mínimo, lockfile, cabeceras/CSP evaluadas, verificación de webhooks, idempotencia y protección de rutas costosas.
5. **Pruebas:** 401/403, IDOR entre usuarios/tenants, datos hostiles, errores, solicitudes duplicadas, sesión expirada, SCA/secret-scan y fallas de proveedores; registrar qué se ejecutó y qué no.
6. **Revisión antes de publicar:** reportar hallazgos críticos, responsables y plan de corrección; no desplegar ni tocar credenciales sin autorización.

## Fuentes obligatorias según contexto
Leer [manual con fuentes y matriz de gates](../../references/INGENIERIA_CIBERSEGURIDAD.md). Priorizar **ASVS 5.0.0 estable** para requisitos, **Top 10:2025** para riesgos y **NIST SSDF 1.1 final** para proceso; **SSDF 1.2 es borrador** en la revisión 2026-11-18. Verificar vigencia para nuevos proyectos. OAuth/browser: RFC 9700 y RFC 10017 si se utiliza.

## Entrega Codex
- Matriz de datos/actores/permisos y amenazas priorizadas.
- Controles trazables a riesgo, referencia y caso de prueba.
- Evidencias de test negativo y revisión de dependencias/config; nada de contraseñas en outputs.
- Hallazgos abiertos, residual, bloqueantes para producción y responsable.
- Si hay control de equipos físicos/OT, **solo lectura por defecto**; requerir autorización y revisión especial antes de escritura.
