# SEO/AEO, contenido útil y medición responsable — Studios.Bit

**AEO aquí significa que el contenido sea comprensible y útil para motores de respuesta, sin afirmar optimización garantizada.** SEO técnico y editorial siguen siendo la base. Este documento separa las recomendaciones de **Google Search** (evidencia de comportamiento de ese buscador) de extrapolaciones a otros sistemas de IA, que deben tratarse como hipótesis.

## 1. Investigar las preguntas de compradores

- Capturar problemas, lenguaje y preguntas reales en ventas, soporte y entrevistas; asignarlas a secciones/páginas. No producir cien páginas sintéticas sin valor ni experiencia propia.
- Para cada página: objetivo del lector, respuesta principal clara, autor/empresa responsable, evidencia y fecha de actualización si importa, CTA contextual y enlace interno útil.
- Definir arquitecturas semánticas: títulos HTML, rutas canónicas, navegación real, metadatos, contenido textual útil en HTML, imágenes/video con alternativas, hreflang recíproco cuando sea sitio multilingüe.
- Evitar duplicación masiva, contenido de IA a escala sin valor, reseñas inventadas, FAQs sintéticas irrelevantes o schema que contradice texto visible.

## 2. Lo que Google sí dice en 2026

De [Google Search Central, AI features](https://developers.google.com/search/docs/appearance/ai-features) y [guía de optimización para AI Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide):

- No existe un requisito especial de markup o archivo de texto «AI» para aparecer en AI Overviews/Mode de Google. No instalar `llms.txt` o schema inventado como requisito de posicionamiento.
- Seguir fundamentos: rastreo permitido, arquitectura enlazada, contenido textual útil y confiable, buena experiencia, recursos multimedia pertinentes, datos estructurados que correspondan a texto visible.
- La indexación y aparición no están garantizadas; registrar impresiones/consultas cuando Search Console lo permita, no prometer ranking ni citas en respuestas.
- El contenido JavaScript-only puede añadir complejidad de rastreo; comprobar versión HTML real servida.

**Hipótesis Studios.Bit para otros buscadores de respuesta:** páginas que contestan preguntas específicas con claridad, fuentes visibles y datos verificables pueden facilitar comprensión, pero el efecto en cada proveedor no está demostrado sin observación por motor. No vender «primer lugar en ChatGPT».

## 3. Checklist técnico que se puede probar

| Área | Comprobación | Evidencia |
|---|---|---|
| Acceso | robots.txt y `noindex` coherentes por ambiente; staging no indexable; prod rastreable según permiso | URL/headers/captura |
| Descubrimiento | Sitemap y enlaces internos relevantes; no rutas huérfanas críticas | Crawl/report |
| Identidad | title, description, H1, canonical y OG específicos, sin duplicación grave | HTML por ruta |
| Idiomas | traducción real, navegación ES/EN, hreflang recíproco cuando aplica | Muestras por locale |
| Estructura | datos estructurados válidos **solo del tipo soportado**, coherentes con contenido visible | Validador + código |
| Multimedia | alt/captions/transcript según contenido, tamaño/carga razonables | Página + prueba |
| Conversión | CTA → evento servidor/agenda/formulario → confirmación y contacto alternativo | Traza E2E |
| Salud | errores 404/500, redirecciones, TLS y contenido principal accesible | Reporte de rutas |

## 4. Analítica diseñada desde la pregunta, no desde el pixel

### Modelo mínimo

`visitante elegible → visita página → entiende oferta → inicia contacto → envío confirmado → lead cualificado → cita realizada → cliente`.

Los pasos finales requieren datos de negocio/CRM bajo autorización. No enviar datos personales identificables a analytics sin base y configuración apropiada. Nunca publicar datos de clientes en capturas de dashboards de marketing.

**Evento recomendado** si se usa GA4: [`generate_lead`](https://developers.google.com/analytics/devguides/collection/ga4/reference/events) cuando se confirma una solicitud real, no al pulsar botón ni cuando falla backend. Otros eventos pueden ser propios, documentados y deduplicados. Para formularios duplicados, correlacionar `submission_id` interno sin exponer email/telefono al proveedor de analítica.

Consentimiento: [Google Tag Platform](https://developers.google.com/tag-platform/security/guides/consent) documenta estados de sus tags; elegir solución apropiada y revisión legal por país/cliente. No confundir la guía técnica de Google con cumplimiento legal completo.

## 5. Tablero de desempeño a 7/30/90 días

| Indicador | Qué ayuda a responder | Precaución |
|---|---|---|
| Leads confirmados y cualificados | ¿El sitio ayuda al negocio? | Depende de operaciones/seguimiento |
| Tasa de error de contacto | ¿Perdemos solicitudes por fallos? | Necesita eventos de error correctamente tratados |
| Visitas de fuentes identificadas | ¿Qué canales atraen interés? | Tráfico sin consentimiento o atribución incompleta |
| Consulta/impresión orgánica | ¿Nos encuentra el mercado? | No existe promesa de indexación |
| Tiempo a respuesta comercial | ¿El proceso pierde oportunidades? | Se mide fuera del sitio también |
| Rendimiento p75 y tareas reales | ¿La experiencia funciona en dispositivos? | Campo vs laboratorio diferenciados |

**Medir antes/después no demuestra causalidad** si cambian campañas, precios, oferta, estacionalidad o infraestructura simultáneamente. Para experimentos A/B usar [guía UX/CRO](UX_INVESTIGACION_CRO.md) y [plantilla](../templates/EXPERIMENTO.md).

## 6. Oferta comercial honesta

- Incluir SEO técnico de base y estructura del contenido según contrato.
- Ofrecer mantenimiento de contenido, Search Console, métricas y mejoras como servicio continuo **si tenemos capacidad real**.
- Informar límites: actualización del buscador, competencia, presupuesto, ritmo de publicación y tiempo de maduración.
- No prometer leads, ventas, citas, primeros lugares ni tráfico de IA.

Fuentes adicionales: [Google Search Essentials](https://developers.google.com/search/docs/essentials), [Google, contenido útil](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [GOV.UK medir servicios](https://www.gov.uk/service-manual/service-standard/point-10-define-success-publish-performance-data).
