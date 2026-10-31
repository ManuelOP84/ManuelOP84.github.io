## Memoria operativa compartida
- Al continuar una tarea o cambiar de sesión/dispositivo, consulta primero `MEMORIA-AGENTES.md` de **este repositorio**. Consulta el resto de la documentación únicamente si falta información concreta.
- Claude Code y Codex usan la skill `memoria-compartida`. Tras un cambio importante **verificado**, actualiza esa memoria en el mismo commit/PR, sin auditorías ni historiales extensos.
- Diferencia siempre preparado, fusionado, instalado y operativo. No guardes secretos, datos personales ni contenidos privados; no afirmes trabajo realizado si no tiene evidencia.

# Codex — página estática SmartThings / JARVIS

- Aplicar `IA-COLABORACION.md` desde Codex Cloud (iPhone/web) y PC. Un único agente, contexto mínimo y tres líneas finales por defecto, sin auditorías generales.
- No exponer información de OAuth, claves ni parámetros sensibles, ni eliminar controles de seguridad del callback.
- Conservar CSP, no añadir rastreo ni servicios externos, no desplegar automáticamente. Cambios en rama y PR.
- Para colaborar con Claude Code Cloud, utilizar el commit/PR; ninguna sesión cloud está vinculada automáticamente con la otra.
