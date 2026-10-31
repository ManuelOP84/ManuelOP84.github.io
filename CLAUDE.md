## Memoria operativa compartida
- Al continuar una tarea o cambiar de sesión/dispositivo, consulta primero `MEMORIA-AGENTES.md` de **este repositorio**. Consulta el resto de la documentación únicamente si falta información concreta.
- Claude Code y Codex usan la skill `memoria-compartida`. Tras un cambio importante **verificado**, actualiza esa memoria en el mismo commit/PR, sin auditorías ni historiales extensos.
- Diferencia siempre preparado, fusionado, instalado y operativo. No guardes secretos, datos personales ni contenidos privados; no afirmes trabajo realizado si no tiene evidencia.

# Claude Code — página estática SmartThings / JARVIS

- Aplicar `IA-COLABORACION.md` en móvil/web/PC: un agente por tarea, cambios mínimos, resultado de tres líneas y sin auditorías generales no solicitadas.
- Esta web es un callback público de SmartThings. No cambies el flujo OAuth ni reveles los parámetros `code` o `state` en logs, analítica o servicios externos. Conserva la política CSP y el carácter local del destino.
- No despliegues ni publiques cambios sin autorización expresa. Pruebas necesarias y estado real, no simulado.
- Si se requiere Codex Cloud, preparar PR con datos mínimos del cambio; no activar el puente local desde la nube por defecto.
