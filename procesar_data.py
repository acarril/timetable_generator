lista_definidos = [['1A', ['ProfA', 'ProfB'], 'Matematica', 7, 2, 'seguidos'],
         ['1A', ['ProfB'], 'Lenguaje', 7, 2, 'seguidos'],
         ['1B', ['ProfB'], 'Lenguaje', 7, 2, 'seguidos']]
lista_no_definidos = [['1C', ['ProfC', 'ProfD'], 'Inglés', 4, 2, 'seguidos']]

cursos_vinculados = [[['1A', '1B'], 'ProfB', 'Lenguaje']]

ramos_en_distintos_dias = {'1A': [['Matematica', 'Lenguaje']]}


limitaciones_profesores = {}
carga_profesores = {}
profesores_por_curso = {}
profesores_a_definir_por_curso = {}
ramos_por_curso = {}

for tupla in lista_definidos:
    for elem in tupla[1]:
        if elem not in limitaciones_profesores:
            limitaciones_profesores[elem] = {"maximo_modulos": 50, "maximo_modulos_diarios": 10}

    for elem in tupla[1]:
        if elem not in carga_profesores:
            carga_profesores[elem] = [[[tupla[0]], tupla[2]]]
        else:
            carga_profesores[elem].append([[tupla[0]], tupla[2]])

    if tupla[0] not in profesores_por_curso:
        profesores_por_curso[tupla[0]] = [[tupla[1], tupla[2]]]
    else:
        profesores_por_curso[tupla[0]].append([tupla[1], tupla[2]])
    
    if tupla[0] not in profesores_a_definir_por_curso:
        profesores_a_definir_por_curso[tupla[0]] = []

    if tupla[0] not in ramos_por_curso:
        ramos_por_curso[tupla[0]] = {tupla[2]: {"modulos_semanales": int(tupla[3]), "maximo_modulos_diarios": int(tupla[4]), "tipo_modulos": tupla[5]}}
    else:
        ramos_por_curso[tupla[0]][tupla[2]] = {"modulos_semanales": int(tupla[3]), "maximo_modulos_diarios": int(tupla[4]), "tipo_modulos": tupla[5]}

for tupla in lista_no_definidos:
    for elem in tupla[1]:
        if elem not in limitaciones_profesores:
            limitaciones_profesores[elem] = {"maximo_modulos": 50, "maximo_modulos_diarios": 10}

    if tupla[0] not in profesores_a_definir_por_curso:
        profesores_a_definir_por_curso[tupla[0]] = [tupla[1], tupla[2]]
    else:
        profesores_a_definir_por_curso[tupla[0]].append([tupla[1], tupla[2]])

    if tupla[0] not in profesores_por_curso:
        profesores_por_curso[tupla[0]] = []

    if tupla[0] not in ramos_por_curso:
        ramos_por_curso[tupla[0]] = {tupla[2]: {"modulos_semanales": int(tupla[3]), "maximo_modulos_diarios": int(tupla[4]), "tipo_modulos": tupla[5]}}
    else:
        ramos_por_curso[tupla[0]][tupla[2]] = {"modulos_semanales": int(tupla[3]), "maximo_modulos_diarios": int(tupla[4]), "tipo_modulos": tupla[5]}

for tupla in cursos_vinculados:
    for carga in carga_profesores[tupla[1]]:
        if carga[0][0] == tupla[0][0] and carga[1] == tupla[2]:
            carga[0] = tupla[0]
    for curso in tupla[0]:
        for carga in carga_profesores[tupla[1]]:
            if carga[0][0] == curso and len(carga[0]) == 1 and carga[1] == tupla[2]:
                carga_profesores[tupla[1]].remove(carga)


for curso in ramos_en_distintos_dias:
    for i in range(len(ramos_en_distintos_dias[curso])):
        for j in range(len(ramos_en_distintos_dias[curso][i])):
            for elem in profesores_por_curso[curso]:
                if elem[1] == ramos_en_distintos_dias[curso][i][j]:
                    ramos_en_distintos_dias[curso][i][j] = elem

print(limitaciones_profesores)
print(carga_profesores)
print(profesores_a_definir_por_curso)
print('-->' + str(profesores_por_curso))
print(ramos_por_curso)
print(ramos_en_distintos_dias)