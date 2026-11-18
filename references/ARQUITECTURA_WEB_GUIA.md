# Arquitectura web — Reglas aplicables a nuevos proyectos de Codex

**Edición:** 2026-11-18. Este marco es tecnología-agnóstico: NO prescribe Next.js, Vercel, una base de datos, microservicios, IA o un CMS por defecto. Ajustar decisiones al brief, tamaño, riesgo, mantenimiento y presupuesto del cliente. Las guías y versiones técnicas deben verificarse de nuevo cuando cambie el stack.

## Índice
1. Fuentes y nivel de evidencia
2. Selección de arquitectura por tipo de proyecto
3. Plano antes de escribir módulos
4. Seguridad y privacidad
5. Calidad no funcional
6. Registros de decisión (ADR)
7. Entregables según tamaño
8. Definition of Done

## Fuentes y nivel de evidencia

| ID | Fuente original / oficial | Aporte que se adopta | Tipo |
|---|---|---|---|
| A01 | [D. L. Parnas (1972), On the Criteria to Be Used in Decomposing Systems into Modules, DOI ACM](https://doi.org/10.1145/361598.361623) | Encapsular decisiones propensas a cambiar y separar responsabilidades; modularidad no equivale a más servicios | Investigación fundacional |
| A02 | [Roy T. Fielding (2000), Architectural Styles and the Design of Network-based Software Architectures, tesis UCI](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm) | Evaluar restricciones y compromisos de estilos de red antes de denominar una API «REST» | Tesis |
| A03 | [W3C (2004), Architecture of the World Wide Web, Volume One](https://www.w3.org/TR/webarch/) | URLs/URIs consistentes, separación de contenido/presentación/interacción, interoperabilidad y estándares | Recomendación W3C |
| A04 | [Simon Brown, C4 model](https://c4model.com/) | Diagramar contexto, contenedores y componentes para comunicar límites y dependencias | Método de documentación |
| A05 | [arc42, método y documentación](https://arc42.org/method/) y [decisiones de arquitectura](https://docs.arc42.org/section-9/) | Registrar objetivos de calidad, restricciones, riesgos, despliegue y decisiones proporcionales al proyecto | Plantilla/método |
| A06 | [CMU Software Engineering Institute, Software Architecture](https://www.sei.cmu.edu/software-architecture/) | Priorizar atributos de calidad y evaluar compromisos frente a metas de negocio | Investigación/aplicación |
| A07 | [ISO/IEC 25010:2023, Quality Model](https://www.iso.org/standard/78176.html) | Usar un modelo de calidad como checklist de propiedades relevantes; no afirmar certificación sin auditoría | Norma de referencia; texto íntegro puede ser de pago |
| A08 | [OWASP ASVS (estándar del proyecto)](https://asvs.owasp.org/) | Derivar requisitos y pruebas de seguridad adecuados al riesgo del sistema | Guía de verificación comunitaria |
| A09 | [The Twelve-Factor App](https://12factor.net/) | Config externa, separación de código/config, servicios reemplazables, procesos y logs | Metodología; aplicar según hosting |
| A10 | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Accesibilidad comprobable desde la estructura de componentes, no parche final | Recomendación W3C |
| A11 | [Google web.dev, Web Vitals](https://web.dev/articles/vitals) | Medir experiencia de carga, respuesta y estabilidad en navegador real | Guía técnica |
| A12 | [Google Search Central, SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | Estructurar URLs, navegación y contenidos accesibles a buscadores cuando importe la indexación | Guía técnica |
| A13 | [MDN, Progressive Enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement) | Mantener una base funcional antes de activar capas dependientes de JS | Principio de ingeniería web |

Las ideas marcadas como «política de trabajo Studios.Bit» abajo son **decisiones operativas nuestras**, no reglas literales prescritas por una norma.

## Marco transversal de ingeniería (actualización v1.0)

Las guías siguientes complementan, sin sustituir, los fundamentos A01–A13:

| Especialidad | Literatura verificada a 2026-11-18 | Decisión + gate |
|---|---|---|
| [Ciberseguridad](INGENIERIA_CIBERSEGURIDAD.md) | OWASP Top 10:2025, ASVS 5.0.0, NIST SSDF 1.1 final (1.2 borrador), OAuth RFC 9700/10017 | Modelo de amenazas; acceso por objeto/tenant, secretos y pruebas negativas |
| [Frontend](INGENIERIA_FRONTEND.md) | W3C WCAG 2.2, WAI APG, web.dev CWV, MDN, React si aplica | UX íntegra; teclado/lector, errores y rendimiento p75 |
| [Backend](INGENIERIA_BACKEND.md) | RFC 9110, RFC 9457, OpenAPI, AWS Builders' Library, OpenTelemetry, Google SRE | Contratos, idempotencia, timeouts, observabilidad, carga medida |
| [Bases de datos](INGENIERIA_BASES_DATOS.md) | PostgreSQL 18: constraints, transacciones, índices, EXPLAIN y PITR | Integridad, aislamiento, migraciones, recuperación demostrada |

**Reglas de adopción:**
1. Landing estática → arquitectura + diseño + frontend (si se escribe UI); controles de seguridad aplicables al hosting, scripts y formularios; no introducir DB ni API artificial.
2. CMS con editores → además permisos, sesiones, cambios editoriales y políticas de datos según proveedor.
3. App con usuarios y datos → las cuatro áreas de ingeniería, con ownership de controles que cruzan capas (p. ej. frontend no sustituye autorización server-side).
4. Múltiples tenants, pagos o sistemas industriales → modelado de amenazas y fallos específicos, límites de confianza y evidencia antes del go-live. Integración industrial de solo lectura por defecto.
5. Siempre separar **estándar publicado**, guía, heurística, decisión local y evidencia empírica; no afirmar que cumplir uno sustituye pruebas del resto.

### Gates de release por escenarios
- **Seguridad:** sin exposición de credenciales, permisos entre tenants, inyección o mutation sin autorización.
- **Frontend:** recorrido accesible y resistente a red lenta; métricas de campo cuando existan; imágenes/video no bloquean CTA.
- **Backend:** timeout y reintentos seguros, contratos de error y operaciones idempotentes cuando haya riesgo de duplicación.
- **Datos:** esquema con integridad, migraciones probadas, backup y restauración ensayada con RPO/RTO definidos si los datos importan.
- **Operaciones:** CI verde + pruebas reproducibles; preview/QA separado; runbook, monitoreo, responsable y rollback proporcional.
- **Scale:** antes de prometer escalabilidad fijar hipótesis de concurrencia, perfil de carga, SLI/SLO, límites de infraestructura y coste; medir y corregir cuello de botella.

Ningún gate se declara aprobado sin prueba ejecutada; lo no medido queda **pendiente**, no «sin problemas».

## 1. Selección de arquitectura según el problema

Antes de escoger librerías/servicios, llenar la matriz:
- Usuarios y tareas; páginas y rutas; canal ES/EN; metas de negocio; contenidos y responsable de edición.
- Datos públicos/privados; origen y dueño de cada dato; integraciones; controles de acceso y sensibilidad.
- Tráfico y disponibilidad esperados; tiempos aceptables; SEO; necesidad de interacción; dependencia de red.
- Presupuesto total (hosting, API, licencias, servicios, soporte, backups), habilidades del equipo y plan de mantenimiento.

| Caso de uso | Punto de partida mínimo a evaluar | Cuándo escalar |
|---|---|---|
| Landing / portafolio / micrositio | HTML estático o generado, navegación nativa, contenido renderizado, formularios solo si existe backend confiable | CMS si hay edición frecuente; funciones de servidor cuando realmente aportan |
| Sitio corporativo editorial bilingüe | Rutas por idioma, contenido estructurado, estrategia de SEO y opción de CMS según la persona que editará | Separar publicación/edición si permisos o volumen lo justifican |
| Cotizador, reservas, prospección o ecommerce | Frontend + límites de negocio del servidor + almacenamiento transaccional cuando persista información | Colas y procesamiento asíncrono si el SLA o latencia lo requieren |
| Dashboard o SaaS con cuentas | Autenticación, autorización por recurso, API con validación, DB, historial, trazabilidad y estados de error | Streaming/eventos solo si hay una necesidad real y plan de reconexión |
| Datos industriales / telemetría | Ingesta acotada y verificable, separación entre muestra simulada y dato real, marcas de tiempo y calidad de señal | Buffer/reintentos, series temporales y canal casi en vivo según disponibilidad y frecuencia |

**Regla de proporcionalidad:** explicar por qué NO se necesitan backend, base de datos, microservicios o video pesado antes de añadirlos. Un monolito modular puede ser apropiado; microservicios y colas son opciones, no signos de calidad por sí mismos.

## 2. Plano obligatorio antes de escribir módulos significativos

1. **Mapa de información y rutas:** sitemap, navegación, idiomas, títulos, estados 404 y redirecciones, qué puede indexarse.
2. **C4 contexto:** actores, sistema, proveedores (hosting, correo, CRM, pagos, CMS, autenticación, dispositivos) y flujos de confianza. Para proyectos simples basta una lista y diagrama corto; no dibujar niveles superfluos.
3. **C4 contenedores cuando aplican:** browser/front, servidor/API, DB, almacenamiento, tareas, proveedor externo; marcar límites de confianza y quién despliega/mantiene cada bloque.
4. **Responsabilidades y módulos:** separar interfaz/presentación, reglas de negocio, adaptadores de servicio, acceso a datos y configuración. Las funciones de negocio no deberían depender del layout; encapsular lo reemplazable (A01).
5. **Modelo de datos:** entidades, claves/relaciones, fuente de verdad, calidad, retención, privacidad, consentimiento, borrado/exportación, backup/restore y migraciones.
6. **Contrato API y eventos:** entradas, respuestas, unidades, timestamps/zona horaria, validaciones, errores, paginación, permisos, límites y reintentos/idempotencia donde haya escritura.
7. **Deploy y operación:** entornos local/preview/prod separados, variables secretas, HTTPS, CI, rollback, monitoreo, alertas y responsables.

### Decisión de renderizado
- **Estático/generado** para contenido público que cambia poco; confirmar preview de contenido.
- **Renderizado de servidor** cuando SEO, contenido condicionado o frescura lo justifiquen; medir coste/latencia/caché.
- **Cliente/hidratación** solo para la interacción que lo necesita; no esconder el mensaje principal detrás de JS o video.
- **Tiempo real** solo con requisito explícito: definir periodicidad, desconexiones, desorden de eventos, backlog y degradación a polling o estado anterior.
- Documentar cuál parte se renderiza dónde y qué ocurre **sin JavaScript, con red lenta o sin datos**.

## 3. Seguridad, privacidad y datos desde el diseño

**Política mínima; mapear a requisitos vigentes de OWASP ASVS y al contexto legal antes de producción.**
- Autenticación ≠ autorización. Comprobar permisos **en el servidor y por recurso**, incluyendo roles, organización/tenant y acceso directo a IDs; el menú oculto no protege.
- Validar entradas del lado del servidor, limitar recursos, tratar consultas parametrizadas y salidas no confiables según contexto; prevenir CSRF/XSS y abuso en flujos aplicables.
- Guardar secretos fuera del repositorio; separar credenciales/DB de preview y prod, privilegio mínimo, rotación y auditoría de acceso.
- No colocar datos personales, tokens, payloads sensibles o detalles de PLC en logs de frontend/analítica; redactar eventos antes de emitirlos.
- Mapear consentimiento, finalidad, retención, borrado, privacidad y proveedores; las obligaciones legales dependen de jurisdicción y proyecto.
- Para pagos, correo, formularios, webhooks y otras acciones externas: validar origen/firmas cuando corresponda, diseñar deduplicación y reintentos seguros; mostrar «enviado» solo ante confirmación real.
- Para telemetría industrial, predeterminar **solo lectura**; nunca habilitar órdenes de control o escritura a equipos físicos sin autorización y diseño de seguridad dedicado.
- Declarar quién respalda los datos y verificar una restauración en entorno seguro antes de afirmar recuperabilidad.

## 4. Calidad no funcional como requisitos verificables

| Dimensión | Pregunta de diseño | Prueba/evidencia |
|---|---|---|
| Accesibilidad (A10) | ¿Puede operarse con teclado, lector y zoom, y sin motion? | WCAG 2.2 AA como objetivo cuando aplique; inspección manual y automatizada |
| Rendimiento (A11) | ¿Carga e interactúa bien en móvil real? | LCP, INP, CLS de campo p75 si existen; laboratorio etiquetado aparte |
| Seguridad (A08) | ¿Cada operación respeta identidad, privilegios y entradas? | Tests de acceso denegado, validación y controles OWASP elegidos por riesgo |
| Confiabilidad (A06–A07) | ¿Qué sucede con timeout, doble envío, dato fuera de orden, caída de proveedor? | E2E de error, reintento seguro, degradación y reconexión |
| Mantenibilidad (A01, A05) | ¿Se puede cambiar CMS, mail o DB sin reescribir el diseño? | Límites de módulos, contratos, PR revisable y ADR de decisiones |
| Usabilidad y contenido | ¿La tarea principal es localizable y se puede completar? | Prueba de recorrido, revisión de copy e investigación con usuarios |
| SEO e internacionalización (A03, A12) | ¿Cada versión tiene ruta, idioma, metadatos, enlaces y canonical correctos? | Crawl técnico, enlaces, hreflang/canonical si aplica y contenido servido |
| Operación (A09) | ¿Se puede desplegar/revertir sin secreto ni pérdida de datos? | Preview, checklist, monitoreo, backups y rollback ensayado |
| Coste y sostenibilidad | ¿El plan mensual y soporte son realistas? | Lista verificable de recursos, cotas, proveedores y riesgos |

**No usar una puntuación única inventada** (por ejemplo, «98 % arquitectura») para reemplazar evidencia detallada.

## 5. Registros de decisión (ADR) mínimos

Documentar decisiones difíciles de revertir, no cada decisión CSS:

- **Contexto y presión:** necesidad, usuarios, restricciones, riesgo.
- **Alternativas:** mínimo dos opciones pertinentes, incluida opción simple.
- **Decisión y por qué:** cualidades priorizadas, costes y trade-offs.
- **Consecuencias:** complejidad, deuda, seguridad, vendor lock-in, performance.
- **Verificación y reversión:** qué prueba demuestra que funcionó y cómo migrar/rollback.
- **Estado y fecha:** propuesta, aceptada o sustituida.

Casos de ADR frecuentes: elegir CMS/no CMS, SSR vs estático, proveedor de identidad, DB, streaming vs polling, multi-tenant, hosting y almacenamientos. El ADR no autoriza comprar, migrar ni desplegar.

## 6. Entregables por tamaño

**Sitio informativo pequeño:** brief, sitemap, componentes, rutas, decisión de render, accesibilidad básica, estrategia de formulario/SEO, QA y responsable de hosting. Arquitectura de una página máximo.

**Sitio corporativo editable:** lo anterior + modelo de contenidos/CMS, roles, preview, flujo de publicación, backups y onboarding de editores.

**Aplicación transaccional o con datos:** lo anterior + diagrama contexto/contenedores, contratos API, esquema datos, matriz roles/recursos, amenazas principales, entornos, integraciones, observabilidad, migraciones y ADR.

**Sistema de múltiples servicios o industrial:** lo anterior + escenarios de fallos, límites de confianza/red, calidad/latencia de datos, continuidad sin internet, estrategia de sincronización y evaluación de seguridad física. Nunca inferir robustez industrial de una demo web.

## 7. Definition of Done de arquitectura (no equivale a despliegue)
- [ ] Usuario, objetivo, fuentes de datos y riesgos documentados; no se supusieron capacidades externas.
- [ ] Arquitectura proporcional y justificada; interfaces y dependencias nombradas.
- [ ] Rutas, estados, accesibilidad y SEO (si aplica) definidos antes de construir.
- [ ] Autenticación/autorización y datos sensibles modelados cuando existen.
- [ ] Pruebas unitarias, integración y E2E para rutas críticas; al menos fallo recuperable por flujo.
- [ ] Sin secretos en Git o cliente; configuración por entorno, rollback y backups verificados si existen datos.
- [ ] Resultados reales separados de muestras/fakes; performance y pruebas en dispositivo etiquetadas correctamente.
- [ ] Decisiones de alto impacto registradas y pendientes explicitados antes de cualquier merge/deploy.

**Complemento creativo:** [Fundamentos de diseño y UX](FUNDAMENTOS_DISENO_LITERATURA.md). Los videos SB son inspiración visual secundaria a estas reglas.
