from chalice import Chalice
import gurobipy as gp
from gurobipy import GRB
import json
import math
from typing import List, Mapping, Tuple, Union

def formar_asignaciones(profesores_por_curso: Mapping[str, List[Union[List[str], str]]]) -> List[Tuple[str, str, str]]:
    """Esta función forma la lista de tuplas (curso,profesor,ramo) que deben ser asignadas de forma que puedan ser ingresadas al modelo.

    Args:
        profesores_por_curso (Mapping[str, List[Union[List[str], str]]]): Diccionario con cursos como llave. Cada curso contiene una lista que tiene a su vez una lista con el o los profesores que harán ese curso y además el nombre del curso.

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
        carga_profesores (Mapping[str, List[Union[List[str], str]]]): Diccionario con los nombres de los profesores como llave. Cada profesor tiene asociada una lista que contiene una lista de uno o más cursos a los que les hace una cierta clase conjunta. 
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
        profesores_a_definir_por_curso (Mapping[str, List[Union[List[str], str]]]): Diccionario con cursos como llave. Cada curso contiene una lista que tiene a su vez una lista con el o los profesores que pueden hacer ese curso y además el nombre del curso.

    Returns:
        List[Tuple[str, str, str]]: Lista de tuplas de la forma (curso, profesor, ramo) las cuales pueden ser asignadas en el horario de cada curso.
    """    
    no_asignaciones = []
    for curso in profesores_a_definir_por_curso:
        for tupla in profesores_a_definir_por_curso[curso]:
            for prof in tupla[0]:
                no_asignaciones.append((curso, prof, tupla[1]))
    return no_asignaciones


app = Chalice(app_name='test')

def armar_modelo(data: dict) -> Mapping[int, str]:
    """Esta función arma el modelo a partir de los datos entregados para armar este. El detalle sobre las restricciones del modelo se encuentra en un archivo dedicado a eso.

    Args:
        data (dict): Set de datos completos que debe proporcionar el usuario.

    Returns:
        Mapping[int, str]: Entrega un diccionario con el número de solución como llave que se relaciona con todas las variables x que toman valor uno en la solución.
    """
    model = gp.Model("Generación de horarios de colegio")
    f = open('data_colegio_internet.json',encoding='utf8')

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

    asignaciones_normales = formar_asignaciones(profesores_por_curso)
    no_asignaciones = []
    no_asignaciones = asignaciones_no_hechas(profesores_a_definir_por_curso)
    total_asignaciones = asignaciones_normales + no_asignaciones
    asignaciones_con_restriccion_de_modulos_diarios = formar_asignaciones_con_restriccion_modulos_diarios(
        ramos_por_curso, total_asignaciones
    )
    tope_dias, profesores_con_dias_limitados = cantidad_maxima_de_dias(carga_profesores, ramos_por_curso)


    x = model.addVars(total_asignaciones,dias,modulos,vtype=GRB.BINARY, name="x")
    s = model.addVars(asignaciones_con_restriccion_de_modulos_diarios,dias,vtype=GRB.BINARY, name="s") 
    w = model.addVars(no_asignaciones, vtype=GRB.BINARY, name="w")
    y = model.addVars(profesores_con_dias_limitados,dias,vtype=GRB.BINARY,name="y")

    model.addConstrs((sum(x[c,ps[0],r,d,j] for ps,r in profesores_por_curso[c]) + sum(x[c,p,r,d,j] for ps,r in profesores_a_definir_por_curso[c] for p in ps) <= 1 for c in horarios for d in horarios[c] for j in horarios[c][d]),name="R1")

    model.addConstrs((sum(x[c,p,r,d,j] for ps,r in profesores_por_curso[c] for p in ps) + sum(x[c,p,r,d,j] for ps,r in profesores_a_definir_por_curso[c] for p in ps) >= 1 for c in horarios for d in horarios[c] for j in horarios[c][d]),name="R2")

    for c in profesores_por_curso:
        for ps,r in profesores_por_curso[c]:
            if len(ps) > 1:
                model.addConstrs((x[c,p1,r,d,j] - x[c,p2,r,d,j] == 0 for p1,p2 in [(ps[a],ps[b]) for a in range(len(ps)) for b in range(len(ps)) if a < b] for d in dias for j in modulos), name=f"R3[{c},{r}]")

    for c in profesores_por_curso:
        for ps,r in profesores_por_curso[c]:
            model.addConstrs((sum(x[c,p,r,d,j] for d in dias for j in modulos) == ramos_por_curso[c][r]['modulos_semanales'] for p in ps),name=f"R4[{c},{r}]")

    for c in profesores_a_definir_por_curso:
        for ps,r in profesores_a_definir_por_curso[c]:
            aux = []
            for p in ps:
                aux.append(p)
            aux = tuple(aux)
            model.addConstrs((sum(x[c,q,r,d,j] for q in aux for d in dias for j in modulos) == ramos_por_curso[c][r]['modulos_semanales']),name=f"R5[{c},{r}]")

    model.addConstrs((sum(x[c,p,r,d,j] for ps,r in profesores_por_curso[c] for p in ps) + sum(x[c,p,r,d,j] for ps,r in profesores_a_definir_por_curso[c] for p in ps) == 0 for c in horarios for d in horarios[c] for j in list(set(modulos) - set(horarios[c][d]))),name="R6")

    model.addConstrs((sum(x[cs[0],p,r,d,j] for cs,r in carga_profesores[p]) <= 1 for p in carga_profesores for d in dias for j in modulos),name="R7")

    for p in carga_profesores:
        for cs,r in carga_profesores[p]:
            model.addConstrs((x[c1,p,r,d,j] - x[c2,p,r,d,j] == 0 for c1,c2 in [(cs[a],cs[b]) for a in range(len(cs)) for b in range(len(cs)) if a < b] for d in dias for j in modulos), name=f"R8[{p},{r}]")

    for c in profesores_por_curso:
        for ps,r in profesores_por_curso[c]:
            model.addConstrs((sum(x[c,ps[0],r,d,j] for j in modulos) <= ramos_por_curso[c][r]['maximo_modulos_diarios'] for d in dias),name=f"R9[{c},{p},{r}]")

    for c in profesores_a_definir_por_curso:
        for ps,r in profesores_a_definir_por_curso[c]:
            aux = []
            for p in ps:
                aux.append(p)
            aux = tuple(aux)
            model.addConstrs((sum(x[c,q,r,d,j] for q in aux for j in modulos) <= ramos_por_curso[c][r]['maximo_modulos_diarios'] for d in dias),name=f"R10[{c},{r}]")

    model.addConstrs((x[c,p,r,d,j] + x[c,p,r,d,z] <= 1 for c,p,r in total_asignaciones if ramos_por_curso[c][r]['tipo_modulos'] == 'seguidos' for d in dias for j,z in list(set([(a,b) for a in horarios[c][d] for b in horarios[c][d] if a < b]) - set([tuple(comb) for comb in modulos_consecutivos]))), name="R11")

    model.addConstrs((x[c,p,r,d,j] + x[c,p,r,d,z] <= 1 for c,p,r in total_asignaciones if ramos_por_curso[c][r]['tipo_modulos'] == 'disjuntos' for d in dias for j,z in modulos_consecutivos), name="R12")

    model.addConstrs((M * s[c,p,r,d] >= sum(x[c,p,r,d,j] for j in modulos) for c,p,r in asignaciones_con_restriccion_de_modulos_diarios for d in dias),name="R13")

    model.addConstrs((sum(s[c,p,r,d] for d in dias) <= math.ceil(ramos_por_curso[c][r]['modulos_semanales'] / 2) for c,p,r in asignaciones_con_restriccion_de_modulos_diarios),name="R14")

    model.addConstrs((sum(x[cs[0],p,r,d,j] for cs,r in carga_profesores[p] for d in dias for j in modulos) <= limitaciones_profesores[p]['maximo_modulos'] for p in carga_profesores),name="R15")

    model.addConstrs((sum(x[cs[0],p,r,d,j] for cs,r in carga_profesores[p] for j in modulos) <= limitaciones_profesores[p]['maximo_modulos_diario'] for p in carga_profesores for d in dias),name="R16")

    model.addConstrs((sum(x[cs[0],p,r,d,j1] + x[cs[0],p,r,d,j2] + x[cs[0],p,r,d,j3] + x[cs[0],p,r,d,j4] + x[cs[0],p,r,d,j5] for cs,r in carga_profesores[p]) <= 4 for p in carga_profesores for d in dias for j1,j2,j3,j4,j5 in [(i,i+1,i+2,i+3,i+4) for i in modulos if i+4 in modulos]), name="R17")

    model.addConstrs((M * y[p,d] >= sum(x[cs[0],p,r,d,j] for cs,r in carga_profesores[p] for j in modulos) for d in dias for p in profesores_con_dias_limitados),name="R18")

    model.addConstrs((sum(y[p,d] for d in dias) <= tope_dias[p] for p in profesores_con_dias_limitados),name="R19")

    for c in profesores_a_definir_por_curso:
        for ps,r in profesores_a_definir_por_curso[c]:
            model.addConstrs((M * w[c,p,r] >= sum(x[c,p,r,d,j] for d in horarios[c] for j in horarios[c][d]) for p in ps),name=f"R20[{c},{r}]")

    model.addConstrs((sum(w[c,p,r] for ps,r in profesores_a_definir_por_curso[c] for p in ps) <= 1 for c in profesores_a_definir_por_curso),name="R21")

    model.addConstrs((x[c,p,r,d,j] == 1 for c,p,r,d,j in asignaciones_fijadas),name="R22");

    lista_restricciones = []
    for c,p,r,d,j in asignaciones_fijadas:
        lista_restricciones.append(f"R22[{c},{p},{r},{d},{j}]")

    model.addConstrs((x[c,p,r,d,j] == 0 for c,p,r,d,j in asignaciones_vetadas),name="R23");

    for c,p,r,d,j in asignaciones_vetadas:  
        lista_restricciones.append(f"R23[{c},{p},{r},{d},{j}]")

    obj = sum(x[c,p,r,d,j] + x[c2,p2,r2,d,z] for c,p,r in asignaciones_normales for c2,p2,r2 in asignaciones_normales if p == p2 and c == c2 for d in dias for j,z in modulos_consecutivos)
    model.setObjective(obj, GRB.MINIMIZE)
    model.update()
    seguir = True
    while seguir:
        model.optimize()
        if 'value' in str(model.getVars()[0]):
            seguir = False
        if seguir:
            model.remove(model.getConstrByName(lista_restricciones[len(lista_restricciones) - 1]))
            lista_restricciones.remove(lista_restricciones[len(lista_restricciones) - 1])
            model.update()
            
        # model.computeIIS()
        # removed =[]
        # for c in model.getConstrs():
        #     if c.IISConstr:
        #         print('%s' % c.constrName)
        #         # Remove a single constraint from the model
        #         removed.append(str(c.constrName))
        #         model.remove(c)

    model.update()
    
    model.write('data.lp')
    model.setParam("PoolSolutions", 10)
    model.setParam('PoolSearchMode', 2)
    model.setParam('OutputFlag', 1)
    model.update()
    # model.computeIIS()
    # removed =[]
    # for c in model.getConstrs():
    #     if c.IISConstr:
    #         print('%s' % c.constrName)
    #         # Remove a single constraint from the model
    #         removed.append(str(c.constrName))
    #         model.remove(c)
    model.optimize()

    out = {}

    for i in range(model.SolCount):
        model.setParam("SolutionNumber", i)
        model.update()

        model.optimize()
        vs = []
        for v in model.getVars():
            if v.VarName[0] == 'x' and round(v.X) == 1:
                vs.append(f"{v.VarName} = {round(v.X)}")
        out[i + 1] = vs
    return out

@app.route('/', methods=['GET'])
def index():
    return {'hello': 'world'}

@app.route('/test', methods=['POST'], content_types=['application/json'])
def test():
    # data = 'hola'
    # data = app.current_request.raw_body
    # decoded = data.decode('UTF-8')
    # print(decoded)
    # loc = decoded.rfind('%5B')
    # breaker = False
    # counter = 1
    # if loc != 1:
    #     while not breaker and loc != 1:
    #         if decoded[loc - counter] != int:
    #             breaker = True
    #         else:
    #             breaker = False
    #         counter += 1
    # last_tuple = decoded[loc - counter + 1:loc]
    # print(last_tuple)
    # first_index = 0
    # final = {}
    # for i in range(int(last_tuple) + 1):
    #     if i != int(last_tuple):
    #         last_index = decoded.find(f'{str(i+1)}%5B')
    #     else:
    #         last_index = len(decoded)
    #     elem = decoded[first_index:last_index]
    #     first_index = last_index
    #     elem = elem.replace(f'{str(i)}%5B', '')
    #     elem = elem.replace('%5D=', ':')
    #     elem = elem.replace('&', ',')
    #     elem = elem.replace('+', ' ')
    #     # print(dict([item.split(":") for item in elem.split(",")]))
    #     final[i] = elem
    #     # decoded = decoded.replace(f'{str(i)}%5B','')
    #     # decoded = decoded.replace('%5D', ':')
    #     # decoded = decoded.replace('%C3%B3', 'ó')
    #     # decoded = decoded.replace('+', ' ')
    # print(final)
    return {'hello': 'world'}



@app.route('/test2', methods=['POST'], content_types=['application/x-www-form-urlencoded; charset=UTF-8'])
def enviar():
    user_as_json = app.current_request.json_body
    resultado = armar_modelo(user_as_json)
    # a = model(user_as_json)
    # out = []
    # for d in user_as_json["dias"]:
    #     out.append(d)
    # cantidad_profesores = len(user_as_json['profesores_por_curso'])
    # return {"output": out, "cantidad_prof": cantidad_profesores, }
    return resultado
