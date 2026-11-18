# UX Research + CRO — de intuición visual a decisiones observables

**Papel:** guía para [diseño web](../skills/diseno-sitios-web/SKILL.md), [director de proyecto](../skills/director-proyecto/SKILL.md) y [estrategia](../skills/estrategia-contenido/SKILL.md). CRO = optimización de conversión, **no** maximización ciega de clics. El objetivo es ayudar a personas a decidir bien.

## Índice
1. Modelo de investigación
2. Estructura de página y confianza
3. Testing cualitativo y cuantitativo
4. Experimentos confiables
5. Evidencia y decisión

## 1. Investigar la tarea, no solo la estética

Para una landing o sitio comercial, completar el mapa:

| Pregunta | Técnica ligera | Señal confiable |
|---|---|---|
| ¿Quién busca la solución? | Entrevistas con usuarios/clientes reales, ventas y soporte | Frases concretas, problemas repetidos, contexto |
| ¿Qué necesita saber para decidir? | Entrevista y mapa de objeciones | Preguntas y comparaciones frecuentes |
| ¿Qué hace ahora? | Observación de tarea y análisis de competidores permitidos | Paso, punto de atasco, alternativa usada |
| ¿Qué evidencia le genera confianza? | Prueba de prototipo con contenido real | Comprende alcance, costo orientativo, proceso y siguiente paso |
| ¿Qué pasa después de hacer clic? | Prueba E2E de CTA | Confirmación real, error recuperable, canal de contacto útil |

No inventar personas sintéticas como investigación real: pueden servir como hipótesis para organizar el brief y deben estar rotuladas.

## 2. Arquitectura persuasiva sin engaño

La primera pantalla debe responder **para quién es, qué problema resuelve y qué paso sigue**. No existe regla universal de «tres segundos» demostrada para cada industria: usarla como prueba interna de claridad, no dato científico.

Secuencia sugerida a validar:

1. Propuesta útil y específica, sin adjetivos vacíos.
2. Evidencia verificable: trabajos propios autorizados, proceso, resultados fechados o demostración real. Proyectos conceptuales señalizados.
3. Servicio y límites: qué incluye, cómo se trabaja, tiempos orientativos y responsabilidad del cliente.
4. Reducción de riesgo percibido: FAQ útil, soporte, privacidad visible, canal alternativo.
5. CTA persistente pero no invasivo; formulario breve con explicación de datos y estado posterior.

Evitar patrones oscuros: urgencia inventada, testimonios falsos, counters simulados, formularios disfrazados, opt-in preseleccionado y vías de salida obstruidas. Si una animación disminuye comprensión o tasa de finalización, retirarla.

## 3. Dos preguntas de investigación diferentes

### Diagnóstico cualitativo: ¿qué obstáculo existe?

- Preparar 3–5 tareas realistas y neutrales: «encuentra qué incluye», «averigua cómo reservar», «corrige este dato», «encuentra el aviso de privacidad».
- Reclutar participantes representativos; en grupos heterogéneos, probar segmentos relevantes separadamente. Un ciclo ligero de 4–6 por segmento es una **heurística operativa**, no muestra estadística ni proporción garantizada de bugs.
- Observar sin guiar; registrar tiempo aproximado, pasos, confusión, gravedad y frase representativa con consentimiento. Evitar almacenar datos personales innecesarios.
- Clasificar problemas por severidad (bloqueo, error recuperable, fricción, cosmético), frecuencia observada y tarea afectada; corregir y repetir.
- Complementar con al menos una revisión de accesibilidad y prueba con usuarios de tecnología de asistencia cuando el alcance lo permita.

### Evaluación cuantitativa: ¿cuánto cambia?

- Definir población y denominador: sesiones humanas válidas, visitantes consentidos, clics, formularios **confirmados**, reuniones atendidas, contactos cualificados.
- No confundir eventos de botón con leads. Un clic puede fallar por SMTP, red, consentimiento o duplicación.
- Registrar fecha, fuente/campaña, rango temporal, cambios del sitio y contexto de marketing. No atribuir un pico a una animación sin diseño experimental.
- Con tráfico bajo, analizar tendencias descriptivas y tareas cualitativas; una prueba A/B puede no tener potencia estadística.

## 4. Protocolo de experimentos A/B confiables

**Inspiración científica:** [Kohavi, Tang y Xu, *Trustworthy Online Controlled Experiments* (2020)](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) y [Microsoft Research, pre-experiment](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/).

1. Redactar hipótesis falsable («si mostramos alcance antes del video, más usuarios completarán la solicitud sin aumentar errores»).
2. Definir métrica primaria y guardrails **antes** de mirar resultados: leads confirmados / visitantes elegibles, errores de formulario, tiempo de carga, accesibilidad, cancelaciones.
3. Definir población, aleatorización persistente, exclusiones y ventana temporal. No asignar variantes por carga de página si rompe consistencia.
4. Calcular tamaño muestral/potencia y efecto mínimo detectable con apoyo estadístico; nunca usar cinco entrevistas como experimento cuantitativo.
5. Prevenir contaminación: cambios paralelos de campañas/precios/formularios; describirlos si ocurren.
6. Monitorear integridad de asignación, errores y seguridad. No detener al primer `p < 0.05` sin método secuencial declarado.
7. Decidir con intervalo de incertidumbre, efecto práctico, costes de implementación y guardrails. Publicar también resultados negativos/inconclusos.

Usar [plantilla de experimento](../templates/EXPERIMENTO.md). No activar scripts de personalización, cookies o seguimiento sin validar consentimiento y permisos.

## 5. Evidencia a entregar al cliente

| Artefacto | Qué debería responder |
|---|---|
| Mapa de tareas | Qué quiere resolver el usuario y qué impide hacerlo |
| Hipótesis de contenido | Por qué se diseñó cada bloque y CTA |
| Notas de 3–5 sesiones reales (si se hicieron) | Qué se observó exactamente, sin venderlo como estadística |
| Registro de eventos consentidos | Cuántos pasos completaron personas reales y qué falló |
| Decisión y backlog | Qué corregimos ahora, qué medimos después, quién es responsable |

**Evidencia:** [ISO 9241-210](https://www.iso.org/standard/77520.html), [Nielsen heurísticas](https://www.nngroup.com/articles/ten-usability-heuristics/), [NN/g límites muestras](https://www.nngroup.com/articles/5-test-users-qual-quant/), [GOV.UK simple de usar](https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use), [W3C involucrar usuarios](https://www.w3.org/WAI/planning/involving-users/).
