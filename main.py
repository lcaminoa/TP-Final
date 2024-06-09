import random
import time
from utils.pokemon import Pokemon
from utils.move import Move
from utils.team import Team
from utils.combat import get_winner

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

def crear_pokemon() -> object:
    """
    Lee un archivo CSV con datos de Pokémon y devuelve un objeto Pokémon aleatorio.

    Esta función abre el archivo "data/pokemons.csv", lee su contenido y lo procesa para crear un objeto Pokémon.

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
        object: Un objeto `Pokemon`.
    """
    with open("data/pokemons.csv", "r") as f:
        f.readline()
        data = {}
        moves_data = definir_moves()
        moves = []
        parametros = ["pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", "is_legendary", "moves"]
        tipos = [int, str, str, str, int, int, int, int, int, int, int, float, float, int, list]
        line = random.choice(f.readlines())
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
    
def crear_equipo(nombre_equipo: str) -> object:
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
    pokemon_names = set()

    while len(equipo_pokemons) < 6:
        pokemon = crear_pokemon()
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

def efectividad()->dict:
    """
    Crea el diccionario con las efectividades de cada tipo de pokemon contra los otros.

        Returns:
        dict: diccionario con las efectividades de cada tipo
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

def aptitud(mi_equipo:object,adversarios:list,effectiveness:dict)->int:
    """
    Calcula la aptitud de el equipo pokemon seleccionado.

    Args:
        mi_equipo: Equipo al que se le desea calcular la aptitud.
        adversarios: Equipos contra los que se enfrentara "mi_equipo".

    Returns:
        int: Cantidad de batallas ganadas.
    """  
    return sum([1 for i in range(len(adversarios)) if get_winner(mi_equipo, adversarios[i], effectiveness) == mi_equipo])

def evaluar_aptitud(list_equipos:list,adversarios:list,effectiveness:dict)->list[tuple]:
    """
    Evalúa la aptitud de una lista de equipos en función de la cantidad de adversarios.

    Parámetros:
        list_equipos (list): Una lista de equipos, donde cada equipo es un objeto que puede ser evaluado por la 
        función `aptitud`.
        adversarios (list): Adversarios que cada equipo debe enfrentar.

    Returns:
        list[tuple]: Una lista de tuplas que contiene la aptitud del equipo y el objeto equipo correspondiente, para cada equipo.
    """
    return [(aptitud(team, adversarios,effectiveness),team) for team in list_equipos]

def seleccion_proporcional(list_aptitudes:list[tuple], cant_adversarios:int)->list[tuple]:
    """
    Selecciona equipos de forma aleatoria, teniendo en cuenta su aptitud.
    Si su aptitud es más alta, entoncés su probabilidad de ser seleccionado será mayor y viceversa.
    Args:
        list_aptitudes: lista de tuplas que contiene la aptitud del equipo y el nombre, para cada equipo.
        cant_adversarios (int): El número de adversarios que cada equipo debe enfrentar.
    """
    seleccionados = []
    for i in range(len(list_aptitudes)):
        candidato = list_aptitudes[i]
        if random.randrange(0,cant_adversarios+1) < candidato[0]:
            seleccionados.append(candidato)
    return seleccionados

def cruce(seleccionados:list[tuple],poblacion:list[object])->list[object]:
    """
    Realiza el cruce genético entre una lista de equipos seleccionados y una población de equipos, generando una nueva generación de equipos.

    Parámetros:
        seleccionados (list[tuple]): Una lista de tuplas donde cada tupla contiene un valor de aptitud y un equipo (padre). 
        poblacion (list[object]): Una lista de equipos (objetos) que representan la población inicial.

    Retorna:
        list[object]: Una lista de nuevos equipos (objetos) generados a partir del cruce genético.
    """
    hijos = []
    for i, team in enumerate(poblacion):
        starter = 0
        equipo = []
        padre = seleccionados[random.randrange(0, len(seleccionados))][1]
        pokemon_names = set()
        for j, madre in enumerate(team.pokemons):
            if random.randrange(0, 101) < 3:
                nuevo = crear_pokemon()
                while nuevo.name in pokemon_names:
                    nuevo = crear_pokemon()
                equipo.append(nuevo)
                pokemon_names.add(nuevo.name)
            elif random.randrange(0, 2) == 1:
                if madre.name not in pokemon_names:
                    equipo.append(madre)
                    pokemon_names.add(madre.name)
                else:
                    nuevo = crear_pokemon()
                    while nuevo.name in pokemon_names:
                        nuevo = crear_pokemon()
                    equipo.append(nuevo)
                    pokemon_names.add(nuevo.name)
            else:
                if padre.pokemons[j].name not in pokemon_names:
                    equipo.append(padre.pokemons[j])
                    pokemon_names.add(padre.pokemons[j].name)
                else:
                    nuevo = crear_pokemon()
                    while nuevo.name in pokemon_names:
                        nuevo = crear_pokemon()
                    equipo.append(nuevo)
                    pokemon_names.add(nuevo.name)
        if random.randrange(0, 101) < 3:
            starter = random.randrange(1,6)
        hijos.append(Team(f"Equipo N°{i + 1}", equipo,starter))
    return hijos

def algoritmo_genetico(cant_equipos:int,cant_adversarios:int,cant_generaciones):
    """
    Ejecuta un algoritmo genético para evolucionar una población de equipos a lo largo de varias generaciones.

    Parámetros:
        cant_equipos (int): La cantidad de equipos en la población inicial y en cada generación.
        cant_adversarios (int): La cantidad de adversarios contra los cuales se evalúa la aptitud de los equipos.
        cant_generaciones (int): El número de generaciones que el algoritmo genético debe ejecutar.

    Retorna:
        list[object]: La última generación de la población de equipos después de ejecutar el número especificado de generaciones.
    """
    adversarios = poblacion(cant_adversarios)
    effectiveness = efectividad()
    población_inicial = poblacion(cant_equipos)
    aptitudes = evaluar_aptitud(población_inicial,adversarios,effectiveness)
    seleccionados = seleccion_proporcional(aptitudes,cant_adversarios)
    for _ in range(cant_generaciones):
        población_inicial = poblacion(cant_equipos)
        nueva_poblacion = cruce(seleccionados,población_inicial)
        aptitudes = evaluar_aptitud(nueva_poblacion,adversarios,effectiveness)
        seleccionados = seleccion_proporcional(aptitudes,cant_adversarios)
    return nueva_poblacion

def main():
    cant_equipos = 10
    cant_adversarios = 100
    cant_generaciones = 10
    adversarios = poblacion(cant_adversarios)
    effectiveness = efectividad()
    inicio = time.time()
    dreams_teams = algoritmo_genetico(cant_equipos,cant_adversarios,cant_generaciones)
    print("--------dreams teams--------")
    for team in dreams_teams:
        print(f"{team.name} aptitud:{aptitud(team,adversarios,effectiveness)}")
        for pokemon in team.pokemons:
            print(pokemon.name)
        print()
    fin = time.time()
    print()
    print(f"La función tardó {fin - inicio} segundos en ejecutarse.")
    print()

if __name__ == "__main__":
    main()