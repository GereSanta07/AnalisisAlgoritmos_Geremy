
"""Experimentos de rendimiento para la lista enlazada y la tabla hash."""

import os
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7,
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con las guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo.

    Args:
        numero: numero que se va a evaluar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def primo_cercano(numero: int) -> int:
    """Busca el numero primo mas cercano al valor recibido.

    Args:
        numero: valor aproximado para el numero de casillas.

    Returns:
        El numero primo mas cercano, prefiriendo el inferior en empate.
    """
    inferior = max(2, int(numero))
    superior = inferior

    while True:
        if es_primo(inferior):
            return inferior
        if es_primo(superior):
            return superior

        inferior -= 1
        superior += 1


def generar_guias(cantidad: int, semilla: int = 42) -> list[int]:
    """Genera guias unicas de diez digitos.

    Args:
        cantidad: numero de guias que se van a generar.
        semilla: semilla para reproducir los datos.

    Returns:
        Una lista de guias distintas.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), cantidad)


def verificar_estructuras(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Compara las respuestas de ambas estructuras.

    Args:
        lista: lista enlazada con las guias.
        tabla: tabla hash con las mismas guias.
        guias: guias existentes que se van a comprobar.
    """
    for guia in guias[:100]:
        assert lista.buscar(guia) == tabla.buscar(guia)


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    consultas: list[int],
) -> float:
    """Calcula el tiempo medio por busqueda.

    Args:
        estructura: estructura donde se realizan las busquedas.
        consultas: guias que se van a buscar.

    Returns:
        Tiempo medio por busqueda, en segundos.
    """
    inicio = time.perf_counter()

    for guia in consultas:
        estructura.buscar(guia)

    fin = time.perf_counter()
    return (fin - inicio) / len(consultas)


def experimento_a() -> None:
    """Compara los tiempos de busqueda de ambas estructuras."""
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n in valores_n:
        guias = generar_guias(n, semilla=42 + n)
        azar = random.Random(100 + n)
        estados = [
            "en bodega",
            "en reparto",
            "entregado",
        ]

        lista = ListaEnlazada()
        for guia in guias:
            lista.insertar(guia, azar.choice(estados))

        m = primo_cercano(n / 2)
        tabla = TablaHash(m)

        azar_estados = random.Random(100 + n)
        for guia in guias:
            tabla.insertar(guia, azar_estados.choice(estados))

        verificar_estructuras(lista, tabla, guias)

        existentes = set(guias)
        consultas = generar_guias_inexistentes(
            existentes,
            200,
            semilla=7,
        )

        tiempo_lista = medir_busquedas(lista, consultas)
        tiempo_tabla = medir_busquedas(tabla, consultas)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"n={n:>6}, m={m:>6}, "
            f"alfa={n / m:.2f}, "
            f"lista={tiempo_lista:.8f} s, "
            f"tabla={tiempo_tabla:.8f} s"
        )

    plt.figure(figsize=(9, 5))
    plt.plot(
        valores_n,
        tiempos_lista,
        marker="o",
        label="Lista enlazada",
    )
    plt.plot(
        valores_n,
        tiempos_tabla,
        marker="s",
        label="Tabla hash",
    )
    plt.title("Tiempo medio de busqueda: lista frente a tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el tiempo de busqueda para distintos factores de carga."""
    n = 20000
    valores_alfa = [0.5, 1, 4, 10]
    tiempos: list[float] = []
    alfas_reales: list[float] = []

    guias = generar_guias(n, semilla=42)
    existentes = set(guias)
    consultas = generar_guias_inexistentes(
        existentes,
        200,
        semilla=7,
    )

    azar = random.Random(200)
    estados = ["en bodega", "en reparto", "entregado"]
    datos = [
        (guia, azar.choice(estados))
        for guia in guias
    ]

    for alfa in valores_alfa:
        m = primo_cercano(n / alfa)

        while n / m > alfa:
            m += 1
            while not es_primo(m):
                m += 1

        tabla = TablaHash(m)

        for guia, estado in datos:
            tabla.insertar(guia, estado)

        alfa_real = tabla.factor_carga()
        tiempo = medir_busquedas(tabla, consultas)

        alfas_reales.append(alfa_real)
        tiempos.append(tiempo)

        print(
            f"alfa solicitado={alfa:>4}, m={m:>6}, "
            f"alfa real={alfa_real:.3f}, "
            f"tabla={tiempo:.8f} s"
        )

    plt.figure(figsize=(9, 5))
    plt.plot(
        alfas_reales,
        tiempos,
        marker="o",
        label="Tabla hash",
    )
    plt.title("Tiempo medio de busqueda segun el factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y genera las graficas."""
    os.makedirs("graficas", exist_ok=True)

    print("Experimento A: lista enlazada frente a tabla hash")
    experimento_a()

    print("\nExperimento B: efecto del factor de carga")
    experimento_b()

    print("\nExperimentos terminados. Graficas guardadas en graficas/.")


if __name__ == "__main__":
    main()
