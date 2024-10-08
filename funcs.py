import random
from tqdm import tqdm
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
        list: Lista con todos los equipos.
    """
    return [crear_equipo(f"Equipo N{n+1}") for n in range(num_equipos)]

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
    for i, equipo in enumerate(poblacion):
        nuevo_equipo = []
        padre = random.choice(seleccionados)[1]
        pokemon_names = set()
        
        for madre in equipo.pokemons:
            if random.random() < 0.03:
                nuevo_pokemon = crear_pokemon()
                while nuevo_pokemon.is_legendary == True:
                    nuevo_pokemon = crear_pokemon()
            elif random.random() < 0.5:  
                nuevo_pokemon = madre
            else:
                nuevo_pokemon = padre.pokemons[equipo.pokemons.index(madre)]
        
            while nuevo_pokemon.name in pokemon_names:
                for pokemon in [madre,padre.pokemons[equipo.pokemons.index(madre)],crear_pokemon()]:
                    if pokemon.name not in pokemon_names:
                        nuevo_pokemon = pokemon
                        while nuevo_pokemon.is_legendary == True:
                            nuevo_pokemon = crear_pokemon()
                        break
            
            nuevo_equipo.append(nuevo_pokemon)
            pokemon_names.add(nuevo_pokemon.name)

        starter = random.randint(1, 5) if random.random() < 0.03 else 0
        hijos.append(Team(f"Equipo N{i + 1}", nuevo_equipo, starter))
    return hijos

def algoritmo_genetico(cant_equipos: int, cant_adversarios: int, cant_generaciones: int) -> tuple[list[object], list[tuple[int, int, dict]], list[tuple[int, object]]]:
    """
    Ejecuta un algoritmo genético para evolucionar una población de equipos a lo largo de varias generaciones.

    Parámetros:
        cant_equipos (int): La cantidad de equipos en la población inicial y en cada generación.
        cant_adversarios (int): La cantidad de adversarios contra los cuales se evalúa la aptitud de los equipos.
        cant_generaciones (int): El número de generaciones que el algoritmo genético debe ejecutar.

    Retorna:
        tuple[list[object], list[tuple[int, int, dict]], list[tuple[int, object]]]:
            - La última generación de la población de equipos después de ejecutar el número especificado de generaciones.
            - Lista de tuplas con datos de diversidad y frecuencia de pokemons por generación.
            - Lista de tuplas con el mejor equipo por generación.
    """
    effectiveness = efectividad()
    nueva_poblacion = poblacion(cant_equipos)
    lista_epochs = []
    lista_teams = []

    for gen in tqdm(range(cant_generaciones), desc="Generaciones", unit="gen", colour="blue"):
        adversarios = poblacion(cant_adversarios)
        aptitudes = evaluar_aptitud(nueva_poblacion, adversarios, effectiveness)
        seleccionados = seleccion_proporcional(aptitudes, cant_adversarios)
        nueva_poblacion = cruce(seleccionados, nueva_poblacion)

        # Registrar datos de la generación para el csv de epochs
        epoch_pokemons = [pokemon.name for team in nueva_poblacion for pokemon in team.pokemons]
        diferentes_pokemons = set(epoch_pokemons)  # Conjunto de pokemons únicos
        diversidad_pokemons = len(diferentes_pokemons)

        frecuencia_pokemons = {}
        for pokemon in epoch_pokemons:
            if pokemon in frecuencia_pokemons:
                frecuencia_pokemons[pokemon] += 1
            else:
                frecuencia_pokemons[pokemon] = 1
        frecuencia_pokemons = dict(sorted(frecuencia_pokemons.items(), key=lambda item: item[1], reverse=True))

        lista_epochs.append((gen, diversidad_pokemons, frecuencia_pokemons))
        lista_teams.append((gen, ordenar_aptitudes(aptitudes)))

    return nueva_poblacion, lista_epochs, lista_teams
        
def ordenar_aptitudes(aptitudes: list[tuple[int, object]]) -> object:
    """
    Ordena los equipos por aptitud de mayor a menor.
    Args:
        aptitudes: lista de tuplas que contiene la aptitud del equipo y el nombre, para cada equipo.
    Returns:
        list: Lista de equipos ordenados por aptitud.
    """
    aptitudes_ord = sorted(aptitudes, key=lambda item: item[0], reverse = True)
    return aptitudes_ord