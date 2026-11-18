# Studios.Bit Design — Biblioteca creativa para Codex

**Versión 1.1 · 61 referencias audiovisuales (SB-01 a SB-61) · 12 skills especializadas + investigación UX, metodología, arquitectura, seguridad y verificación.**

Repositorio independiente de **Studios.Bit** para diseño de sitios web, edición y diseño de video, microinteracciones, identidad visual y estrategia de contenido. La biblioteca se utiliza para planear y producir trabajo original de clientes **sin reutilizar literalmente obras de terceros**. No es la landing ni sustituye el brief del cliente.

## Elige tu especialidad

| Necesitas | Skill de Codex | Contenidos |
|---|---|---|
| Direccionar un proyecto de principio a fin | [Director de proyecto](skills/director-proyecto/SKILL.md) | Brief, investigación, decisiones, especialidades, validación y handoff |
| Verificar entregables sin afirmar pruebas inexistentes | [BitProof / QA](skills/bitproof-qa/SKILL.md) | Gates por riesgo, evidencia, reporte y GO/NO-GO |
| Arquitectura web, stack, límites, despliegue y decisiones | [Arquitectura web](skills/arquitectura-web/SKILL.md) | Requisitos, límites, decisiones técnicas y QA antes de construir |
| Autenticación, permisos, amenazas, secretos, seguridad | [Ciberseguridad web](skills/ciberseguridad-web/SKILL.md) | OWASP ASVS/Top 10, NIST SSDF, modelo de amenazas y pruebas negativas |
| Componentes, responsive, accesibilidad, rendimiento | [Frontend](skills/frontend-ingenieria/SKILL.md) | WCAG, Core Web Vitals, estado, formularios y pruebas |
| APIs, servicios, webhooks, fiabilidad, observabilidad | [Backend](skills/backend-ingenieria/SKILL.md) | RFC HTTP, OpenAPI, reintentos, SLO y pruebas de carga |
| Esquemas, SQL, migraciones, índices y recuperación | [Bases de datos](skills/bases-de-datos/SKILL.md) | Integridad, concurrencia, Postgres, backups y restauración |
| Landing, sitio corporativo, CMS, UI/UX, responsive, SEO técnico | [Diseño de sitios web](skills/diseno-sitios-web/SKILL.md) | Estructura, diseño, prototipos, conversión y QA |
| Reels, TikTok, edición, motion de video, guion, carruseles | [Diseño de videos](skills/diseno-videos/SKILL.md) | Ganchos, secuencias, ritmo, subtítulos, formatos |
| Navegaciones animadas, glow, scroll, GSAP, efectos | [Motion e interacciones](skills/motion-interacciones/SKILL.md) | Timing, accesibilidad y performance |
| Branding, tipografía, paletas, dirección de arte | [Identidad visual](skills/identidad-visual/SKILL.md) | Sistemas de marca y adaptación a cada cliente |
| Marketing de contenidos, posicionamiento, autoridad y procesos | [Estrategia de contenido](skills/estrategia-contenido/SKILL.md) | Pilares editoriales, evidencias, conversión |
 
**Inicio recomendado para todo proyecto web:** combinar [Arquitectura web](skills/arquitectura-web/SKILL.md) + [Diseño de sitios](skills/diseno-sitios-web/SKILL.md). Las decisiones se basan en [literatura y fundamentos UX](references/FUNDAMENTOS_DISENO_LITERATURA.md), la [guía arquitectónica](references/ARQUITECTURA_WEB_GUIA.md), y cuatro guías documentadas: [seguridad](references/INGENIERIA_CIBERSEGURIDAD.md), [frontend](references/INGENIERIA_FRONTEND.md), [backend](references/INGENIERIA_BACKEND.md), [bases de datos](references/INGENIERIA_BASES_DATOS.md). Activar skills de ingeniería según alcance: landing estática no necesita obligatoriamente backend o BD. Los videos SB inspiran soluciones, pero no sustituyen requisitos, estándares ni pruebas.

Consulta el [Índice por categorías](references/INDICE_POR_CATEGORIA.md), las [fichas SB-31 a SB-35](references/SB31_SB35.md) y las [fichas SB-36 a SB-41](references/SB36_SB41.md) y las [fichas SB-42 a SB-54](references/SB42_SB54.md) y [SB-55 a SB-61](references/SB55_SB61.md). Los análisis históricos están en [SB-01–SB-10](references/REFERENCIAS.md) y [SB-11–SB-30](references/LOTE_2026-11-06_SB11_SB30.md); [contenido y formatos](references/CONTENIDO_Y_FORMATOS.md).

**Para usar en un nuevo proyecto:** ver [Instalación en Codex](docs/INSTALACION_CODEX.md). Estas skills no se instalan automáticamente en los demás repositorios. El archivo [AGENTS.md](AGENTS.md) orienta su selección cuando se trabaja dentro de esta biblioteca.

## Método Studios.Bit v1.1 — investigación → implementación → evidencia

Comienza cualquier proyecto significativo con la [skill de dirección de proyecto](skills/director-proyecto/SKILL.md). Combina [metodología de ocho fases](references/METODO_STUDIOSBIT.md), [literatura crítica y fuentes originales](references/LITERATURA_PROFUNDA_2026.md), [UX y CRO](references/UX_INVESTIGACION_CRO.md), [video interactivo integrado](references/VIDEO_INTERACCION_SIGNATURE.md), [SEO/AEO y analítica](references/SEO_AEO_MEDICION.md), [ingeniería para escalar](references/ESCALABILIDAD_OPERACION.md) y [CMS fácil de usar](references/CMS_HANDOFF.md). Para lanzar, consulta [BitProof](references/BITPROOF_GATES.md) y la [skill de QA](skills/bitproof-qa/SKILL.md); prueba la biblioteca con [evaluación de skills](references/EVALUACION_SKILLS.md).

Plantillas reutilizables: [brief](templates/BRIEF_PROYECTO.md), [ADR](templates/ADR.md), [validación](templates/PLAN_VALIDACION.md), [evidencias de release](templates/RELEASE_EVIDENCIAS.md), [handoff al cliente](templates/HANDOFF_CLIENTE.md), [experimento A/B](templates/EXPERIMENTO.md) y [guion de video hero](templates/VIDEO_HERO.md).

Herramientas locales: usar los comandos python3 scripts/repo_quality.py y python3 -m unittest discover -s tests -v para metadatos y estructura. El ejemplo BitProof debe producir NO-GO porque no documenta pruebas reales. CI de esta biblioteca valida documentación, nunca sitios productivos.

## Cómo agregamos referencias

1. Analizar el material suministrado **visualmente**; distinguir observación, hipótesis y afirmaciones no verificadas.
2. Crear ficha SB-xx con fuente/fecha, patrón web, patrón de video, posible uso, riesgos y técnica original.
3. Etiquetar una o varias categorías en el índice; no duplicar manuales enteros.
4. Validar con el brief, dispositivos reales y alcance comercial de cada proyecto antes de convertirlo en regla.
5. Actualizar `references/CHANGELOG.md` y versión si cambia el método.

## Límites importantes

- **No publicar en este repositorio público los videos, música, renders, logotipos ni fotogramas de terceros**. Se documentan nombres de archivos privados para localizar el material autorizado en el equipo del usuario.
- No atribuirse trabajos o resultados de los creadores de referencia. Etiquetar demos no entregadas como **Proyecto conceptual**.
- La identidad Studios.Bit (negro #0B0B0D, blanco #F5F5F5, gris #9CA3AF, naranja #FF6A00, Manrope) aplica solo a la agencia. Los clientes tienen identidad propia.
- No editar automáticamente producción, precios, privacidad, información fiscal, SEO o integraciones cuando la solicitud sea creativa.
- No prometer resultados de marketing, IA o conversión sin pruebas.
