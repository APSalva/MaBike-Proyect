# Importamos librerias necesarias 
import requests
import json

# Acceder a la base de datos desde la API de Mongo
def ObtenerJson():
  url = "https://data.mongodb-api.com/app/data-aeqmn/endpoint/data/v1/action/find"
  payload = json.dumps({
      "collection": "bikes",
      "database": "bike_database",
      "dataSource": "bike",
      "projection":{
        "_id" : 0
      }
  })
  headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': "Xt3Zlv6lt9PaokpzjqYvIhqVD5eD4ild4mVKSczjZ3xzT2WWavTABFAD1u3ng9Sl",
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  result = response.text
  result = json.loads(result)

  f = open("Database/bikes.json", "w", encoding="UTF-8")
  json.dump(result["documents"], f, ensure_ascii=False)
  f.close()

ObtenerJson()