# pokedex_bot
A small and simple Discord Bot that can give you a basic overview of Pokemon in your Discord.
The current functionality is to use data from JSON files pulled from Pokeapi and populate Discord embeds with the Pokemon's name, which is also a link to the Pokemon's Bulbapedia page, the type/types, the base stats, and an image of the Pokemon. It also colors the side of the embed to match the type.

Included in this repo is the script I used to pull all Pokemon from the first 5 gens from Pokeapi and save them in a 'pokedex_data' folder. After pulling them, I wanted to rename them so that each file had the ID number as well as the Pokemon name as the file name, so there is a script for that in here as well.
