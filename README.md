# Generador de Horarios para colegios

## Objetivo
El objetivo de este programa es generar horario para colegios respetando todas las restricciones que impone este tipo de problemas. Hasta el momento se presentan dos programas: una versión intenta resolver el completo, mientras que la otra asume que se conoce qué profesores le harán clases a cada curso. El segundo problema es considerablemente más fácil de resolver.

## Datos necesarios
Para hacer funcionar el programa se requieren las disponibilidades de todos los profesores y qué curso hace cada uno de ellos, la cantidad de horas que cada ramo tendrá para cada curso, entre qué módulos se encuentran las pausas (para conocer qué módulos son continuos) y conocer cuántos módulos de clases hay por día.

Uno de los archivos necesarios para el programa es `preasignacion,ipynb`, el cual permite elaborar una asignación de profesores a clases y cursos a partir de su disponibilidad. Por lo que tengo entendido, esta asignación ya está hecha en los colegios para el momento en que se elaboran los horarios, pero es una herramienta que puede estar y no ser usada. Este programa usa los datos del archivo `parametros_preasignacion.json`.
El archivo más importante es `modelo_limpio.ipynb` que presenta la última versión del modelo de optimización general a ser usado al momento de programar los horarios. Este programa usa los datos en el archivo `parametros3.json`. 

<!-- ## ¿Cómo funciona?
0. Se hace un precómputo si la asignación será factible (¿la "oferta" de horas de los profesores logra cumplir la "demanda" de horas de clases?). SI esto no se cumple se agregarán profesores imaginarios que representan profesores que el colegio debe conseguirse para lograr cumplir con la demanda.
1. Se asignan los profesores a los cursos. En este punto se tienen en cuenta los cursos que ya se encuentran preasignados (como las jefaturas) y también la *wishlist* de cada profesor.
2. Se generan los horarios en base a las asignaciones hechas en el punto 2. -->

## ¿Cómo funciona?
0. Se puede usar el programa de preasignación para asignar cada ramo de cada clase a un profesor. 
1. Se ingresan los datos de cada curso en la interfaz. Los datos necesarios son:
- Cantidad de módulos semanales para cada ramo
- En base a la cantidad de módulos de clases que tendrá cada semana armar la forma que tendrá el horario (cantidad de módulos por día)
- Fijar módulos de clases (o vetarlos). Esto también se puede hacer por profesor
2. Correr el programa. Aquí se podría separar en una opción que intente correrlo teniendo en cuenta todas las restricciones y otra opción que vaya agregándolas de a poco. Esta última forma se podría calibrar probando el programa para conocer de a cuántas restricciones es conveniente agregar.
3. Dar la posibilidad de hacer cambios a partir de los horarios que se generen (preservar algunas estructuras, vetar otras dentro de lo posible)


## Idea interfaz
1. Se ingresa, para cada curso, las horas de clases que se tiene de cada ramo. Aquí se podría aprovechar de agregar el nombre de el/los profesor/es que hacen esa clase.
2. Se elabora la forma que se quiere que tenga cada horario, distribuyendo la cantidad de horas que se ingresaron en el paso anterior en los módulos de clases disponibles.
3. Se fijan algunas clases y se ponen como opción algunas reglas. Estas reglas pueden ser, pero no están limitadas a: disposición de profesores, veto de algunos módulos, simultaneidad de algunas clases. Todas estas reglas se ponen en una lista de prioridades, de forma que, si no se pueden lograr todas al mismo tiempo, se prioricen algunas sobre otras.

## Herramientas implementadas
- [x] Asignar manualmente un módulo de clases
- [x] Limitar la cantidad de días que un profesor hace clases
- [ ] Considerar salas (¿es lo mismo que ciertos cursos que no pueden realizarse simultáneamente? &rarr; Considerablemente más fácil de resolver)
- [x] Ramos con más de un profesor
- [x] Ramos simultáneos (un profesor para varios cursos)
- [x] Módulos de clases continuos
- [x] Vetar combinaciones de módulos
- [ ] Priorizar restricciones adicionales e ir eliminando de menos a más importantes

## Trabajo futuro
- Generar archivos `.json` a partir de una interfaz gráfica (hay una idea de esto en el archivo `interfaz.py`, pero muy básica)
- Conseguirse datos reales