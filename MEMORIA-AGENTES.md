# Memoria operativa — Web auxiliar J.A.R.V.I.S.
Actualizado: 2026-11-07. No registrar secretos ni datos personales.

## Objetivo
Página estática de retorno de autorización Samsung SmartThings hacia J.A.R.V.I.S. Desktop.

## Verificado
- El repositorio incluye el callback descrito en `README.md` y las instrucciones móviles de Claude y Codex.
- Revisión cruzada por riesgo (R0/R1/R2, máx. 2 rondas) añadida a `puente-compartido` y a `AGENTS.md` (Review guidelines). Preparado en PR; ver su descripción para el resultado de la prueba.

- PixelCreAtI: portadas reales (libros 1-3 de El sueño de ser policía) y una página interior alojadas en `pixelcreati/img/` para emails; importación de Canva vía Actions (`.github/importar/README.md`). ASIN B0D7SR382J, B0HPNXF4J4 y B0HQGQ192R, libro 4 B0HQTTPR65 (portada-4.jpg) comprobados en Amazon.es el 2026-11-07.
- PixelCreAtI embudo: `pixelcreati/kit.html` (kit gratuito PDF en `recursos/`), `privacidad.html` y botón en `index.html`. Alta por mailto a pixelredmedia (la dirección se verifica sola al escribir).

## Pendiente

- 2026-11-08 — Captación PixelCreAtI: PR #10 **fusionado**; CI de GitHub Pages (run 42427040879) despliegue correcto. Enlace a inscripción voluntaria junto al kit y aclaración de descarga gratuita; validación textual 8/8. **Pendiente**: comprobar visualmente desde móvil y validar la entrega del kit en navegador externo. Sin formularios externos, seguimiento ni envíos comerciales activados.
- `privacidad.html`: responsable identificado solo por nombre (decisión de Manuel, sin NIF).
- Para futuros cambios, comprobar el retorno local y la seguridad antes de desplegar.
- Activar *Code review* de Codex para este repo (decisión de Manuel) y repetir la prueba `@codex review` si no respondió.

## Bloqueos
- No registrar ni transmitir parámetros sensibles del flujo OAuth.
- Conservar políticas CSP y no añadir servicios de análisis o seguimiento sin autorización.

## Evidencia
- `README.md`; `IA-COLABORACION.md`; skill `puente-compartido`.
