def agregar_clase(ramos_por_curso: dict, curso: str, ramo: str, horas: int, horas_por_curso: dict):
    """
    Esta función permite agregar la cantidad de clases de cada ramo que tendrá un curso
    """
    ramos_por_curso[curso][ramo] = horas
    horas_por_curso[curso] += horas

def eliminar_clase(ramos_por_curso: dict, curso: str, ramo: str, horas: int, horas_por_curso: dict):
    """
    Esta función permite eliminar una clase de las que se habían asignado a un curso
    """
    del ramos_por_curso[curso][ramo]
    horas_por_curso[curso] -= horas

def agregar_curso(ramos_con_modulos_seguidos: dict, curso: str):
    ramos_con_modulos_seguidos[curso] = []

def eliminar_curso(ramos_por_curso: dict, curso: str, horas_por_curso: dict):
    """
    Esta función permite eliminar uno de los cursos que se habían agregado anteriormente
    """
    del ramos_por_curso[curso]
    del horas_por_curso[curso]

def cambiar_nombre_curso(ramos_por_curso: dict, nombre_curso_antiguo: str, horas_por_curso: dict, nuevo_nombre: str):
    """
    Esta función permite cambiar el nombre de alguno de los cursos ingresados anteriormente
    """
    ramos_por_curso[nuevo_nombre] = ramos_por_curso[nombre_curso_antiguo]
    horas_por_curso[nuevo_nombre] = horas_por_curso[nombre_curso_antiguo]
    del ramos_por_curso[nombre_curso_antiguo]
    del horas_por_curso[nombre_curso_antiguo]

def preparar_horario_curso(horarios: dict, horas_por_curso, curso: str, dias_de_la_semana: list):
    """
    Esta función se usa en el momento en el que se ingresaron todas las clases para un curso
    """
    for dia in dias_de_la_semana:
        horarios[curso][dia] = []

def agregar_modulo_a_curso(horarios: dict, curso: str, dia_de_la_semana: str, modulo: int):
    """
    Esta función permite agregar un módulo de clases a un curso al momento de fijar su horario
    """
    horarios[curso][dia_de_la_semana].append(modulo)

def eliminar_modulo_a_curso(horarios: dict, curso: str, dia_de_la_semana: str, modulo: int):
    """
    Esta función permite eliminar un módulo de clases de un curso al momento de fijar su horario
    """
    horarios[curso][dia_de_la_semana].remove(modulo)

def copiar_forma_horario(horarios: dict, curso_a_copiar: str, curso_objetivo: str):
    """
    Esta función permite copiar la forma de un horario de clases y pegarla en otro curso
    """
    horarios[curso_objetivo] = horarios[curso_a_copiar]

def agregar_ramos_modulos_seguidos(ramos_con_modulos_seguidos: dict, curso: str, ramo: str):
    """
    Esta función permite agregar un curso a la lista de ramos que se quiere que tengan módulos de clases consecutivos
    """
    ramos_con_modulos_seguidos[curso].append(ramo)

def eliminar_ramos_modulos_seguidos(ramos_con_modulos_seguidos: dict, curso: str, ramo: str):
    """"
    Esta función permite eliminar un curso de la lista de ramos que se quiere que tengan módulos de clases consecutivas
    """
    ramos_con_modulos_seguidos[curso].remove(ramo)
    
def modificar_dias(dias: list, nombre: str, indice_a_modificar: int = -1):
    """"
    Esta función permite modificar los días del horario. Estos días vienen dados por defecto (Lunes, Martes, Miércoles, Jueves, Viernes)
    """
    if indice_a_modificar > 0:
        dias[indice_a_modificar] = nombre
    else:
        dias.append(nombre)

if __name__ == '__main__':
    ramos_por_curso = {
            "1A": {
                "Orientaci\u00f3n": 1,
                "Educaci\u00f3n_F\u00edsica": 3}}

    horas_por_curso = {'1A': 4}
    horarios = {
        "1A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        }}

    agregar_clase(ramos_por_curso, '1A', 'Perking', 3, horas_por_curso)
    eliminar_clase(ramos_por_curso, '1A', 'Orientación', 1, horas_por_curso)
    cambiar_nombre_curso(ramos_por_curso, '1A', horas_por_curso, '2A')

    agregar_modulo_a_curso(horarios, '1A', 'Lunes', 8)

    print(horarios)

