from utils.pokemon import Pokemon
from utils.team import Team
from funcs import definir_moves
import pygame
import sys

def crear_equipo_personalizado(nombre_equipo:str, pokedex_nums:list[int]) -> object:
    """
    Lee un archivo CSV con datos de Pokémon y devuelve un objeto Pokémon aleatorio.
    Args:
        nombre_equipo: Nombre del equipo.
        pokedex_nums: Lista de números de la Pokédex de los Pokémon que formarán parte del equipo.
    Returns:
        object: Objeto Team con los Pokémon seleccionados
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

def show_text(screen, text, xy, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, xy)

def wait():
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                flag = False

def barra_vida(screen:pygame.Surface, n_team:int, current_hp:int, max_hp:int)->None:
    barra_largo = 178  
    YELLOW = (255,255,0)
    GREEN = (0, 255, 0)
    RED = (255,0,0)
    if n_team == 1:
        barra_x,barra_y = (517,354)
    elif n_team == 2:
        barra_x,barra_y = (78,90)
    
    porcentaje_barra = (current_hp/max_hp)
    tamaño_barra = barra_largo*porcentaje_barra

    if porcentaje_barra > 0.5:
        pygame.draw.rect(screen, GREEN, (barra_x, barra_y, tamaño_barra, 12))#barra 
    elif porcentaje_barra > 0.25:
        pygame.draw.rect(screen, YELLOW, (barra_x, barra_y, tamaño_barra, 12))#barra
    else:
        pygame.draw.rect(screen, RED, (barra_x, barra_y, tamaño_barra, 12))#barra 

def show_action(action_1, target_1, first, second, effectiveness,old_pokemon, old_hp):
    if any(pokemon.current_hp > 0 for pokemon in first.pokemons):

        if action_1 == 'attack':
            print(f"{first.get_current_pokemon().name} utiliza {target_1.name}")
            print(f"Causo {target_1.get_damage(first.get_current_pokemon(), second.get_current_pokemon(), effectiveness):.2f} de daño")
        elif action_1 == 'switch':
            if old_hp == 0:
                print(f"{old_pokemon.name} fue derrotado")
                print(f"Entra {first.get_current_pokemon().name}")
            else:
                print(f"{first.name} cambia a {old_pokemon.name}")
                print(f"Entra {first.get_current_pokemon().name}")
        else:
            print(f"{first.name} salta el turno")
    else:
        return


def simulacion_pelea(team1: Team, team2: Team, effectiveness: dict[str, dict[str, float]]) -> Team:
    """
    Simula una pelea entre dos equiós. La pelea finaliza cuando todos los pokemones de un equipo han sido derrotados.

    Args:
        team1 (Team): Uno de los equipos.
        team2 (Team): El otro equipo.
        effectiveness (dict[str, dict[str, float]]): Un diccionario que contiene la efectividad de los tipos de un pokemon contra otro.

    Returns:
        Team: El equipo ganador.
    """
    # Inicializa Pygame
    pygame.init()

    # Define el tamaño de la ventana
    window_size = (800, 600)

    # Crea la ventana
    screen = pygame.display.set_mode(window_size)

    # Configura el título de la ventana
    pygame.display.set_caption("Batalla Pokemon")

    # fuente de txt pokemon
    BLACK = (0, 0, 0)
    font_path = "data/Pokemon_GB.ttf"
    font_size = 20
    font = pygame.font.Font(font_path, font_size)


    # Carga la imagen
    image_path = "data/fondoPokemon.png"
    background = pygame.image.load(image_path)

    # Escala la imagen al tamaño de la ventana
    background = pygame.transform.scale(background, window_size)

    # pokemon 1
    pokemon_position_1 = (75, 310)  # Coordenadas donde se posicionará la imagen

    # pokemon 2
    pokemon_position_2 = (500, 50)  # Coordenadas donde se posicionará la imagen
    #//////////
    clock = pygame.time.Clock()
    turn = 0
    contador_muertes_team1 = 6
    contador_muertes_team2 = 6
    contador_1_position = (510,315)
    contador_2_position = (70,50)
    name_position_1= (495,315)
    name_position_2= (55,50)
    hp_position_1= (495,375)
    hp_position_2= (55,110)

    while any(pokemon.current_hp > 0 for pokemon in team1.pokemons) and any(pokemon.current_hp > 0 for pokemon in team2.pokemons): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #muestra todo
        screen.blit(background, (0, 0))#fondo
        barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
        barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
        show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
        show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
        show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
        show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
        show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
        show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
        screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
        screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
        pygame.display.update()
        wait()

        action_1, target_1 = team1.get_next_action(team2, effectiveness)
        action_2, target_2 = team2.get_next_action(team1, effectiveness)
        
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
        old_pokemon = first.get_current_pokemon()
        old_hp = first.get_current_pokemon().current_hp
        first.do_action(action_1, target_1, second, effectiveness)
        show_action(action_1,target_1,first,second,effectiveness,old_pokemon,old_hp)

        #actualiza todo
        screen.blit(background, (0, 0))
        barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
        barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
        show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
        show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
        show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
        show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
        show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
        show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
        screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
        screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
        pygame.display.update()
        wait()


        # If any of the pokemons fainted, the turn ends, and both have the chance to switch
        if team1.get_current_pokemon().current_hp == 0 or team2.get_current_pokemon().current_hp == 0:
            #faint_change 
            if team1.get_current_pokemon().current_hp == 0:
                fainted_team = team1
                contador_muertes_team1 -= 1
                other_team = team2
            else:
                fainted_team = team2
                contador_muertes_team2 -= 1
                other_team = team1
            action_1, target_1 = fainted_team.get_next_action(other_team, effectiveness)
            old_pokemon = fainted_team.get_current_pokemon()
            old_hp = fainted_team.get_current_pokemon().current_hp
            fainted_team.do_action(action_1, target_1, other_team, effectiveness)
            show_action(action_1,target_1,fainted_team,other_team,effectiveness,old_pokemon,old_hp)
            action_2, target_2 = other_team.get_next_action(fainted_team, effectiveness)

            #actualiza todo
            screen.blit(background, (0, 0))
            barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
            barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
            show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
            show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
            show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
            show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
            show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
            show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
            screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
            screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
            pygame.display.update()
            wait()

            if action_2 == 'switch':
                old_pokemon = other_team.get_current_pokemon()
                old_hp = other_team.get_current_pokemon().current_hp
                other_team.do_action(action_2, target_2, fainted_team, effectiveness)
                show_action(action_2,target_2,other_team,fainted_team,effectiveness,old_pokemon,old_hp)

                #actualiza todo
                screen.blit(background, (0, 0))
                barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
                barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
                show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
                show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
                show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
                show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
                show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
                show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
                screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
                screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
                pygame.display.update()
                wait()
        else:
            if action_2 == 'attack' and target_2 is None:
                action_2, target_2 = second.get_next_action(first, effectiveness)
            old_pokemon = second.get_current_pokemon()
            old_hp = second.get_current_pokemon().current_hp
            second.do_action(action_2, target_2, first, effectiveness)
            show_action(action_2,target_2,second,first,effectiveness,old_pokemon,old_hp)            

            #actualiza todo
            screen.blit(background, (0, 0))
            barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
            barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
            show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
            show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
            show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
            show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
            show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
            show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
            screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
            screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
            pygame.display.update()
            wait()

            if team1.get_current_pokemon().current_hp == 0 or team2.get_current_pokemon().current_hp == 0:
                if team1.get_current_pokemon().current_hp == 0:
                    fainted_team = team1
                    contador_muertes_team1 -= 1
                    other_team = team2
                else:
                    fainted_team = team2
                    contador_muertes_team2 -= 1
                    other_team = team1
                action_1, target_1 = fainted_team.get_next_action(other_team, effectiveness)
                old_pokemon = fainted_team.get_current_pokemon()
                old_hp = fainted_team.get_current_pokemon().current_hp
                fainted_team.do_action(action_1, target_1, other_team, effectiveness)
                show_action(action_1,target_1,fainted_team,other_team,effectiveness,old_pokemon,old_hp)
                #actualiza todo
                screen.blit(background, (0, 0))
                barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
                barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
                show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
                show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
                show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
                show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
                show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
                show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
                screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
                screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
                pygame.display.update()
                wait()

                action_2, target_2 = other_team.get_next_action(fainted_team, effectiveness)
                if action_2 == 'switch':
                    old_pokemon = other_team.get_current_pokemon()
                    old_hp = other_team.get_current_pokemon().current_hp
                    other_team.do_action(action_2, target_2, fainted_team, effectiveness)
                    show_action(action_2,target_2,other_team,fainted_team,effectiveness,old_pokemon,old_hp)
                    #actualiza todo
                    screen.blit(background, (0, 0))
                    barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
                    barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
                    show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
                    show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
                    show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
                    show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
                    show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
                    show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
                    screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
                    screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
                    pygame.display.update()
                    wait()
                if team1.get_current_pokemon().current_hp == 0:
                    fainted_team = team1
                    contador_muertes_team1 -= 1
                    other_team = team2
                else:
                    fainted_team = team2
                    contador_muertes_team2 -= 1
                    other_team = team1
                action_1, target_1 = fainted_team.get_next_action(other_team, effectiveness)
                old_pokemon = fainted_team.get_current_pokemon()
                old_hp = fainted_team.get_current_pokemon().current_hp
                fainted_team.do_action(action_1, target_1, other_team, effectiveness)
                show_action(action_1,target_1,fainted_team,other_team,effectiveness,old_pokemon,old_hp)
                #actualiza todo
                screen.blit(background, (0, 0))
                barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
                barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
                show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
                show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
                show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
                show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
                show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
                show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
                screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
                screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
                pygame.display.update()
                wait()

                action_2, target_2 = other_team.get_next_action(fainted_team, effectiveness)
                if action_2 == 'switch':
                    old_pokemon = other_team.get_current_pokemon()
                    old_hp = other_team.get_current_pokemon().current_hp
                    other_team.do_action(action_2, target_2, fainted_team, effectiveness)
                    show_action(action_2,target_2,other_team,fainted_team,effectiveness,old_pokemon,old_hp)
                    #actualiza todo
                    screen.blit(background, (0, 0))
                    barra_vida(screen, 1, team1.get_current_pokemon().current_hp, team1.get_current_pokemon().max_hp)#barra 1
                    barra_vida(screen, 2, team2.get_current_pokemon().current_hp, team2.get_current_pokemon().max_hp)#barra 2
                    show_text(screen, f"{team1.get_current_pokemon().name}", name_position_1, font, BLACK)#nombre1
                    show_text(screen, f"{team2.get_current_pokemon().name}", name_position_2, font, BLACK)#nombre2
                    show_text(screen, f"{contador_muertes_team1}/6", contador_1_position, font, BLACK)#restantes1
                    show_text(screen, f"{contador_muertes_team2}/6", contador_2_position, font, BLACK)#restantes2
                    show_text(screen, f"{team1.get_current_pokemon().current_hp:.0f}/{team1.get_current_pokemon().max_hp:.0f} HP", hp_position_1, font, BLACK)#hp1
                    show_text(screen, f"{team2.get_current_pokemon().current_hp:.0f}/{team2.get_current_pokemon().max_hp:.0f} HP", hp_position_2, font, BLACK)#hp2
                    screen.blit(pygame.image.load(f"data/imgs/{str(str(team1.get_current_pokemon().pokedex_number).zfill(3)).zfill(3)}.png"), pokemon_position_1)#pokemon 1
                    screen.blit(pygame.image.load(f"data/imgs/{str(team2.get_current_pokemon().pokedex_number).zfill(3)}.png"), pokemon_position_2)#pokemon 2
                    pygame.display.update()
                    wait()

        turn += 1
        clock.tick(30)

    print(f"{team1.name} gano el combate") if any(pokemon.current_hp > 0 for pokemon in team1.pokemons) else print(f"{team2.name} gano el combate")
    pygame.quit()








# # Dibuja la imagen en la ventana
# screen.blit(background, (0, 0))

#     # Dibuja la imagen adicional en la ventana
# screen.blit(pokemon_image_1, pokemon_position_1)
# screen.blit(pokemon_image_2, pokemon_position_2)