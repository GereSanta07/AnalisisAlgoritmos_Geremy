"""Experimento de tiempos para los algoritmos de subarreglo maximo."""
 
import random
import time
from pathlib import Path
 
import matplotlib.pyplot as plt
 
from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)
 
 
def ejecutar_experimento() -> None:
    """Mide los algoritmos y genera una grafica comparativa."""
    tamanos = [10, 50, 100, 500, 1000, 4000]
    semilla = 2026
    repeticiones = 3
 
    generador = random.Random(semilla)
 
    tiempos_fuerza = []
    tiempos_divide = []
 
    for cantidad in tamanos:
        # Generar los datos fuera de las mediciones.
        valores = [
            generador.randint(-100, 100)
            for _ in range(cantidad)
        ]
 
        mediciones_fuerza = []
        mediciones_divide = []
 
        # Medir fuerza bruta.
        for _ in range(repeticiones):
            inicio_tiempo = time.perf_counter()
            resultado_fuerza = subarreglo_fuerza_bruta(valores)
            fin_tiempo = time.perf_counter()
 
            mediciones_fuerza.append(
                fin_tiempo - inicio_tiempo
            )
 
        # Medir divide y venceras.
        for _ in range(repeticiones):
            inicio_tiempo = time.perf_counter()
            resultado_divide = subarreglo_maximo(
                valores, 0, len(valores) - 1
            )
            fin_tiempo = time.perf_counter()
 
            mediciones_divide.append(
                fin_tiempo - inicio_tiempo
            )
 
        # Comprobar los resultados fuera del cronometro.
        assert resultado_fuerza[2] == resultado_divide[2], (
            f"Las sumas no coinciden para n={cantidad}: "
            f"{resultado_fuerza[2]} != {resultado_divide[2]}"
        )
 
        # Guardar el promedio de las mediciones, en segundos.
        promedio_fuerza = (
            sum(mediciones_fuerza) / repeticiones
        )
        promedio_divide = (
            sum(mediciones_divide) / repeticiones
        )
 
        tiempos_fuerza.append(promedio_fuerza)
        tiempos_divide.append(promedio_divide)
 
        print(
            f"n={cantidad:4} | "
            f"Fuerza bruta: {promedio_fuerza:.6f} s | "
            f"Divide y venceras: {promedio_divide:.6f} s"
        )
 
    # Crear la carpeta de la grafica junto a este archivo si no existe.
    carpeta_graficas = Path(__file__).parent / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)
 
    # Dibujar ambas curvas en los mismos ejes.
    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos,
        tiempos_fuerza,
        marker="o",
        label="Fuerza bruta",
    )
    plt.plot(
        tamanos,
        tiempos_divide,
        marker="s",
        label="Divide y venceras",
    )
 
    plt.title("Tiempo de ejecucion segun el tamano de entrada")
    plt.xlabel("Tamano de entrada (n elementos)")
    plt.ylabel("Tiempo promedio de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
 
    plt.savefig(
        carpeta_graficas / "tiempo_vs_n.png",
        dpi=150,
    )
    plt.close()
 
    print("\nExperimento terminado.")
    print("Grafica guardada en graficas/tiempo_vs_n.png")
 
 
if __name__ == "__main__":
    ejecutar_experimento()
 