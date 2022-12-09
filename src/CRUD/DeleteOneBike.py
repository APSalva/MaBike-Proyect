# Importamos las librerias necesarias 
import json
import requests

# Función que elimina bicis de la base de datos
def DeleteOneBike():
    # Creamos una variable que le pida la id de la bici que quiera eliminar
    idBike = input("Que bici es la que quieres eliminar: ")

    url = "https://data.mongodb-api.com/app/data-aeqmn/endpoint/data/v1/action/deleteOne"
    payload = json.dumps({
        "collection": "bikes",
        "database": "bike_database",
        "dataSource": "bike",
        "filter":{"_id":{"$oid":idBike}} })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "Xt3Zlv6lt9PaokpzjqYvIhqVD5eD4ild4mVKSczjZ3xzT2WWavTABFAD1u3ng9Sl",
    }

    response = requests.request("POST", url, headers=headers, data=payload)