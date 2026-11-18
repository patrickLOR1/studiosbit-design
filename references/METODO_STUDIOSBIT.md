# Studios.Bit — sistema operativo de producción digital (v1.1)

**Objetivo:** repetir una calidad comprobable sin que cada nuevo sitio dependa de recordar instrucciones sueltas. Se usa con [director de proyecto](../skills/director-proyecto/SKILL.md), [BitProof](../skills/bitproof-qa/SKILL.md) y [literatura](LITERATURA_PROFUNDA_2026.md).

## Índice
1. Qué significa excepcional
2. Clasificación y responsables
3. Fases con decisiones de salida
4. Modelo de calidad y aceptación
5. Trabajo con Codex
6. Revisión de madurez

## 1. Qué significa excepcional (definición operativa propia)

Un proyecto es excepcional cuando cumple simultáneamente:

1. **Relevancia:** resuelve una necesidad identificada de un segmento concreto; no solo «se ve premium».
2. **Claridad:** propósito y siguiente acción comprensibles, sin guion o video obligatorio.
3. **Firma original:** dirección visual y editorial que no parezca una plantilla ni copie referencias SB.
4. **Calidad inclusiva:** funciona con teclado, lector, movimiento reducido y pantallas comunes; evidencia explícita.
5. **Fiabilidad:** las interacciones generan efectos verificables y fallan de manera recuperable.
6. **Autonomía:** el cliente puede ejecutar operaciones acordadas sin pedir al desarrollador cambios triviales.
7. **Impacto:** se miden resultados reales (contactos cualificados, citas, ventas, tareas, soporte), sin garantía de cifras.
8. **Responsabilidad:** seguridad, privacidad, mantenimiento y coste asignados a personas reales.

Ninguna dimensión reemplaza otra; un sitio cinematográfico lento o un SaaS estable que nadie entiende no cumplen la definición.

## 2. Clasificación por riesgo y carga de trabajo

| Perfil | Ejemplo | Disciplinas mínimas | Entregables proporcionales |
|---|---|---|---|
| S — público | Landing/portafolio estático | UX, arte, frontend, controles web y BitProof | Brief corto, sitemap, 1 journey, QA de CTA y dispositivo |
| M — editable/integrado | Corporativo con CMS, formulario o reservas | S + backend/seguridad/datos **solo según dependencias** | Mapa de integración, privacidad, fallas, entrenamiento editor |
| A — crítico | Usuarios, pagos, tenants, datos sensibles o máquina | Seguridad, frontend, backend, BD, operación, UX y BitProof | Matriz de permisos, amenazas, recuperación, pruebas negativas y monitoreo |

Si el caso incluye cambios de maquinaria/OT, exige especialista, segmentación y autorización para cualquier escritura; no usar una guía web como autorización técnica industrial.

**Responsables:** Patrick lidera arquitectura, seguridad, ingeniería y operaciones; Emiliano lidera estrategia, posicionamiento, contenido y aceptación comercial. Para proyectos de clientes, asignar un dueño por producto, un contacto aprobador, operador del CMS, mantenedor y responsable de incidentes. Son roles sugeridos, no delegación automática.

## 3. Fases y condiciones de salida

### F0 — Descubrimiento (no diseño visual todavía)

- Entrevistar al dueño y, si es posible, a un usuario representativo. Recoger tareas, problemas actuales, objeciones, restricciones y activos.
- Mapear qué dato es observado, dicho por cliente, asumido o medido. Identificar permisos de uso de fotografías/testimonios y quién podrá editar el sitio.
- Definir «fuera de alcance» y estimar costes recurrentes (dominio, hosting, CMS, correo, mantenimiento, licencias).
- **Gate de salida:** brief revisable; si faltan precios/información legal/derechos/credenciales, registrarlos como bloqueantes de la función implicada.

### F1 — Investigación y arquitectura de información

- 1–3 entrevistas exploratorias cuando disponibles, tarea principal, mapa de objeciones y análisis de alternativas comerciales sin copiar.
- Jerarquizar mensajes. Dibujar sitemap e itinerario CTA → confirmación. No tratar captación como un botón aislado: debe llegar a servicio real, correo/agenda o DB autorizada.
- Identificar riesgos y decidir si conviene prototipo estático antes del backend.
- **Gate:** tarea crítica demostrable y ruta de recuperación cuando falla.

### F2 — Dirección de arte y concepto

- Preparar dos propuestas genuinamente diferentes de jerarquía, ritmo, tipografía, imagen/video y navegabilidad, ambas compatibles con el objetivo.
- Definir tokens de cliente (tipografía, semántica de color, spacing, radios, motion) y no imponer los de Studios.Bit.
- Registrar por cada efecto su propósito, coste de red/CPU y alternativa inmóvil. Reducir efectos si compiten con mensaje/CTA.
- **Gate:** diseño aprobado y criterios de interacción accesible por estado.

### F3 — Arquitectura técnica y ADR

- Comparar opciones realistas: estático vs CMS, renderizado, hosting, terceros, persistencia, autenticación, inversión futura.
- Registrar contratos (quién edita, quién ejecuta, dónde viajan datos, qué pasa si un proveedor cae), presupuesto de costo mensual y puntos de salida.
- **Gate:** diagrama proporcional y ADR corto cuando decisión influye en costo, privacidad, riesgo o reversibilidad.

### F4 — Implementación vertical

- Priorizar ruta completa funcional: visita → mensaje → acción → respuesta del servidor/proveedor → confirmación real → evidencia observable.
- Construir componentes de negocio por módulos con contratos y estados de error; aislar animaciones para no interrumpir tareas.
- Nunca llenar el cliente con métricas, reseñas o datos falsos como si fueran reales.
- **Gate:** test de cada tramo crítico y preview sin credenciales productivas reutilizadas.

### F5 — BitProof

- Crear matriz de pruebas antes de empezar la implementación: qué evidencia existe, qué falta, quién aprueba una excepción.
- Ejecutar pruebas automatizadas **y manuales** según riesgo: navegación, teclado, formularios, permisos, datos, disponibilidad, errores, SEO, rendimiento y autoría.
- Ejecutar un caso negativo deliberado: red desconectada, proveedor caído, recurso no autorizado o formulario duplicado, según alcance.
- **Gate:** críticos probados; no se abre publicación cuando existen `pending` críticos.

### F6 — Handoff, publicación y soporte

- Publicación solo bajo autoridad del dueño; documentar cambios y paso de reversión.
- Probar con el cliente un cambio real en preview si necesita CMS, o su acceso a estadísticas y recepción de leads.
- Entregar guía de 1–2 páginas, contrato de soporte y propietario de dominio/cuentas/renovaciones.
- **Gate:** cliente completó su tarea sin guía del desarrollador o se registró la dificultad restante.

### F7 — Aprendizaje 7/30/90 días (política, no dato científico)

- 7 días: enlaces, formularios/citas, fallos, indexación técnica y desempeño inicial.
- 30 días: contenidos, análisis de tareas, fuentes de contacto y tickets; evitar atribuir por poco tráfico.
- 90 días: hipótesis de mejora, priorización por impacto/esfuerzo/evidencia; considerar A/B solo con volumen y medición adecuadas.
- Reportar datos y limitaciones; no atribuir resultados comerciales sin atribución razonable.

## 4. Matriz de calidad por resultado

| Resultado | KPI posible | Instrumentación y verificación | Propietario |
|---|---|---|---|
| Comprensión | Usuario explica oferta/CTA | Entrevista + observación de tarea | UX/marketing |
| Acción útil | Solicitud válida de contacto o cita | Confirmación backend/tercero y evento consentido | Backend/negocio |
| Operación | Editor cambia contenido y revierte | Prueba de cliente en preview | Soporte/CMS |
| Inclusión | Tarea con teclado/lector | Auditoría técnica y manual, según contrato | Frontend/QA |
| Rapidez | LCP/INP/CLS | Laboratorio + percentil 75 de campo cuando haya datos | Frontend |
| Seguridad | Acceso indebido denegado | Casos negativos, revisión y evidencia | Seguridad |
| Recuperación | Restore/rollback comprobado | Ensayo controlado con fecha y RPO/RTO acordados | Operaciones |

## 5. Disciplina de Codex

1. Inspeccionar `AGENTS.md`, dependencias, cambios no confirmados, permisos y arquitectura existente antes de editar.
2. Cargar [director de proyecto](../skills/director-proyecto/SKILL.md) y solo skills requeridas; usar referencias progresivas.
3. Proponer plan breve con criterios de aceptación y riesgos; después trabajar en rama/PR y preview.
4. Separar código, evidencia de pruebas y sugerencias; documentar versionado y rollback.
5. Si un requisito involucra secretos, dominios, costo, publicación o datos productivos no autorizados: detener y pedir decisión.
6. Ningún agente debe declarar tests que no ejecutó. La revisión humana final y la aceptación de riesgo pertenecen al equipo/cliente.

## 6. Mejorar el propio sistema

- Mantener una base de [casos de evaluación de skills](EVALUACION_SKILLS.md) que detecte si Codex olvida pedir datos, crea servicios innecesarios, publica sin permiso o confunde simulaciones.
- Medir por proyecto: alcance entregado, errores reabiertos, retrabajo, horas de soporte y satisfacción observable; no crear un «puntaje mágico» de excelencia.
- En cada retrospectiva, actualizar una plantilla o un caso negativo concreto, no añadir reglas decorativas.

**Fuentes guía:** [ISO 9241-210](https://www.iso.org/standard/77520.html), [GOV.UK Service Standard](https://www.gov.uk/service-manual/service-standard), [DORA 2025](https://dora.dev/research/2025/dora-report/), [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), [W3C WAI](https://www.w3.org/WAI/planning/involving-users/).
