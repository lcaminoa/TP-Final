<h1 style="color: #00698f; font-size: 40px;">Trabajo Práctico Final de Pensamiento Computacional</h1>

### Autores: Lautaro Caminoa, Álvaro Guerrero y Nicolás Heuser

![Portada Pokémon](https://www.lared.cl/wp-content/uploads/2016/02/portada-pokemon.jpg "Portada Pokémon")

# Estructura de Carpetas y Archivos

## Data

- **Imgs**
    - Carpeta que contiene las imágenes de cada pokémon en formato `.png`.

- **effectiveness_graph.png**
    - Gráfico de efectividades de los distintos tipos de pokémon contra otros tipos.

- **effectiveness_chart.csv**
    - Archivo CSV que contiene la misma información que `effectiveness_graph.png`, pero ordenada en formato CSV.

- **moves.csv**
    - Archivo CSV que contiene la información de todos los distintos movimientos pokémon:

| Campo       | Descripción                 |
| ----------- | --------------------------- |
| `name`      | Nombre del movimiento          |
| `type`     | Tipo del movimiento     |
| `category`     | Categoría del movimienton    |
| `pp`        | Puntos de poder del movimiento            |
| `power`    | Poder del movimiento          |
| `accuracy`   | Precisión del movimiento         |


- **pokemons.csv**
  - Archivo CSV que contiene la información de cada pokémon:

| Campo       | Descripción                 |
| ----------- | --------------------------- |
| `name`      | Nombre del pokémon          |
| `type1`     | Primer tipo del pokémon     |
| `type2`     | Segundo tipo del pokémon    |
| `hp`        | Vida del pokémon            |
| `attack`    | Ataque del pokémon          |
| `defense`   | Defensa del pokémon         |
| `sp_attack` | Ataque especial del pokémon|
| `sp_defense`| Defensa especial del pokémon|
| `speed`     | Velocidad del pokémon        |
| `generation`| Generación del pokémon      |
| `height_m`  | Altura del pokémon en metros |
| `weight_kg` | Peso del pokémon en kilogramos |
| `is_legendary` | Indica si el pokémon es legendario |
| `moves`     | Movimientos que puede aprender el pokémon |

# Utils

## combat.py
Contiene las funciones necesarias para simular los combates entre equipos pokémon.

### Funciones

---

#### `__faint_change__(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> None`
Cambia el pokémon actual del equipo que tiene un pokémon debilitado. El otro equipo también puede cambiar su pokémon después del equipo que tiene el pokémon debilitado.

**Parámetros:**
- `team1 (Team)`: Uno de los equipos.
- `team2 (Team)`: El otro equipo.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

---

#### `__fight__(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> Team`
Simula una pelea entre dos equipos. La pelea termina cuando todos los pokémon de uno de los equipos han sido debilitados.

**Parámetros:**
- `team1 (Team)`: Uno de los equipos.
- `team2 (Team)`: El otro equipo.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

**Retorna:**
- `Team`: El equipo que ganó la pelea.

---

#### `get_winner(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> Team`
Simula una pelea entre dos equipos. La pelea termina cuando todos los pokémon de uno de los equipos han sido debilitados. Los pokémon de los equipos se restauran a su estado inicial después de la pelea.

**Parámetros:**
- `team1 (Team)`: Uno de los equipos.
- `team2 (Team)`: El otro equipo.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

**Retorna:**
- `Team`: El equipo que ganó la pelea.

## move.py
Contiene la clase para definir un objeto `Move` y sus respectivas funciones.

### Clases y Funciones

---

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

##### `@staticmethod from_dict(name: str, data: dict[str, str | int]) -> Move`
Crea un objeto `Move` a partir de un diccionario.

**Parámetros:**
- `name (str)`: El nombre del movimiento.
- `data (dict[str, str | int])`: Un diccionario que contiene el tipo, categoría, pp, poder y precisión del movimiento.

**Retorna:**
- `Move`: El movimiento creado a partir del diccionario.

**Ejemplo:**
```
data = {'type': 'fire', 'category': 'special', 'pp': 10, 'power': 90, 'accuracy': 100}
move = Move.from_dict('Flamethrower', data)
```


## pokemon.py
Contiene la clase para definir un objeto `Pokemon` y sus respectivas funciones.
### Clases y Funciones

---

#### `class Pokemon`
Representa un pokémon.

##### `__init__(self, pokedex_number: int, name: str, type1: str, type2: str|None, hp: int, attack: int, defense: int, sp_attack: int, sp_defense: int, speed: int, generation: int, height: float, weight: float, is_legendary: bool, moves: list[Move], level: int=50)`
Constructor para inicializar un objeto `Pokemon`.

**Parámetros:**
| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| `pokedex_number` | `int` | El número en la pokédex del pokémon. |
| `name` | `str` | El nombre del pokémon. |
| `type1` | `str` | El tipo primario del pokémon. |
| `type2` | `str` |None` | El tipo secundario del pokémon. Si el pokémon tiene solo un tipo, debe ser None. |
| `hp` | `int` | Los puntos de vida base del pokémon. |
| `attack` | `int` | El ataque base del pokémon. |
| `defense` | `int` | La defensa base del pokémon. |
| `sp_attack` | `int` | El ataque especial base del pokémon. |
| `sp_defense` | `int` | La defensa especial base del pokémon. |
| `speed` | `int` | La velocidad base del pokémon. |
| `generation` | `int` | La generación del pokémon. |
| `height` | `float` | La altura del pokémon en metros. |
| `weight` | `float` | El peso del pokémon en kilogramos. |
| `is_legendary` | `bool` | Si el pokémon es legendario o no. |
| `moves` | `list[Move]` | Los movimientos que el pokémon puede usar. |
| `level` | `int` | El nivel del pokémon. Por defecto es 50. |

##### `@staticmethod from_dict(name: str, data: dict[str, str|int|float|bool|None], moves_data: dict[str, dict[str, str|int]]) -> Pokemon`
Crea un objeto `Pokemon` a partir de un diccionario.

**Parámetros:**
- `name (str)`: El nombre del pokémon.
- `data (dict[str, str|int|float|bool|None])`: Un diccionario que contiene el número en la pokédex, tipo1, tipo2, hp, ataque, defensa, ataque especial, defensa especial, velocidad, generación, altura, peso, si es legendario y los movimientos del pokémon.
- `moves_data (dict[str, dict[str, str|int]])`: Un diccionario que contiene los datos de los movimientos del pokémon.

**Retorna:**
- `Pokemon`: El pokémon creado a partir del diccionario.

**Ejemplo:**
```
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
```

## team.py
Contiene la clase para definir un objeto `Team` y sus respectivas funciones.
### Clases y Funciones

---

### `class Team`
Representa un equipo de pokémon.

##### `__init__(self, name: str, pokemons: list[Pokemon], starter: int=0)`
Constructor para inicializar un objeto `Team`.

**Parámetros:**
- `name (str)`: El nombre del equipo.
- `pokemons (list[Pokemon])`: Los pokémons que tiene el equipo.
- `starter (int)`: El índice del pokémon que comienza la batalla. Por defecto es 0.

##### `get_current_pokemon(self) -> Pokemon`
Retorna el pokémon actual del equipo.

**Retorna:**
- `Pokemon`: El pokémon actual del equipo.

##### `change_pokemon(self, index: int) -> None`
Cambia el pokémon actual del equipo.

**Parámetros:**
- `index (int)`: El índice del pokémon que se convertirá en el pokémon actual.

##### `recieve_damage(self, damage: float) -> None`
Reduce los puntos de vida actuales del pokémon actual por el daño recibido.

**Parámetros:**
- `damage (float)`: El daño que el pokémon recibirá.

##### `get_next_action(self, defending_team: 'Team', effectiveness: dict[str, dict[str, float]]) -> tuple[str, Move|int|None]`
Retorna la próxima acción que el equipo realizará.

**Parámetros:**
- `defending_team (Team)`: El equipo al que el equipo atacará.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

**Retorna:**
- `str`: La acción que el equipo realizará. Puede ser 'attack', 'switch' o 'skip'.
- `Move|int|None`: El movimiento que el equipo usará si la acción es 'attack', el índice del pokémon al que el equipo cambiará si la acción es 'switch' o None si la acción es 'skip'.

##### `do_action(self, action: str, target: Move|int|None, defender: 'Team', effectiveness: dict[str, dict[str, float]]) -> None`
Ejecuta una acción.

**Parámetros:**
- `action (str)`: La acción que el equipo realizará. Puede ser 'attack' o 'switch'.
- `target (Move|int|None)`: El movimiento que el equipo usará si la acción es 'attack', el índice del pokémon al que el equipo cambiará si la acción es 'switch' o None si la acción es 'skip'.
- `defender (Team)`: El equipo que recibirá la acción.
- `effectiveness (dict[str, dict[str, float]])`: Un diccionario que contiene la efectividad de cada tipo contra otro.

## archivos_csv
Contiene las funciones para generar los archivos csv de salida.
### Funciones

---

### `csv_epochs(lista_epochs: list[tuple]) -> None`

Escribe en un archivo CSV que contiene un registro de los Pokémon que aparecen en cada época de equipos,
junto con la cantidad de veces que cada uno aparece.

##### Args:

* `lista_epochs`: lista de tuplas que contiene el número de generación, la diversidad de pokémon y un diccionario con los pokémon y su frecuencia

#### Código:
```
def csv_epochs(lista_epochs: list[tuple]) -> None:
    with open("epochs.csv", "w") as f:
        for epoch in lista_epochs:
            num_gen, diversidad, pokemon_dict = epoch
            f.write(f"{num_gen},{diversidad}")
            for pokemon, freq in pokemon_dict.items():
                f.write(f",{pokemon},{freq}")
            f.write("\n")
```

---

### `csv_best_team(lista_teams: list[tuple]) -> None`

Escribe en un archivo CSV los datos de los mejores equipos por generación ordenados primero por época y luego según
su función de aptitud definida.

#### Args:

* `lista_teams`: lista de tuplas que contiene el número de generación y equipos ordenados por aptitud, para cada generación.

#### Código:
```
def csv_best_team(lista_teams: list[tuple]) -> None:
    with open("best_teams.csv", "w", newline='') as f:
        writer = csv.writer(f)
        encabezados = ["epoch", "aptitude", "team_name", "starter", "pokemon_1", "pokemon_2", "pokemon_3", "pokemon_4", "pokemon_5", "pokemon_6"]
        writer.writerow(encabezados)
        for epoch in lista_teams:
            for tupla_team in epoch[1]:
                num_gen = epoch[0]
                aptitude = tupla_team[0]
                team = tupla_team[1]
                starter = team.current_pokemon_index
                team_name = team.name
                pokemons = [pokemon.name for pokemon in team.pokemons]
                row = [num_gen, aptitude, team_name, starter] + pokemons
                writer.writerow(row)
```
## funcs.py
Contiene todas las funciones relacionadas con el algoritnmo genético y su funcionamiento.
### Funciones

---

### `definir_moves() -> dict[str : object]`

Lee un archivo CSV con datos de movimientos y devuelve un diccionario de objetos `Move`.

#### Args:

* None

#### Returns:

* `dict`: Un diccionario donde las claves son los nombres de los movimientos (str) y los valores son objetos `Move`.

---

### `crear_pokemon() -> object`

Lee un archivo CSV con datos de Pokémon y devuelve un objeto Pokémon aleatorio.

#### Args:

* None

#### Returns:

* `object`: Un objeto `Pokemon`.

---

### `crear_equipo(nombre_equipo: str) -> object`

Crea un equipo de Pokémon no legendarios ni duplicados aleatorios.

#### Args:

* `nombre_equipo` (str): El nombre del equipo.

#### Returns:

* `Team`: Un objeto `Team` que contiene el nombre del equipo y una lista de 6 objetos `Pokemon`.

---

### `poblacion(num_equipos: int) -> list[object]`

Crea una lista con una cantidad indicada de equipos pokemon.

#### Args:

* `num_equipos` (int): Cantidad de equipos que se deseen generar.

#### Returns:

* `list`: Lista con todos los equipos.

---

### `efectividad() -> dict`

Crea el diccionario con las efectividades de cada tipo de pokemon contra los otros.

#### Args:

* None

#### Returns:

* `dict`: Diccionario con las efectividades de cada tipo.

---

### `aptitud(mi_equipo: object, adversarios: list, effectiveness: dict) -> int`

Calcula la aptitud de el equipo pokemon seleccionado.

#### Args:

* `mi_equipo` (object): Equipo al que se le desea calcular la aptitud.
* `adversarios` (list): Equipos contra los que se enfrentara "mi_equipo".
* `effectiveness` (dict): Diccionario con las efectividades de cada tipo.

#### Returns:

* `int`: Cantidad de batallas ganadas.

---

### `evaluar_aptitud(list_equipos: list, adversarios: list, effectiveness: dict) -> list[tuple]`

Evalúa la aptitud de una lista de equipos en función de la cantidad de adversarios.

#### Args:

* `list_equipos` (list): Una lista de equipos, donde cada equipo es un objeto que puede ser evaluado por la función `aptitud`.
* `adversarios` (list): Adversarios que cada equipo debe enfrentar.
* `effectiveness` (dict): Diccionario con las efectividades de cada tipo.

#### Returns:

* `list[tuple]`: Una lista de tuplas que contiene la aptitud del equipo y el objeto equipo correspondiente, para cada equipo.

---

### `seleccion_proporcional(list_aptitudes: list[tuple], cant_adversarios: int) -> list[tuple]`

Selecciona equipos de forma aleatoria, teniendo en cuenta su aptitud.

#### Args:

* `list_aptitudes` (list[tuple]): Lista de tuplas que contiene la aptitud del equipo y el nombre, para cada equipo.
* `cant_adversarios` (int): El número de adversarios que cada equipo debe enfrentar.

#### Returns:

* `list[tuple]`: Lista de tuplas que contiene la aptitud del equipo y el objeto equipo correspondiente, para cada equipo seleccionado.

---

### `cruce(seleccionados: list[tuple], poblacion: list[object]) -> list[object]`

Realiza el cruce genético entre una lista de equipos seleccionados y una población de equipos, generando una nueva generación de equipos.

#### Args:

* `seleccionados` (list[tuple]): Una lista de tuplas donde cada tupla contiene un valor de aptitud y un equipo (padre).
* `poblacion` (list[object]): Una lista de equipos (objetos) que representan la población inicial.

#### Returns:

* `list[object]`: Una lista de nuevos equipos (objetos) generados a partir del cruce genético.

---

### `algoritmo_genetico(cant_equipos: int, cant_adversarios: int, cant_generaciones: int) -> tuple[list[object], list[tuple[int, int, dict]], list[tuple[int, object]]]`

Ejecuta un algoritmo genético para evolucionar una población de equipos a lo largo de varias generaciones.

#### Args:

* `cant_equipos` (int): La cantidad de equipos en la población inicial y en cada generación.
* `cant_adversarios` (int): La cantidad de adversarios contra los cuales se evalúa la aptitud de los equipos.
* `cant_generaciones` (int): El número de generaciones que el algoritmo genético debe ejecutar.

### Returns:

* `tuple[list[object], list[tuple[int, int, dict]], list[tuple[int, object]]]`:
    - La última generación de la población de equipos después de ejecutar el número especificado de generaciones.
    - Lista de tuplas con datos de diversidad y frecuencia de pokemons por generación.
    - Lista de tuplas con el mejor equipo por generación.

---

### `ordenar_aptitudes(aptitudes: list[tuple[int, object]]) -> object`

Ordena los equipos por aptitud de mayor a menor.

#### Args:

* `aptitudes`: lista de tuplas que contiene la aptitud del equipo y el nombre, para cada equipo.

#### Returns:

* `list`: Lista de equipos ordenados por aptitud.

## graphs.py

### Funciones

---

### graphs.py

Contiene las funciones necesarias para generar los gráficos de salida.

### `grafico_aptitud() -> None`

Grafica la aptitud promedio por época.

#### Args:

* None

#### Returns:

* `None`

### `grafico_epochs() -> None`

Crea un gráfico de la diversidad de pokémons por cada epoch.

#### Args:

* None

#### Returns:

* `None`

### `graph_distribution_last_epoch() -> None`

Crea un gráfico de barras que muestra la distribución de los Pokémon en los equipos de la última epoch.

#### Args:

* None

#### Returns:

* `None`

### `get_types(pokemon: str) -> list[str]`

Devuelve los tipos de un Pokémon.

#### Args:

* `pokemon` (str): Nombre del Pokémon.

#### Returns:

* `list[str]`: Lista con los tipos del Pokémon.

### `types_distribution_last_epoch(cant_generaciones: int) -> None`

Crea un gráfico de barras que muestra la distribución de los tipos de Pokémon en la última época.

#### Args:

* `cant_generaciones` (int): Cantidad de generaciones.

#### Returns:

* `None`

## main.py
Archivo principal para ejecutar el programa.
