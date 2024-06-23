from funcs import algoritmo_genetico
from archivos_csv import csv_epochs, csv_best_team
import time
import pygame
from menu import draw_menu, handle_main_menu, handle_graphics_menu, handle_battles_menu, MAIN_MENU, GRAPHICS_MENU, BATTLES_MENU, main_menu_items, graphics_menu_items, battles_menu_items, selected_item_main, selected_item_graphics, selected_item_battles, current_menu

def main():
    #opciones algoritmo
    cant_equipos = 10
    cant_adversarios = 100
    cant_generaciones = 10
    inicio = time.time()

    # ult_gen, lista_epochs, lista_teams = algoritmo_genetico(cant_equipos,cant_adversarios,cant_generaciones)
    # csv_epochs(lista_epochs)
    # csv_best_team(lista_teams)

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
