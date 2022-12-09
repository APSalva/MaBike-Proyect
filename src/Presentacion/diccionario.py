import json

def Diccionario_JSON():
    with open("Database/bikes.json") as json_file:
        diccionario = json.load(json_file)
    return diccionario