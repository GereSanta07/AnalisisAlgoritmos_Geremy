"""Experimento de los tres escenarios de Tamiza para el Laboratorio 1."""

import time
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
SEMILLA = 42


def ejecutar_experimento():
    """Ejecuta las pruebas de tiempo y comparaciones para A, B y C."""

    resultados = {
        "A - Aleatorio": {"tiempo": [], "comparaciones": []},
        "B - Casi ordenado": {"tiempo": [], "comparaciones": []},
        "C - Inverso": {"tiempo": [], "comparaciones": []},
    }

    for n in TAMANOS:
        datos_a = generar_aleatorio(n, SEMILLA)
        datos_b = generar_casi_ordenado(n, SEMILLA)
        datos_c = generar_inverso(n)

        escenarios = [
            ("A - Aleatorio", datos_a),
            ("B - Casi ordenado", datos_b),
            ("C - Inverso", datos_c),
        ]

        for nombre, datos in escenarios:
            inicio = time.perf_counter()
            _, comparaciones = insertion_sort(datos)
            fin = time.perf_counter()

            resultados[nombre]["tiempo"].append(fin - inicio)
            resultados[nombre]["comparaciones"].append(comparaciones)

    return resultados


def generar_grafica_comparaciones(resultados):
    """Genera la gráfica de comparaciones contra tamaño de entrada."""

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.title("Insertion Sort: comparaciones por escenario")

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "."))
    )
    
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()


def generar_grafica_tiempo(resultados):
    """Genera la gráfica de tiempo contra tamaño de entrada."""

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempo"],
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Insertion Sort: tiempo de ejecución por escenario")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    resultados = ejecutar_experimento()

    for nombre, datos in resultados.items():
        print(f"\n{nombre}")
        print("Comparaciones:", datos["comparaciones"])
        print("Tiempo:", datos["tiempo"])

    generar_grafica_comparaciones(resultados)
    generar_grafica_tiempo(resultados)