# Ingeniería frontend escalable — guía para Codex

**Revisado: 2026-11-18.** Complementa la identidad y UX del cliente, la skill de diseño de sitios y las normas aplicables. No impone React, Next.js o un framework por defecto.

## Bibliografía primaria
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — estándar W3C; definir nivel objetivo por proyecto y comprobarlo, no solo ejecutar un escáner.
- [W3C WAI ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) — patrones, roles y teclado; preferir semántica HTML nativa antes de recrear controles.
- [web.dev Core Web Vitals](https://web.dev/articles/vitals) — documentación técnica de LCP, INP y CLS; campo p75 vs pruebas sintéticas.
- [React: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) — documentación oficial **solo para proyectos React** sobre derivación de estado y efectos.
- [MDN Progressive Enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement) — principio de acceso básico y robustez.
- [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) — capa de protección al renderizar contenidos y cargar terceros.
- [Google Search Central SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) — si la web necesita indexación.

## 1. Diseño funcional antes del framework
- Determinar tareas, semántica, navegación, rutas, idiomas, contenido, formularios, validaciones y estados: carga, vacío, pendiente, error, sin conexión, éxito confirmado y permiso denegado.
- Crear tokens de color/tipo/espacio, componentes con responsabilidades pequeñas y patrones reutilizables **por necesidad real**. No convertir una sola página en design system gigantesco.
- Priorizar HTML y enlaces/formularios nativos; elegir SSG/SSR/CSR según contenido, frescura, coste de JS, SEO y hosting. Describir qué ocurre sin JS.
- Separar: UI presentacional, estado de interacción, acceso a datos/transportes y contrato compartido. Evitar solicitudes de red o lógica de autorización escondidas en el componente visual.
- Control de acceso frontend solo mejora UX; autorización real siempre en backend.

## 2. Rendimiento y presupuestos de carga
Medir Core Web Vitals reales cuando hay tráfico suficiente: **LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1** en p75, segmentando móvil y escritorio (metas de la guía web.dev; no son certificación). Sin RUM/CrUX: informar medición de laboratorio como **estimación**, no evidencia de campo.
- Presupuestar imágenes responsive, formatos/codificación apropiados, dimensiones para evitar CLS, poster y estrategia de carga de video, lazy load **debajo** del pliegue y priorización del elemento LCP.
- Reducir JS enviado/ejecutado; división por rutas o funcionalidades cuando aporte; posponer terceros y medir su impacto. Animaciones preferentemente transform/opacity, sin bloquear interacción.
- Medir con red/CPU representativas y dispositivos reales cuando sea posible; registrar baseline y comparación tras cambios. Evitar «100 Lighthouse = funciona perfecto».

## 3. Accesibilidad y experiencia
- Objetivo recomendado para interfaces públicas: WCAG 2.2 **AA**, sujeto a alcance y norma local aplicable. Probar teclado/foco visible, navegación lógica, zoom/reflow, lector, labels/errores de campo, contraste y elementos táctiles.
- Reducir movimiento con `prefers-reduced-motion`; no hacer que contenido vital dependa de animación, scroll o video.
- Menús, modales, combobox y tabs deben manejar foco/escape/estados con patrones APG cuando se implementen; usar componentes nativos cuando existan.
- En contenido ES/EN: `lang`, rutas coherentes, metadata por idioma y traducción completa de botones/errores, sin mezclar textos.
- Validación de formularios explicativa, sin perder datos al fallar, y éxito solo tras confirmación del servidor.

## 4. Estado, datos y fallos
- Diferenciar estado local de interfaz, URL navegable, estado servidor y persistencia; no duplicar datos derivados. En React evitar efectos de sincronización innecesarios según guía React.
- Llamadas de red: cancelación/timeout según plataforma, estados claros, refetch/retry medido, y **no** repetir escrituras no idempotentes sin acuerdo backend.
- No exponer tokens secretos, claves de DB, endpoints privados o payloads sensibles en HTML, source maps públicos o telemetría. Datos de prueba rotulados.

## 5. Matriz de QA mínima
| Área | Prueba |
|---|---|
| Funcional | Ruta crítica completa: navegar → acción → validación → confirmación real → recuperación |
| Responsive | 320, 390, 768, 1024, 1440 px y contenido largo; móvil real si está disponible |
| Accesibilidad | Teclado, tab, foco, lector de pantalla, zoom 200–400 %, reduced motion |
| Rendimiento | LCP/INP/CLS de campo cuando existan y ensayo sintético etiquetado |
| Robustez | Red lenta/offline, 4xx/5xx, error de validación, doble clic, timeout |
| Seguridad | XSS en contenido no fiable, no secretos en bundle, headers y cookies adecuados |
| Calidad | Typecheck, lint, pruebas de componentes de interacción y E2E |

Entregar capturas, reportes, rutas y comandos reales de verificación, fallos pendientes y trade-offs, sin confundir screenshots con E2E.
