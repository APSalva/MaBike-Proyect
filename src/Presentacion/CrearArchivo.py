# Creamos una función para crear archivos
def CrearArchivo(archivo,contenido):
    crear_archivo = open(archivo,"w", encoding="UTF-8")
    crear_archivo.write(contenido)