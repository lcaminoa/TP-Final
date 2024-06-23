import csv

def csv_best_team(lista_teams):
    """
    Escribe en un archivo CSV los datos de los mejores equipos por generación.
    Args:
        lista_teams: lista de tuplas que contiene el número de generación y el mejor equipo, para cada generación.
    """
    with open("best_teams.csv", "w", newline='') as f:
        writer = csv.writer(f)
        
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

def csv_epochs(lista_epochs) -> None:
    with open("epochs.csv", "w") as f:

        for epoch in lista_epochs:
            num_gen, diversidad, pokemon_dict = epoch
            f.write(f"{num_gen},{diversidad}")
            for pokemon, freq in pokemon_dict.items():
                f.write(f",{pokemon},{freq}")
            f.write("\n")