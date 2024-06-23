import csv

def csv_epochs(lista_epochs: list[tuple]) -> None:
    """
    Escribe en un archivo CSV que contiene un registro de los Pokémon que aparecen en cada época de equipos,
    junto con la cantidad de veces que cada uno aparece.
    Args:
        lista_epochs: lista de tuplas que contiene el número de generación, la diversidad de pokémon y un diccionario con los pokémon y su frecuencia
    """
    with open("epochs.csv", "w") as f:

        for epoch in lista_epochs:
            num_gen, diversidad, pokemon_dict = epoch
            f.write(f"{num_gen},{diversidad}")
            for pokemon, freq in pokemon_dict.items():
                f.write(f",{pokemon},{freq}")
            f.write("\n")

def csv_best_team(lista_teams: list[tuple]) -> None:
    """
    Escribe en un archivo CSV los datos de los mejores equipos por generación ordenados primero por época y luego según
    su función de aptitud definida.
    Args:
        lista_teams: lista de tuplas que contiene el número de generación y equipos ordenados por aptitud, para cada generación.
    """
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