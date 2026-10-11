# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Geremy Santa Duque · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `2f8d673`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre un resultado correcto y un resultado que llega a tiempo, y explica que la lista tardía afecta todo el trabajo del centro de contacto.
- Explica que duplicar el servidor no arregla el problema de fondo: el trabajo del algoritmo crece con los registros.
- Su ejemplo propio (la ETL de CCT con unos 30.000 registros) es real y concreto.
- En la parte ética señala al paciente como quien asume el costo, y también al operador y a la Secretaría. Discute bien que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- En el ejemplo propio falta decir con claridad qué límite de tiempo se incumple (a qué hora debe estar lista la prefacturación) y cuántos registros haría inviable el proceso.
- En la parte ambiental falta un ejemplo numérico o una idea más concreta de cómo las horas de cómputo se acumulan durante años.
- Nombre la restricción incumplida de forma directa: las cuatro horas de la ventana.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define los tres casos con el tamaño fijo y escribe la predicción antes de medir, y la contrasta después.
- Justifica que el peor caso es el que decide la entrada a producción.
- Plantea la recurrencia de merge sort explicando el término 2T(n/2) y el costo de mezclar, y la resuelve con el método maestro verificando que f(n) y n^(log_2 2) tienen el mismo orden.
- Presenta la tabla de complejidades.

**Lo que puede mejorar:**
- El cálculo de insertion sort línea a línea solo cubre el peor caso. Falta mostrar cómo cambia el conteo en el mejor caso para justificar el Θ(n).
- La tabla de líneas indica cuántas veces se ejecuta cada una, pero falta sumar los costos de forma explícita antes de concluir.
- No explica cómo salió el caso promedio Θ(n²).

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista original y cuentan solo comparaciones entre elementos. No usan `sorted()` ni `sort()`.
- Los tres generadores producen lotes del tamaño pedido, sin repetidos, y con semilla reproducible.

**Lo que puede mejorar:**
- La función interna `ordenar` de `merge_sort` no tiene tipos ni explicación (docstring).
- Las funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen tipos ni estilo Google completo (faltan `Args` y `Returns`).
- En `algoritmos.py` falta una línea en blanco más entre las dos funciones, y en los docstrings falta separar el bloque `Args`.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica correctamente C como peor caso, B como mejor y A como intermedio, con datos de la tabla.
- Concluye que merge sort conviene y lo conecta con Θ(n²) y Θ(n log n).
- El concepto técnico recomienda merge sort, responde a la propuesta del servidor con un dato medido (C con n = 6.400), extrapola a 1.200.000 registros declarándolo estimación y menciona la memoria extra.

**Lo que puede mejorar:**
- Los ejes de las gráficas no dicen la unidad de los registros y la gráfica de comparaciones no indica que son conteos.
- La gráfica de la Parte 4 llega a cerca de 1,0 s para insertion sort, pero el informe habla de 1,68 s. Aclare de qué corrida salió cada dato.
- Cada tiempo se midió una sola vez; repetir y promediar da curvas más estables, y conviene decir cómo midió.
- La explicación de por qué los tamaños pequeños se ven parecidos es breve; mencione el costo de copiar listas y llamar funciones en merge sort.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- El informe está organizado por partes, las gráficas se ven incrustadas y los enlaces a `algoritmos.py`, `datos.py` y `parte3_casos.py` funcionan.
- Hay siete commits que tocan el laboratorio, con mensajes descriptivos.

**Lo que puede mejorar:**
- No siguió la convención de entrega: el trabajo está en la rama `master` y debía estar en `main`.
- La Parte 4 no enlaza `parte4_complejidad.py` ni `algoritmos.py`; solo menciona el nombre de la gráfica.
- Las instrucciones de reproducción no incluyen cómo activar el entorno virtual ni instalar los requisitos.
- Hay una carpeta `evidencia_colaborador/` en la raíz, que no es parte del entregable (solo se anota).

## ¿El código funciona?
Sí. Ambos scripts corren sin errores y generan las gráficas. Los dos algoritmos ordenan bien listas pequeñas, aleatorias, casi ordenadas e inversas, y el conteo de comparaciones es correcto.

## Para el próximo laboratorio
- Entregue en la rama `main`.
- Enlace el código de cada parte práctica al inicio de su sección, incluida la Parte 4.
- Agregue tipos y docstrings completos a todas las funciones, también a las internas y a los scripts de experimentos.
- Repita cada medición varias veces y reporte el promedio, indicando de qué corrida salen los datos del informe.
- Concrete sus ejemplos con cantidades y la restricción exacta que se incumple.
