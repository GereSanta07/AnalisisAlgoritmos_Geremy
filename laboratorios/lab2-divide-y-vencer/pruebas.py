"""Pruebas para los algoritmos de subarreglo maximo."""
 
import random
 
from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)
 
 
def verificar_resultados(valores: list[float]) -> None:
    """Comprueba que ambos algoritmos encuentren la misma suma maxima.
 
    Args:
        valores: Lista de variaciones diarias que se desea verificar.
    """
    valores_originales = valores.copy()
 
    resultado_fuerza = subarreglo_fuerza_bruta(valores)
    resultado_divide = subarreglo_maximo(
        valores, 0, len(valores) - 1
    )
 
    assert resultado_fuerza[2] == resultado_divide[2], (
        f"Resultados diferentes para {valores}: "
        f"{resultado_fuerza[2]} != {resultado_divide[2]}"
    )
 
    assert valores == valores_originales, (
        "Los algoritmos modificaron la lista original."
    )
 
 
def ejecutar_pruebas() -> None:
    """Ejecuta los casos obligatorios del laboratorio."""
    # Caso 1: ejemplo del enunciado, suma maxima de 17.
    serie_ejemplo = [-3, 5, -2, 8, -6, 3, 9, -4]
 
    assert subarreglo_fuerza_bruta(serie_ejemplo)[2] == 17
    assert subarreglo_maximo(
        serie_ejemplo, 0, len(serie_ejemplo) - 1
    )[2] == 17
 
    verificar_resultados(serie_ejemplo)
 
    # Caso 2: lista con un solo elemento.
    serie_un_elemento = [7]
 
    verificar_resultados(serie_un_elemento)
    assert subarreglo_maximo(
        serie_un_elemento, 0, 0
    )[2] == 7
 
    # Caso 3: todos los valores son negativos.
    serie_negativa = [-8, -3, -6, -2, -9]
 
    verificar_resultados(serie_negativa)
    assert subarreglo_fuerza_bruta(serie_negativa)[2] == -2
 
    # Caso 4: todos los valores son positivos.
    serie_positiva = [2, 4, 1, 3]
 
    verificar_resultados(serie_positiva)
    assert subarreglo_fuerza_bruta(serie_positiva)[2] == 10
 
    # Caso 5: la mejor racha cruza el punto medio.
    serie_cruzada = [4, -1, 2, 1]
 
    verificar_resultados(serie_cruzada)
    assert subarreglo_maximo(
        serie_cruzada, 0, len(serie_cruzada) - 1
    )[2] == 6
 
    # Caso 6: veinte listas aleatorias.
    generador = random.Random(42)
 
    for _ in range(20):
        cantidad = generador.randint(1, 30)
 
        serie_aleatoria = [
            generador.randint(-20, 20)
            for _ in range(cantidad)
        ]
 
        verificar_resultados(serie_aleatoria)
 
    print("Todas las pruebas finalizaron correctamente.")
 
 
if __name__ == "__main__":
    ejecutar_pruebas()