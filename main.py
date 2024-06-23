from graphs import grafico_epochs, grafico_aptitud, graph_distribution_last_epoch, types_distribution_last_epoch
from funcs import algoritmo_genetico, efectividad
from archivos_csv import csv_epochs, csv_best_team
from peleas import simulacion_pelea,crear_equipo_personalizado
import time
import pygame
import sys

#opciones algoritmo
cant_equipos = 10
cant_adversarios = 100
cant_generaciones = 10

efectividades = efectividad()

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Configuración de pantalla
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Menú en Pygame")

# Fuente
font = pygame.font.Font(None, 40)
large_font = pygame.font.Font(None, 60)

# Opciones del menú principal
main_menu_items = ["Simular Batallas", "Gráficos", "Salir"]
graphics_menu_items = ["grafico_epochs", "grafico_aptitud", "graph_distribution_last_epoch", "types_distribution_last_epoch", "Todos los gráficos", "Atrás"]
battles_menu_items = ["Will", "Koga", "Bruno", "Karen", "Lance", "Atrás"]

# Estados del menú
MAIN_MENU = "main"
GRAPHICS_MENU = "graphics"
BATTLES_MENU = "battles"
current_menu = MAIN_MENU

# Opción seleccionada en cada menú
selected_item_main = 0
selected_item_graphics = 0
selected_item_battles = 0

def draw_menu(menu_items, selected_item):
    screen.fill(WHITE)
    for index, item in enumerate(menu_items):
        if index == selected_item:
            color = GRAY
        else:
            color = BLACK
        text = font.render(item, True, color)
        text_rect = text.get_rect(center=(screen_size[0]//2, screen_size[1]//2 + index * 50))
        screen.blit(text, text_rect)

def handle_main_menu():
    global current_menu, selected_item_main
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item_main = (selected_item_main - 1) % len(main_menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item_main = (selected_item_main + 1) % len(main_menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item_main == 0:
                    current_menu = BATTLES_MENU
                elif selected_item_main == 1:
                    current_menu = GRAPHICS_MENU
                elif selected_item_main == 2:
                    pygame.quit()
                    sys.exit()

def handle_graphics_menu():
    global current_menu, selected_item_graphics
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item_graphics = (selected_item_graphics - 1) % len(graphics_menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item_graphics = (selected_item_graphics + 1) % len(graphics_menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item_graphics == 0:
                    grafico_epochs()
                elif selected_item_graphics == 1:
                    grafico_aptitud()
                elif selected_item_graphics == 2:
                    graph_distribution_last_epoch()
                elif selected_item_graphics == 3:
                    types_distribution_last_epoch(cant_generaciones)
                elif selected_item_graphics == 4:
                    grafico_epochs()
                    grafico_aptitud()
                    graph_distribution_last_epoch()
                    types_distribution_last_epoch(cant_generaciones)
                elif selected_item_graphics == 5:
                    current_menu = MAIN_MENU

def handle_battles_menu():
    global current_menu, selected_item_battles
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item_battles = (selected_item_battles - 1) % len(battles_menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item_battles = (selected_item_battles + 1) % len(battles_menu_items)
            elif event.key == pygame.K_RETURN:
                mi_equipo = crear_equipo_personalizado("Alvi y Lauti", [150, 151, 386, 384, 385, 6])
                if selected_item_battles == 0:
                    elite_four_member_1 = crear_equipo_personalizado("Will", [437, 124, 326, 80, 282, 178])
                    simulacion_pelea(mi_equipo, elite_four_member_1, efectividades)
                elif selected_item_battles == 1:
                    elite_four_member_2 = crear_equipo_personalizado("Koga", [435, 454, 317, 49, 89, 169])
                    simulacion_pelea(mi_equipo, elite_four_member_2, efectividades)
                elif selected_item_battles == 2:
                    elite_four_member_3 = crear_equipo_personalizado("Bruno", [237, 106, 297, 68, 448, 107])
                    simulacion_pelea(mi_equipo, elite_four_member_3, efectividades)
                elif selected_item_battles == 3:
                    elite_four_member_4 = crear_equipo_personalizado("Karen", [461, 442, 430, 197, 229, 359])
                    simulacion_pelea(mi_equipo, elite_four_member_4, efectividades)
                elif selected_item_battles == 4:
                    champion = crear_equipo_personalizado("Lance", [373, 445, 149, 6, 334, 130])
                    simulacion_pelea(mi_equipo, champion, efectividades)
                elif selected_item_battles == 5:
                    current_menu = MAIN_MENU

def main():

    inicio = time.time()

    ult_gen, lista_epochs, lista_teams = algoritmo_genetico(cant_equipos,cant_adversarios,cant_generaciones)
    csv_epochs(lista_epochs)
    csv_best_team(lista_teams)

    fin = time.time()
    print(f"La función tardó {fin - inicio} segundos en ejecutarse.")

    clock = pygame.time.Clock()
    while True:
        if current_menu == MAIN_MENU:
            handle_main_menu()
            draw_menu(main_menu_items, selected_item_main)
        elif current_menu == GRAPHICS_MENU:
            handle_graphics_menu()
            draw_menu(graphics_menu_items, selected_item_graphics)
        elif current_menu == BATTLES_MENU:
            handle_battles_menu()
            draw_menu(battles_menu_items, selected_item_battles)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
