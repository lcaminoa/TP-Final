# Trabajo Práctico Final de Pensamiento Computacional
### Autores: Lautaro Caminoa, Álvaro Guerrero y Nicolás Heuser

## Estructura de Carpetas y Archivos

### Data

#### Imgs
Contiene las imágenes de cada pokémon en formato `.png`.

#### effectiveness_graph.png
Gráfico de efectividades de los distintos tipos de pokémon contra otros tipos.

#### effectiveness_chart.csv
Archivo CSV que contiene la misma información que `effectiveness_graph.png`, pero ordenada en formato CSV.

#### moves.csv
Archivo CSV que contiene la información de todos los distintos movimientos pokémon:
- `name`: Nombre del movimiento.
- `type`: Tipo del movimiento.
- `category`: Categoría del movimiento.
- `pp`: Puntos de poder del movimiento.
- `power`: Poder del movimiento.
- `accuracy`: Precisión del movimiento.

#### pokemons.csv
Archivo CSV que contiene la información de cada pokémon:
- `pokedex_number`: Número del pokémon en la Pokédex.
- `name`: Nombre del pokémon.
- `type1`: Primer tipo del pokémon.
- `type2`: Segundo tipo del pokémon (si tiene).
- `hp`: Vida del pokémon.
- `attack`: Ataque del pokémon.
- `defense`: Defensa del pokémon.
- `sp_attack`: Ataque especial del pokémon.
- `sp_defense`: Defensa especial del pokémon.
- `speed`: Velocidad del pokémon.
- `generation`: Generación del pokémon.
- `height_m`: Altura del pokémon en metros.
- `weight_kg`: Peso del pokémon en kilogramos.
- `is_legendary`: Indica si el pokémon es legendario.
- `moves`: Movimientos que puede aprender el pokémon.

### Utils

#### combat.py
Contiene las funciones necesarias para simular los combates entre equipos pokémon.
### Funciones

#### `__faint_change__(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> None`
Cambia el pokémon actual del equipo que tiene un pokémon debilitado. El otro equipo también puede cambiar su pokémon después del equipo que tiene el pokémon debilitado.

**Parámetros:**
- `team1 (Team)`: Uno de los equipos.
- `team2 (Team)`: El otro equipo.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

#### `__fight__(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> Team`
Simula una pelea entre dos equipos. La pelea termina cuando todos los pokémon de uno de los equipos han sido debilitados.

**Parámetros:**
- `team1 (Team)`: Uno de los equipos.
- `team2 (Team)`: El otro equipo.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

**Retorna:**
- `Team`: El equipo que ganó la pelea.

#### `get_winner(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> Team`
Simula una pelea entre dos equipos. La pelea termina cuando todos los pokémon de uno de los equipos han sido debilitados. Los pokémon de los equipos se restauran a su estado inicial después de la pelea.

**Parámetros:**
- `team1 (Team)`: Uno de los equipos.
- `team2 (Team)`: El otro equipo.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

**Retorna:**
- `Team`: El equipo que ganó la pelea.

#### move.py
Contiene la clase para definir un objeto `Move` y sus respectivas funciones.
### Clases y Funciones

#### `class Move`
Representa un movimiento de pokémon.

##### `__init__(self, name: str, type: str, category: str, pp: int, power: int, accuracy: int)`
Constructor para inicializar un objeto `Move`.

**Parámetros:**
- `name (str)`: El nombre del movimiento.
- `type (str)`: El tipo del movimiento.
- `category (str)`: La categoría del movimiento (puede ser 'physical' o 'special').
- `pp (int)`: Puntos de poder del movimiento.
- `power (int)`: Poder del movimiento.
- `accuracy (int)`: Precisión del movimiento.

##### `@staticmethod from_dict(name: str, data: dict[str, str|int]) -> Move`
Crea un objeto `Move` a partir de un diccionario.

**Parámetros:**
- `name (str)`: El nombre del movimiento.
- `data (dict[str, str|int])`: Un diccionario que contiene el tipo, categoría, pp, poder y precisión del movimiento.

**Retorna:**
- `Move`: El movimiento creado a partir del diccionario.

**Ejemplo:**
```python```
data = {'type': 'fire', 'category': 'special', 'pp': 10, 'power': 90, 'accuracy': 100}
move = Move.from_dict('Flamethrower', data)


#### pokemon.py
Contiene la clase para definir un objeto `Pokemon` y sus respectivas funciones.
### Clases y Funciones

#### `class Pokemon`
Representa un pokémon.

##### `__init__(self, pokedex_number: int, name: str, type1: str, type2: str|None, hp: int, attack: int, defense: int, sp_attack: int, sp_defense: int, speed: int, generation: int, height: float, weight: float, is_legendary: bool, moves: list[Move], level: int=50)`
Constructor para inicializar un objeto `Pokemon`.

**Parámetros:**
- `pokedex_number (int)`: El número en la pokédex del pokémon.
- `name (str)`: El nombre del pokémon.
- `type1 (str)`: El tipo primario del pokémon.
- `type2 (str|None)`: El tipo secundario del pokémon. Si el pokémon tiene solo un tipo, debe ser None.
- `hp (int)`: Los puntos de vida base del pokémon.
- `attack (int)`: El ataque base del pokémon.
- `defense (int)`: La defensa base del pokémon.
- `sp_attack (int)`: El ataque especial base del pokémon.
- `sp_defense (int)`: La defensa especial base del pokémon.
- `speed (int)`: La velocidad base del pokémon.
- `generation (int)`: La generación del pokémon.
- `height (float)`: La altura del pokémon en metros.
- `weight (float)`: El peso del pokémon en kilogramos.
- `is_legendary (bool)`: Si el pokémon es legendario o no.
- `moves (list[Move])`: Los movimientos que el pokémon puede usar.
- `level (int)`: El nivel del pokémon. Por defecto es 50.

##### `@staticmethod from_dict(name: str, data: dict[str, str|int|float|bool|None], moves_data: dict[str, dict[str, str|int]]) -> Pokemon`
Crea un objeto `Pokemon` a partir de un diccionario.

**Parámetros:**
- `name (str)`: El nombre del pokémon.
- `data (dict[str, str|int|float|bool|None])`: Un diccionario que contiene el número en la pokédex, tipo1, tipo2, hp, ataque, defensa, ataque especial, defensa especial, velocidad, generación, altura, peso, si es legendario y los movimientos del pokémon.
- `moves_data (dict[str, dict[str, str|int]])`: Un diccionario que contiene los datos de los movimientos del pokémon.

**Retorna:**
- `Pokemon`: El pokémon creado a partir del diccionario.

**Ejemplo:**
```python```
data = {
    'pokedex_number': 1,
    'type1': 'grass',
    'type2': 'poison',
    'hp': 45,
    'attack': 49,
    'defense': 49,
    'sp_attack': 65,
    'sp_defense': 65,
    'speed': 45,
    'generation': 1,
    'height_m': 0.7,
    'weight_kg': 6.9,
    'is_legendary': False,
    'moves': ['tackle', 'growl', 'leer', 'vine whip']
}
moves_data = {
    'tackle': {'type': 'normal', 'category': 'physical', 'pp': 35, 'power': 40, 'accuracy': 100},
    'growl': {'type': 'normal', 'category': 'status', 'pp': 40, 'power': 0, 'accuracy': 100},
    'leer': {'type': 'normal', 'category': 'status', 'pp': 30, 'power': 0, 'accuracy': 100},
    'vine whip': {'type': 'grass', 'category': 'physical', 'pp': 25, 'power': 45, 'accuracy': 100}
}
pokemon = Pokemon.from_dict('Bulbasaur', data, moves_data)


#### team.py
Contiene la clase para definir un objeto `Team` y sus respectivas funciones.

#### main.py
Archivo principal para ejecutar el programa.
