import random
import json
import string

class MultiDimensionalArrayEncoder(json.JSONEncoder):
    def encode(self, obj):
        def hint_tuples(item):
            if isinstance(item, tuple):
                return {'__tuple__': True, 'items': item}
            if isinstance(item, list):
                return [hint_tuples(e) for e in item]
            if isinstance(item, dict):
                return {key: hint_tuples(value) for key, value in item.items()}
            else:
                return item

        return super(MultiDimensionalArrayEncoder, self).encode(hint_tuples(obj))
def hinted_tuple_hook(obj):
    if '__tuple__' in obj:
        return tuple(obj['items'])
    else:
        return obj
enc = MultiDimensionalArrayEncoder()

def generar_horas_libres(ramos_por_curso):

    horas_libre_disposicion = {
        '1': 6,
        '2': 6,
        '3': 6,
        '4': 6,
        '5': 6,
        '6': 6,
        '7': 6,
        '8': 6,
        'I': 6,
        'II': 6,
        'III': 15,
        'IV': 15,
    }
    for curso in list(ramos_por_curso.keys()):
        nivel = curso[:-1]
        for i in range(horas_libre_disposicion[nivel]):
            ramos_por_curso[curso][random.choice(list(ramos_por_curso[curso]))] += 1
    
    return ramos_por_curso

def generar_profesores(length: int, cantidad: int, cantidad_profesores_por_ramo: dict, cantidad_cursos_profesor: dict):
    lista_profesores_para_asignaciones = []
    lista_profesores = []
    for _ in range(cantidad):
        first_letter = string.ascii_uppercase
        letters = string.ascii_lowercase
        first_letter = random.choice(first_letter)
        result_str = ''.join(random.choice(letters) for _ in range(length))
        result_str = first_letter + result_str
        ramo_elegido = False
        while not ramo_elegido:
            ramo = random.choice(list(cantidad_profesores_por_ramo.keys()))
            if cantidad_profesores_por_ramo[ramo] > 0:
                cantidad_profesores_por_ramo[ramo] -=1 
                ramo_elegido = True
        lista_profesores_para_asignaciones.append([result_str,ramo,cantidad_cursos_profesor[ramo]])
        lista_profesores.append(result_str)
    return lista_profesores_para_asignaciones, lista_profesores

def generar_asignaciones(lista_profesores_para_asignaciones: list, ramos_por_curso):
    profesores_por_curso = {}
    for curso in ramos_por_curso.keys():
        profesores_por_curso[curso] = []
        for ramo in list(ramos_por_curso[curso].keys()):
            # print(curso, ramo)
            # print(lista_profesores_para_asignaciones)
            profesor_elegido = False
            while not profesor_elegido:
                profesor = random.choice(lista_profesores_para_asignaciones)
                if profesor[1] == ramo:
                    profesores_por_curso[curso].append((profesor[0],profesor[1]))
                    profesor[2] -= 1
                    profesor_elegido = True
                    if profesor[2] == 0:
                        lista_profesores_para_asignaciones.remove(profesor)
    return profesores_por_curso

cantidad_profesores_ramo = {
    "Lenguaje": 10,
    "Matemáticas": 10,
    "Historia": 7,
    "Artes_Visuales": 5,
    "Música": 5,
    "Educación_Física": 8,
    "Orientación": 4,
    "Tecnología": 4,
    "Religión": 5,
    "Ciencias_Naturales": 7,
    "Inglés": 7,
    "Consejo_de_Curso": 1,
    "Filosofía": 1
}

cantidad_cursos_profesor = {
    "Lenguaje": 4,
    "Matemáticas": 4,
    "Historia": 4,
    "Artes_Visuales": 6,
    "Música": 6,
    "Educación_Física": 4,
    "Orientación": 10,
    "Tecnología": 10,
    "Religión": 7,
    "Ciencias_Naturales": 4,
    "Inglés": 4,
    "Consejo_de_Curso": 10,
    "Filosofía": 10
}


if __name__ == '__main__':
    with open('Reducido/parametros.json',encoding='utf8') as f:
        data = json.load(f, object_hook=hinted_tuple_hook)

    ramos_por_curso = data['ramos_por_curso']

    nivel = 'III'

    ramos_por_curso = generar_horas_libres(ramos_por_curso)

    lista_profesores_para_asignaciones, profesores = generar_profesores(7, 74, cantidad_profesores_ramo, cantidad_cursos_profesor)

    print(lista_profesores_para_asignaciones)

    for elem in lista_profesores_para_asignaciones:
        if elem[1] == 'Matemáticas':
            print(elem)

    print(generar_asignaciones(lista_profesores_para_asignaciones, ramos_por_curso))

