# Laboratorio 1 — Fundamentos, Complejidad y Recurrencias

**Estudiante:** Geremy Santa Duque

---

## Instrucciones para reproducir el experimento

*Esta sección se completará con los comandos correspondientes a la ejecución de las Partes 3 y 4.*

---

## Parte 1 — Analizar el algoritmo antes de comprar hardware

En este caso es importante empezar teniendo en cuenta las condiciones actuales del sistema. Que el algoritmo funcione y entregue el resultado correcto no significa que siga siendo adecuado para el contexto del sistema que mencioné. El Insertion Sort puede cumplir con la tarea asignada de ordenar los registros, pero solo se está viendo un lado del problema, ya que la condición de cumplir esta tarea dentro del rango de tiempo necesario no se está cumpliendo. Es decir, no podemos seguir utilizando algo que cumple correctamente una parte de la necesidad, pero que no logra cumplir con el tiempo requerido para completar todo el proceso.

Aunque el resultado correcto nos llegue después del tiempo establecido, esto significa incumplir con la necesidad del sistema: recibir el resultado en una hora determinada con el fin de realizar las llamadas al inicio del día. La tarea del centro de contacto es realizar las llamadas según el orden de criticidad de los registros, pero si esta tarea no se puede cumplir según la necesidad por la dependencia que existe del resultado del algoritmo, significa que no se está afectando una sola parte del proceso, sino todo el proceso.

Duplicar la velocidad, aunque reduzca el tiempo de ejecución, no soluciona el problema de fondo. En este caso, el inconveniente no radica solamente en qué tan rápido trabaja el servidor, sino en cómo aumentará el trabajo que debe realizar el algoritmo cuando la cantidad de registros aumente. Claramente, debemos contemplar que en el futuro la información seguirá creciendo. Antes de invertir en hardware, lo importante sería analizar si el algoritmo que se está utilizando sigue siendo apropiado para el problema actual y para el crecimiento esperado de los registros.

Un ejemplo propio lo he encontrado en mi trabajo mientras participo en el desarrollo de **CCT (Customer Control Tower)**, una plataforma que busca centralizar información para los comerciales y otras áreas, y que también sirve como apoyo para la generación de prefacturas. En este proyecto desarrollé en Python una ETL que lee reportes de Excel, carga la información en una tabla de la base de datos y posteriormente realiza un *match* entre los registros de los reportes y la tabla de clientes. En nuestro caso se procesaban aproximadamente dos reportes de 15.000 filas cada uno, es decir, cerca de 30.000 registros. El proceso puede producir correctamente las correspondencias, pero si el volumen aumentara considerablemente y el algoritmo utilizado para realizar el *match* necesitara revisar demasiados registros para encontrar cada coincidencia, el resultado podría seguir siendo correcto, pero tardar demasiado para que la información estuviera disponible a tiempo para la prefacturación mensual. En ese escenario, el algoritmo sería correcto, pero dejaría de ser viable respecto al tiempo de procesamiento.

Por esto, analizar el algoritmo permite determinar si el problema se puede solucionar realmente con más hardware o si es necesario mejorar primero la forma en que se procesa la información.
