import os
import json

DATA_DIR = 'pokedex_data'

def rename_files():
    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)
        with open(file_path, 'r') as file:
            data = json.load(file)
        pokemon_id = data['id']
        pokemon_name = data['name']
        new_file = f'{pokemon_id:03}_{pokemon_name}.json'
        new_file_path = os.path.join(DATA_DIR, new_file)
        os.rename(file_path, new_file_path)
        print(f'Renamed {file_path} to {new_file_path}')

def sort_files():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    sorted_files = sorted(files, key=lambda x: int(x.split("_")[0]))
    print('Files sorted.')
    return sorted_files
