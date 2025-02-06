import os
import json
import datetime
import discord
from discord.ext import commands

DATA_DIR = 'pokedex_data'
TYPE_COLORS = {
    "Normal": 0xA8A878,
    "Fire": 0xF08030,
    "Water": 0x6890F0,
    "Electric": 0xF8D030,
    "Grass": 0x78C850,
    "Ice": 0x98D8D8,
    "Fighting": 0xC03028,
    "Poison": 0xA040A0,
    "Ground": 0xE0C068,
    "Flying": 0xA890F0,
    "Psychic": 0xF85888,
    "Bug": 0xA8B820,
    "Rock": 0xB8A038,
    "Ghost": 0x705898,
    "Dragon": 0x7038F8,
    "Dark": 0x705848,
    "Steel": 0xB8B8D0,
    "Fairy": 0xEE99AC
}

intents = discord.Intents.default()
intents.message_content = True # Enable access to msg content
bot = commands.Bot(command_prefix='!', intents=intents)

def query_filename(query):
    for filename in os.listdir(DATA_DIR):
        poke_id = filename.split('_')[0].lstrip('0')
        poke_name = filename.split('_')[1].replace('.json', '')
        if (isinstance(query, str) and poke_id == query) or \
            (isinstance(query, str) and poke_name.strip().lower() == query):
                return os.path.join(DATA_DIR, filename)
        
def get_pokemon_details(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    poke_name = data['name'].capitalize()
    poke_id = data['id']
    poke_type = ' / '.join(t['type']['name'].capitalize() for t in data['types'])
    poke_stats = '\n'.join([f"{stat['base_stat']}: {stat['stat']['name'].upper()}" for stat in data['stats']])
    image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    embed_color = TYPE_COLORS.get(poke_type.split(' / ')[0], 0x000000)
    embed = discord.Embed(title=f"{poke_name} | #{poke_id}",
                      url=f"https://bulbapedia.bulbagarden.net/wiki/{poke_name}_(Pok%C3%A9mon)",
                      colour=embed_color,
                      timestamp=datetime.datetime.now())
    embed.set_author(name="Prof Oak")
    embed.add_field(name=f"{poke_type}",
                value=f"{poke_stats}",
                inline=False)
    embed.set_image(url=image_url)
    embed.set_footer(text="PoKeDeX") 
    return embed


# Event: When the bot is ready...
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('-----')

@bot.command()
async def pokedex(ctx, name: str):
    filename = query_filename(name)
    if not filename:
        await ctx.send(f'Could not find Pokémon: {name}')
        return
    response = get_pokemon_details(filename)
    await ctx.send(embed=response)
    

# Run the bot
token = 'enter_your_bot_token_here'
bot.run(token)