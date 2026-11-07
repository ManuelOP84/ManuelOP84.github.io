# Memoria operativa — Web auxiliar J.A.R.V.I.S.
Actualizado: 2026-11-07. No registrar secretos ni datos personales.

## Objetivo
Página estática de retorno de autorización Samsung SmartThings hacia J.A.R.V.I.S. Desktop.

## Verificado
- El repositorio incluye el callback descrito en `README.md` y las instrucciones móviles de Claude y Codex.
- Revisión cruzada por riesgo (R0/R1/R2, máx. 2 rondas) añadida a `puente-compartido` y a `AGENTS.md` (Review guidelines). Preparado en PR; ver su descripción para el resultado de la prueba.

## Pendiente
- Para futuros cambios, comprobar el retorno local y la seguridad antes de desplegar.
- Activar *Code review* de Codex para este repo (decisión de Manuel) y repetir la prueba `@codex review` si no respondió.

## Bloqueos
- No registrar ni transmitir parámetros sensibles del flujo OAuth.
- Conservar políticas CSP y no añadir servicios de análisis o seguimiento sin autorización.

## Evidencia
- `README.md`; `IA-COLABORACION.md`; skill `puente-compartido`.
