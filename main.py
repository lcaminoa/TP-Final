import random
from utils.pokemon import Pokemon
from utils.move import Move


'''
Nota: 
Creo que definir_moves anda bien, aunque no entendi porque tuve
que poner move_dict en vez de usar move directamente.

En crear_pokemon, solo faltaria implementar la parte de los moves
que no entendi como hacerlo.
'''

def definir_moves():
    with open("data/moves.csv", "r") as f:
        move_dict = {}
        moves = []
        parametros = ["name", "type", "category", "pp", "power", "accuracy"]
        tipos = [str, str, str, int, int, int]
        f.readline()
        for line in f:
            valor_parametro = line.split(",")
            for i in range(len(parametros)):
                move_dict[parametros[i]] = tipos[i](valor_parametro[i]) # Convertir a tipo de dato correspondiente
            move = Move(
                move_dict["name"],
                move_dict["type"],
                move_dict["category"],
                move_dict["pp"],
                move_dict["power"],
                move_dict["accuracy"]
            )
            moves.append(move)
    return moves  
definir_moves()

def crear_pokemon():
    with open("data/pokemons.csv", "r") as f:
        f.readline()
        pokemon = {}
        pokemons = []
        parametros = ["pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", "is_legendary", "moves"]
        tipos = [int, str, str, str, int, int, int, int, int, int, int, float, float, int, list] 
        for line in f:
            valor_parametro = line.split(",")
            for i in range(len(parametros)):
                pokemon[parametros[i]] = tipos[i](valor_parametro[i]) # Convertir a tipo de dato correspondiente
            pokemon = Pokemon(
                pokemon["pokedex_number"],
                pokemon["name"],
                pokemon["type1"],
                pokemon["type2"],
                pokemon["hp"],
                pokemon["attack"],
                pokemon["defense"],
                pokemon["sp_attack"],
                pokemon["sp_defense"],
                pokemon["speed"],
                pokemon["generation"],
                pokemon["height_m"],
                pokemon["weight_kg"],
                pokemon["is_legendary"],
                pokemon["moves"]
            )
            pokemons.append(pokemon)
    return pokemons
    
#moves = definir_moves()
pokemons = crear_pokemon()
