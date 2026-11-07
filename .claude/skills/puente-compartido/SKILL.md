---
name: puente-compartido
description: Coordina Claude Code y Codex con un intercambio breve y comprobable de PR/commits en GitHub, también desde móvil o nube, solo cuando la segunda IA sea necesaria.
---
# Puente compartido optimizado — móvil y nube

En sesiones cloud aisladas, usa **GitHub como punto de intercambio**, no asumas que puedes ejecutar la CLI del otro proveedor.

1. Trabaja con **una sola IA** por tarea. Si hace falta segunda opinión, deja un PR/commit o nota corta en GitHub con objetivo, archivos modificados, pruebas reales y duda concreta.
2. El segundo agente lee únicamente el diff y la pregunta, no el historial completo. No relances trabajo ni dupliques auditorías.
3. Si la revisión detecta un problema concreto, anota el archivo y motivo. El agente ejecutor corrige y verifica. Si no hay problema, informa en una línea.
4. Resultado final en español de tres líneas: HECHO, PRUEBAS, PENDIENTE (solo bloqueo).
5. En Windows, el puente ejecutable local es opcional y depende de las sesiones instaladas. **Esta skill no conecta automáticamente cuentas de Claude y ChatGPT ni crea sesiones en segundo plano.**
6. Nunca usar API de pago, publicar, fusionar o desplegar sin permiso. No adjuntar secretos.

## Revisión cruzada proporcional al riesgo (Claude Code desarrolla, Codex revisa)
Antes de cerrar un PR, escribe en su descripción `Riesgo: R0|R1|R2` y el motivo en una línea.
- **R0** textos, docs, estilos o cambios sin lógica: sin revisión cruzada.
- **R1** lógica acotada fuera de zonas sensibles: bastan tus pruebas. Revisión solo si Manuel la pide.
- **R2** OAuth, credenciales o secretos, pagos/Stripe, CSP o seguridad, borrado o migración de datos, CI/despliegue, permisos, o más de 300 líneas en varios módulos: **una** revisión de Codex.
  Cómo: PR listo (no borrador) y un único comentario `@codex review` con objetivo, archivos clave, pruebas hechas y la duda concreta. Si el comentario de Claude Code no activa a Codex, Manuel lo escribe desde la app de GitHub.

**Límites anti-bucle**
- Máximo 2 rondas por PR: revisión inicial y una re-revisión solo tras corregir un P0/P1. Después decide Manuel.
- Codex revisa y comenta; no escribe en la rama mientras Claude Code trabaje en ella (un solo agente escribe).
- Corrige solo P0/P1 verificables. P2 y estilo se anotan en el PR y no abren otra ronda.
- No repitas revisión sobre el mismo commit ni para cambios de memoria o documentación.

**Rescate (equivalente a /codex:rescue)**: solo si Claude Code falla dos veces en lo mismo o Manuel lo pide, comenta `@codex <tarea concreta>` en el PR y deja de editar esa rama hasta que Codex termine.

**Disponibilidad y coste**
- `@codex` en GitHub exige que Manuel active *Code review* del repo en la configuración de Codex. Usa la cuota del plan ChatGPT, no API de pago. Mantener *Automatic reviews* desactivado: revisaría también R0/R1.
- Si Codex no reacciona (👀) en unos 15 minutos, no reintentes: anota `Revisión Codex pendiente` en el PR.
- Plugin local `openai/codex-plugin-cc` (`/codex:review`, `/codex:rescue`): opcional y solo en PC con Codex CLI iniciada; no existe en Claude Code Cloud ni en el iPhone. Nunca activar su *review gate* (bucle y consumo).
