import requests
import json
url = "https://data.mongodb-api.com/app/data-aeqmn/endpoint/data/v1/action/find"

payload = json.dumps({
    "collection": "bikes",
    "database": "bike_database",
    "dataSource": "bike",
    "filter": {
        
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "kX4cSFDNtPfXvCxbpXUnKpiQppEdI7Uc8lfD4LjgEcF6WLDJ8YEAcP0IqiSGlhFu", 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
