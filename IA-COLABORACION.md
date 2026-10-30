# Política de colaboración Claude Code + Codex — móvil, nube y escritorio

Versión: 2026-10-31. Ámbito: sesiones de programación que abren este repositorio desde Claude Code (móvil/web/PC) o Codex (ChatGPT móvil/web/PC).

## Ahorro de uso y trabajo efectivo
- Un único agente por encargo. No solicites revisión al segundo por defecto; justifica la intervención solo ante una dificultad concreta, riesgo importante o petición expresa.
- Prioriza métodos deterministas y pruebas locales antes de gastar contexto de otro modelo. No abras todo el repositorio o toda la memoria sin necesidad; revisa primero los archivos implicados.
- Respuesta final en español, normalmente tres líneas: HECHO (resultado), PRUEBAS (realizadas y estado), PENDIENTE (solo bloqueo). Idealmente menos de 450 caracteres. Sin auditorías, largos informes o recomendaciones no solicitadas.
- Si se solicita una investigación completa o hay un riesgo de seguridad, informa de lo necesario y conserva la evidencia íntegra. No ocultes pruebas fallidas ni simules capacidades.
- Evita repetir acciones fallidas: ante dos errores iguales, interrumpe los reintentos y expón el bloqueo concreto.
- No cambies automáticamente a APIs de pago; no compres, publiques, despliegues, fusiones PR ni amplíes permisos sin autorización específica.
- Conserva las restricciones particulares del repositorio: estas reglas no eliminan controles existentes.
- Extracción de documentos: usa extractos relevantes cuando la tarea lo permita. El texto parcial nunca sustituye la lectura completa o visual cuando esta sea necesaria. No instales MarkItDown/MCP automáticamente.

## Colaboración desde el teléfono, sin ordenador de casa
1. Elige el repositorio en **Claude Code Cloud** o **Codex Cloud**. Las instrucciones raíz `CLAUDE.md` / `AGENTS.md` aplican en las sesiones que lean este código.
2. Un agente ejecuta y prepara **un PR o commit** con cambios y resultados. Si necesita al otro agente, deja el punto exacto por revisar en el PR o en un documento pequeño, no copies conversaciones enteras.
3. El segundo agente revisa ese PR o commit **solo cuando proceda**, y responde al mismo contexto de GitHub. No presupongas que las sesiones aisladas se comunican automáticamente.
4. Las credenciales de suscripción de Claude y ChatGPT son independientes. **GitHub comparte código y evidencias, no cuotas ni sesiones**. Un puente que llame a la CLI de la otra empresa no está disponible en la nube hasta verificar allí el ejecutable, inicio de sesión y permisos.
5. El PC doméstico puede estar apagado durante las tareas en Cloud. Una sesión local o remota dependiente del PC sí requiere que esté operativo.

## Nuevos proyectos
Copiar las secciones esenciales a los `CLAUDE.md` y `AGENTS.md` raíz al crear cada repositorio. El instalador global de Windows aplica a la cuenta del equipo, pero **GitHub no distribuye por sí solo estas reglas a futuros repositorios ni a nuevas máquinas virtuales**. Para automatizar altas futuras sería necesaria una integración con permisos explícitos.
