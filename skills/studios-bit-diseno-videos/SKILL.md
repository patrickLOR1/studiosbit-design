---
name: studios-bit-diseno-videos
description: Guion, dirección, animación, render y QA técnico de Reels, TikTok y Shorts para Studios.Bit y clientes, con HyperFrames/GSAP, especificaciones fijas de exportación, zonas seguras y control de estilos para no repetir. Úsala cuando se pida un Reel, TikTok, Short, video animado, guion o portada de video.
---

# Diseño y producción de videos — Studios.Bit

**Ámbito:** idea → gancho → guion por segundos → dirección de arte → animación (HyperFrames + GSAP) → render → QA técnico → portada y copy → entrega.

Esta skill tiene dos mitades igual de obligatorias: **la creativa** (que el video diga algo y detenga el scroll) y **la técnica** (que el archivo salga perfecto en el celular). Un video bonito que se corta en la interfaz de Instagram o que suena saturado no está terminado.

---

## 1. Antes de empezar (5 preguntas)

Responde por escrito antes de animar nada:

1. **¿Para quién es?** (dueño de clínica, inmobiliaria, pyme de servicios…)
2. **¿Qué tiene que pensar o hacer al terminar?** Una sola acción: guardar, comentar, escribir "WEB", visitar el perfil.
3. **¿Cuál es la idea en una frase?** Si no cabe en una frase, son dos videos.
4. **¿Qué estilo visual usarás?** Revisa [estilos usados](../../references/ESTILOS_USADOS.md) y elige uno que **no** esté en las últimas 10 piezas.
5. **¿Es real o conceptual?** Si el ejemplo no es un cliente real, el video muestra la etiqueta **"Ejemplo conceptual"** o **"Concepto / rediseño no oficial"**.

---

## 2. Estructura y guion

**Esqueleto base** (ajusta los tiempos al contenido, no al revés):

| Tramo | Segundos | Qué pasa |
|---|---|---|
| Gancho | 0–2 | Pregunta, tensión o imagen inesperada. Texto en pantalla desde el primer cuadro. |
| Contexto | 2–6 | El problema, en palabras del cliente. |
| Demostración | 6–18 | La transformación visible: antes → después, error → corrección, idea → resultado. |
| Aprendizaje | 18–24 | La regla que se lleva el espectador. |
| Cierre | últimos 2–3 s | Logo real + **un solo** CTA. |

**Reglas de guion**
- Una idea por video. Máximo **3 puntos** en una lista.
- Frases de **≤ 8 palabras** en pantalla; cada texto visible **≥ 1.5 s** (más 0.3 s por cada palabra extra después de 5).
- Español de México, sin tecnicismos. Si hace falta un término técnico, se explica en la misma pantalla.
- Debe entenderse **sin sonido**. El audio refuerza, no explica.
- Diseña el final para que conecte con el inicio (loop natural).

**Entregable de guion:** tabla con segundo, texto en pantalla, animación, transición y audio. Si el usuario va a grabar, añade lista de tomas suficiente para editar sin preguntar.

---

## 3. Dirección de arte

- **Un estilo por video** y llevado hasta el final (no mezclar cinco estéticas sin intención). Excepción: piezas cuyo concepto *es* el cambio de estilo; ahí cada cambio debe ser una transición diseñada.
- **Marca Studios.Bit:** negro `#0B0B0D`, blanco `#F5F5F5`, gris `#9CA3AF`, acento naranja `#FF6A00`, tipografía **Manrope**. El naranja es acento (CTA, subrayado, cuadrito), no fondo de todo. En videos de clientes se usa **su** marca, nunca la nuestra.
- **Logo:** usar el kit oficial `StudiosBit_Kit_Logos` (lo comparten los socios; colócalo en `brand/StudiosBit_Kit_Logos/` de tu copia local). Usar los **PNG**: los SVG actuales tienen curvas segmentadas y se ven cortados a gran tamaño. Sin redibujar, estirar, rotar ni cambiar colores. Tamaño mínimo en pantalla: 160 px de ancho.

  | Fondo | Archivo |
  |---|---|
  | Oscuro | `09_Horizontal_blanco_transparente.png` o `11_Isotipo_blanco.png` |
  | Claro | `08_Horizontal_negro_transparente.png` o `13_Isotipo_transparente.png` |
  | Naranja / cierre | `12_Isotipo_naranja.png` |

  Si no encuentras el kit, **detente y pídelo**; no recrees el logo.
- **Arte con código:** SVG, CSS, Canvas o WebGL. Sin imágenes de stock, sin capturas de marcas de terceros, sin imitar a un artista, personaje o videojuego reconocible.
- **Contraste:** texto contra fondo ≥ 4.5:1. Texto sobre imagen o textura siempre con placa o sombra sólida.
- **Tamaños mínimos de texto (a 1080 px de ancho):** titular 72 px+, texto de apoyo 44 px+, etiquetas 32 px+. Nada por debajo de 28 px.

---

## 4. Especificaciones técnicas fijas

Toda pieza vertical se entrega con estas especificaciones salvo que el brief diga otra cosa:

| Parámetro | Valor |
|---|---|
| Resolución | **1080 × 1920** (9:16) |
| Cuadros por segundo | **30 fps constantes** |
| Duración | 7–45 s (ideal 12–30 s) |
| Contenedor / códec | MP4, **H.264 High**, `yuv420p`, `+faststart` |
| Calidad | CRF 18–20 (o ~8–12 Mbps); nunca menos de 6 Mbps |
| Audio | AAC 48 kHz estéreo, 192 kbps; **−14 LUFS** integrados, picos ≤ −1 dBTP |
| Sin audio | Si no lleva audio, incluir pista silenciosa (algunas plataformas rechazan video sin pista) |
| Peso | Menor a 100 MB |
| Portada | PNG/JPG 1080 × 1920, texto dentro de la zona central 1080 × 1350 |

**Zonas seguras (no colocar texto, logo ni CTA aquí):**
- **Arriba:** 250 px (barra de estado, nombre de cuenta).
- **Abajo:** 400 px (caption, botones, música).
- **Derecha:** 140 px (iconos de like, comentar, compartir).
- **Izquierda:** 60 px de margen.

Zona útil resultante para texto: x 60–940, y 250–1520.

**Música:** solo licenciada para uso comercial o añadida después dentro de la app. Si el usuario dice que pondrá la música en Instagram, **no** incrustes música.

---

## 5. Producción con HyperFrames + GSAP

1. Preparación: confirmar Node 22+, FFmpeg y HyperFrames (`npx skills add heygen-com/hyperframes`). Usar `/hyperframes` y `/gsap`. Si falta algo, decir qué se instalará antes de hacerlo.
2. Crear proyecto: `npx hyperframes init <nombre>`; configurar 1080 × 1920 a 30 fps desde el inicio.
3. Animar con una **línea de tiempo GSAP única** controlada por el reloj del render (sin `setTimeout`, `Date.now()` ni animaciones CSS independientes que no se sincronicen con el cuadro).
4. Curvas: entradas `power3.out`/`expo.out` (0.4–0.7 s), salidas más cortas que las entradas. Evitar rebotes salvo que el estilo lo pida.
5. Fuentes cargadas localmente o con `font-display: block` y espera a `document.fonts.ready` antes del primer cuadro.
6. Previsualizar con `npx hyperframes preview` y **pedir aprobación del preview** antes del render final.
7. Render: `npx hyperframes render`. Si el MP4 resultante no cumple la tabla del punto 4, re-codificar con FFmpeg:

```bash
ffmpeg -i render.mp4 -r 30 -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 -preset slow \
  -c:a aac -b:a 192k -ar 48000 -af loudnorm=I=-14:TP=-1:LRA=11 -movflags +faststart final.mp4
```

---

## 6. QA técnico obligatorio (antes de entregar)

Ejecutar sobre el archivo final:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,codec_name,pix_fmt -of default=nw=1 final.mp4
ffprobe -v error -show_entries format=duration,size,bit_rate -of default=nw=1 final.mp4
ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12   # volumen (si hay audio)
ffmpeg -i final.mp4 -vf "fps=1,scale=270:-1,tile=6x3" -frames:v 1 hoja_contacto.png   # revisión visual
```

**Checklist (todo debe ser "sí")**
- [ ] 1080 × 1920, 30 fps, H.264, yuv420p.
- [ ] Duración y peso dentro de rango.
- [ ] Audio en −14 LUFS ± 1 o pista silenciosa.
- [ ] Ningún texto, logo o CTA dentro de las zonas seguras (revisar la hoja de contacto con una plantilla de zonas encima).
- [ ] Cada texto se lee completo a velocidad normal; sin palabras cortadas ni encimadas.
- [ ] Ortografía y acentos revisados (¿, ¡, á, é, í, ó, ú, ñ).
- [ ] Logo real, proporciones intactas.
- [ ] Sin cuadros negros, saltos o parpadeos al inicio y al final.
- [ ] Etiqueta "Ejemplo conceptual" visible si aplica.
- [ ] Sin clientes, cifras, testimonios, precios ni resultados inventados.
- [ ] El estilo no se repite respecto a [estilos usados](../../references/ESTILOS_USADOS.md); registrar el nuevo.

Si algo falla, corregir y volver a pasar el checklist completo.

---

## 7. Entrega

Por cada pieza entregar:
- `NN · Reel · <Etiqueta> · <Tema>.mp4` (NN = número consecutivo; etiquetas: Presentación, Web, Marketing, Redes, Branding, Contacto).
- `NN · Portada · <Tema>.png`.
- Texto para publicar (2–4 líneas + 1 CTA) y **5 hashtags** relevantes en español.
- Texto alternativo de una línea.
- Resumen de QA: salida de `ffprobe`, LUFS y la hoja de contacto.
- Línea nueva en [estilos usados](../../references/ESTILOS_USADOS.md).

---

## 8. Series originales de Studios.Bit

- **Bit Audit:** problema observado → corrección conceptual → por qué mejora (sin ridiculizar a nadie).
- **1 Bit de Diseño:** principio → antes/después propio → cómo aplicarlo.
- **Dentro del Estudio:** brief → opciones → decisión → resultado.
- **Mitos de negocios digitales:** mito → explicación con contexto y límites.
- **Construimos en Codex:** concepto → prototipo → QA, sin prometer resultados.

## 9. Referencias

Leer [contenido y formatos](../../references/CONTENIDO_Y_FORMATOS.md), [índice categorizado](../../references/INDICE_POR_CATEGORIA.md) y las fichas SB pertinentes (SB-04, 08, 10, 11–13, 17, 19, 22, 25–27, 29–35). Elegir máximo dos patrones por pieza y explicar qué **no** se copiará.

**Copyright y honestidad:** no reutilizar audios, clips, proyectos ni voces de los creadores del catálogo; son referencias, no material autorizado. Las pruebas de IA de terceros no demuestran capacidades propias.
