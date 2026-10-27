
"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista() -> None:
    """Verifica busquedas exitosas e infructuosas en la lista."""
    lista = ListaEnlazada()
    lista.insertar(10, "en bodega")
    lista.insertar(24, "en reparto")

    assert lista.buscar(10) == "en bodega"
    assert lista.buscar(24) == "en reparto"
    assert lista.buscar(99) is None


def probar_tabla() -> None:
    """Verifica busquedas y colisiones en la tabla hash."""
    tabla = TablaHash(7)

    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara las dos estructuras con colecciones aleatorias."""
    random.seed(42)

    estados = [
        "en bodega",
        "en reparto",
        "entregado",
    ]

    for _ in range(20):
        guias = random.sample(range(1, 1000), 30)
        lista = ListaEnlazada()
        tabla = TablaHash(random.randint(5, 20))

        for guia in guias:
            estado = random.choice(estados)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)

        for guia in range(1000, 1010):
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

        assert lista.tamano == tabla.tamano


def main() -> None:
    """Ejecuta todas las pruebas."""
    probar_lista()
    probar_tabla()
    probar_colecciones_aleatorias()

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
