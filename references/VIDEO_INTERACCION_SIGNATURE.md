# Studios.Bit Signature Experience — narrativa, video y motion con propósito

**No es una colección de efectos ni un clon visual.** Es un sistema para que una web se sienta distintiva y **comunicativamente mejor**: el video demuestra, el movimiento explica y la interacción confirma. Requiere dirección artística propia de cada cliente y pruebas en condiciones reales.

## Índice
1. Selección del medio
2. Composición de video integrado
3. Interacciones y estados
4. Accesibilidad
5. Presupuesto y pruebas
6. Criterios de aprobación

## 1. Decisión editorial por bloque

Antes de filmar o añadir WebGL/GSAP/scroll storytelling, definir:

| Pregunta | Buena respuesta | Señal de retirar el efecto |
|---|---|---|
| ¿Qué demuestra? | Producto, proceso, contexto real, resultado autorizado | Solo rellena espacio o parece un stock genérico |
| ¿Qué debe entenderse sin sonido/movimiento? | Beneficio, navegación y CTA siguen presentes | El usuario tiene que esperar a terminar animación |
| ¿Qué gana al interactuar? | Compara, revela detalle, cambia estado, decide | Solo hover ornamental en un control crítico |
| ¿Qué cuesta? | Tiempo, bytes, CPU, licencia, producción y mantenimiento medidos | Compite con LCP/INP, batería o legibilidad |
| ¿Cómo falla? | Poster, contenido estático, navegación, reintento | Pantalla negra o CTA bloqueado |

### Tres modos de uso

- **Narrativa ambiente** (hero): video breve propio/licenciado, sin audio indispensable, loop discreto, poster y contenido de texto real. El medio es decorativo, nunca el único portador de mensaje.
- **Demostración de producto** (caso/feature): controles explícitos, subtítulos/alternativa accesible y pasos verificables. No simular funcionalidades como si existieran.
- **Estudio de caso** (evidencia): contexto → decisión → artefacto real → resultados medidos y atribución prudente. Si no hay datos, explicar el proceso, no inventar ROI.

## 2. Arquitectura de un hero donde el video se vea integrado

1. Una cuadrícula editorial: columna de promesa + CTA y escena visual que responde a esa promesa; o fondo visual con gradiente y contraste realmente verificado.
2. `aspect-ratio` y tamaños definidos antes de descargar para evitar CLS. Poster del mismo encuadre/estilo que video, transición sin flash. Video en `object-fit: cover` solo si el sujeto tolera recorte; para demos de UI, preferir `contain` o dispositivo/marco legible.
3. Mantener títulos y acciones como HTML accesible **por encima del video**, no quemados dentro del metraje. Móvil puede reordenar texto primero y video después.
4. Política de reproducción: no exigir autoplay; video decorativo solo muted/playsinline, pausable y degradable. Audio y demostraciones funcionales requieren control y contexto accesible.
5. Escena debe tener un primer frame claro incluso sin video. Usar compresión moderna compatible con audiencia y ruta alterna cuando el navegador no soporte el formato elegido.
6. Cargar video secundario cuando se acerque al viewport y pausar fuera; **no diferir indiscriminadamente el poster LCP del hero**. Medir competidores de ancho de banda (fuentes, JS, imagen).

### Esquema de storyboard de sitio (ejemplo de método)

| Capítulo | Texto HTML permanente | Visual | Interacción útil | Fallback |
|---|---|---|---|---|
| 1. Promesa | ¿Qué hacemos y para quién? | Escena breve o poster | CTA y navegación | Imagen inmóvil |
| 2. Prueba | Evidencia de proceso/caso | Demo visual sin secretos | Reproducir/pausar, abrir caso | Capturas + texto |
| 3. Método | Pasos visibles | Microtransiciones coherentes | Navegar etapas, volver atrás | Lista semántica |
| 4. Acción | Servicio, alcance, contacto | Motion solo de feedback | Formulario/agenda con éxito real | Contacto alternativo |

**Firma original:** sistema tipográfico, encuadres, iluminación, textura, transiciones y ritmo creados por el proyecto. Las referencias SB-53 y otras sirven para estudiar problemas, no para recrear tomas/pixels.

## 3. Microinteracciones como contratos de estado

Definir para cada componente:

```
trigger → state_before → state_after → focus_target → interruption
        → reduced_motion → touch_equivalent → disabled/error → test
```

- Navegación animada: `aria-current`/estado activo inequívoco, foco estable, URL correcta, Back del navegador funcional.
- Acordeón: usar HTML `details`/`summary` cuando cubra tarea; si es custom, controles/relación de estado APG probados.
- Carrusel: no autoplay imperceptible, controles de pausa y avance, gestos no exclusivos, orden de lectura estable; evitar que el carrusel impida acceder a CTA.
- Glow/cursor: capa no interactiva (`pointer-events: none`), decorativa, desactivada táctil/reduced-motion y sin esconder foco.
- Scroll: preservar scroll nativo y anclas, no bloquear/restablecer scroll por efecto. Evitar escenas que revelan texto únicamente al entrar en viewport.
- Error de formulario: feedback textual asociado al campo, conservar valores y ofrecer reintento sin duplicación; nunca celebración de «éxito» antes de respuesta válida.

## 4. Accesibilidad audiovisual: mapa de decisión

| Tipo | Regla de contenido |
|---|---|
| Video meramente decorativo | Información completa en HTML; ocultar medio a lector si redundante, opción de pausar, alternativa inmóvil |
| Video informativo con voz/sonidos | Subtítulos precisos y controles accesibles; transcripción cuando aplique |
| Información visual no narrada | Descripción audiovisual o alternativa textual equivalente según contenido y WCAG correspondiente |
| Video de UI | Evitar cursor diminuto; crop/zoom que permita leer; describir acciones con texto y narración |

No declararse WCAG AA porque existe un botón de pausa. Ver [W3C WAI medios accesibles](https://www.w3.org/WAI/media/av/) y [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## 5. Presupuesto y métricas sin dogmas

- Objetivos Web Vitals de referencia: **LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1** al p75 de datos reales cuando sean suficientes. Son umbrales recomendados, no el resultado automático de comprimir un video.
- Establecer presupuesto por página (bytes video/imagen, JS, terceros), medir baseline en dispositivo real móvil/red razonable y documentar excepciones; no imponer un número de MB universal.
- Usar Lighthouse CI para regresión de laboratorio y RUM/CrUX cuando haya muestra. Anotar versión, red, dispositivo y condición de caché.
- Inspeccionar reducción de datos, red lenta, `prefers-reduced-motion: reduce`, texto 200 %, zoom, contraste, CPU limitada, Safari iPhone/Android físicos cuando disponibles.
- Un video que mejora estética pero frustra CTA, aumenta salto visual o induce mareo debe sustituirse o rediseñarse.

## 6. Gate Signature Experience

1. ¿La primera pantalla funciona sin video, sin sonido y con JavaScript limitado?
2. ¿El texto no se confunde con el plano y se mantiene legible en cada frame?
3. ¿Se puede pausar o reducir movimiento y acceder por teclado/touch?
4. ¿Carga sin bloqueo, recortes extraños, saltos de layout o jank visibles?
5. ¿Media/licencias/imagen de personas están autorizadas y atribuidas según contrato?
6. ¿El demo muestra capacidad real o dice «Proyecto conceptual»?
7. ¿La escena tiene argumento comercial y una salida hacia acción real?

### Fuentes originales y de fabricantes

- [W3C WAI medios accesibles](https://www.w3.org/WAI/media/av/), [transcripciones](https://www.w3.org/WAI/media/av/transcripts/)
- [web.dev video performance](https://web.dev/learn/performance/video-performance), [lazy loading video](https://web.dev/articles/lazy-loading-video)
- [MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion)
- [W3C APG](https://www.w3.org/WAI/ARIA/apg/), [GOV.UK diseño accesible](https://design-system.service.gov.uk/accessibility/)

**Prototipo reutilizable:** [plantilla de hero de video](../templates/VIDEO_HERO.md) con requisitos y pseudocontrato de componentes; no supone un asset ni un stack concreto.
