import apikey
import requests
import json


apikey.save("my_api_key", "26077340633089b830b7985c32a15ff1")

my_api_key = apikey.load("my_api_key")

url = "http://api.weatherstack.com/current"

params = {
    "access_key": "26077340633089b830b7985c32a15ff1",
    "query": "Urbana, Illinois"
}

response = requests.get(url, params=params)

data = response.json()

with open('weather.json', 'w') as f:
    json.dump(data, f)