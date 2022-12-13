# Creamos una función para crear archivos
def CrearArchivo(archivo,contenido):
    
    # precondiciones:
    # assert isinstance(archivo,str), "No es un string"
    # assert isinstance(contenido,str), "No es un string"
    # assert len(archivo) > 0

    # try: 
        crear_archivo = open(archivo,"w", encoding="UTF-8")
    # except FileNotFoundError:
    #     print("La ruta o el nombre del archivo no es correcto")
    # except TypeError: 
    #     print("El tipo del nombre del archivo es incorrecto")
    # except IOError: 
    #     print("Error de entrada/salida")
    # else:
        crear_archivo.write(contenido)