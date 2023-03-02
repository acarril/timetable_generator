# Generador de Horarios para colegios

## Objetivo
El objetivo de este programa es generar horario para colegios respetando todas las restricciones que impone este tipo de problemas. Hasta el momento se presentan dos programas: una versión intenta resolver el completo, mientras que la otra asume que se conoce qué profesores le harán clases a cada curso. El segundo problema es considerablemente más fácil de resolver.

## Datos necesarios
Los datos mínimos para comenzar con la generación de horarios son los siguientes:
- Información sobre profesores (cuántos módulos de clases semanales pueden hacer, qué ramos y a qué cursos pueden hacer)
- Información sobre cantidad de módulos de clases para cada curso (cantidad de módulos de clases semanales)
- Forma que se quiere que tenga el horario de cada curso

El programa se encuentras disponible en la carpeta `Asignador`. Hay dos archivos `main.py` y `main.ipynb` (cualquiera de los dos sirve, en el Jupyter Notebook hay algunas herramientas de visualización eso sí). 

También se encuentra disponible un programa que permite tomar decisiones para asignar qué profesor le hace qué ramo a qué curso. Este está disponible en la carpeta `Preasignador`.
<!-- Para hacer funcionar el programa se requieren las disponibilidades de todos los profesores y qué curso hace cada uno de ellos, la cantidad de horas que cada ramo tendrá para cada curso, entre qué módulos se encuentran las pausas (para conocer qué módulos son continuos) y conocer cuántos módulos de clases hay por día. -->

<!-- ## ¿Cómo funciona?
0. Se hace un precómputo si la asignación será factible (¿la "oferta" de horas de los profesores logra cumplir la "demanda" de horas de clases?). SI esto no se cumple se agregarán profesores imaginarios que representan profesores que el colegio debe conseguirse para lograr cumplir con la demanda.
1. Se asignan los profesores a los cursos. En este punto se tienen en cuenta los cursos que ya se encuentran preasignados (como las jefaturas) y también la *wishlist* de cada profesor.
2. Se generan los horarios en base a las asignaciones hechas en el punto 2. -->

## ¿Cómo funciona con interfaz?
0. Se puede usar el programa de preasignación para asignar cada ramo de cada clase a un profesor. 
1. Se ingresan los datos de cada curso en la interfaz. Los datos necesarios son:
- Cantidad de módulos semanales para cada ramo
- En base a la cantidad de módulos de clases que tendrá cada semana armar la forma que tendrá el horario (cantidad de módulos por día)
- Fijar módulos de clases (o vetarlos). Esto también se puede hacer por profesor
2. Correr el programa. Aquí se podría separar en una opción que intente correrlo teniendo en cuenta todas las restricciones y otra opción que vaya agregándolas de a poco. Esta última forma se podría calibrar probando el programa para conocer de a cuántas restricciones es conveniente agregar.
3. Dar la posibilidad de hacer cambios a partir de los horarios que se generen (preservar algunas estructuras, vetar otras dentro de lo posible)

<!-- 
## Idea interfaz
1. Se ingresa, para cada curso, las horas de clases que se tiene de cada ramo. Aquí se podría aprovechar de agregar el nombre de el/los profesor/es que hacen esa clase.
2. Se elabora la forma que se quiere que tenga cada horario, distribuyendo la cantidad de horas que se ingresaron en el paso anterior en los módulos de clases disponibles.
3. Se fijan algunas clases y se ponen como opción algunas reglas. Estas reglas pueden ser, pero no están limitadas a: disposición de profesores, veto de algunos módulos, simultaneidad de algunas clases. Todas estas reglas se ponen en una lista de prioridades, de forma que, si no se pueden lograr todas al mismo tiempo, se prioricen algunas sobre otras. -->

## Herramientas implementadas
- [x] Asignar manualmente un módulo de clases
- [x] Limitar la cantidad de días que un profesor hace clases
- [x] Ramos con más de un profesor
- [x] Ramos simultáneos (un profesor para varios cursos)
- [x] Módulos de clases continuos
- [x] Vetar combinaciones de módulos
- [x] Priorizar restricciones adicionales e ir eliminando de menos a más importantes
- [ ] Considerar salas (¿es lo mismo que ciertos cursos que no pueden realizarse simultáneamente? &rarr; Considerablemente más fácil de resolver)

En sí, considerar las salas no es un problema muy difícil, solo que no fue una de mis prioridades al programar. Se me ocurren dos maneras de modelar este problema:
1. Se puede agregar un subíndice *s* a las variables del problema. Las asignaciones se pueden formar considerando las salas también. En la práctica se sabe (casi siempre) en qué sala sera un ramo. Luego, se puede modelar de forma parecida a los profesores. Por lo general se conocerá la sala en la que se hace clases (la misma sala del curso). Si se no se conoce se tiene la opción de meter tomar una decisión de forma similar a como se hace cuando no se conoce qué profesor hará un ramo. El problema con esta forma de implementar el uso de salas es que introducir un nuevo subíndice puede hacer que el programa tarde más en resolver. Habría que testear la *performance* de Gurobi con este tema.
2. La otra opción es simplemente agrupar los ramos que no pueden ocurrir al mismo tiempo (ya que usan una misma sala). También se puede limitar cuántos de estos ramos ocurren al mismo tiempo. Por ejemplo, en un gimnasio podrían ocurrir 2 clases al mismo tiempo, por lo que todas las clases que usarán ese gimnasio no deben sumar más de 2 en cada módulo de clases. 

## Benchmarks
Los tiempos que se presentan a continuación pueden servir como cota superior al momento de programar horarios. De esta forma, se puede tener una estimación de tiempo para el cómputo de los horarios que se le puede entregar al usuario. Estos valores surgen de una programación de horarios que repetía harto los profesores, tenía prácticamente todos los bloques de clases duplicados, donde se simulo que algunos profesores tenían restricción de días y se tenía a disposición casi 50 módulos de clases a la semana. Es difícil que otro colegio supere las condiciones impuestas por este colegio, por lo que es un buen punto de referencia para una cota superior.

El procesador usado fue un **i7-1165G7 @ 2.80GHz, 4 núcleos**.

El tiempo a medir considera todo el procesamiento de datos, el tiempo que se demora Gurobi en armar el modelo, en resolverlo y el tiempo que se demora en escribir archivos con los datos. Al momento de implementarlo no se tendrá que escribir archivos, pero si se tendrá que considerar el tiempo que se demora en recibir y enviar requests el servidor.

| Cantidad de cursos | Tiempo sin variable n <br> F.O. = 0 | Tiempo con variable n | Sugerencia de tiempo <br> sin variable n | Sugerencia de tiempo <br> con variable n | 
| :----: | :----: | :----: | :----: | :----: |
| 2 cursos | 0.35s | 0.7s | 1s | 1s |
| 4 cursos | 1.40s | 0.9s | 2s | 2s |
| 6 cursos | 0.94s | 2.13s | 2s | 3s |
| 8 cursos | 1.45s | 1.54s | 2s | 4s |
| 10 cursos | 2.32s | 4.08s | 3s | 6s |
| 12 cursos | 2.26s | 9.40s | 3s | 10s |
| 14 cursos | 3.53s | 16.75s | 4s | 20s |
| 16 cursos | 5.12s | 29.62s | 6s | 35s |
| 18 cursos | 3.80s | 18.51s | 6s | 45s |
| 20 cursos | 4.73s | 41.44s | 7s | 1min |
| 22 cursos | 6.79s | 27.85s | 9s | 1min 10s |
| 24 cursos | 7.35s | 51.11s | 10s | 1min 30s |

Las dos últimas columnas son una sugerencia para poner en el programa de forma que se tenga un "colchón para los resultados". Tal como se puede ver en la tabla, hay algunas cantidades de cursos que a pesar de ser menor (en número) tardan más, por lo que para asegurarse de no tener al usuario esperando se recomienda ser conservadores con la estimación de tiempo. Mayor cantidad de pruebas podrán acercar esta cota a un valor real, pero los valores que se presentan en la tabla no debieran estar muy alejados de las cotas reales.

