# Fundamentos de diseño web y UX — Evidencia y reglas para Codex

**Edición:** 2026-11-18. **Alcance:** dirección de arte, contenido, navegación, interacción, formularios, responsive y validación. Esta bibliografía no reemplaza pruebas con usuarios reales ni la identidad del cliente.

## Cómo interpretar la evidencia

| Clase | Significado | Tratamiento |
|---|---|---|
| **E1 · Norma técnica** | Criterio formal verificable (p. ej., WCAG 2.2) | Tratar los requisitos aplicables como puertas de calidad; comprobar con pruebas manuales y automáticas |
| **E2 · Investigación, autor y literatura** | Modelo explicativo o heurística de autor reconocido | Adaptar al problema y verificar con usuarios; no presentar como ley inmutable |
| **E3 · Sistema de diseño / guía oficial** | Patrones probados y documentados por su equipo | Adaptar, respetar licencia y comprobar que sirven a la audiencia |
| **E4 · Video de referencia SB** | Observación visual de terceros | Inspiración estética opcional, nunca evidencia de conversión ni permiso para copiar |

**Orden de resolución:** necesidades y restricciones reales del cliente → seguridad/privacidad/accesibilidad exigibles → evidencia verificable → hipótesis de diseño → recurso de inspiración SB. Si dos heurísticas chocan, documentar el compromiso y validar, no elegir por moda.

## Literatura y fuentes originales

| ID | Fuente primaria | Idea operacional derivada | Clasificación |
|---|---|---|---|
| D01 | [Donald A. Norman, The Design of Everyday Things, edición revisada (2013), página del autor](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/) | Indicar qué acciones son posibles, qué acaba de ocurrir, cómo deshacer y cómo funciona el sistema; usar señales comprensibles | E2 · libro |
| D02 | [Jakob Nielsen, 10 Usability Heuristics for User Interface Design (1994), NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/) | Visibilidad de estado, coherencia, prevención/recuperación de errores, reconocimiento en vez de memoria, control y ayuda contextual | E2 · heurísticas |
| D03 | [Rosenfeld, Morville y Arango, Information Architecture for the Web and Beyond, 4.ª ed. (2015), O’Reilly](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/copyright-page01.html) | Diseñar categorías, etiquetas, navegación, búsqueda y relaciones a partir de tareas e información del usuario | E2 · libro |
| D04 | [Ethan Marcotte, Responsive Web Design (2010), A List Apart](https://alistapart.com/article/responsive-web-design/) | Componer con rejillas e imágenes flexibles y adaptaciones a rangos de pantalla; el contenido determina la disposición | E2 · artículo del autor |
| D05 | [Jason Pamental, Responsive Typography (2014), O’Reilly](https://www.oreilly.com/library/view/responsive-typography/9781491907085/) | Ajustar escala, proporción y rendimiento tipográfico según contexto; no usar tamaños estáticos como única solución | E2 · libro |
| D06 | [GOV.UK Design System, componentes](https://design-system.service.gov.uk/components/) y [guía de formularios](https://www.gov.uk/service-manual/design/form-structure) | Etiquetas claras, preguntas agrupadas, validaciones recuperables; investigar antes de adaptar patrones | E3 · guía pública |
| D07 | [W3C, WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Requisitos verificables sobre percepción, operación, comprensión y robustez; objetivo inicial para proyectos web: nivel AA cuando corresponda | E1 · recomendación W3C |
| D08 | [W3C, ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Patrones de teclado, roles, estados y foco para controles complejos; preferir HTML semántico nativo cuando basta | E3 · guía informativa, no norma |
| D09 | [web.dev, Web Vitals](https://web.dev/articles/vitals) | Medir LCP, INP y CLS en campo, en percentil 75; contrastar resultados de laboratorio con usuarios reales | E3 · guía técnica |
| D10 | [Google Search Central, SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | Arquitectura navegable, URL claras, títulos útiles y contenido auténtico; no prometer posiciones en buscadores | E3 · guía oficial |
| D11 | [MDN, Progressive Enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement) | Contenido y acciones esenciales disponibles antes de añadir efectos y mejoras dependientes de JS | E3 · documentación |
| D12 | [Nielsen Norman Group, Recognition and Recall](https://www.nngroup.com/articles/recognition-and-recall/) | Mantener opciones/contexto visibles; evitar que el usuario memorice códigos, estados o pasos entre pantallas | E2 · explicación de UX |

La página del editor o del autor verifica la existencia y enfoque de un libro; **no** implica acceso integral al contenido de pago ni una revisión de cada capítulo. Los puntos anteriores son síntesis de aplicación, no citas textuales.

## Reglas prácticas para nuevos proyectos

### Investigación y estructura
- **UX-01 (D01–D03):** Antes de dibujar, documentar quién usa el sitio, sus tres tareas prioritarias, necesidades de contenido, dispositivos, idiomas y riesgos. No inventar entrevistas ni datos de negocio.
- **UX-02 (D03):** Entregar sitemap, nombres de navegación comprensibles, jerarquía de encabezados, URLs legibles y caminos hacia cada tarea/CTA. Validar etiquetas con el lenguaje del cliente; no imponer la jerga de la agencia.
- **UX-03 (D02, D12):** Mantener orientación y estado visibles: página activa, filtros activos, progreso, confirmaciones, estados vacío/cargando/error. Reducir memoria necesaria entre pasos.

### Composición, texto e identidad
- **UX-04 (D01, D02, D05):** Definir jerarquía editorial con título que comunique beneficio, párrafos breves, escalas tipográficas consistentes, ancho de lectura razonable, contraste y un CTA principal claramente distinguible. No hay una escala única obligatoria.
- **UX-05 (D03, D05):** Establecer tokens de espaciado, tipografía, color por función, radios e iconografía según la marca. Usar evidencia/ejemplos propios. Evitar elementos repetitivos sin función.
- **UX-06 (D04):** Diseño responsive por prioridades de contenido, no por reducir el desktop. Probar 320, 390, 768, 1024, 1440 px y zoom; sin scroll horizontal accidental.

### Interacción y formularios
- **UX-07 (D01, D02, D06):** Controles reconocibles y accesibles por teclado/tacto; mostrar feedback inmediato, errores junto al campo, instrucciones concretas y recuperación. No usar efectos como única indicación de estado.
- **UX-08 (D02):** Acciones destructivas requieren prevención, confirmación según riesgo y recuperación cuando sea posible. No bloquear al usuario en un paso, overlay o animación.
- **UX-09 (D06):** Formularios con etiquetas persistentes, campos necesarios, validación cliente y servidor, mensajes útiles y estado de envío/reintento, sin prometer entrega si el backend no confirmó.
- **UX-10 (D07, D08):** Priorizar HTML semántico, orden de foco, contraste, nombres accesibles, alternativas de movimiento y pruebas de lector de pantalla; no declarar conformidad WCAG solo con una auditoría automatizada.

### Movimiento, medios, SEO y rendimiento
- **UX-11 (D01, D07):** El motion explica cambio/continuidad. Respetar prefers-reduced-motion, permitir pausa de animaciones relevantes y conservar funcionalidad sin video.
- **UX-12 (D09):** Como objetivos de rendimiento web orientativos: LCP ≤ 2.5 s, INP ≤ 200 ms y CLS ≤ 0.1 en percentil 75 de tráfico real; separar medición de laboratorio, estimación y campo.
- **UX-13 (D10, D11):** Priorizar contenido HTML enlazable/útil y navegación estable; elegir renderizado, metadatos, idioma, canonicals, sitemaps y datos estructurados solo según arquitectura real. Evitar claims SEO/AEO no demostrados.
- **UX-14 (D04, D07, D11):** Para video integrado: definir propósito narrativo, poster, tamaño/adaptación, controles accesibles, subtítulos cuando aplique, lazy load, fallback, audio no intrusivo y pruebas móviles; que el contenido clave no dependa de reproducirlo.

## Matriz mínima de comprobación por pantalla
- [ ] Se comprende qué ofrece/permite y cuál es la acción principal sin depender de efectos.
- [ ] El sitemap, la etiqueta y la ruta permiten encontrarla desde navegación normal.
- [ ] Diseño, foco y contenido funcionan en móvil, escritorio, zoom y teclado.
- [ ] Carga, error, vacío, éxito y reintento tienen estados diseñados y probados.
- [ ] No hay datos ficticios presentados como reales ni productos/casos ajenos apropiados.
- [ ] Se probaron de manera manual los criterios WCAG aplicables, además del test automatizado.
- [ ] Se registraron resultados, capturas, limitaciones y cuestiones pendientes.

**Aplicación:** usar este documento con [Arquitectura web](ARQUITECTURA_WEB_GUIA.md) y la [skill de diseño web](../skills/diseno-sitios-web/SKILL.md). Las fichas SB solo aportan inspiración opcional.
