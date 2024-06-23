from utils.pokemon import Pokemon
from utils.team import Team
from utils.combat import __faint_change__
from funcs import definir_moves, efectividad

def crear_equipo_personalizado(nombre_equipo:str, pokedex_nums:list[int]) -> object:
    """
    Lee un archivo CSV con datos de Pokémon y devuelve un objeto Pokémon aleatorio.
    """
    equipo_pokemons = []
    with open("data/pokemons.csv", "r") as f:
        f.readline()
        lineas = f.readlines()
        for pokemon_num in pokedex_nums:
            data = {}
            moves_data = definir_moves()
            moves = []
            parametros = ["pokedex_number", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation", "height_m", "weight_kg", "is_legendary", "moves"]
            tipos = [int, str, str, str, int, int, int, int, int, int, int, float, float, int, list]
            line = lineas[pokemon_num - 1]
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
            equipo_pokemons.append(pokemon)
    return Team(nombre_equipo, equipo_pokemons)

def simulacion_pelea(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> Team:
    """
    Simulates a fight between two teams. The fight ends when all the pokemons of one of the teams have fainted.

    Parameters:
    team1 (Team): One of the teams.
    team2 (Team): The other team.
    effectiveness (dict[str, dict[str, float]]): A dictionary that contains the effectiveness of each type against
    another.

    Returns:
    Team: The team that won the fight.
    """
    turn = 0
    contador_muertes_team1 = 6
    contador_muertes_team2 = 6
    while any(pokemon.current_hp > 0 for pokemon in team1.pokemons) and any(pokemon.current_hp > 0 for pokemon in team2.pokemons):            
        action_1, target_1 = team1.get_next_action(team2, effectiveness)

        if action_1 == 'attack':
            print(f"El {team1.get_current_pokemon().name} de {team1.name} ataca al {team2.get_current_pokemon().name} de {team2.name}, utilizando {target_1.name} y generando {target_1.get_damage(team1.get_current_pokemon(), team2.get_current_pokemon(), effectiveness):.2f} de daño.")
            print(f"Vida de {team2.get_current_pokemon().name}: {team2.get_current_pokemon().current_hp:.2f} HP")
        elif action_1 == 'switch':
            print(f"{team1.name} cambia a {team1.pokemons[target_1].name} por {team1.get_current_pokemon().name}")
        else:
            print(f"{team1.name} salta el turno")

        action_2, target_2 = team2.get_next_action(team1, effectiveness)

        if action_1 == 'attack':
            print(f"El {team2.get_current_pokemon().name} de {team2.name} ataca al {team1.get_current_pokemon().name} de {team1.name}, utilizando {target_2.name} y generando {target_2.get_damage(team2.get_current_pokemon(), team1.get_current_pokemon(), effectiveness):.2f} de daño.")
            print(f"Vida de {team1.get_current_pokemon().name}: {team1.get_current_pokemon().current_hp:.2f} HP\n")
        elif action_1 == 'switch':
            print(f"{team2.name} cambia a {team2.pokemons[target_2].name} por {team2.get_current_pokemon().name}\n")
        else:
            print(f"{team2.name} salta el turno\n")
        
        # Switching always happens first
        if action_1 == 'switch':
            first = team1
            second = team2
        elif action_2 == 'switch':
            first = team2
            second = team1
            action_1, target_1, action_2, target_2 = action_2, target_2, action_1, target_1
        # If nobody is switching, the fastest pokemon goes firsts
        elif team1.get_current_pokemon().speed > team2.get_current_pokemon().speed:
            first = team1
            second = team2
        else:
            first = team2
            second = team1
            action_1, target_1, action_2, target_2 = action_2, target_2, action_1, target_1
    
        first.do_action(action_1, target_1, second, effectiveness)
        
        # If any of the pokemons fainted, the turn ends, and both have the chance to switch
        
        if team1.get_current_pokemon().current_hp == 0 or team2.get_current_pokemon().current_hp == 0:
            if team1.get_current_pokemon().current_hp == 0:
                contador_muertes_team1 -= 1
                print(f"Fue derrotado el {team1.get_current_pokemon().name} de {team1.name}.")
                print(f"Quedan {contador_muertes_team1} pokemones en el equipo {team1.name}." if contador_muertes_team1 != 1 else f"Queda {contador_muertes_team1} pokemon en el equipo {team1.name}.")
                team2_old_pokemon = team2.get_current_pokemon()
                __faint_change__(team1, team2, effectiveness)
                if team2.get_current_pokemon() != team2_old_pokemon:
                    print(f"Entra el {team1.get_current_pokemon().name} de {team1.name} y {team2.name} cambia a {team1_old_pokemon.name} por {team2.get_current_pokemon().name}\n")
                else:
                    print(f"Entra el {team1.get_current_pokemon().name} de {team1.name} y continua el {team2.get_current_pokemon().name} de {team2.name}\n")
            
            else:
                contador_muertes_team2 -= 1
                print(f"Fue derrotado el {team2.get_current_pokemon().name} de {team2.name}.")
                print(f"Quedan {contador_muertes_team2} pokemones en el equipo {team2.name}." if contador_muertes_team2 != 1 else f"Queda {contador_muertes_team2} pokemon en el equipo {team2.name}.")
                team1_old_pokemon = team1.get_current_pokemon()
                __faint_change__(team1, team2, effectiveness)
                if team1.get_current_pokemon() != team1_old_pokemon:
                    print(f"Entra el {team2.get_current_pokemon().name} de {team2.name} y {team1.name} cambia a {team2_old_pokemon.name} por {team1.get_current_pokemon().name}\n")
                else:
                    print(f"Entra el {team2.get_current_pokemon().name} de {team2.name} y continua el {team1.get_current_pokemon().name} de {team1.name}\n")

        else:
            if action_2 == 'attack' and target_2 is None:
                action_2, target_2 = second.get_next_action(first, effectiveness)
            second.do_action(action_2, target_2, first, effectiveness)

            if team1.get_current_pokemon().current_hp == 0 or team2.get_current_pokemon().current_hp == 0:
                if team1.get_current_pokemon().current_hp == 0:
                    contador_muertes_team1 -= 1
                    print(f"Fue derrotado el {team1.get_current_pokemon().name} de {team1.name}.")
                    print(f"Quedan {contador_muertes_team1} pokemones en el equipo {team1.name}.")
                    print(f"El equipo {team2.name} ganó la batalla.")
                    team2_old_pokemon = team2.get_current_pokemon()
                    __faint_change__(team1, team2, effectiveness)
                    
                else:
                    contador_muertes_team2 -= 1
                    print(f"Fue derrotado el {team2.get_current_pokemon().name} de {team2.name}.")
                    print(f"Quedan {contador_muertes_team2} pokemones en el equipo {team2.name}.")
                    print(f"El equipo {team1.name} ganó la batalla.")
                    team1_old_pokemon = team1.get_current_pokemon()
                    __faint_change__(team1, team2, effectiveness)
                    
        turn += 1
    
    return team1 if any(pokemon.current_hp > 0 for pokemon in team1.pokemons) else team2

elite_four_member_1 = crear_equipo_personalizado("Will", [437, 124, 326, 80, 282, 178]) # Bronzong, Jynx, Grumpig, Slowbro, Gardevoir, Xatu
elite_four_member_2 = crear_equipo_personalizado("Koga", [435, 454, 317, 49, 89, 169]) # Skunktank, Toxicroak, Swalot, Venomoth, Muk, Crobat
elite_four_member_3 = crear_equipo_personalizado("Bruno", [237, 106, 297, 68, 448, 107]) # Hitmontop, Hitmonlee, Hariyama, Machamp, Lucario, Hitmonchan
elite_four_member_4 = crear_equipo_personalizado("Karen", [461, 442, 430, 197, 229, 359]) # Weavile, Spiritomb, Honchkrow, Umbreon, Houndoom, Absol
champion = crear_equipo_personalizado("Lance", [373, 445, 149, 6, 334, 130]) # Salamence, Garchomp, Dragonite, Charizard, Altaria, Gyarados

dict_efectividad = efectividad()
simulacion_pelea(elite_four_member_4, champion, dict_efectividad)