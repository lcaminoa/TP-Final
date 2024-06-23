from graphs import grafico_epochs, grafico_aptitud, graph_distribution_last_epoch, types_distribution_last_epoch
from funcs import algoritmo_genetico, efectividad
from archivos_csv import csv_epochs, csv_best_team
from peleas import simulacion_pelea,crear_equipo_personalizado
import time

def main():
    cant_equipos = 10
    cant_adversarios = 100
    cant_generaciones = 10

    efectividades = efectividad()

    # inicio = time.time()

    # ult_gen, lista_epochs, lista_teams = algoritmo_genetico(cant_equipos,cant_adversarios,cant_generaciones)
    # csv_epochs(lista_epochs)
    # csv_best_team(lista_teams)

    # fin = time.time()
    # print(f"La función tardó {fin - inicio} segundos en ejecutarse.")
    k = ""
    while k != "0":
        print("\nOpciones:")
        print("1-simular batallas")
        print("2-graficos")
        print("0-exit")
        k = input(">")

        if k == "2":
            print("\nseleccione grafico a visualizar:")
            print("1-grafico_epochs")
            print("2-grafico_aptitud")
            print("3-graph_distribution_last_epoch")
            print("4-types_distribution_last_epoch")
            print("5-Todos los graficos")
            print("0-exit")
            k = input(">")
            if k == "1":
                grafico_epochs()
            elif k == "2":
                grafico_aptitud()
            elif k == "3":
                graph_distribution_last_epoch()
            elif k == "4":
                types_distribution_last_epoch(cant_generaciones)
            elif k == "5":
                grafico_epochs()
                grafico_aptitud()
                graph_distribution_last_epoch()
                types_distribution_last_epoch(cant_generaciones)
            elif k == "0":
                break
            else:
                print("\nopcion no valida\n")
        elif k == "1":
            print("\nseleccione un rival")
            print("1-Will")
            print("2-Koga")
            print("3-Bruno")
            print("4-Karen")
            print("5-Lance")
            print("0-exit")
            k = input(">")

            mi_equipo = crear_equipo_personalizado("Alvi y Lauti", [150, 151, 386, 384, 385, 6]) 

            if k == "1":
                elite_four_member_1 = crear_equipo_personalizado("Will", [437, 124, 326, 80, 282, 178]) # Bronzong, Jynx, Grumpig, Slowbro, Gardevoir, Xatu
                simulacion_pelea(mi_equipo,elite_four_member_1,efectividades)
            elif k == "2":
                elite_four_member_2 = crear_equipo_personalizado("Koga", [435, 454, 317, 49, 89, 169]) # Skunktank, Toxicroak, Swalot, Venomoth, Muk, Crobat
                simulacion_pelea(mi_equipo,elite_four_member_2,efectividades)
            elif k == "3":
                elite_four_member_3 = crear_equipo_personalizado("Bruno", [237, 106, 297, 68, 448, 107]) # Hitmontop, Hitmonlee, Hariyama, Machamp, Lucario, Hitmonchan
                simulacion_pelea(mi_equipo,elite_four_member_3,efectividades)
            elif k == "4":
                elite_four_member_4 = crear_equipo_personalizado("Karen", [461, 442, 430, 197, 229, 359]) # Weavile, Spiritomb, Honchkrow, Umbreon, Houndoom, Absol
                simulacion_pelea(mi_equipo,elite_four_member_4,efectividades)
            elif k == "5":
                champion = crear_equipo_personalizado("Lance", [373, 445, 149, 6, 334, 130]) # Salamence, Garchomp, Dragonite, Charizard, Altaria, Gyarados
                simulacion_pelea(mi_equipo,champion,efectividades)
            elif k == "0":
                break
            else:
                print("\nopcion no valida\n")
        else:
            print("\nopcion no valida\n")

if __name__ == "__main__":
    main()
    