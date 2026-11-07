# Importar imágenes de Canva

Desde la nube de Claude no se pueden descargar las exportaciones de Canva ni abrir Amazon. Este flujo lo hace GitHub Actions:

1. Exportar el diseño en Canva (MCP `export-design`) y copiar la URL firmada (caduca en horas).
2. En una rama `claude/...`, crear `.github/importar/lista.txt` con líneas `nombre.jpg|URL`.
3. Al subirla, Actions descarga los archivos a `.github/importar/descargas/`, comprueba los títulos de los libros en Amazon (`amazon.txt`), borra la lista y hace commit en la misma rama.
4. Recortar/optimizar en local y mover el resultado a `pixelcreati/img/`. Las descargas en bruto no se fusionan a `main`.
