import requests
import json

def fetch_data(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    with open (f"{pokemon}.json", "w") as file:
        json.dump(response.json(), file, indent = 4)

fetch_data("pikachu")