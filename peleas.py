from utils.pokemon import Pokemon
from funcs import definir_moves

def crear_pokemon_pokedex_num(pokedex_num:int) -> object:
    """
    Lee un archivo CSV con datos de Pokémon y devuelve un objeto Pokémon aleatorio.
    """
    with open("data/pokemons.csv", "r") as f:
        f.readline()
        data = {}
        moves_data = definir_moves()
        moves = []
        parametros = ["pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", "is_legendary", "moves"]
        tipos = [int, str, str, str, int, int, int, int, int, int, int, float, float, int, list]
        line = f.readlines(pokedex_num + 1)
        valor_parametro = line.strip().split(",")

        for i,parametro in enumerate(parametros):
            if parametro != "name" and parametro != "moves":
                data[parametro] = tipos[i](valor_parametro[i]) if valor_parametro[i] else None # Convertir a tipo de dato correspondiente
            elif parametro == "name":
                name = valor_parametro[i]
            else:
                moves = valor_parametro[i].strip().split(";")
                data[parametro] = tipos[i](moves) if valor_parametro[i] else []
        pokemon = Pokemon.from_dict(name,data,moves_data)
    return pokemon

def crear_equipo(nombre_equipo: str, pokemon_nums: list[int]) -> object:
    """
    Crea un equipo de Pokémon no legendarios ni duplicados aleatorios.

    Esta función genera un equipo de 6 Pokémon seleccionados aleatoriamente generados de la funcion crear_pokemon() la cual crea un objeto pokemon creado a partir 
    de los datos leídos del archivo "data/pokemons.csv". Solo se incluyen Pokémon no legendarios y sin duplicados 
    en el equipo.

    Parámetros:
        nombre_equipo (str): El nombre del equipo.

    Returns:
        Team: Un objeto `Team` que contiene el nombre del equipo y una lista de 6 objetos `Pokemon`.
    """
    equipo_pokemons = []

    for pokedex_num in pokemon_nums:
        pokemon = crear_pokemon_pokedex_num(pokedex_num)
        equipo_pokemons.append(pokemon)

elite_four_member_1 = crear_equipo("Elite Four Member 1", [437, 124, 326, 80, 282, 178]) # Bronzong, Jynx, Grumpig, Slowbro, Gardevoir, Xatu
elite_four_member_2 = crear_equipo("Elite Four Member 2", [435, 454, 317, 49, 89, 169]) # Skunktank, Toxicroak, Swalot, Venomoth, Muk, Crobat
elite_four_member_3 = crear_equipo("Elite Four Member 3", [237, 106, 297, 68, 448, 107]) # Hitmontop, Hitmonlee, Hariyama, Machamp, Lucario, Hitmonchan
elite_four_member_4 = crear_equipo("Elite Four Member 4", [461, 442, 430, 197, 229, 359]) # Weavile, Spiritomb, Honchkrow, Umbreon, Houndoom, Absol
champion = crear_equipo("Champion", [373, 445, 149, 6, 334, 130]) # Salamence, Garchomp, Dragonite, Charizard, Altaria, Gyarados

