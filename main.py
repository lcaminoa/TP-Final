from graphs import grafico_epochs, grafico_aptitud, graph_distribution_last_epoch, types_distribution_last_epoch
from funcs import algoritmo_genetico, csv_epochs, csv_best_team
import time

def main():
    cant_equipos = 10
    cant_adversarios = 100
    cant_generaciones = 10

    inicio = time.time()

    ult_gen, lista_epochs, lista_teams = algoritmo_genetico(cant_equipos,cant_adversarios,cant_generaciones)
    csv_epochs(lista_epochs)
    csv_best_team(lista_teams)

    fin = time.time()
    print(f"La función tardó {fin - inicio} segundos en ejecutarse.")
    k = "1"
    while k != "0":
        print("seleccione grafico a visualizar:")
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

if __name__ == "__main__":
    main()
    