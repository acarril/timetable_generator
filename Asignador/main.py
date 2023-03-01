import gurobipy as gp
from gurobipy import GRB
import json
import math
from prettytable import PrettyTable
from typing import List, Mapping, Tuple, Union

def formar_asignaciones(profesores_por_curso: Mapping[str, List[Union[List[str], str]]]) -> List[Tuple[str, str, str]]:
    """Esta función forma la lista de tuplas (curso,profesor,ramo) que deben ser asignadas de forma que puedan ser ingresadas al modelo.

    Args:
        profesores_por_curso (Mapping[str, List[List[str], str]]): Diccionario con cursos como llave. Cada curso contiene una lista que tiene a su vez una lista con el o los profesores que harán ese curso y además el nombre del curso.

    Returns:
        List[Tuple[str, str, str]]: Lista de tuplas de la forma (curso, profesor, ramo) las cuales deben ser asignadas en el horario de cada curso.
    """
    lista_asignaciones = []
    for curso in profesores_por_curso:
        for tupla in profesores_por_curso[curso]:
            for prof in tupla[0]:
                lista_asignaciones.append((curso, prof, tupla[1]))
    return lista_asignaciones

def formar_asignaciones_con_restriccion_modulos_diarios(ramos_por_curso: Mapping[str, Mapping[str, Mapping[str, int]]], asignaciones: List[Tuple[str, str, str]]) -> List[Tuple[str, str, str]]:
    """Esta función forma la lista de las clases que se quiere que necesariamente tengan módulos de clases seguidos.

    Args:
        ramos_con_modulos_seguidos (Mapping[str, Mapping[str, Mapping[str, int]]]): Diccionario con cursos como llave. Cada curso tiene asociado una lista con los ramos que se quiere que tengan módulos dobles. Cada ramo es llave de un diccionario que tiene las llaves "modulos_semanales", "maximo_modulos_diarios" y "tipo_modulos".
        asignaciones (Tuple[str, str, str]): Lista de tuplas de la forma (curso, profesor, ramo) las cuales pueden o deben ser asignadas en el horario de cada curso.

    Returns:
        Tuple[str, str, str]: Lista de tuplas de la forma (curso, profesor, ramo) que deben tener módulos seguidos de clases.
    """ 
    lista_modulos_seguidos = []
    for curso in ramos_por_curso:
        for ramo in ramos_por_curso[curso]:
            if ramos_por_curso[curso][ramo]['tipo_modulos'] == 'seguidos':
                lista_modulos_seguidos.append((curso, ramo))
    asignaciones_con_restriccion_de_modulos_diarios = []
    for elem in asignaciones:
        if (elem[0],elem[2]) in lista_modulos_seguidos:
            asignaciones_con_restriccion_de_modulos_diarios.append(elem)
    return asignaciones_con_restriccion_de_modulos_diarios

def cantidad_maxima_de_dias(carga_profesores: Mapping[str, List[Union[List[str], str]]], ramos_por_curso: Mapping[str, Mapping[str, Mapping[str, int]]]) -> Tuple[Mapping[str, int], List[str]]:
    """Esta función asigna un tope de días de trabajo a los profesores que hacen pocos módulos de clases. En la práctica esto debería ser ingresado por el usuario.

    Args:
        carga_profesores (Mapping[str, List[List[str], str]]): Diccionario con los nombres de los profesores como llave. Cada profesor tiene asociada una lista que contiene una lista de uno o más cursos a los que les hace una cierta clase conjunta. 
        ramos_por_curso (Mapping[str, Mapping[str, Mapping[str, int]]]): Diccionario con los cursos como llave. Cada uno de estos lleva a un diccionario con los ramos como llave, los cuales entregan la cantidad de módulos semanales de cada ramo y el máximo de módulos diarios permitidos.

    Returns:
        Tuple[Mapping[str, int], List[str]]: Tupla que contiene, por una parte, un diccionario con nombres de profesores como llave y entregan el máximo de días que puede trabajar cada uno y, por otra parte, una lista con todos los profesores que no tienen disponibilidad completa.
    """    
    tope_dias = {}
    for profesor in carga_profesores:
        suma = 0
        for tupla in carga_profesores[profesor]:
            suma += ramos_por_curso[tupla[0][0]][tupla[1]]['modulos_semanales']
        if suma <= 2:
            tope_dias[profesor] = 1
        elif suma <= 4:
            tope_dias[profesor] = 2
        elif suma <= 6:
            tope_dias[profesor] = 3
        elif suma <= 8:
            tope_dias[profesor] = 4
    profesores_con_dias_limitados = []
    for elem in tope_dias.keys():
        profesores_con_dias_limitados.append(elem)
    profesores_con_dias_limitados
    
    return tope_dias, profesores_con_dias_limitados

def asignaciones_no_hechas(profesores_a_definir_por_curso: Mapping[str, List[Union[List[str], str]]]) -> List[Tuple[str, str, str]]:
    """Función que forma las tuplas de los cursos que no tienen profesor definido

    Args:
        profesores_a_definir_por_curso (Mapping[str, List[List[str], str]]): Diccionario con cursos como llave. Cada curso contiene una lista que tiene a su vez una lista con el o los profesores que pueden hacer ese curso y además el nombre del curso.

    Returns:
        List[Tuple[str, str, str]]: Lista de tuplas de la forma (curso, profesor, ramo) las cuales pueden ser asignadas en el horario de cada curso.
    """    
    no_asignaciones = []
    for curso in profesores_a_definir_por_curso:
        for tupla in profesores_a_definir_por_curso[curso]:
            for prof in tupla[0]:
                no_asignaciones.append((curso, prof, tupla[1]))
    return no_asignaciones

model = gp.Model("Generación de horarios de colegio")
# model.setParam('OutputFlag', 1)
f = open('data/probando_formato.json',encoding='utf8')

M = 10000
data = json.load(f)
dias = data['dias']
modulos = data['modulos']
horarios = data['horarios']
profesores_por_curso = data['profesores_por_curso']
ramos_por_curso = data['ramos_por_curso']
carga_profesores = data['carga_profesores']
modulos_consecutivos = data['modulos_consecutivos']
limitaciones_profesores = data['limitaciones_profesores']
profesores_a_definir_por_curso = data['profesores_a_definir_por_curso']
asignaciones_fijadas = data['asignaciones_fijadas']
asignaciones_vetadas = data['asignaciones_vetadas']
ramos_en_distintos_dias = data['ramos_en_distintos_dias']
primeros_modulos = []
segundos_modulos = []
for j,k in modulos_consecutivos:
    primeros_modulos.append(j)
    segundos_modulos.append(k)
primeros_modulos_exclusivos = list(set(primeros_modulos) - set(segundos_modulos))
segundos_modulos_exclusivos = list(set(segundos_modulos) - set(primeros_modulos))
primeros_modulos_exclusivos, segundos_modulos_exclusivos

asignaciones_normales = formar_asignaciones(profesores_por_curso)
no_asignaciones = []
# no_asignaciones = asignaciones_no_hechas(profesores_por_curso)
total_asignaciones = asignaciones_normales + no_asignaciones
asignaciones_con_restriccion_de_modulos_diarios = formar_asignaciones_con_restriccion_modulos_diarios(
    ramos_por_curso, total_asignaciones
)
tope_dias, profesores_con_dias_limitados = cantidad_maxima_de_dias(carga_profesores, ramos_por_curso)


x = model.addVars(total_asignaciones,dias,modulos,vtype=GRB.BINARY, name="x")
z = model.addVars(total_asignaciones,dias,modulos,vtype=GRB.BINARY, name="z")
y = model.addVars(total_asignaciones,dias,modulos,vtype=GRB.BINARY, name="y")
# * Solo para los cursos donde se prefieren módulos dobles
w = model.addVars(no_asignaciones, vtype=GRB.BINARY, name="w")
s = model.addVars(profesores_con_dias_limitados,dias,vtype=GRB.BINARY,name="s") # * Solo para los profesores que tienen menos de 5 días
n = model.addVars(list(carga_profesores.keys()),dias,[i for i in modulos if i+4 in modulos],vtype=GRB.BINARY,name="v")


model.addConstrs((sum(x[c,ps[0],r,d,j] + z[c,ps[0],r,d,j] + y[c,ps[0],r,d,j]for ps,r in profesores_por_curso[c]) + sum(x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] for ps,r in profesores_a_definir_por_curso[c] for p in ps) <= 1 for c in horarios for d in horarios[c] for j in horarios[c][d]),name="R1")

model.addConstrs((sum(x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] for ps,r in profesores_por_curso[c] for p in ps) + sum(x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] for ps,r in profesores_a_definir_por_curso[c] for p in ps) >= 1 for c in horarios for d in horarios[c] for j in horarios[c][d]),name="R2")

for c in profesores_por_curso:
    for ps,r in profesores_por_curso[c]:
        if len(ps) > 1:
            model.addConstrs((x[c,p1,r,d,j] - x[c,p2,r,d,j] == 0 for p1,p2 in [(ps[a],ps[b]) for a in range(len(ps)) for b in range(len(ps)) if a < b] for d in dias for j in modulos), name=f"R3[{c},{r}]")

for c in profesores_por_curso:
    for ps,r in profesores_por_curso[c]:
        if len(ps) > 1:
            model.addConstrs((z[c,p1,r,d,j] - z[c,p2,r,d,j] == 0 for p1,p2 in [(ps[a],ps[b]) for a in range(len(ps)) for b in range(len(ps)) if a < b] for d in dias for j in modulos), name=f"R4[{c},{r}]")

for c in profesores_por_curso:
    for ps,r in profesores_por_curso[c]:
        if len(ps) > 1:
            model.addConstrs((y[c,p1,r,d,j] - y[c,p2,r,d,j] == 0 for p1,p2 in [(ps[a],ps[b]) for a in range(len(ps)) for b in range(len(ps)) if a < b] for d in dias for j in modulos), name=f"R5[{c},{r}]")

for c in profesores_por_curso:
    for ps,r in profesores_por_curso[c]:
        if ramos_por_curso[c][r]['tipo_modulos'] == 'seguidos':
            model.addConstrs((sum(x[c,p,r,d,j] for d in dias for j in modulos) == (ramos_por_curso[c][r]['modulos_semanales']) % 2 for p in ps),name=f"R6[{c},{r}]")
            model.addConstrs((sum(z[c,p,r,d,j] for d in dias for j in modulos) == math.floor((ramos_por_curso[c][r]['modulos_semanales']) / 2) for p in ps),name=f"R7[{c},{r}]")
            model.addConstrs((sum(y[c,p,r,d,j] for d in dias for j in modulos) == math.floor((ramos_por_curso[c][r]['modulos_semanales']) / 2) for p in ps),name=f"R8[{c},{r}]")
        else:
            model.addConstrs((sum(x[c,p,r,d,j] for d in dias for j in modulos) == ramos_por_curso[c][r]['modulos_semanales'] for p in ps if ramos_por_curso[c][r]),name=f"R9[{c},{r}]")

for c in profesores_a_definir_por_curso:
    for ps,r in profesores_a_definir_por_curso[c]:
        aux = []
        for p in ps:
            aux.append(p)
        aux = tuple(aux)
        if ramos_por_curso[c][r]['tipo_modulos'] == 'seguidos':
            model.addConstrs((sum(x[c,q,r,d,j] for q in aux for d in dias for j in modulos) == (ramos_por_curso[c][r]['modulos_semanales']) % 2),name=f"R10[{c},{r}]")
            model.addConstrs((sum(z[c,q,r,d,j] for q in aux for d in dias for j in modulos) == math.floor((ramos_por_curso[c][r]['modulos_semanales']) / 2)),name=f"R11[{c},{r}]")
            model.addConstrs((sum(y[c,q,r,d,j] for q in aux for d in dias for j in modulos) == math.floor((ramos_por_curso[c][r]['modulos_semanales']) / 2)),name=f"R12[{c},{r}]")
        else:
            model.addConstrs((sum(x[c,q,r,d,j] for q in aux for d in dias for j in modulos) == ramos_por_curso[c][r]['modulos_semanales']),name=f"R13[{c},{r}]")

model.addConstrs((sum(x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] for ps,r in profesores_por_curso[c] for p in ps) + sum(x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] for ps,r in profesores_a_definir_por_curso[c] for p in ps) == 0 for c in horarios for d in horarios[c] for j in list(set(modulos) - set(horarios[c][d]))),name="R14")

model.addConstrs((sum(x[cs[0],p,r,d,j] + z[cs[0],p,r,d,j] + y[cs[0],p,r,d,j] for cs,r in carga_profesores[p]) <= 1 for p in carga_profesores for d in dias for j in modulos),name="R15")

for p in carga_profesores:
    for cs,r in carga_profesores[p]:
        model.addConstrs((x[c1,p,r,d,j] - x[c2,p,r,d,j] == 0 for c1,c2 in [(cs[a],cs[b]) for a in range(len(cs)) for b in range(len(cs)) if a < b] for d in dias for j in modulos), name=f"R16[{p},{r}]")

for p in carga_profesores:
    for cs,r in carga_profesores[p]:
        model.addConstrs((z[c1,p,r,d,j] - z[c2,p,r,d,j] == 0 for c1,c2 in [(cs[a],cs[b]) for a in range(len(cs)) for b in range(len(cs)) if a < b] for d in dias for j in modulos), name=f"R17[{p},{r}]")

for p in carga_profesores:
    for cs,r in carga_profesores[p]:
        model.addConstrs((y[c1,p,r,d,j] - y[c2,p,r,d,j] == 0 for c1,c2 in [(cs[a],cs[b]) for a in range(len(cs)) for b in range(len(cs)) if a < b] for d in dias for j in modulos), name=f"R18[{p},{r}]")
    
for c in profesores_por_curso:
    for ps,r in profesores_por_curso[c]:
        model.addConstrs((sum(x[c,ps[0],r,d,j] + z[c,ps[0],r,d,j] + y[c,ps[0],r,d,j] for j in modulos) <= ramos_por_curso[c][r]['maximo_modulos_diarios'] for d in dias),name=f"R19[{c},{p},{r}]")

for c in profesores_a_definir_por_curso:
    for ps,r in profesores_a_definir_por_curso[c]:
        aux = []
        for p in ps:
            aux.append(p)
        aux = tuple(aux)
        model.addConstrs((sum(x[c,q,r,d,j] + z[c,q,r,d,j] + y[c,q,r,d,j] for q in aux for j in modulos) <= ramos_por_curso[c][r]['maximo_modulos_diarios'] for d in dias),name=f"R20[{c},{r}]")

model.addConstrs((x[c,p,r,d,j] + x[c,p,r,d,k] <= 1 for c,p,r in total_asignaciones if ramos_por_curso[c][r]['tipo_modulos'] == 'disjuntos' for d in dias for j,k in modulos_consecutivos), name="R21")

model.addConstrs((sum(x[cs[0],p,r,d,j] + z[cs[0],p,r,d,j] + y[cs[0],p,r,d,j] for cs,r in carga_profesores[p] for d in dias for j in modulos) <= limitaciones_profesores[p]['maximo_modulos'] for p in carga_profesores),name="R22")

model.addConstrs((sum(x[cs[0],p,r,d,j] + z[cs[0],p,r,d,j] + y[cs[0],p,r,d,j] for cs,r in carga_profesores[p] for j in modulos) <= limitaciones_profesores[p]['maximo_modulos_diario'] for p in carga_profesores for d in dias),name="R23")

model.addConstrs((M * s[p,d] >= sum(x[cs[0],p,r,d,j] + z[cs[0],p,r,d,j] + y[cs[0],p,r,d,j] for cs,r in carga_profesores[p] for j in modulos) for d in dias for p in profesores_con_dias_limitados),name="R24")

model.addConstrs((sum(s[p,d] for d in dias) <= tope_dias[p] for p in profesores_con_dias_limitados),name="R25")

for c in profesores_a_definir_por_curso:
    for ps,r in profesores_a_definir_por_curso[c]:
        model.addConstrs((M * w[c,p,r] >= sum(x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] for d in horarios[c] for j in horarios[c][d]) for p in ps),name=f"R26[{c},{r}]")

model.addConstrs((sum(w[c,p,r] for ps,r in profesores_a_definir_por_curso[c] for p in ps) <= 1 for c in profesores_a_definir_por_curso),name="R27")

model.addConstrs((x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] == 1 for c,p,r,d,j in asignaciones_fijadas),name="R28");

lista_restricciones = []
for c,p,r,d,j in asignaciones_fijadas:
    lista_restricciones.append(f"R28[{c},{p},{r},{d},{j}]")

model.addConstrs((x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] == 0 for c,p,r,d,j in asignaciones_vetadas),name="R29");

for c,p,r,d,j in asignaciones_vetadas:
    lista_restricciones.append(f"R29[{c},{p},{r},{d},{j}]")

for c in ramos_en_distintos_dias:
    for ls in ramos_en_distintos_dias[c]:
        for p1,r1,p2,r2 in [(ls[b][0][i],ls[b][1],ls[d][0][k],ls[d][1]) for b in range(len(ls)) for d in range(len(ls)) if b < d for i in range(len(ls[b][0])) for k in range(len(ls[d][0]))]:
            model.addConstrs((sum(x[c,p1,r1,d,j] + x[c,p2,r2,d,j] + z[c,p1,r1,d,j] + z[c,p2,r2,d,j] + y[c,p1,r1,d,j] + y[c,p2,r2,d,j] for j in modulos) <= max(ramos_por_curso[c][r1]['maximo_modulos_diarios'], ramos_por_curso[c][r2]['maximo_modulos_diarios']) for d in dias),name="R30")

model.addConstrs((x[c,p,r,d,j] + z[c,p,r,d,j] + y[c,p,r,d,j] <= 1 for c,p,r in total_asignaciones for d in dias for j in modulos),name="R31")

model.addConstrs((z[c,p,r,d,j] - y[c,p,r,d,k] == 0 for c,p,r in total_asignaciones for d in dias for j,k in [(modulos[i],modulos[i+1]) for i in range(len(modulos) - 1)]),name="R32")

model.addConstrs((z[c,p,r,d,j] == 0 for c,p,r in total_asignaciones for d in dias for j in segundos_modulos_exclusivos),name="R33")

model.addConstrs((y[c,p,r,d,j] == 0 for c,p,r in total_asignaciones for d in dias for j in primeros_modulos_exclusivos),name="R34")

model.addConstrs((M * n[p,d,j] >= sum(x[c,p,r,d,j] + y[c,p,r,d,j] + z[c,p,r,d,j] for cs,r in carga_profesores[p] for c in cs) for p in carga_profesores for d in dias for j in [i for i in modulos if i+4 in modulos]),name="R33")

# model.addConstrs((sum(x[cs[0],p,r,d,j1] + x[cs[0],p,r,d,j2] + x[cs[0],p,r,d,j3] + x[cs[0],p,r,d,j4] + x[cs[0],p,r,d,j5] + z[cs[0],p,r,d,j1] + z[cs[0],p,r,d,j2] + z[cs[0],p,r,d,j3] + z[cs[0],p,r,d,j4] + z[cs[0],p,r,d,j5] + y[cs[0],p,r,d,j1] + y[cs[0],p,r,d,j2] + y[cs[0],p,r,d,j3] + y[cs[0],p,r,d,j4] + y[cs[0],p,r,d,j5] for cs,r in carga_profesores[p]) <= 4 for p in carga_profesores for d in dias for j1,j2,j3,j4,j5 in [(i,i+1,i+2,i+3,i+4) for i in modulos if i+4 in modulos]), name="R34")

obj = sum(n[p,d,j] for p in carga_profesores for d in dias for j in [i for i in modulos if i+4 in modulos])
model.setObjective(obj, GRB.MINIMIZE)
# model.setObjective(0, GRB.MINIMIZE)

model.setParam("PoolSolutions", 1)
model.setParam('PoolSearchMode', 2)
model.setParam('OutputFlag', 1)
model.update()

seguir = True
        
model.write('probando.lp')
# model.computeIIS()
# removed =[]
# for c in model.getConstrs():
#     if c.IISConstr:
#         print('%s' % c.constrName)
#         # Remove a single constraint from the model
#         removed.append(str(c.constrName))
#         model.remove(c)

while seguir:
    model.optimize()
    if 'value' in str(model.getVars()[0]):
        seguir = False
    if seguir:
        model.remove(model.getConstrByName(lista_restricciones[len(lista_restricciones) - 1]))
        lista_restricciones.remove(lista_restricciones[len(lista_restricciones) - 1])
        model.update()

model.update()
for i in range(model.SolCount):
    model.setParam("SolutionNumber", i)
    model.update()

    print(model.optimize())
    model.write(f"solutions/out{i+1}.sol")