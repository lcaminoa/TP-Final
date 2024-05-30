import random
from utils.pokemon import Pokemon

def crear_pokemon():
    with open("data/pokemons.csv", "r") as f:
        pokemon = {}
        pokemons = []
        f.readline()
        for line in f:
            info = line.split(",")
            pokemon["pokedex_numer"] = int(info[0])
            pokemon["name"] = str(info[1])
            pokemon["type1"] = str(info[2])
            pokemon["type2"] = str(info[3])
            pokemon["hp"] = int(info[4])
            pokemon["attack"] = int(info[5])
            pokemon["defense"] = int(info[6])
            pokemon["sp_attack"] = int(info[7])
            pokemon["sp_defense"] = int(info[8])
            pokemon["speed"] = int(info[9])
            pokemon["generation"] = int(info[10])
            pokemon["height_m"] = float(info[11])
            pokemon["weight_kg"] = float(info[12])
            pokemon["is_legendary"] = int(info[13])
            pokemon["moves"] = list(info[14])
            Pokemon()
            pokemons.append(Pokemon)
        print(pokemons)
    

crear_pokemon()