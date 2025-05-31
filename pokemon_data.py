import requests
import json
import os

def fetch_data(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    with open (f"{pokemon}.json", "w") as file:
        json.dump(response.json(), file, indent = 4)

def read_data(pokemon):
    file_name = f"{pokemon}.json"
    if not os.path.exists(file_name):
        fetch_data(pokemon)

    with open(file_name, "r") as file:
        data = json.load(file)
        return data


data = read_data("ivysaur")
print(data)
