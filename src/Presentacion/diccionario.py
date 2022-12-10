import json

def Diccionario_JSON():
    try: 
        with open("JSON/bikes.json") as json_file:
            diccionario = json.load(json_file)
    except FileNotFoundError: 
        print("No se encuentra el archivo JSON")
    except UnboundLocalError:
        print("El archivo no tiene contenido")
    else:
        return diccionario