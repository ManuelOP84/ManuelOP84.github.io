# Página de retorno de J.A.R.V.I.S. Desktop

Página estática y pública que usa la autorización oficial de Samsung SmartThings para devolver el control a J.A.R.V.I.S. Desktop, que escucha solo en este ordenador (`http://localhost:51888`).

- No contiene datos, cuentas ni secretos. No carga scripts externos ni analítica (CSP estricta, sin referer).
- Solo reenvía `code` y `state` al propio ordenador y borra la dirección del historial.
- El código no sirve sin la clave secreta de la aplicación, que solo existe cifrada en el ordenador del propietario.
