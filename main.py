import random
from utils.pokemon import Pokemon
from utils.move import Move
from utils.team import Team


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
        moves = {}
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
            moves[move_dict["name"]] = move
    return moves

def crear_pokemon():
    with open("data/pokemons.csv", "r") as f:
        f.readline()
        pokemon_dicc = {}
        pokemons = []
        parametros = ["pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", "is_legendary", "moves"]
        tipos = [int, str, str, str, int, int, int, int, int, int, int, float, float, int, list]
        lista_moviemintos = definir_moves()
        for line in f:
            valor_parametro = line.split(",")
            for i in range(len(parametros)-1):
                pokemon_dicc[parametros[i]] = tipos[i](valor_parametro[i]) if valor_parametro[i] else 0 # Convertir a tipo de dato correspondiente
            movs_pokemon = []
            for movimiento in valor_parametro[-1].strip().split(";"):
                if movimiento:
                    movs_pokemon.append(lista_moviemintos[movimiento])
            pokemon_dicc["moves"] = movs_pokemon

            pokemon = Pokemon(
                pokemon_dicc["pokedex_number"],
                pokemon_dicc["name"],
                pokemon_dicc["type1"],
                pokemon_dicc["type2"],
                pokemon_dicc["hp"],
                pokemon_dicc["attack"],
                pokemon_dicc["defense"],
                pokemon_dicc["sp_attack"],
                pokemon_dicc["sp_defense"],
                pokemon_dicc["speed"],
                pokemon_dicc["generation"],
                pokemon_dicc["height_m"],
                pokemon_dicc["weight_kg"],
                pokemon_dicc["is_legendary"],
                pokemon_dicc["moves"]
            )
            pokemons.append(pokemon)
    return pokemons
    
def crear_equipo(nombre_equipo):
    lista_pokemons = []
    pokemons = crear_pokemon()
    while len(lista_pokemons) < 6:
        pokemon_agregado = pokemons[random.randint(0, len(pokemons))]
        if not pokemon_agregado.is_legendary and pokemon_agregado not in lista_pokemons:
            lista_pokemons.append(pokemon_agregado)
    return Team(nombre_equipo, lista_pokemons)

pokemon_list = crear_equipo("Equipo random").pokemons

for pokemon in pokemon_list:
    print(pokemon.name)