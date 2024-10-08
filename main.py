from graphs import grafico_epochs, grafico_aptitud, graph_distribution_last_epoch, types_distribution_last_epoch, best_team_stats_graph
from funcs import algoritmo_genetico, efectividad
from archivos_csv import csv_epochs, csv_best_team
from peleas import simulacion_pelea,crear_equipo_personalizado
import time

def main():
    cant_equipos = 50
    cant_adversarios = 400
    cant_generaciones = 50

    efectividades = efectividad()

    inicio = time.time()

    ult_gen, lista_epochs, lista_teams = algoritmo_genetico(cant_equipos,cant_adversarios,cant_generaciones)

    csv_epochs(lista_epochs)
    csv_best_team(lista_teams)
    mejor_equipo_ult_gen = crear_equipo_personalizado("Alvi", [373, 445, 149, 6, 334, 130])
    mejor_equipo_ult_gen = lista_teams[-1][1][0][1] # Ultima generacion, mejor equipo
    mejor_equipo_ult_gen.name = "Best team"
    fin = time.time()
    print(f"La función tardó {fin - inicio} segundos en ejecutarse.")
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
            print("5-best_team_stats")
            print("6-todos los graficos")
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
                best_team_stats_graph(cant_generaciones)
            elif k == "6":
                grafico_epochs()
                grafico_aptitud()
                graph_distribution_last_epoch()
                types_distribution_last_epoch(cant_generaciones)
                best_team_stats_graph(cant_generaciones)
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

            if k == "1":
                elite_four_member_1 = crear_equipo_personalizado("Will", [437, 124, 326, 80, 282, 178]) # Bronzong, Jynx, Grumpig, Slowbro, Gardevoir, Xatu
                simulacion_pelea(mejor_equipo_ult_gen,elite_four_member_1,efectividades)
            elif k == "2":
                elite_four_member_2 = crear_equipo_personalizado("Koga", [435, 454, 317, 49, 89, 169]) # Skunktank, Toxicroak, Swalot, Venomoth, Muk, Crobat
                simulacion_pelea(mejor_equipo_ult_gen,elite_four_member_2,efectividades)
            elif k == "3":
                elite_four_member_3 = crear_equipo_personalizado("Bruno", [237, 106, 297, 68, 448, 107]) # Hitmontop, Hitmonlee, Hariyama, Machamp, Lucario, Hitmonchan
                simulacion_pelea(mejor_equipo_ult_gen,elite_four_member_3,efectividades)
            elif k == "4":
                elite_four_member_4 = crear_equipo_personalizado("Karen", [461, 442, 430, 197, 229, 359]) # Weavile, Spiritomb, Honchkrow, Umbreon, Houndoom, Absol
                simulacion_pelea(mejor_equipo_ult_gen,elite_four_member_4,efectividades)
            elif k == "5":
                champion = crear_equipo_personalizado("Lance", [373, 445, 149, 6, 334, 130]) # Salamence, Garchomp, Dragonite, Charizard, Altaria, Gyarados
                simulacion_pelea(mejor_equipo_ult_gen,champion,efectividades)
            elif k == "0":
                break
            else:
                print("\nopcion no valida\n")
        elif k!= "1" and k!= "2" and k!= "0":
            print("\nopcion no valida\n")

        for pokemon in mejor_equipo_ult_gen.pokemons:
            pokemon.current_hp = pokemon.max_hp
if __name__ == "__main__":
    main()
    