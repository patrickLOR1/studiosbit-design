# Studios.Bit — revisión crítica de literatura y estándares para productos digitales

**Corte de investigación:** 18 de noviembre de 2026. **Versión metodológica:** 1.1. **Alcance:** diseño, experiencia, contenido/SEO, experimentación, frontend, backend, arquitectura, bases de datos, seguridad, calidad y operación. Se priorizaron **fuentes originales**: organismos que emiten normas, autores de investigación, documentación mantenida por creadores y reportes primarios. No es una revisión sistemática PRISMA ni cubre literalmente toda la literatura existente.

## Cómo interpretar la evidencia

| Tipo | Valor | Precaución |
|---|---|---|
| Norma o estándar publicado | Define un vocabulario o criterios verificables aplicables | Confirmar alcance, versión, obligatoriedad contractual/legal y métodos de prueba |
| Guía oficial de plataforma | Instrucciones vigentes de un proveedor o proyecto técnico | Puede ser específica del stack y cambiar sin aviso |
| Investigación original / experimento | Evidencia sobre población, condiciones y resultados estudiados | No extrapolar porcentajes o causalidad al cliente sin replicar condiciones |
| Método/heurística | Ayuda a detectar riesgos y formular hipótesis | No es certificación ni garantía ni sustituye prueba con usuarios |
| Política Studios.Bit | Decisión operativa que crea consistencia | Adaptar al presupuesto y riesgos; no atribuirla a la fuente |
| Video SB de referencia | Inspiración visual/edición observada | No transfiere licencias, código, eficacia ni resultados de terceros |

**Regla de incertidumbre:** para cada recomendación técnica citar fuente, versión/fecha verificadas, contexto de aplicabilidad, evidencia local y nivel de confianza. La fecha del documento no vuelve obsoleta una buena investigación clásica: distinguir principios duraderos de versiones que requieren revalidación.

## 1. Diseño centrado en personas e investigación de experiencia

| ID | Fuente primaria | Hallazgo adoptado en Studios.Bit | Operacionalización |
|---|---|---|---|
| UX01 | [ISO 9241-210:2019, diseño centrado en personas](https://www.iso.org/standard/77520.html) | Las decisiones deben surgir del contexto, necesidades y evaluación iterativa | Descubrimiento, prototipo, pruebas y mejoras; la norma completa tiene acceso/licencia separados |
| UX02 | [ISO 9241-110:2020, principios de interacción](https://www.iso.org/standard/75258.html) | Evaluar interacción útil y coherente | Revisar tareas, estados, errores y recuperación; sin afirmar conformidad ISO por leer resumen |
| UX03 | [Jakob Nielsen, diez heurísticas (1994; revisión 2024)](https://www.nngroup.com/articles/ten-usability-heuristics/) | Visibilidad, correspondencia con lenguaje real, libertad, prevención de errores, consistencia y claridad | Revisión heurística estructurada + investigación, no puntaje absoluto |
| UX04 | [Nielsen Norman Group, estudio cualitativo y muestra](https://www.nngroup.com/articles/5-test-users-qual-quant/) | Pocos participantes por grupo pueden identificar problemas en ciclos iterativos; no son muestra estadística para tasas de conversión | 4–6 participantes por grupo como hipótesis operativa, no límite universal ni afirmación de representar población |
| UX05 | [W3C WAI: involucrar usuarios](https://www.w3.org/WAI/planning/involving-users/) | Usuarios con discapacidad aportan barreras que auditorías automatizadas no capturan | Pruebas de tareas con tecnología de asistencia y consentimiento |
| UX06 | [GOV.UK Service Standard: entender necesidades](https://www.gov.uk/service-manual/service-standard/point-1-understand-user-needs) | Diseñar alrededor de tareas reales, no atributos estéticos arbitrarios | Definir top tareas y evidencia, entrevistas breves, journey |
| UX07 | [GOV.UK: hacer servicios simples](https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use) | Usabilidad debe evaluarse frecuentemente con usuarios | Sesión sobre cada flujo crítico antes de release |
| UX08 | [GOV.UK Design System, patrones](https://design-system.service.gov.uk/patterns/) | Los patrones documentan contexto y evaluación, no son decoración universal | Patrón → problema → adaptación → validación propia |

**Síntesis original:** una interfaz distintiva no requiere más animaciones. Su calidad depende de promesa entendible, tareas realizables, estados recuperables y evidencia de uso real. Contrastar hallazgos cualitativos con analítica sin confundirlos.

## 2. Accesibilidad, diseño visual y medios

| ID | Fuente primaria | Criterio y alcance | Acción / verificación |
|---|---|---|---|
| UI01 | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Recomendación W3C; elegir nivel de conformidad contractual | Evaluación por criterio y evidencia, no solo Lighthouse |
| UI02 | [W3C WCAG-EM 2.0](https://www.w3.org/TR/WCAG-EM/) | Metodología publicada para evaluar accesibilidad de sitios | Definir alcance, muestra representativa de páginas y resultados |
| UI03 | [W3C WAI, evaluación con usuarios](https://www.w3.org/WAI/test-evaluate/involving-users/) | Complementa conformidad técnica con experiencia humana | Test teclado, lector, zoom y tareas con participantes pertinentes |
| UI04 | [W3C WAI ARIA APG](https://www.w3.org/WAI/ARIA/apg/) | Patrones de teclado/roles/estados | Preferir HTML nativo; usar patrones APG si un control complejo lo necesita |
| UI05 | [W3C Design Tokens Community Group 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) | Formato de intercambio de tokens del grupo comunitario, **no Recomendación W3C de la vía principal** | Separar tokens de marca, semánticos y componentes; no imponer JSON al stack |
| UI06 | [WAI, hacer audio y video accesible](https://www.w3.org/WAI/media/av/) | Subtítulos, descripciones y alternativas dependen del tipo de contenido | Plan de subtitulado, controles, transcripción/alternativas según caso |
| UI07 | [MDN, prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion) | Preferencia del usuario para reducir movimiento | Versión inmóvil equivalente, sin perder navegación ni CTA |
| UI08 | [GOV.UK Design System, estrategia de accesibilidad](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) | Componentes probados necesitan además verificación contextual | Prueba manual + automatizada + usuario cuando posible |

## 3. Rendimiento web y audiovisual

| ID | Fuente primaria | Qué sostiene | Uso correcto |
|---|---|---|---|
| PF01 | [web.dev: Web Vitals](https://web.dev/articles/vitals) | LCP, INP y CLS son indicadores de experiencia en campo | Evaluar percentil 75 en móvil/escritorio por separado si existe muestra suficiente |
| PF02 | [web.dev: definición de umbrales](https://web.dev/articles/defining-core-web-vitals-thresholds) | Umbrales «buenos»: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 | Objetivos base, no garantía de negocio; reportar diferencia laboratorio/campo |
| PF03 | [web.dev: video performance](https://web.dev/learn/performance/video-performance) | Video/poster pueden competir por red y LCP | Medir presupuesto de bytes, poster, preload y carga según viewport |
| PF04 | [web.dev: lazy-loading video](https://web.dev/articles/lazy-loading-video) | Diferir recursos fuera del primer viewport evita carga innecesaria | Video principal y secundarios requieren estrategias distintas |
| PF05 | [Lighthouse CI, proyecto oficial](https://github.com/GoogleChrome/lighthouse-ci) | Automatiza auditorías de laboratorio y regresiones | Configurar assertions graduales; no confundir puntuación con CWV de campo |

## 4. Arquitectura, servicios, confiabilidad y datos

| ID | Fuente primaria | Idea robusta | Entregable útil |
|---|---|---|---|
| AR01 | [D. L. Parnas (1972), modularidad](https://doi.org/10.1145/361598.361623) | Encapsular decisiones propensas a cambiar | Módulos por responsabilidad, no microservicios automáticos |
| AR02 | [AWS Well-Architected, seis pilares](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html) | Operación, seguridad, confiabilidad, rendimiento, coste y sostenibilidad | Trade-offs y límites de operación por proyecto |
| AR03 | [Google SRE, SLO](https://sre.google/sre-book/service-level-objectives/) | Definir fiabilidad y señales observables desde necesidades del usuario | SLI/SLO contextual; sin inventar «99.99%» |
| AR04 | [Google SRE, presupuesto de error](https://sre.google/workbook/error-budget-policy/) | Balancear cambios y fiabilidad para servicios operados | Política simple de release/rollback si hay SLO y tráfico suficientes |
| AR05 | [DORA, investigación 2025](https://dora.dev/research/2025/dora-report/) | IA y entrega dependen del sistema de trabajo y feedback | Medir tiempo de entrega, fallos y recuperación, no líneas generadas |
| AR06 | [RFC 9110, semántica HTTP](https://www.rfc-editor.org/rfc/rfc9110.html) | Distinguir métodos, estado, caché y recursos | Contratos que no contradicen semántica HTTP |
| AR07 | [RFC 9457, Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) | Errores estructurados para APIs HTTP | Errores coherentes, sin filtrar secretos |
| AR08 | [OpenTelemetry, señales](https://opentelemetry.io/docs/concepts/signals/) | Logs, métricas y trazas complementarias | Observabilidad, sin atributos de alta cardinalidad ni datos privados |
| DB01 | [PostgreSQL 18, restricciones](https://www.postgresql.org/docs/current/ddl-constraints.html) | Integridad pertenece también a BD, no solo UI | UNIQUE, FK, CHECK según dominio; pruebas de carrera |
| DB02 | [PostgreSQL 18, backup y recuperación](https://www.postgresql.org/docs/current/backup.html) | Copia no equivale a recuperación | Restauración ensayada, RPO/RTO acordados |
| DB03 | [PostgreSQL 18, PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) | Recuperación puntual requiere estrategia WAL/base backups | Plan contextual, no declarar PITR si proveedor no lo soporta |

## 5. Seguridad y cadena de suministro

| ID | Fuente primaria | Estado revisado | Uso |
|---|---|---|---|
| SE01 | [OWASP Top 10:2025](https://top10.owasp.org/2025/) | Publicado, lista de concientización | Priorizar acceso roto, misconfiguración, supply chain, inyección y fallos excepcionales |
| SE02 | [OWASP ASVS 5.0.0](https://asvs.owasp.org/) | Estable | Convertir amenazas a verificaciones específicas, no «certificación OWASP» |
| SE03 | [OWASP API Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/) | Edición publicada a la revisión | Probar autorización por objeto/función, cuotas, datos expuestos y terceros |
| SE04 | [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) | **Final**; [v1.2 inicial](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) sigue **borrador** a esta revisión | Proceso de protección, producción, revisión y respuesta; reevaluar estado futuro |
| SE05 | [NIST SP 800-63B-4 (julio de 2025)](https://csrc.nist.gov/pubs/sp/800/63/B/4/final) | Final; guía de autenticadores para ámbito de identidad digital NIST | Evaluar sesiones/autenticación según riesgo, no importar automáticamente requisitos federales |
| SE06 | [OWASP SCVS](https://scvs.owasp.org/scvs/using-scvs/) | Guía de verificación de componentes | Inventario, lockfiles, SBOM cuando amerite, procedencia y SCA |
| SE07 | [GitHub, uso seguro de Actions](https://docs.github.com/en/actions/reference/security/secure-use) | Guía mantenida | Permisos mínimos, revisión de acciones, secretos y PR |
| SE08 | [GitHub, proteger contra amenazas](https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats) | Guía mantenida | Secret scanning, dependencias, CodeQL y revisiones según disponibilidad |

## 6. Descubrimiento orgánico, medición y experimentación

| ID | Fuente primaria | Conclusión | Aplicación |
|---|---|---|---|
| MK01 | [Google Search Central, AI features](https://developers.google.com/search/docs/appearance/ai-features) | SEO convencional sigue importando; **no exige** archivos «AI» ni schema especial para AI Overviews/Mode | Texto útil, enlaces internos, indexabilidad y datos estructurados acordes al contenido |
| MK02 | [Google, guía de optimización para IA (2026)](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Rechaza atajos mágicos; Search funciona sobre rastreo e información útil | Evitar prometer posiciones y trafico de LLMs |
| MK03 | [Google, contenido útil y confiable](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Originalidad y utilidad centradas en usuario | Evidencia real, autoría, contenido propio, mantenimiento |
| MK04 | [Google Analytics, generate_lead](https://developers.google.com/analytics/devguides/collection/ga4/reference/events) | Evento recomendado para solicitudes de contacto/demo | Solo emitir tras confirmación de éxito y consentimiento aplicable |
| MK05 | [Google Tag Platform, consentimiento](https://developers.google.com/tag-platform/security/guides/consent) | La etiqueta debe comportarse conforme a la elección del visitante | Diseño de consentimiento, prueba y validación jurídica contextual |
| MK06 | [Microsoft Research, experimentos confiables](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) | Hipótesis/métricas/asignación y calidad de datos antes de interpretar | Guardrails, preregistro, control de sesgo y criterio de parada |
| MK07 | [Kohavi, Tang y Xu (2020), libro original](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) | Métodos, fallas y límites de A/B tests | No concluir de muestras pequeñas o espiar significancia continuamente |
| MK08 | [GOV.UK, medir éxito del servicio](https://www.gov.uk/service-manual/service-standard/point-10-define-success-publish-performance-data) | Evidencia de uso real guía mejora continua | Panel mínimo de tareas terminadas, errores, leads válidos y soporte |

## 7. Automatización de calidad y control de cambios

| ID | Fuente primaria | Regla |
|---|---|---|
| QA01 | [Playwright, CI](https://playwright.dev/docs/ci) | Probar flujos completos con navegador; mantener versiones de browsers y trazas |
| QA02 | [Playwright, accesibilidad](https://playwright.dev/docs/accessibility-testing) | axe detecta parte de fallos; añadir prueba manual de teclado/lector |
| QA03 | [GitHub, análisis de código](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning) | Automatizar análisis en PR si stack y plan lo permiten; no sustituye revisión |
| QA04 | [Lighthouse CI, inicio](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md) | Laboratorio reproducible y umbrales evolutivos, con variabilidad documentada |

## Contradicciones y malas interpretaciones que debemos impedir

1. **«Más interacción = mejor UX».** Falso como regla universal; observar tarea, carga cognitiva, acceso y rendimiento. El movimiento es opcional y justificable.
2. **«Cinco usuarios prueban una tasa de conversión».** No; grupos pequeños son útiles para hallar problemas cualitativos, no para inferencia estadística de porcentajes.
3. **«Lighthouse verde = WCAG AA o CWV».** No; son instrumentos distintos; manual + campo cuando aplique.
4. **«Schema/llms.txt garantizan visibilidad en respuestas IA».** No; Google no exige archivo especial para sus AI features.
5. **«Microservicios escalan mejor siempre».** No; empezar por límites, contención, datos, costo y carga medidos.
6. **«Backup activado = base de datos recuperable».** No; probar restauración/RPO/RTO.
7. **«Un escáner sin hallazgos certifica seguridad».** No; falta revisar permisos de negocio, amenazas, configuraciones y operación.
8. **«A/B siempre es una mejora».** No; sin potencia, instrumentación confiable, guardrails o consentimiento, usar entrevistas, sesiones o observación cualitativa.
9. **«El trabajo generado por IA está probado».** No; el código debe revisarse, probarse, rastrearse y mantenerse por una persona responsable.

## Vigilancia de vigencia y fuentes futuras

- **Por release:** revisar versiones efectivamente instaladas, avisos de seguridad y documentación de framework/hosting/cms/proveedor antes de proponer cambios.
- **Trimestral:** verificar cambios de WCAG/WAI, OWASP, NIST, Google Search Central, web.dev, Playwright, Postgres, GitHub Actions y guías legales del proyecto. Registrar en un PR los cambios concretos, no actualizar solo la fecha.
- **Normativa:** un estándar publicado no crea automáticamente obligación legal para todos los clientes. Evaluar ley aplicable con asesoría competente cuando se requiera.
- **Citas:** conservar nombre, año/versión, URL original y aplicabilidad. No reproducir texto o diagramas largos de obras con copyright sin licencia.

## Siguientes manuales específicos

- [Metodología de trabajo](METODO_STUDIOSBIT.md)
- [UX, investigación y conversión](UX_INVESTIGACION_CRO.md)
- [Video e interacciones distintivas](VIDEO_INTERACCION_SIGNATURE.md)
- [SEO/AEO y medición](SEO_AEO_MEDICION.md)
- [Arquitectura operativa y escala](ESCALABILIDAD_OPERACION.md)
- [CMS y entrega al cliente](CMS_HANDOFF.md)
- [BitProof y release gates](BITPROOF_GATES.md)
- [Evaluación y mejora de skills](EVALUACION_SKILLS.md)
