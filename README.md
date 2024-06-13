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

#### pokemon.py
Contiene la clase para definir un objeto `Pokemon` y sus respectivas funciones.

#### team.py
Contiene la clase para definir un objeto `Team` y sus respectivas funciones.

#### main.py
Archivo principal para ejecutar el programa.
