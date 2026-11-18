# Ingeniería de ciberseguridad web — guía para Codex

**Revisado: 2026-11-18.** Es una política técnica de trabajo inspirada en estándares, no una certificación. Antes de aplicar controles, verificar vigencia, jurisdicción, amenazas y stack. Ninguna guía garantiza ausencia de vulnerabilidades.

## 1. Jerarquía y bibliografía original
| Fuente | Estado a esta revisión | Para qué se usa |
|---|---|---|
| [OWASP Top 10:2025](https://top10.owasp.org/2025/) | Lista de riesgos, 2025 | Priorizar clases de fallas web; no es lista completa ni checklist certificable |
| [OWASP ASVS 5.0.0](https://asvs.owasp.org/) | Publicación estable | Convertir riesgo en requisitos verificables de autenticación, acceso, datos, API y configuración |
| [NIST SSDF SP 800-218 v1.1](https://csrc.nist.gov/Projects/ssdf/publications) | **Final**; v1.2 sigue como **borrador** a 2026-11-18 | Integrar seguridad al ciclo de desarrollo, cadena de suministro y respuesta |
| [RFC 9700, OAuth 2.0 Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) | BCP, 2025 | Flujos OAuth, tokens, redirect URIs, PKCE y controles ante ataques |
| [RFC 10017, OAuth 2.0 for Browser-Based Applications](https://www.rfc-editor.org/rfc/rfc10017.html) | BCP, 2026 | Decidir sesión y OAuth en clientes de navegador |
| [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) | Guía mantenida | Consultas parametrizadas y límites de confianza |
| [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) y [cookies seguras](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Cookies) | Guías técnicas | Defensa en profundidad para navegador y sesiones |

**Distinción:** Top 10 orienta riesgos, ASVS detalla verificaciones, SSDF orienta proceso. No decir que «pasar Top 10» equivale a conformidad o seguridad total. Enumerar y citar los controles concretos de ASVS elegidos por proyecto.

## 2. Modelo de amenazas previo a código
1. Inventariar actores: anónimo, usuario, editor, administrador, soporte, servicio externo y, si existe, tenant.
2. Identificar activos: cuentas, datos personales, pagos, secretos, documentos, registros industriales, integraciones y capacidad de operar equipos.
3. Dibujar flujos y **límites de confianza**: browser ↔ edge/API ↔ aplicación ↔ DB ↔ proveedor ↔ dispositivo. Marcar llamadas entre tenants.
4. Analizar abuso realista: suplantación, escalamiento horizontal/vertical, inyección, XSS, CSRF, SSRF, robo de sesión, filtración, denegación por uso, supply chain.
5. Registrar riesgo, severidad explicada, control preventivo, test, propietario, residual y decisión de aceptación. No usar «seguro» como estado binario.

## 3. Reglas de implementación verificables
- **Identidad y sesiones:** usar mecanismos mantenidos y adecuados; MFA para cuentas privilegiadas cuando corresponda; tokens/cookies con expiración, revocación y rotación según amenaza; sesiones en cookies Secure, HttpOnly y SameSite donde apliquen, con CSRF mitigado. OAuth/OIDC solo con flujos y recomendaciones vigentes; no guardar claves sensibles en localStorage por comodidad.
- **Autorización:** por defecto denegar; verificar en **servidor** cada operación sobre cada recurso y tenant (IDOR/BOLA). Separar autenticar de autorizar; probar acceso horizontal, vertical, usuario deshabilitado y objeto inexistente.
- **Entradas/salidas:** validar esquema, longitud, formato y límites en servidor; consultas parametrizadas; codificar salida según contexto; sanitización de HTML rico cuando corresponda; no concatenar SQL. Validar tipo/tamaño de archivos y almacenarlos sin rutas ejecutables.
- **Seguridad browser:** TLS, encabezados apropiados, política CSP progresiva (medir Report-Only si se adopta), sin recursos de orígenes innecesarios; no depender solo de CSP para neutralizar XSS. Controlar CORS con orígenes específicos, no comodines con credenciales.
- **Secretos/config:** mantener credenciales en gestor/variables por entorno; no commitear .env; separar QA/prod; mínimo privilegio por servicio; rotación y revocación; inventario de terceros y permisos. Jamás mostrar contraseñas en capturas, outputs o logs.
- **Dependencias/CI:** lockfile, revisión de dependencias y licencias, SCA y actualización de vulnerabilidades, secret scanning, SAST y análisis de configuración; revisar falsos positivos sin silenciarlos por defecto. Proteger ramas, revisar PR y evitar acciones CI con permisos innecesarios.
- **Operación:** rate limits en rutas abusables; cuotas y tamaños máximos; backups probados y cifrado según sensibilidad; logs de seguridad redactados, alertas útiles, respuesta a incidentes y proceso de parcheo. Separar datos de analítica y datos personales.
- **Webhooks/pagos/correos:** firmas o validación de procedencia si proveedor las soporta, verificación del cuerpo **antes** de mutar, idempotencia, tratamiento de duplicados y replays. Nunca marcar operación exitosa por solo hacer clic.
- **Datos industriales:** integraciones de lectura como opción por defecto. Cualquier escritura/control de maquinaria exige autorización explícita, segmentación OT, evaluación física y revisión especializada; esta guía no habilita comandos de planta.

## 4. Gates y pruebas negativas
| Gate | Prueba mínima y evidencia |
|---|---|
| Acceso | Casos 401/403, acceso a ID de otro usuario/tenant, roles elevados, sesión expirada |
| Entrada | Payload malformado, exceso de longitud/tamaño, caracteres hostiles, inyección, archivos inesperados |
| Sesión | Cookie/headers efectivos, CSRF aplicable, logout/invalidación, redirecciones seguras |
| Configuración | Sin secretos en Git/cliente/bundle/log; entornos y permisos aislados |
| Dependencias | SCA y revisión de paquetes/cambios; pipeline CI protegido |
| Integraciones | Firma webhook, doble entrega, timeout, reintento y rate limit |
| Datos | Exposición mínima, autorización de descarga/exportación, retención y restauración |

**Fallo crítico:** no publicar ni describir como listo si acceso entre tenants, secretos, inyección o mutaciones críticas no están verificados. Corregir en rama aislada; no probar destructivamente en producción.

## 5. Registro de salida Codex
Entregar: activos y flujos, matriz de roles, riesgos priorizados, controles y fuentes citadas, pruebas reproducibles con resultados y evidencia, hallazgos abiertos con severidad, responsable y fecha de revisión. Diferenciar prueba automatizada de revisión manual y de pentest independiente.
