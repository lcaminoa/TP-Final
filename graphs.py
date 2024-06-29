import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TABLEAU_COLORS
import random

TYPES = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']
TYPES_COLORS = ['#A8A77A', '#EE8130', '#6390F0', '#F7D02C', '#7AC74C', '#96D9D6', '#C22E28', '#A33EA1', '#E2BF65', '#A98FF3', '#F95587', '#A6B91A', '#B6A136', '#735797', '#6F35FC', '#705746', '#B7B7CE', '#D685AD']
COLORS_RADAR = ['#01befe', '#ffdd00', '#ff7d00', '#ff006d', '#adff01', '#8f00ff']
def grafico_aptitud() -> None:
    """
    Grafica la aptitud promedio por época.
    """
    # Leer los datos en un DataFrame 
    df = pd.read_csv("best_teams.csv")

    # Agrupar por la columna 'epoch' y calcular el promedio de la columna 'aptitude'
    aptitud_promedio = df.groupby('epoch')['aptitude'].mean()

    # Graficar los resultados
    plt.plot(aptitud_promedio.index, aptitud_promedio.values)
    plt.xlabel('época')
    plt.ylabel('Promedio de Aptitud')
    plt.title('Promedio de Aptitud por época')
    plt.show()

def grafico_epochs() -> None:
    """
    Crea un gráfico de la diversidad de pokémons por cada epoch.
    """
    # Leer el archivo CSV
    csv = pd.read_csv("epochs.csv")

    # Obtener los datos de las columnas
    n_epoch = pd.to_numeric(csv.iloc[:, 0], errors ='coerce')  # Primera columna
    diversidad = pd.to_numeric(csv.iloc[:, 1], errors ='coerce')  # Segunda columna

    # Crear grafico
    plt.plot(n_epoch, diversidad)
    plt.xlabel('Epoch')
    plt.ylabel('Diversidad')
    plt.title('Diversidad de pokemons por epoch')
    plt.show()

def graph_distribution_last_epoch() -> None:
    """
    Crea un gráfico de barras que muestra la distribución de los Pokémon en los equipos de la última epoch.
    Usando pandas y matplotlib.
    """
    # Leer los datos desde el archivo CSV sin encabezado y asignar los nombres de las columnas
    df = pd.read_csv("best_teams.csv")
    
    # Encontrar la última epoch
    last_epoch = df['epoch'].max()

    # Filtrar los datos para obtener solo las filas de la última epoch
    last_epoch_df = df[df['epoch'] == last_epoch]

    # Obtener la frecuencia de los pokémon en los equipos de la última epoch
    pokemons = last_epoch_df.iloc[:, 4:].values.flatten()
    pokemon_freq = pd.Series(pokemons).value_counts()

    # Filtrar pokémon que aparecen más de una vez
    pokemon_freq_filtered = pokemon_freq.loc[pokemon_freq > 1]

    # Crear un gráfico de barras
    pokemon_freq_filtered.plot(kind='bar')
    plt.title("Distribución de Pokémon en los equipos de la última epoch")
    plt.xlabel("Pokémon")
    plt.ylabel("Frecuencia")
    plt.show()

def get_types(pokemon: str) -> list[str]:
    """
    Devuelve los tipos de un Pokémon.
    Args:
        pokemon: Nombre del Pokémon.
    Returns:
        list[str]: Lista con los tipos del Pokémon.
    """
    pokemon_types = []
    df = pd.read_csv('data/pokemons.csv')
     # Buscar el Pokémon en el DataFrame
    pokemon_row = df[df['name'] == pokemon]

    # Obtener los valores de las columnas 'type1' y 'type2'
    type1 = pokemon_row['type1'].values[0]
    type2 = pokemon_row['type2'].values[0]

    # Si 'type2' es nulo, devolver solo 'type1'
    if pd.isnull(type2):
        pokemon_types = [type1]
    else: 
        pokemon_types = [type1, type2]

    return pokemon_types

def types_distribution_last_epoch(cant_generaciones: int) -> None:
    """
    Crea un gráfico de barras que muestra la distribución de los tipos de Pokémon en la última época.
    Args:
        cant_generaciones: Cantidad de generaciones.
    """
    df = pd.read_csv("best_teams.csv")

    # Seleccionar la ultima epoch
    empieza_last_epoch = df[df["epoch"].astype(str).str.startswith(str(cant_generaciones-1))].index[0]
    last_epoch = df.loc[empieza_last_epoch:,:]

    # Obtener pokemons de ultima epoch
    pokemons_last_epoch = last_epoch.iloc[:, 4:].values.flatten()

    # Obtener los tipos de los pokémon
    types = []
    for pokemon in pokemons_last_epoch:
        types.extend(get_types(pokemon))

    # Contar las veces que aparece cada tipo
    types_series = pd.Series(types)
    type_counts = types_series.value_counts()

    # Crear un diccionario de colores
    color_dict = dict(zip(TYPES, TYPES_COLORS))

    # Asegurarse de que los tipos en type_counts.index estén en el mismo formato que TYPES
    formatted_types = [type.lower().strip() for type in type_counts.index]

    # Asignar colores a las barras
    bar_colors = [color_dict[type] for type in formatted_types]

    type_counts.plot(kind='bar', color=bar_colors)

    
    plt.title('Distribución de los tipos de Pokémon en la última época')
    plt.xlabel('Tipo de Pokémon')
    plt.ylabel('Frecuencia')
    plt.show()

def get_best_team_stats(pokemon: str) -> dict:
    """
    Devuelve las estadísticas base de un Pokémon.
    Args:
        pokemon: Nombre del Pokémon.
    Returns:
        dict: Diccionario con las estadísticas base del Pokémon.
    """
    
    df = pd.read_csv('data/pokemons.csv')
    # Buscar el Pokémon en el DataFrame
    pokemon_row = df[df['name'] == pokemon]

    # Obtener las estadísticas base del Pokémon
    stats = {
        'hp': pokemon_row['hp'].values[0],
        'attack': pokemon_row['attack'].values[0],
        'defense': pokemon_row['defense'].values[0],
        'sp_attack': pokemon_row['sp_attack'].values[0],
        'sp_defense': pokemon_row['sp_defense'].values[0],
        'speed': pokemon_row['speed'].values[0]
    }

    return stats

def best_team_stats_graph(cant_generaciones) -> None:
    """
    Grafica las estadísticas base del mejor equipo de Pokémon de la última generación.
    Args:
        cant_generaciones: Número de generaciones a considerar.
    """
    df = pd.read_csv("best_teams.csv")

    # Seleccionar la última epoch
    empieza_last_epoch = df[df["epoch"].astype(str).str.startswith(str(cant_generaciones-1))].index[0]
    last_epoch = df.loc[empieza_last_epoch:, :]

    # Obtener el equipo con la mayor aptitud
    best_team = last_epoch.loc[last_epoch['aptitude'].idxmax()]

    # Obtener los nombres de los Pokémon en el mejor equipo
    team_pokemons = best_team[4:].values.tolist()

    # Obtener las estadísticas de cada Pokémon en el equipo
    team_stats = [get_best_team_stats(pokemon) for pokemon in team_pokemons]

    # Crear el radar chart
    labels = list(team_stats[0].keys())[:-1]  
    num_vars = len(labels)

    # Calcular los ángulos de cada eje
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Dibujar cada eje y etiquetarlo
    for i, stats in enumerate(team_stats):
        values = list(stats.values())[:-1]  
        values += values[:1]
        color = COLORS_RADAR[i]
        ax.fill(angles, values, color=color, alpha=0.25)
        ax.plot(angles, values, color=color, linewidth=2, label=team_pokemons[i])

    # Configurar los ejes
    ax.set_yticklabels([]) 
    ax.set_xticks(angles[:-1]) 
    ax.set_xticklabels(labels) 

    plt.title(f'Estadísticas del Mejor Equipo: {best_team["team_name"]}')

    # Crear la tabla de colores
    cell_text = [[pokemon, COLORS_RADAR[i]] for i, pokemon in enumerate(team_pokemons)]
    plt.table(cellText=cell_text, colLabels=['Pokémon', 'Color'], cellLoc='center', loc='bottom', bbox=[0.1, -0.3, 0.8, 0.15])

    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    
    plt.show()

