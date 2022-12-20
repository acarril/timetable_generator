# Generador de Horarios para colegios

## Objetivo
El objetivo de este programa es generar horario para colegios respetando todas las restricciones que impone este tipo de problemas. Hasta el momento se presentan dos programas: una versión intenta resolver el completo, mientras que la otra asume que se conoce qué profesores le harán clases a cada curso. El segundo problema es considerablemente más fácil de resolver.

## Datos necesarios
Para hacer funcionar el programa se requieren las disponibilidades de todos los profesores y qué curso hace cada uno de ellos, la cantidad de horas que cada ramo tendrá para cada curso, entre qué módulos se encuentran las pausas (para conocer qué módulos son continuos) y conocer cuántos módulos de clases hay por día.

Los programas `main.ipynb` se encuentran en las carpetas `Completo` y `Reducido` (para ambas opciones de problemas). Cada una con su archivo `parametros.json` que la idea es que contenga todos los datos necesarios para generar los horarios. Hasta el momento solo la versión reducida está totalmente vinculada con su archivo `parametros.json`. 

## Trabajo futuro
- Generar archivos `.json` a partir de una interfaz gráfica (hay una idea de esto en el archivo `idea_programa.py`, pero muy básica)
- Conseguirse datos reales