# Importamos las librerias que necesitamos 
import json
import requests

# Función para modificar una bici ya creada en la base de datos
def UpdateOneBike():
    # Pedimos al usuario que nos diga la id de la bici a modificar, el campo a modificar y el valor que queremos modificar
    idBike = input("Pon la id de la bici que quieres modificar: ")
    campoBike = input("""Que campo quieres modificar: """)

    # Si campoBike es algunos de esos campos que lo convierta en inter
    if campoBike == "precio" or campoBike == "stock" or campoBike == "n_velocidades" or campoBike == "peso" or campoBike == "volumen_ruedas":
        nuevovalor = float(input(f"Que valor le quieres dar a {campoBike}: "))
    else:
        nuevovalor = input(f"Que valor le quieres dar a {campoBike}: ")

    url = "https://data.mongodb-api.com/app/data-aeqmn/endpoint/data/v1/action/updateOne"
    payload = json.dumps({
        "collection": "bikes",
        "database": "bike_database",
        "dataSource": "bike",
        "filter":{"_id": {"$oid":idBike }},
            "update": {
                "$set": {
                    campoBike : nuevovalor
                }
            }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "Xt3Zlv6lt9PaokpzjqYvIhqVD5eD4ild4mVKSczjZ3xzT2WWavTABFAD1u3ng9Sl",
    }

    response = requests.request("POST", url, headers=headers, data=payload)