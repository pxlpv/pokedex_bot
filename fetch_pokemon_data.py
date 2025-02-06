import requests
import json
import os
import time

DATA_DIR = 'pokedex_data'
os.makedirs(DATA_DIR, exist_ok=True)

def get_pokemon_data(pokemon_id):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            file_path = os.path.join(DATA_DIR, f'{pokemon_id}.json')
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f'Saved data for Pokémon ID: {pokemon_id}')
        else:
            print(f'!! Failed to fetch data for Pokémon ID: {pokemon_id}')

def fetch_all_pokemon():
    for pokemon_id in range(1, 650):
        get_pokemon_data(pokemon_id)
        time.sleep(1)

fetch_all_pokemon()