# Generador de Horarios para colegios

## Objetivo
El objetivo de este programa es generar horario para colegios respetando todas las restricciones que impone este tipo de problemas. Hasta el momento se presentan dos programas: una versión intenta resolver el completo, mientras que la otra asume que se conoce qué profesores le harán clases a cada curso. El segundo problema es considerablemente más fácil de resolver.

## Datos necesarios
Para hacer funcionar el programa se requieren las disponibilidades de todos los profesores y qué curso hace cada uno de ellos, la cantidad de horas que cada ramo tendrá para cada curso, entre qué módulos se encuentran las pausas (para conocer qué módulos son continuos) y conocer cuántos módulos de clases hay por día.

Los programas `main.ipynb` se encuentran en las carpetas `Completo` y `Reducido` (para ambas opciones de problemas). Cada una con su archivo `parametros.json` que la idea es que contenga todos los datos necesarios para generar los horarios. Hasta el momento solo la versión reducida está totalmente vinculada con su archivo `parametros.json`. 

## ¿Cómo funciona?
1. Se hace un precómputo si la asignación será factible (¿la "oferta" de horas de los profesores logra cumplir la "demanda" de horas de clases?). SI esto no se cumple se agregarán profesores imaginarios que representan profesores que el colegio debe conseguirse para lograr cumplir con la demanda.
2. Se asignan los profesores a los cursos. En este punto se tienen en cuenta los cursos que ya se encuentran preasignados (como las jefaturas) y también la *wishlist* de cada profesor.
3. Se generan los horarios en base a las asignaciones hechas en el punto 2.

## Trabajo futuro
- Generar archivos `.json` a partir de una interfaz gráfica (hay una idea de esto en el archivo `idea_programa.py`, pero muy básica)
- Conseguirse datos reales