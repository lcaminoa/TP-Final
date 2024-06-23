import pandas as pd
import matplotlib.pyplot as plt

TYPES = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']
TYPES_COLORS = ['#A8A77A', '#EE8130', '#6390F0', '#F7D02C', '#7AC74C', '#96D9D6', '#C22E28', '#A33EA1', '#E2BF65', '#A98FF3', '#F95587', '#A6B91A', '#B6A136', '#735797', '#6F35FC', '#705746', '#B7B7CE', '#D685AD']

def grafico_aptitud():
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

def grafico_epochs():
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
    plt.figure(figsize=(10, 10))
    pokemon_freq_filtered.plot(kind='bar')
    plt.title("Distribución de Pokémon en los equipos de la última epoch")
    plt.xlabel("Pokémon")
    plt.ylabel("Frecuencia")
    plt.show()

def get_types(pokemon):
    """
    Devuelve los tipos de un Pokémon.
    Args:
        pokemon: Nombre del Pokémon.
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

def types_distribution_last_epoch(cant_generaciones):
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