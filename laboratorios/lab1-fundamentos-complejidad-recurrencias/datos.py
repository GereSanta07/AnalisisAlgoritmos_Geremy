"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros a generar.
        semilla: semilla para obtener resultados reproducibles.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    datos = list(range(n))
    generador = random.Random(semilla)
    generador.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros a generar.
        semilla: semilla para obtener resultados reproducibles.

    Returns:
        Lista con el 98% de los datos ordenados y el 2% restante
        desordenado al final.
    """
    datos = list(range(n - 1, -1, -1))

    cantidad_ordenada = int(n * 0.98)

    parte_ordenada = datos[:cantidad_ordenada]
    parte_desordenada = datos[cantidad_ordenada:]

    generador = random.Random(semilla)
    generador.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros a generar.

    Returns:
        Lista de n indices distintos, en el orden inverso al que
        el algoritmo debe producir.
    """
    return list(range(n))