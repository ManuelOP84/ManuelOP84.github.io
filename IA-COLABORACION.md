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
Copiar las secciones esenciales a los `CLAUDE.md` y `AGENTS.md` raíz al crear cada repositorio. El instalador global de Windows aplica a la cuenta del equipo, pero **GitHub no distribuye por sí solo estas reglas a futuros repositorios ni a nuevas máquinas virtuales**. La automatización de ChatGPT para repositorios nuevos ya está habilitada con acceso GitHub; incorpora la plantilla común periódicamente si la conexión y permisos siguen vigentes. No implica ejecución directa del puente en la nube.

## Asesor práctico de mejora de trabajo
- **Primero completa el encargo.** Mientras trabajas, detecta fricciones reales: pasos manuales repetidos, pruebas redundantes, gasto de contexto, esperas, errores frecuentes o tareas que no llegan a resultados visibles.
- Sugiere al final **como máximo UNA mejora opcional**, y solo si existe una oportunidad concreta, respaldada por lo observado y con beneficio mayor que la complejidad. En una tarea rutinaria sin hallazgo útil, no sugieras nada.
- Fórmula de una línea: **Mejora sugerida:** cambio específico + por qué ahorra trabajo o mejora resultados + coste o condición. No hagas una auditoría general ni una lista de herramientas cada turno.
- Prioriza aprovechar el sistema actual; compara una herramienta externa solo si resuelve un bloqueo y confirma precio, permisos y limitaciones antes de aconsejar instalarla. Evita nuevas capas que dupliquen funciones.
- Separa hallazgos **verificados** (código, CI, métricas de proveedores) de hipótesis. Prioriza una prueba real de usuario sobre nuevas funciones cosméticas. No inventes ahorros, ingresos, integraciones ni servicios funcionando.
- Para propuestas que requieran gastos, publicación, permisos, credenciales o cambios críticos, **recomienda sin ejecutar** y espera autorización específica. Para mejoras pequeñas, seguras y autorizadas, verifica y entrega el resultado sin explicaciones largas.

