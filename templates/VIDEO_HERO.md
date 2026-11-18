# Patrón implementable — hero audiovisual sin depender de efectos

## Contrato de componente (válido con cualquier framework)

Props conceptuales: `poster`, `sources[]` con tipo y tamaño, `decorative`, `captionTrack`, `title`, `description`, `primaryAction`, `secondaryAction`, `allowAutoplay`, `reducedMotionFallback`, `ratio`.

## Semántica y estructura

1. El `h1`, descripción y CTA se renderizan en HTML antes de reproducir video; nunca dentro de un canvas/video.
2. Reservar espacio con `aspect-ratio` o dimensiones. Poster visual aprobado y alternativo con mensaje legible.
3. Video decorativo: `muted`, `playsinline`, `aria-hidden` si redundante, no reemplaza texto. Controles para pausar; respetar media query `prefers-reduced-motion` y dar imagen equivalente.
4. Video informativo: controles accesibles y subtítulos/descripción/transcripción según contenido. No ocultarlo de lector.
5. No cargar archivos de terceros ni usar imágenes de personas sin licencia/permiso. No poner keys en `src`.
6. Reactivar reproducción solo si el usuario/prefiere movimiento y el elemento está visible; no bloquear UI si `play()` rechaza.
7. Conectar CTA a una acción real y probar estados de error y éxito.

## Pseudocódigo de estados

```text
initial: show poster + HTML CTA; video optional
if reducedMotion or dataSaver or unsupported: remain poster; CTA works
if decorative and allowed and inViewport: try play; on reject remain poster
if pauseClick: pause and keep control keyboard-focusable
if leavesViewport: pause unless user explicitly requests continue
if mediaError: show poster and ordinary content; never blank hero
```

## Validación de aceptación

- Capturas de 320, 390, 768, 1024, 1440 px con el encuadre correcto.
- Pausa por teclado, `reduced-motion`, sin JavaScript, red lenta y sin video.
- Medición de LCP/CLS y budget móvil; contraste de texto sobre **todos los frames**, no solo poster.
- Aprobación de storyboard, derechos y fallback. Si el medio es decorativo, transcripción de información no necesaria porque no debe contener mensaje exclusivo.

Fuentes: [web.dev video](https://web.dev/learn/performance/video-performance), [W3C WAI](https://www.w3.org/WAI/media/av/).
