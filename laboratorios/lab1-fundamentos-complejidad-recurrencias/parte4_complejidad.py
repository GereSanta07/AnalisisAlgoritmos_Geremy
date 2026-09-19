"""Experimento de complejidad para Insertion Sort y Merge Sort."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
SEMILLA = 42


def ejecutar_experimento():
    """Ejecuta las pruebas de tiempo para ambos algoritmos."""

    resultados = {
        "Insertion Sort": [],
        "Merge Sort": [],
    }

    for n in TAMANOS:
        datos = generar_aleatorio(n, SEMILLA)

        inicio = time.perf_counter()
        insertion_sort(datos)
        fin = time.perf_counter()

        resultados["Insertion Sort"].append(fin - inicio)

        inicio = time.perf_counter()
        merge_sort(datos)
        fin = time.perf_counter()

        resultados["Merge Sort"].append(fin - inicio)

    return resultados


def generar_grafica_tiempo(resultados):
    """Genera la gráfica de tiempo contra tamaño de entrada."""

    for nombre, tiempos in resultados.items():
        plt.plot(
            TAMANOS,
            tiempos,
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempo: Insertion Sort vs Merge Sort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    resultados = ejecutar_experimento()

    for nombre, tiempos in resultados.items():
        print(f"\n{nombre}")
        print("Tiempo:", tiempos)

    generar_grafica_tiempo(resultados)