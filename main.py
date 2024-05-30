import random
from utils.pokemon import Pokemon

def crear_pokemon():
    with open("data/pokemons.csv", "r") as f:
        num_pokemon = random.randint(1, len(f.readlines())-1)
        pokedex_number,name,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,generation,height_m,weight_kg,is_legendary,moves = f.readline(num_pokemon).split(",")
    print(f[num_pokemon])

crear_pokemon()