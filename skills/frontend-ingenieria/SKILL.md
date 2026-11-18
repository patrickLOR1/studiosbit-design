---
name: studios-bit-frontend-ingenieria
description: Construir y auditar frontend escalable, responsive, accesible y rápido en proyectos web de Studios.Bit y clientes. Activar al decidir SSR/SSG/CSR, componentes, estado, formularios, i18n, rendimiento Core Web Vitals, UX y QA visual/funcional. Tecnología agnóstica; React solo si el stack lo usa.
---

# Frontend de calidad, accesible y mantenible

**Objetivo:** interfaces originales, utilizables y medibles, con complejidad proporcional. Utilizar junto a diseño de sitios si el trabajo incluye experiencia visual; junto a arquitectura web para desarrollo de una aplicación.

## Flujo de trabajo
1. **Brief + tareas:** definir usuario, flujo crítico, sitemap/rutas, contenido, dispositivos, idiomas, estados y requisitos de accesibilidad.
2. **Estrategia técnica:** elegir renderizado por SEO/frescura/uso de JS; componentes pequeños, tokens semánticos, tipado donde exista, separación de transporte y presentación, ninguna clave secreta en navegador.
3. **Rendimiento:** medir baseline y presupuestar video, imágenes, LCP, división de JS y terceros; no forzar animación cara ni hidratación indiscriminada.
4. **Interacción completa:** loading, error, vacío, sin permisos, éxito real, red lenta, doble clic; formularios que conserven valores y no mientan sobre envíos.
5. **Accesibilidad:** HTML semántico, teclado, foco, reflow, labels y contraste; patrón APG si hace falta; reduced motion. Objetivo WCAG 2.2 AA cuando se acuerde, con pruebas, no una etiqueta.
6. **QA:** 320/390/768/1024/1440 px; unidad/componente/E2E de flujos, dispositivo real cuando esté disponible, p75 de campo para Core Web Vitals cuando existan datos, distinguir laboratorio.

## Referencias que debes leer
[Ingeniería frontend y fuentes oficiales](../../references/INGENIERIA_FRONTEND.md); [fundamentos de UX](../../references/FUNDAMENTOS_DISENO_LITERATURA.md). Complementar con [diseño de sitios](../diseno-sitios-web/SKILL.md) y [motion](../motion-interacciones/SKILL.md) si corresponde. React: leer documentación oficial sobre efectos **solo si React aplica**.

## Salida
Rutas y estados, componentes y responsabilidades, decisiones de renderizado, QA de teclado/lector/responsive, evidencia de LCP/INP/CLS correctamente etiquetada, riesgos de terceros y reporte de cambios. Evitar prometer rendimiento por un mockup.
