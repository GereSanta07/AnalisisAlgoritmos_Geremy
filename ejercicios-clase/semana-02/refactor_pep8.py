def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números enteros.

    Args:
        lista: Lista de números enteros.

    Returns:
        El promedio de los valores de la lista.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma / len(lista)


def main() -> None:
    """Ejecuta el programa principal."""
    numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros))


if __name__ == "__main__":
    main()