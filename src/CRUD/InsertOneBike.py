# Importamos la librerias necesarias
import json
import requests

# Creamos una función para poder crear una nueva bici
def InsertOneBike():

    nombreBike = input("Nombre:")
    precioBike = float(input("Precio: "))
    tipoBike = input("Tipo: ")
    tallaBike = input("Talla: ")
    marcaBike = input("Marca: ")
    materialBike = input("Material: ")
    stockBike = int(input("Stock: "))
    n_velocidadesBike = int(input("Número de velocidades: "))
    pesoBike = float(input("Peso: "))
    ubicacionBike = input("Ubicación: ")
    imgBike = input("Link de la img: ")
    volumen_ruedasBike = float(input("Volumen rueda: "))


    url = "https://data.mongodb-api.com/app/data-aeqmn/endpoint/data/v1/action/insertOne"
    payload = json.dumps({
        "collection": "bikes",
        "database": "bike_database",
        "dataSource": "bike",
        "document":{
            "nombre" : nombreBike,
            "precio" : precioBike,
            "tipo" : tipoBike,
            "marca" : marcaBike,
            "material" : materialBike,
            "stock" : stockBike,
            "n_velocidades" : n_velocidadesBike,
            "peso" : pesoBike,
            "ubicacion": ubicacionBike,
            "img" : imgBike,
            "volumen_ruedas" : volumen_ruedasBike
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "Xt3Zlv6lt9PaokpzjqYvIhqVD5eD4ild4mVKSczjZ3xzT2WWavTABFAD1u3ng9Sl",
    }

    response = requests.request("POST", url, headers=headers, data=payload)