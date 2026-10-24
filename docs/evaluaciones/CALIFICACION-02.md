# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Geremy Santa Duque · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `d50d09b`

Muy buen trabajo: el código es correcto y el informe está bien encaminado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- Comparó con el problema del máximo de un arreglo y llegó a `T(n) = 2T(n/2) + Θ(1) = Θ(n)`: dividir no mejora el orden.
- Recomendó divide y vencerás y declaró que lo de 1.000.000 de registros es una estimación.
- Dio cifras concretas (cerca de 11,9 horas contra 4,8 segundos).

**Lo que puede mejorar:**
- En "tamaños pequeños" dice que desde 100 elementos gana divide y vencerás, pero no muestra los valores de ese tamaño ni explica por qué la ventaja no aparece antes (costo de las llamadas recursivas).
- En la estimación a 1.000.000 no explica cómo llegó a las cifras: debe decir qué crecimiento aplicó a cada algoritmo (`n²` y `n log n`) y por qué.
- Al justificar el máximo del arreglo, falta decir claramente que combinar cuesta tiempo constante.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Planteó la recurrencia con sus dos subproblemas de tamaño `n/2` y el recorrido cruzado de costo `Θ(n)`.
- Aplicó el método maestro (`a = 2`, `b = 2`, caso 2) y justificó el `Θ(n²)` de la fuerza bruta con `n(n+1)/2`.

**Lo que puede mejorar:**
- Verificar la condición del caso 2 con más detalle (comparar `f(n)` con `n^(log₂ 2)`) en vez de afirmarla.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta y ninguna función modifica la lista.
- Cumple PEP 8, tiene type hints y docstrings en cada función. `pruebas.py` cubre todo lo pedido.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con seis tamaños.
- Calculó el factor al duplicar de 500 a 1.000 (cerca de 3,17 y 1,86) y lo comparó con `n²` y `n log n`.
- Los valores que cita para n = 4.000 coinciden con la gráfica (fuerza bruta cerca de 0,68 s, divide y vencerás cerca de 0,012 s).

**Lo que puede mejorar:**
- El 3,17 queda algo lejos de 4: faltó comentar por qué (tamaños todavía pequeños, ruido de medición).
- El informe no dice que los tiempos son promedios de tres repeticiones al leer la gráfica (solo lo menciona en la Parte 2).

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, enlaza `subarreglo.py`, `pruebas.py` y `medicion.py`, y la gráfica se ve con ruta relativa.
- Hay varios commits descriptivos sobre el laboratorio.

**Lo que puede mejorar:**
- No siguió la convención de rama: entregó en `master` y no en `main`.
- Las instrucciones de reproducción solo sirven para Windows; conviene indicar también cómo hacerlo en otros sistemas o usar `requirements.txt`.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas funciones dan siempre la misma suma máxima y `medicion.py` corre rápido y genera la gráfica.

## Para el próximo laboratorio
- Entregue en la rama `main`.
- Explique paso a paso cómo calcula una estimación (qué fórmula de crecimiento usa).
- Agregue una tabla de tiempos medidos para sustentar lo que dice de los tamaños pequeños.
- Compare siempre el factor medido con el teórico y explique la diferencia.
