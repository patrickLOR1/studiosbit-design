# Autogestión del cliente, CMS y entrega que realmente funciona

El cliente debe poder mantener el sitio en las tareas contratadas sin volverse dependiente de Studios.Bit para cada palabra o imagen. «Tiene un CMS» no significa «puede usarlo».

## Definir el contrato editorial antes de escoger CMS

| Campo | Pregunta de decisión |
|---|---|
| Actores | ¿Quién escribe, aprueba, publica y revierte? ¿Quién recupera cuenta? |
| Contenido | ¿Qué entidades cambia? Servicios, artículos, fotos, FAQ, testimonios, precios, horarios, ES/EN |
| Alcance | ¿Hay campos que no puede editar porque afectan diseño/legalidad/SEO? |
| Aprobación | ¿Necesita borrador, preview, historial, dos roles o revisión? |
| Calidad | ¿Qué validaciones impiden imágenes enormes, enlaces rotos y traducciones incompletas? |
| Recuperación | ¿Se puede revertir una publicación? ¿Quién guarda backups? |
| Costos | Licencias, asientos, tráfico API, almacenamiento, mantenimiento y soporte |

## Modelo de UX editorial de 6 tareas

En ambiente de prueba con cuenta de editor **no administrativa**, el cliente debe poder:

1. Iniciar sesión y recuperarla con mecanismo seguro.
2. Encontrar el contenido deseado con nombres y lenguaje comprensible.
3. Cambiar un título e imagen con vista previa en móvil y escritorio.
4. Crear un borrador sin publicarlo accidentalmente.
5. Publicar (si su rol lo permite) y comprobar el resultado en la web.
6. Corregir, deshacer o solicitar ayuda y saber a quién llamar.

Registrar para cada paso: éxito, tiempo orientativo, ayuda requerida, error, comentario real, captura sin PII y mejora. No dar al cliente permisos de admin si solo necesita editor. No probar con información personal real.

## Modelo de contenido y accesibilidad

- Campos claros, agrupados por tarea; instrucciones cortas y ejemplos reales. Usar validación cercana al campo y preservar valor si falla.
- Bloquear o advertir ante texto crítico faltante, alt de imagen necesario, links inválidos, CTA roto y traducción inconsistente; validación servidor para integridad.
- Prever publicación asincrónica/caché: mostrar estado real de build/revalidación, fecha y acción de reintento; nunca «publicado» por solo guardar un draft.
- Las páginas públicas deben mantener HTML legible, metadatos/canonical correctos y performance incluso si el CMS se cae.
- Derechos: el cliente debe poseer o tener acceso acordado a contenido, assets, dominio, proveedores y exportaciones. Documentar salida/reversibilidad de CMS.

## Entrega comercial de alta confianza

Adjuntar:

- Mapa de cuentas con propietario y responsables (sin contraseñas en documento).
- Video corto o guía visual **hecha sobre su panel real**, no tutorial genérico de 45 minutos; incluir tareas 1–6 y errores frecuentes.
- Política de soporte, mantenimiento, actualizaciones y respaldo con alcance/horario acordados.
- Instrucciones de publicar/rollback, plan de contenido, campos que no se editan y criterios de actualización.
- Registro de sesión de capacitación: quién participó, tarea completada, pendientes, responsable y fecha.

**Regla de aceptación:** pedir al cliente cambiar un contenido y publicarlo en preview sin ayuda verbal. Si falla, simplificar y volver a probar antes de vender «autogestión» como capacidad probada.

**Fundamentos:** [GOV.UK Service Standard usabilidad](https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use), [patrones de validación](https://design-system.service.gov.uk/patterns/validation/), [Nielsen heurísticas](https://www.nngroup.com/articles/ten-usability-heuristics/), [W3C involucrar personas](https://www.w3.org/WAI/planning/involving-users/).
