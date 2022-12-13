# Importamos la librerias necesarias
import json
import requests

# Creamos una función que nos muestre todas las bicis
def FindBike():
    url = "https://data.mongodb-api.com/app/data-aeqmn/endpoint/data/v1/action/find"
    payload = json.dumps({
        "collection": "bikes",
        "database": "bike_database",
        "dataSource": "bike",
        "filter":{}
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "Xt3Zlv6lt9PaokpzjqYvIhqVD5eD4ild4mVKSczjZ3xzT2WWavTABFAD1u3ng9Sl",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
FindBike()