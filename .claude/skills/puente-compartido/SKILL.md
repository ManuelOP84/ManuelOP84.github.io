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
