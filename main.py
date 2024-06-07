import random
import time
from utils.pokemon import Pokemon
from utils.move import Move
from utils.team import Team
from utils.combat import get_winner

cant_adversarios = 10
num_equipos = 20

def definir_moves() -> dict[str : object]:
    """
    Lee un archivo CSV con datos de movimientos y devuelve un diccionario de objetos Move.

    Esta función abre el archivo "data/moves.csv", lee su contenido y lo procesa para crear un diccionario de movimientos.
    Cada movimiento es representado por un objeto de la clase `Move` y se almacena en un diccionario donde la clave es 
    el nombre del movimiento.

    Formato del archivo CSV:
        La primera línea del archivo CSV es un encabezado que se ignora.
        Las líneas siguientes contienen los datos de los movimientos separados por comas.
        Los campos en cada línea representan los siguientes parámetros en orden: "name", "type", "category", "pp", "power", "accuracy".

    Returns:
        dict: Un diccionario donde las claves son los nombres de los movimientos (str) y los valores son objetos `Move`.
    """
    with open("data/moves.csv", "r") as f:
        moves_data = {}
        move = {}
        parametros = ["type", "category", "pp", "power", "accuracy"]
        tipos = [str, str, int, int, int]
        f.readline()
        for line in f:
            valor_parametro = line.split(",")
            name = valor_parametro.pop(0)
            for i,parametro in enumerate(parametros):
                move[parametro] = tipos[i](valor_parametro[i])
            moves_data[name] = move
            
    return moves_data

def crear_pokemon() -> list[object]:
    """
    Lee un archivo CSV con datos de Pokémon y devuelve una lista de objetos Pokémon.

    Esta función abre el archivo "data/pokemons.csv", lee su contenido y lo procesa para crear una lista de Pokémon.
    Cada Pokémon es representado por un objeto de la clase `Pokemon` y se almacena en una lista.

    Formato del archivo CSV:
        La primera línea del archivo CSV es un encabezado que se ignora.
        Las líneas siguientes contienen los datos de los Pokémon separados por comas.
        Los campos en cada línea representan los siguientes parámetros en orden: 
        "pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", 
        "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", 
        "is_legendary", "moves".

    Parámetros de los campos:
        - pokedex_number: int
        - name: str
        - type1: str
        - type2: str
        - hp: int
        - attack: int
        - defense: int
        - sp_attack: int
        - sp_defense: int
        - speed: int
        - generation: int
        - height_m: float
        - weight_kg: float
        - is_legendary: int (0 o 1)
        - moves: list (lista de objetos `Move`)

    Returns:
        list: Una lista de objetos `Pokemon`.
    """
    with open("data/pokemons.csv", "r") as f:
        f.readline()
        data = {}
        pokemons = []
        parametros = ["pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", "is_legendary", "moves"]
        tipos = [int, str, str, str, int, int, int, int, int, int, int, float, float, int, list]
        moves_data = definir_moves()
        for line in f:
            valor_parametro = line.strip().split(",")

            for i,parametro in enumerate(parametros):
                if parametro != "name" and parametro != "moves":
                    data[parametro] = tipos[i](valor_parametro[i]) if valor_parametro[i] else None # Convertir a tipo de dato correspondiente
                elif parametro == "name":
                    name = valor_parametro[i]
                else:
                    moves = valor_parametro[i].strip().split(";")
                    data[parametro] = tipos[i](moves) if valor_parametro[i] else ""
            pokemon = Pokemon.from_dict(name,data,moves_data)
            pokemons.append(pokemon)
    return pokemons
    
def crear_equipo(nombre_equipo: str) -> object:
    """
    Crea un equipo de Pokémon no legendarios aleatorios.

    Esta función genera un equipo de 6 Pokémon seleccionados aleatoriamente de una lista de Pokémon creada a partir 
    de los datos leídos del archivo "data/pokemons.csv". Solo se incluyen Pokémon no legendarios y sin duplicados 
    en el equipo.

    Parámetros:
        nombre_equipo (str): El nombre del equipo.

    Returns:
        Team: Un objeto `Team` que contiene el nombre del equipo y una lista de 6 objetos `Pokemon`.
    """
    pokemons = crear_pokemon()
    equipo_pokemons = []
    pokemon_names = set()

    while len(equipo_pokemons) < 6:
        pokemon = random.choice(pokemons)
        if pokemon.name not in pokemon_names and not pokemon.is_legendary:
            equipo_pokemons.append(pokemon)
            pokemon_names.add(pokemon.name)

    return Team(nombre_equipo, equipo_pokemons)

def poblacion(num_equipos:int)->list[object]:
    """
    Crea una lista con una cantidad indicada de equipos pokemon.

    Args:
        num_equipos: Cantidad de equipos que se deseen generar.

    Returns:
        list: Lista con todods los equipos.
    """
    return [crear_equipo(f"Equipo N°{n+1}") for n in range(num_equipos)]

def efectividad():
    """
    Crea el diccionario con las efectividades de cada tipo de pokemon contra los otros.
    """
    dict_efectividades = {}
    with open("data/effectiveness_chart.csv", "r") as f:
        f.readline()
        tipos = ["normal","fire","water","electric","grass","ice","fighting","poison","ground","flying","psychic","bug","rock","ghost","dragon","dark","steel","fairy"]
        for line in f:
            dic_pokemon = {}
            valores = line.strip().split(",")
            for i in range(len(tipos)):
                dic_pokemon[tipos[i]] = float(valores[i+1])
            dict_efectividades[valores[0]] = dic_pokemon
    return dict_efectividades

def aptitud(mi_equipo:object,cant_adversarios:int)->int:
    """
    Calcula la aptitud de el equipo pokemon seleccionado.

    Args:
        mi_equipo: Equipo al que se le desea calcular la aptitud.
        adversarios_aleatorios: Cantidad de equipos aleatorios contra los que se enfrentara "mi_equipo".

    Returns:
        int: Cantidad de batallas ganadas.
    """  
    adversarios = poblacion(cant_adversarios)
    effectiveness = efectividad()
    return sum([1 for i in range(cant_adversarios-1) if get_winner(mi_equipo, adversarios[i], effectiveness) == mi_equipo])

def evaluar_aptitud(list_equipos:list,cant_adversarios:int)->list[tuple]:
    """
    Evalúa la aptitud de una lista de equipos en función de la cantidad de adversarios.

    Esta función calcula la aptitud de cada equipo en la lista proporcionada, basándose en el número de adversarios
    especificado. 

    Parámetros:
        list_equipos (list): Una lista de equipos, donde cada equipo es un objeto que puede ser evaluado por la 
        función `aptitud`.
        cant_adversarios (int): El número de adversarios que cada equipo debe enfrentar.

    Returns:
        list[tuple]: Una lista de tuplas que contiene la aptitud del equipo y el nombre, para cada equipo.
    """
    return [(aptitud(team, cant_adversarios),team) for team in list_equipos]

def seleccion_proporcional(list_aptitudes:list[tuple], cant_adversarios:int)->list[tuple]:
    """
    Selecciona equipos de forma aleatoria, teniendo en cuenta su aptitud.
    Si su aptitud es más alta, entoncés su probabilidad de ser seleccionado será mayor y viceversa.
    Args:
        list_aptitudes: lista de tuplas que contiene la aptitud del equipo y el nombre, para cada equipo.
        cant_adversarios (int): El número de adversarios que cada equipo debe enfrentar.
    """
    seleccionados = []
    for _ in list_aptitudes:
        candidato = random.choice(list_aptitudes)
        if random.randrange(0,cant_adversarios) < candidato[0]:
            seleccionados.append(candidato)
    return seleccionados

def main():
    inicio = time.time()
    lista_equipos = poblacion(num_equipos)
    generacion =evaluar_aptitud(lista_equipos,cant_adversarios)
    for team in lista_equipos:
        print(team.name)
        for pokemon in team.pokemons:
            print(pokemon.name)
        print()
    seleccionados = seleccion_proporcional(generacion)
    print("------sellecionados------")
    print()
    for tupla in seleccionados:
        print(f"{tupla[1].name} aptitud:{tupla[0]}")
        for pokemon in tupla[1].pokemons:
            print(pokemon.name)
        print()
    fin = time.time()
    print(f"La función tardó {fin - inicio} segundos en ejecutarse.")

if __name__ == "__main__":
    main()