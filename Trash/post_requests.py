import json
import requests

url = 'http://localhost:8000/test2'
myobj = {
    "dias": [
        "Lunes","Martes","Miercoles","Jueves","Viernes"
    ],
    "modulos": [
        1,2,3,4,5,6,7,8,9,10
    ],
    "modulos_consecutivos": [
        [1,2],[2,3],[4,5],[6,7],[8,9]
    ],
    "ramos_con_modulos_seguidos": {
        "1A": [
            "Educacion_Fisica", "Artes_Visuales", "Tecnologia"
        ],
        "1B": [],
        "1C": [],
        "1D": [],
        "2A": [],
        "2B": [],
        "2C": [],
        "2D": [],
        "3A": [],
        "3B": [],
        "3C": [],
        "3D": [],
        "4A": [],
        "4B": [],
        "4C": [],
        "4D": [],
        "5A": [],
        "5B": [],
        "5C": [],
        "5D": [],
        "6A": [],
        "6B": [],
        "6C": [],
        "6D": [],
        "7A": [],
        "7B": [],
        "7C": [],
        "7D": [],
        "8A": [],
        "8B": [],
        "8C": [],
        "8D": [],
        "IA": [],
        "IB": [],
        "IC": [],
        "ID": [],
        "IIA": [],
        "IIB": [],
        "IIC": [],
        "IID": [],
        "IIIA": [],
        "IIIB": [],
        "IIIC": [],
        "IIID": [],
        "IVA": [],
        "IVB": [],
        "IVC": [],
        "IVD": []
    },
    "horarios": {
        "1A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "1B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "1C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "1D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miercoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "ID": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IID": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIIA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIIB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIIC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIID": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVD": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miercoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        }
    },
    "profesores_por_curso": {
        "1A": {
            "0": {},
            "1": [
                [
                    "Eieyagjc",
                    "Aleman"
                ],
                [
                    "Ycaeozob",
                    "Artes_Visuales"
                ],
                [
                    "Ncnqafso",
                    "Ciencias_Naturales"
                ],
                [
                    "Yiqzsxsm",
                    "Educacion_Fisica"
                ],
                [
                    "Nipudbji",
                    "Historia"
                ],
                [
                    "Zjszbjef",
                    "Lenguaje"
                ],
                [
                    "Bzbkyeqh",
                    "Matematicas"
                ],
                [
                    "Pxymekhf",
                    "Musica"
                ],
                [
                    "Wrbjwpou",
                    "Orientacion"
                ],
                [
                    "Bzbkyeqh",
                    "Religion"
                ],
                [
                    "Atzgrmcj",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Mlvafpyt",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "1B": {
            "0": {},
            "1": [
                [
                    "Gksjyzam",
                    "Aleman"
                ],
                [
                    "Zcnkzivy",
                    "Artes_Visuales"
                ],
                [
                    "Nbvukocd",
                    "Ciencias_Naturales"
                ],
                [
                    "Qthqkwjq",
                    "Educacion_Fisica"
                ],
                [
                    "Yycaxjta",
                    "Historia"
                ],
                [
                    "Gvkndpxu",
                    "Lenguaje"
                ],
                [
                    "Tiifkdsx",
                    "Matematicas"
                ],
                [
                    "Zcnkzivy",
                    "Musica"
                ],
                [
                    "Zpijftra",
                    "Orientacion"
                ],
                [
                    "Zjszbjef",
                    "Religion"
                ],
                [
                    "Uskngdik",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Oacufynm",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "1C": {
            "0": {},
            "1": [
                [
                    "Artfsbvj",
                    "Aleman"
                ],
                [
                    "Atzgrmcj",
                    "Artes_Visuales"
                ],
                [
                    "Orvyxhyd",
                    "Ciencias_Naturales"
                ],
                [
                    "Mmbudkeu",
                    "Educacion_Fisica"
                ],
                [
                    "Zhlczlpq",
                    "Historia"
                ],
                [
                    "Tiifkdsx",
                    "Lenguaje"
                ],
                [
                    "Uzkjwjne",
                    "Matematicas"
                ],
                [
                    "Xtknjgfi",
                    "Musica"
                ],
                [
                    "Dwsfwtcu",
                    "Orientacion"
                ],
                [
                    "Uvpdhdwa",
                    "Religion"
                ],
                [
                    "Zxozenmu",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Uskngdik",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "1D": {
            "0": {},
            "1": [
                [
                    "Zpijftra",
                    "Aleman"
                ],
                [
                    "Jumijrpx",
                    "Artes_Visuales"
                ],
                [
                    "Ybufanza",
                    "Ciencias_Naturales"
                ],
                [
                    "Xfhyxhmf",
                    "Educacion_Fisica"
                ],
                [
                    "Pwekysoi",
                    "Historia"
                ],
                [
                    "Vkmfgwym",
                    "Lenguaje"
                ],
                [
                    "Lkmhjlav",
                    "Matematicas"
                ],
                [
                    "Suahrayh",
                    "Musica"
                ],
                [
                    "Kgpidnxy",
                    "Orientacion"
                ],
                [
                    "Bjczvdlx",
                    "Religion"
                ],
                [
                    "Eamagaxo",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Xwmgnbka",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "2A": {
            "0": {},
            "1": [
                [
                    "Dlrlhevn",
                    "Aleman"
                ],
                [
                    "Vkmfgwym",
                    "Artes_Visuales"
                ],
                [
                    "Xrgtkdbt",
                    "Ciencias_Naturales"
                ],
                [
                    "Nolmbzqj",
                    "Educacion_Fisica"
                ],
                [
                    "Wrbjwpou",
                    "Historia"
                ],
                [
                    "Enctmbwa",
                    "Lenguaje"
                ],
                [
                    "Artfsbvj",
                    "Matematicas"
                ],
                [
                    "Xfyryhan",
                    "Musica"
                ],
                [
                    "Cjntorhr",
                    "Orientacion"
                ],
                [
                    "Ulvuyjza",
                    "Religion"
                ],
                [
                    "Yycaxjta",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Ktalejxl",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "2B": {
            "0": {},
            "1": [
                [
                    "Cjntorhr",
                    "Aleman"
                ],
                [
                    "Peyaycgc",
                    "Artes_Visuales"
                ],
                [
                    "Ncnqafso",
                    "Ciencias_Naturales"
                ],
                [
                    "Vvfythjg",
                    "Educacion_Fisica"
                ],
                [
                    "Vccyqwgt",
                    "Historia"
                ],
                [
                    "Wrvitfwn",
                    "Lenguaje"
                ],
                [
                    "Ztyjwzin",
                    "Matematicas"
                ],
                [
                    "Cdinnylg",
                    "Musica"
                ],
                [
                    "Mmbudkeu",
                    "Orientacion"
                ],
                [
                    "Lkmhjlav",
                    "Religion"
                ],
                [
                    "Vokwrssi",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Xtknjgfi",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "2C": {
            "0": {},
            "1": [
                [
                    "Cjntorhr",
                    "Aleman"
                ],
                [
                    "Mfrsyvvt",
                    "Artes_Visuales"
                ],
                [
                    "Oacufynm",
                    "Ciencias_Naturales"
                ],
                [
                    "Vccyqwgt",
                    "Educacion_Fisica"
                ],
                [
                    "Vvfythjg",
                    "Historia"
                ],
                [
                    "Jumijrpx",
                    "Lenguaje"
                ],
                [
                    "Ktalejxl",
                    "Matematicas"
                ],
                [
                    "Zxozenmu",
                    "Musica"
                ],
                [
                    "Pwekysoi",
                    "Orientacion"
                ],
                [
                    "Yicoxcly",
                    "Religion"
                ],
                [
                    "Lhhvlhbs",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Bsgruzbz",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "2D": {
            "0": {},
            "1": [
                [
                    "Fkkvumii",
                    "Aleman"
                ],
                [
                    "Enctmbwa",
                    "Artes_Visuales"
                ],
                [
                    "Bstpquhk",
                    "Ciencias_Naturales"
                ],
                [
                    "Wrvitfwn",
                    "Educacion_Fisica"
                ],
                [
                    "Xfhyxhmf",
                    "Historia"
                ],
                [
                    "Peyaycgc",
                    "Lenguaje"
                ],
                [
                    "Trnctbzf",
                    "Matematicas"
                ],
                [
                    "Ilcmctde",
                    "Musica"
                ],
                [
                    "Izhnrdcv",
                    "Orientacion"
                ],
                [
                    "Uskngdik",
                    "Religion"
                ],
                [
                    "Lhhvlhbs",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Wumylfsy",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "3A": {
            "0": {},
            "1": [
                [
                    "Vkmfgwym",
                    "Aleman"
                ],
                [
                    "Mmbudkeu",
                    "Artes_Visuales"
                ],
                [
                    "Xrgtkdbt",
                    "Ciencias_Naturales"
                ],
                [
                    "Orvyxhyd",
                    "Educacion_Fisica"
                ],
                [
                    "Xfyryhan",
                    "Historia"
                ],
                [
                    "Uzkjwjne",
                    "Lenguaje"
                ],
                [
                    "Nolmbzqj",
                    "Matematicas"
                ],
                [
                    "Kgpidnxy",
                    "Musica"
                ],
                [
                    "Artfsbvj",
                    "Orientacion"
                ],
                [
                    "Fswbqxvq",
                    "Religion"
                ],
                [
                    "Artfsbvj",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Peyaycgc",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "3B": {
            "0": {},
            "1": [
                [
                    "Jjjbjxan",
                    "Aleman"
                ],
                [
                    "Zxozenmu",
                    "Artes_Visuales"
                ],
                [
                    "Dkcpfgmz",
                    "Ciencias_Naturales"
                ],
                [
                    "Ycaeozob",
                    "Educacion_Fisica"
                ],
                [
                    "Wrbjwpou",
                    "Historia"
                ],
                [
                    "Dwivygdq",
                    "Lenguaje"
                ],
                [
                    "Nbvukocd",
                    "Matematicas"
                ],
                [
                    "Weofvsvu",
                    "Musica"
                ],
                [
                    "Atzgrmcj",
                    "Orientacion"
                ],
                [
                    "Xfhyxhmf",
                    "Religion"
                ],
                [
                    "Jumijrpx",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Dkcpfgmz",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "3C": {
            "0": {},
            "1": [
                [
                    "Mfrsyvvt",
                    "Aleman"
                ],
                [
                    "Qmxargmc",
                    "Artes_Visuales"
                ],
                [
                    "Cdnujdgy",
                    "Ciencias_Naturales"
                ],
                [
                    "Weofvsvu",
                    "Educacion_Fisica"
                ],
                [
                    "Uskngdik",
                    "Historia"
                ],
                [
                    "Xwmgnbka",
                    "Lenguaje"
                ],
                [
                    "Eyygrfpx",
                    "Matematicas"
                ],
                [
                    "Izdefgii",
                    "Musica"
                ],
                [
                    "Uvpdhdwa",
                    "Orientacion"
                ],
                [
                    "Pfqfrspa",
                    "Religion"
                ],
                [
                    "Bjczvdlx",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Hbgzrbec",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "3D": {
            "0": {},
            "1": [
                [
                    "Pwekysoi",
                    "Aleman"
                ],
                [
                    "Zjszbjef",
                    "Artes_Visuales"
                ],
                [
                    "Weofvsvu",
                    "Ciencias_Naturales"
                ],
                [
                    "Xfyryhan",
                    "Educacion_Fisica"
                ],
                [
                    "Uzkjwjne",
                    "Historia"
                ],
                [
                    "Trnctbzf",
                    "Lenguaje"
                ],
                [
                    "Bsgruzbz",
                    "Matematicas"
                ],
                [
                    "Eamagaxo",
                    "Musica"
                ],
                [
                    "Xrgtkdbt",
                    "Orientacion"
                ],
                [
                    "Bzbkyeqh",
                    "Religion"
                ],
                [
                    "Dwivygdq",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Atkvuhru",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "4A": {
            "0": {},
            "1": [
                [
                    "Zjszbjef",
                    "Aleman"
                ],
                [
                    "Ukpzxoex",
                    "Artes_Visuales"
                ],
                [
                    "Ekclmkxn",
                    "Ciencias_Naturales"
                ],
                [
                    "Kdfpngqg",
                    "Educacion_Fisica"
                ],
                [
                    "Fjmedzyi",
                    "Historia"
                ],
                [
                    "Kgpidnxy",
                    "Lenguaje"
                ],
                [
                    "Uvpdhdwa",
                    "Matematicas"
                ],
                [
                    "Jjjbjxan",
                    "Musica"
                ],
                [
                    "Zcnkzivy",
                    "Orientacion"
                ],
                [
                    "Uvpdhdwa",
                    "Religion"
                ],
                [
                    "Zxozenmu",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Xulhdtye",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "4B": {
            "0": {},
            "1": [
                [
                    "Skzvkdfn",
                    "Aleman"
                ],
                [
                    "Ztyjwzin",
                    "Artes_Visuales"
                ],
                [
                    "Cdajgsjh",
                    "Ciencias_Naturales"
                ],
                [
                    "Ylbruxtg",
                    "Educacion_Fisica"
                ],
                [
                    "Nncolmnk",
                    "Historia"
                ],
                [
                    "Zcnkzivy",
                    "Lenguaje"
                ],
                [
                    "Ekclmkxn",
                    "Matematicas"
                ],
                [
                    "Uzkjwjne",
                    "Musica"
                ],
                [
                    "Zcnkzivy",
                    "Orientacion"
                ],
                [
                    "Ulvuyjza",
                    "Religion"
                ],
                [
                    "Xfyryhan",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Tiifkdsx",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "4C": {
            "0": {},
            "1": [
                [
                    "Xwmgnbka",
                    "Aleman"
                ],
                [
                    "Trnctbzf",
                    "Artes_Visuales"
                ],
                [
                    "Zcnkzivy",
                    "Ciencias_Naturales"
                ],
                [
                    "Eyygrfpx",
                    "Educacion_Fisica"
                ],
                [
                    "Fswbqxvq",
                    "Historia"
                ],
                [
                    "Fswbqxvq",
                    "Lenguaje"
                ],
                [
                    "Lhguzsdp",
                    "Matematicas"
                ],
                [
                    "Uskngdik",
                    "Musica"
                ],
                [
                    "Xrgtkdbt",
                    "Orientacion"
                ],
                [
                    "Fjmedzyi",
                    "Religion"
                ],
                [
                    "Ekclmkxn",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Ulvuyjza",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "4D": {
            "0": {},
            "1": [
                [
                    "Pxymekhf",
                    "Aleman"
                ],
                [
                    "Cigviwln",
                    "Artes_Visuales"
                ],
                [
                    "Onyodhku",
                    "Ciencias_Naturales"
                ],
                [
                    "Xfhyxhmf",
                    "Educacion_Fisica"
                ],
                [
                    "Hcaebpbd",
                    "Historia"
                ],
                [
                    "Cdajgsjh",
                    "Lenguaje"
                ],
                [
                    "Svixsrbd",
                    "Matematicas"
                ],
                [
                    "Ilcmctde",
                    "Musica"
                ],
                [
                    "Rlybywxl",
                    "Orientacion"
                ],
                [
                    "Pfqfrspa",
                    "Religion"
                ],
                [
                    "Pwekysoi",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Fjmedzyi",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "5A": {
            "0": {},
            "1": [
                [
                    "Ukpzxoex",
                    "Aleman"
                ],
                [
                    "Vdlrplrh",
                    "Artes_Visuales"
                ],
                [
                    "Ktalejxl",
                    "Ciencias_Naturales"
                ],
                [
                    "Tiifkdsx",
                    "Educacion_Fisica"
                ],
                [
                    "Nbvukocd",
                    "Geografia"
                ],
                [
                    "Kbksxvdi",
                    "Historia"
                ],
                [
                    "Bzbkyeqh",
                    "Ingles"
                ],
                [
                    "Hbgzrbec",
                    "Lenguaje"
                ],
                [
                    "Nncolmnk",
                    "Matematicas"
                ],
                [
                    "Mmbudkeu",
                    "Musica"
                ],
                [
                    "Izhnrdcv",
                    "Orientacion"
                ],
                [
                    "Yiqzsxsm",
                    "Religion"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "5B": {
            "0": {},
            "1": [
                [
                    "Hgcsbhrt",
                    "Aleman"
                ],
                [
                    "Zhlczlpq",
                    "Artes_Visuales"
                ],
                [
                    "Zxozenmu",
                    "Ciencias_Naturales"
                ],
                [
                    "Trnctbzf",
                    "Educacion_Fisica"
                ],
                [
                    "Izdefgii",
                    "Geografia"
                ],
                [
                    "Rlybywxl",
                    "Historia"
                ],
                [
                    "Oueurwlr",
                    "Ingles"
                ],
                [
                    "Mjelvrnp",
                    "Lenguaje"
                ],
                [
                    "Ipgxqoqq",
                    "Matematicas"
                ],
                [
                    "Cigviwln",
                    "Musica"
                ],
                [
                    "Gvkndpxu",
                    "Orientacion"
                ],
                [
                    "Jxlritwl",
                    "Religion"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "5C": {
            "0": {},
            "1": [
                [
                    "Wywsbftg",
                    "Aleman"
                ],
                [
                    "Vvfythjg",
                    "Artes_Visuales"
                ],
                [
                    "Xtknjgfi",
                    "Ciencias_Naturales"
                ],
                [
                    "Mmbudkeu",
                    "Educacion_Fisica"
                ],
                [
                    "Wvmqroil",
                    "Geografia"
                ],
                [
                    "Sllrohmp",
                    "Historia"
                ],
                [
                    "Noayogmf",
                    "Ingles"
                ],
                [
                    "Mbkhrirw",
                    "Lenguaje"
                ],
                [
                    "Kvqamngw",
                    "Matematicas"
                ],
                [
                    "Gksjyzam",
                    "Musica"
                ],
                [
                    "Lwrkdqhz",
                    "Orientacion"
                ],
                [
                    "Pwekysoi",
                    "Religion"
                ],
                [
                    "Dtqrwfpf",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "5D": {
            "0": {},
            "1": [
                [
                    "Zxozenmu",
                    "Aleman"
                ],
                [
                    "Qthqkwjq",
                    "Artes_Visuales"
                ],
                [
                    "Vccyqwgt",
                    "Ciencias_Naturales"
                ],
                [
                    "Pfqfrspa",
                    "Educacion_Fisica"
                ],
                [
                    "Ylbruxtg",
                    "Geografia"
                ],
                [
                    "Yycaxjta",
                    "Historia"
                ],
                [
                    "Lkmhjlav",
                    "Ingles"
                ],
                [
                    "Izhnrdcv",
                    "Lenguaje"
                ],
                [
                    "Qmxargmc",
                    "Matematicas"
                ],
                [
                    "Ncnqafso",
                    "Musica"
                ],
                [
                    "Nolmbzqj",
                    "Orientacion"
                ],
                [
                    "Pxymekhf",
                    "Religion"
                ],
                [
                    "Ipgxqoqq",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "6A": {
            "0": {},
            "1": [
                [
                    "Vccyqwgt",
                    "Aleman"
                ],
                [
                    "Fjmedzyi",
                    "Artes_Visuales"
                ],
                [
                    "Zhlczlpq",
                    "Ciencias_Naturales"
                ],
                [
                    "Vkmfgwym",
                    "Educacion_Fisica"
                ],
                [
                    "Zjszbjef",
                    "Historia"
                ],
                [
                    "Kvqamngw",
                    "Lenguaje"
                ],
                [
                    "Yicoxcly",
                    "Matematicas"
                ],
                [
                    "Ilcmctde",
                    "Musica"
                ],
                [
                    "Fpqpcfbq",
                    "Orientacion"
                ],
                [
                    "Artfsbvj",
                    "Religion"
                ],
                [
                    "Atkvuhru",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Uskngdik",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "6B": {
            "0": {},
            "1": [
                [
                    "Onyodhku",
                    "Aleman"
                ],
                [
                    "Vvfythjg",
                    "Artes_Visuales"
                ],
                [
                    "Wvmqroil",
                    "Ciencias_Naturales"
                ],
                [
                    "Mfrsyvvt",
                    "Educacion_Fisica"
                ],
                [
                    "Ulvuyjza",
                    "Historia"
                ],
                [
                    "Xtknjgfi",
                    "Lenguaje"
                ],
                [
                    "Wvmqroil",
                    "Matematicas"
                ],
                [
                    "Tiifkdsx",
                    "Musica"
                ],
                [
                    "Atzgrmcj",
                    "Orientacion"
                ],
                [
                    "Xrgtkdbt",
                    "Religion"
                ],
                [
                    "Txhbhqio",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Cjntorhr",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "6C": {
            "0": {},
            "1": [
                [
                    "Ilcmctde",
                    "Aleman"
                ],
                [
                    "Nncolmnk",
                    "Artes_Visuales"
                ],
                [
                    "Mlvafpyt",
                    "Ciencias_Naturales"
                ],
                [
                    "Svixsrbd",
                    "Educacion_Fisica"
                ],
                [
                    "Btutuqlu",
                    "Historia"
                ],
                [
                    "Ilcmctde",
                    "Lenguaje"
                ],
                [
                    "Wrvitfwn",
                    "Matematicas"
                ],
                [
                    "Svixsrbd",
                    "Musica"
                ],
                [
                    "Fpqpcfbq",
                    "Orientacion"
                ],
                [
                    "Yiqzsxsm",
                    "Religion"
                ],
                [
                    "Yiqzsxsm",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Izxqvpvk",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "6D": {
            "0": {},
            "1": [
                [
                    "Ktalejxl",
                    "Aleman"
                ],
                [
                    "Weofvsvu",
                    "Artes_Visuales"
                ],
                [
                    "Igijmzip",
                    "Ciencias_Naturales"
                ],
                [
                    "Uvpdhdwa",
                    "Educacion_Fisica"
                ],
                [
                    "Ychzycdi",
                    "Historia"
                ],
                [
                    "Apkctzml",
                    "Lenguaje"
                ],
                [
                    "Upmsvroi",
                    "Matematicas"
                ],
                [
                    "Eieyagjc",
                    "Musica"
                ],
                [
                    "Rlybywxl",
                    "Orientacion"
                ],
                [
                    "Oueurwlr",
                    "Religion"
                ],
                [
                    "Cigviwln",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "Uskngdik",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "7A": {
            "0": {},
            "1": [
                [
                    "Eieyagjc",
                    "Aleman"
                ],
                [
                    "Uskngdik",
                    "Biologia"
                ],
                [
                    "Bzbkyeqh",
                    "Educacion_Fisica"
                ],
                [
                    "Upmsvroi",
                    "Fisica"
                ],
                [
                    "Pwekysoi",
                    "Historia"
                ],
                [
                    "Fjmedzyi",
                    "Ingles"
                ],
                [
                    "Fkkvumii",
                    "Lenguaje"
                ],
                [
                    "Atkvuhru",
                    "Matematicas"
                ],
                [
                    "Sllrohmp",
                    "Musica"
                ],
                [
                    "Uskngdik",
                    "Orientacion"
                ],
                [
                    "Cigviwln",
                    "Quimica"
                ],
                [
                    "Dwsfwtcu",
                    "Religion"
                ],
                [
                    "Onyodhku",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "7B": {
            "0": {},
            "1": [
                [
                    "Yycaxjta",
                    "Aleman"
                ],
                [
                    "Kgpidnxy",
                    "Biologia"
                ],
                [
                    "Oacufynm",
                    "Educacion_Fisica"
                ],
                [
                    "Izdefgii",
                    "Fisica"
                ],
                [
                    "Yokgsgdf",
                    "Historia"
                ],
                [
                    "Ycaeozob",
                    "Ingles"
                ],
                [
                    "Ipgxqoqq",
                    "Lenguaje"
                ],
                [
                    "Wywsbftg",
                    "Matematicas"
                ],
                [
                    "Rlybywxl",
                    "Musica"
                ],
                [
                    "Xwmgnbka",
                    "Orientacion"
                ],
                [
                    "Bstpquhk",
                    "Quimica"
                ],
                [
                    "Svixsrbd",
                    "Religion"
                ],
                [
                    "Xulhdtye",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "7C": {
            "0": {},
            "1": [
                [
                    "Skzvkdfn",
                    "Aleman"
                ],
                [
                    "Atkvuhru",
                    "Biologia"
                ],
                [
                    "Lwrkdqhz",
                    "Educacion_Fisica"
                ],
                [
                    "Fpqpcfbq",
                    "Fisica"
                ],
                [
                    "Wrvitfwn",
                    "Historia"
                ],
                [
                    "Ulvuyjza",
                    "Ingles"
                ],
                [
                    "Ychzycdi",
                    "Lenguaje"
                ],
                [
                    "Atkvuhru",
                    "Matematicas"
                ],
                [
                    "Eyygrfpx",
                    "Musica"
                ],
                [
                    "Bsgruzbz",
                    "Orientacion"
                ],
                [
                    "Xfyryhan",
                    "Quimica"
                ],
                [
                    "Nncolmnk",
                    "Religion"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "7D": {
            "0": {},
            "1": [
                [
                    "Txhbhqio",
                    "Aleman"
                ],
                [
                    "Hgcsbhrt",
                    "Biologia"
                ],
                [
                    "Vvfythjg",
                    "Educacion_Fisica"
                ],
                [
                    "Bsgruzbz",
                    "Fisica"
                ],
                [
                    "Sgnzggdl",
                    "Historia"
                ],
                [
                    "Xfyryhan",
                    "Ingles"
                ],
                [
                    "Dlrlhevn",
                    "Lenguaje"
                ],
                [
                    "Apkctzml",
                    "Matematicas"
                ],
                [
                    "Qmxargmc",
                    "Musica"
                ],
                [
                    "Yicoxcly",
                    "Orientacion"
                ],
                [
                    "Orvyxhyd",
                    "Quimica"
                ],
                [
                    "Vokwrssi",
                    "Religion"
                ],
                [
                    "Pfqfrspa",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "8A": {
            "0": {},
            "1": [
                [
                    "Jjjbjxan",
                    "Aleman"
                ],
                [
                    "Btutuqlu",
                    "Biologia"
                ],
                [
                    "Zhlczlpq",
                    "Educacion_Fisica"
                ],
                [
                    "Apkctzml",
                    "Fisica"
                ],
                [
                    "Jxlritwl",
                    "Historia"
                ],
                [
                    "Bjczvdlx",
                    "Ingles"
                ],
                [
                    "Zpijftra",
                    "Lenguaje"
                ],
                [
                    "Wumylfsy",
                    "Matematicas"
                ],
                [
                    "Wumylfsy",
                    "Musica"
                ],
                [
                    "Mbkhrirw",
                    "Orientacion"
                ],
                [
                    "Wsaytkdx",
                    "Quimica"
                ],
                [
                    "Hcaebpbd",
                    "Religion"
                ],
                [
                    "Gvkndpxu",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "8B": {
            "0": {},
            "1": [
                [
                    "Dtqrwfpf",
                    "Aleman"
                ],
                [
                    "Dwsfwtcu",
                    "Biologia"
                ],
                [
                    "Rlybywxl",
                    "Educacion_Fisica"
                ],
                [
                    "Xfhyxhmf",
                    "Fisica"
                ],
                [
                    "Suahrayh",
                    "Historia"
                ],
                [
                    "Mfrsyvvt",
                    "Ingles"
                ],
                [
                    "Tqeiwlki",
                    "Lenguaje"
                ],
                [
                    "Txhbhqio",
                    "Matematicas"
                ],
                [
                    "Ylbruxtg",
                    "Musica"
                ],
                [
                    "Orvyxhyd",
                    "Orientacion"
                ],
                [
                    "Dwsfwtcu",
                    "Quimica"
                ],
                [
                    "Enctmbwa",
                    "Religion"
                ],
                [
                    "Svixsrbd",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "8C": {
            "0": {},
            "1": [
                [
                    "Jumijrpx",
                    "Aleman"
                ],
                [
                    "Yiqzsxsm",
                    "Biologia"
                ],
                [
                    "Wvmqroil",
                    "Educacion_Fisica"
                ],
                [
                    "Oueurwlr",
                    "Fisica"
                ],
                [
                    "Nbvukocd",
                    "Historia"
                ],
                [
                    "Ycaeozob",
                    "Ingles"
                ],
                [
                    "Fswbqxvq",
                    "Lenguaje"
                ],
                [
                    "Wywsbftg",
                    "Matematicas"
                ],
                [
                    "Atzgrmcj",
                    "Musica"
                ],
                [
                    "Cigviwln",
                    "Orientacion"
                ],
                [
                    "Zcnkzivy",
                    "Quimica"
                ],
                [
                    "Tqeiwlki",
                    "Religion"
                ],
                [
                    "Ulvuyjza",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "8D": {
            "0": {},
            "1": [
                [
                    "Dlrlhevn",
                    "Aleman"
                ],
                [
                    "Eyygrfpx",
                    "Biologia"
                ],
                [
                    "Atzgrmcj",
                    "Educacion_Fisica"
                ],
                [
                    "Uskngdik",
                    "Fisica"
                ],
                [
                    "Xwmgnbka",
                    "Historia"
                ],
                [
                    "Vdlrplrh",
                    "Ingles"
                ],
                [
                    "Xtknjgfi",
                    "Lenguaje"
                ],
                [
                    "Hgcsbhrt",
                    "Matematicas"
                ],
                [
                    "Uzkjwjne",
                    "Musica"
                ],
                [
                    "Orvyxhyd",
                    "Orientacion"
                ],
                [
                    "Cjntorhr",
                    "Quimica"
                ],
                [
                    "Eieyagjc",
                    "Religion"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IA": {
            "0": {},
            "1": [
                [
                    "Vokwrssi",
                    "Aleman"
                ],
                [
                    "Dtqrwfpf",
                    "Biologia"
                ],
                [
                    "Oacufynm",
                    "Educacion_Fisica"
                ],
                [
                    "Xulhdtye",
                    "Fisica"
                ],
                [
                    "Wvmqroil",
                    "Historia"
                ],
                [
                    "Igijmzip",
                    "Ingles"
                ],
                [
                    "Cdinnylg",
                    "Lenguaje"
                ],
                [
                    "Bstpquhk",
                    "Matematicas"
                ],
                [
                    "Zhlczlpq",
                    "Musica"
                ],
                [
                    "Xfyryhan",
                    "Orientacion"
                ],
                [
                    "Ycaeozob",
                    "Quimica"
                ],
                [
                    "Ylbruxtg",
                    "Religion"
                ],
                [
                    "Kdfpngqg",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IB": {
            "0": {},
            "1": [
                [
                    "Ylbruxtg",
                    "Aleman"
                ],
                [
                    "Zhlczlpq",
                    "Biologia"
                ],
                [
                    "Mfrsyvvt",
                    "Educacion_Fisica"
                ],
                [
                    "Rlybywxl",
                    "Fisica"
                ],
                [
                    "Bjczvdlx",
                    "Historia"
                ],
                [
                    "Dwsfwtcu",
                    "Ingles"
                ],
                [
                    "Sgnzggdl",
                    "Lenguaje"
                ],
                [
                    "Hbgzrbec",
                    "Matematicas"
                ],
                [
                    "Eamagaxo",
                    "Musica"
                ],
                [
                    "Cdajgsjh",
                    "Orientacion"
                ],
                [
                    "Ybufanza",
                    "Quimica"
                ],
                [
                    "Atzgrmcj",
                    "Religion"
                ],
                [
                    "Wrbjwpou",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IC": {
            "0": {},
            "1": [
                [
                    "Qmxargmc",
                    "Aleman"
                ],
                [
                    "Pfqfrspa",
                    "Biologia"
                ],
                [
                    "Zpijftra",
                    "Educacion_Fisica"
                ],
                [
                    "Vvfythjg",
                    "Fisica"
                ],
                [
                    "Dtqrwfpf",
                    "Historia"
                ],
                [
                    "Pxymekhf",
                    "Ingles"
                ],
                [
                    "Kvqamngw",
                    "Lenguaje"
                ],
                [
                    "Cdinnylg",
                    "Matematicas"
                ],
                [
                    "Mjelvrnp",
                    "Musica"
                ],
                [
                    "Nbvukocd",
                    "Orientacion"
                ],
                [
                    "Eyygrfpx",
                    "Quimica"
                ],
                [
                    "Ychzycdi",
                    "Religion"
                ],
                [
                    "Vdlrplrh",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "ID": {
            "0": {},
            "1": [
                [
                    "Mlvafpyt",
                    "Aleman"
                ],
                [
                    "Vccyqwgt",
                    "Biologia"
                ],
                [
                    "Zxozenmu",
                    "Educacion_Fisica"
                ],
                [
                    "Xfyryhan",
                    "Fisica"
                ],
                [
                    "Vokwrssi",
                    "Historia"
                ],
                [
                    "Vokwrssi",
                    "Ingles"
                ],
                [
                    "Lhguzsdp",
                    "Lenguaje"
                ],
                [
                    "Bsgruzbz",
                    "Matematicas"
                ],
                [
                    "Artfsbvj",
                    "Musica"
                ],
                [
                    "Rlybywxl",
                    "Orientacion"
                ],
                [
                    "Lwrkdqhz",
                    "Quimica"
                ],
                [
                    "Dlrlhevn",
                    "Religion"
                ],
                [
                    "Hbgzrbec",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IIA": {
            "0": {},
            "1": [
                [
                    "Mjelvrnp",
                    "Aleman"
                ],
                [
                    "Atzgrmcj",
                    "Biologia"
                ],
                [
                    "Pxymekhf",
                    "Educacion_Fisica"
                ],
                [
                    "Lkmhjlav",
                    "Fisica"
                ],
                [
                    "Nolmbzqj",
                    "Historia"
                ],
                [
                    "Ekclmkxn",
                    "Ingles"
                ],
                [
                    "Txhbhqio",
                    "Lenguaje"
                ],
                [
                    "Kbksxvdi",
                    "Matematicas"
                ],
                [
                    "Hbgzrbec",
                    "Musica"
                ],
                [
                    "Orvyxhyd",
                    "Orientacion"
                ],
                [
                    "Tqeiwlki",
                    "Quimica"
                ],
                [
                    "Gvkndpxu",
                    "Religion"
                ],
                [
                    "Nolmbzqj",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IIB": {
            "0": {},
            "1": [
                [
                    "Bjczvdlx",
                    "Aleman"
                ],
                [
                    "Artfsbvj",
                    "Biologia"
                ],
                [
                    "Vdlrplrh",
                    "Educacion_Fisica"
                ],
                [
                    "Xfhyxhmf",
                    "Fisica"
                ],
                [
                    "Eieyagjc",
                    "Historia"
                ],
                [
                    "Hcaebpbd",
                    "Ingles"
                ],
                [
                    "Wrbjwpou",
                    "Lenguaje"
                ],
                [
                    "Tqeiwlki",
                    "Matematicas"
                ],
                [
                    "Btutuqlu",
                    "Musica"
                ],
                [
                    "Wumylfsy",
                    "Orientacion"
                ],
                [
                    "Kbksxvdi",
                    "Quimica"
                ],
                [
                    "Hgcsbhrt",
                    "Religion"
                ],
                [
                    "Eamagaxo",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IIC": {
            "0": {},
            "1": [
                [
                    "Izhnrdcv",
                    "Aleman"
                ],
                [
                    "Vdlrplrh",
                    "Biologia"
                ],
                [
                    "Dwsfwtcu",
                    "Educacion_Fisica"
                ],
                [
                    "Bstpquhk",
                    "Fisica"
                ],
                [
                    "Enctmbwa",
                    "Historia"
                ],
                [
                    "Apkctzml",
                    "Ingles"
                ],
                [
                    "Hcaebpbd",
                    "Lenguaje"
                ],
                [
                    "Jxlritwl",
                    "Matematicas"
                ],
                [
                    "Ztyjwzin",
                    "Musica"
                ],
                [
                    "Pfqfrspa",
                    "Orientacion"
                ],
                [
                    "Rlybywxl",
                    "Quimica"
                ],
                [
                    "Gvkndpxu",
                    "Religion"
                ],
                [
                    "Dwsfwtcu",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IID": {
            "0": {},
            "1": [
                [
                    "Pfqfrspa",
                    "Aleman"
                ],
                [
                    "Ipgxqoqq",
                    "Biologia"
                ],
                [
                    "Oacufynm",
                    "Educacion_Fisica"
                ],
                [
                    "Atzgrmcj",
                    "Fisica"
                ],
                [
                    "Onyodhku",
                    "Historia"
                ],
                [
                    "Lwrkdqhz",
                    "Ingles"
                ],
                [
                    "Ychzycdi",
                    "Lenguaje"
                ],
                [
                    "Suahrayh",
                    "Matematicas"
                ],
                [
                    "Fpqpcfbq",
                    "Musica"
                ],
                [
                    "Wrbjwpou",
                    "Orientacion"
                ],
                [
                    "Mbkhrirw",
                    "Quimica"
                ],
                [
                    "Eyygrfpx",
                    "Religion"
                ],
                [
                    "Ukpzxoex",
                    "Tecnologia"
                ]
            ],
            "M": []
        },
        "IIIA": {
            "0": {},
            "1": [
                [
                    "Wumylfsy",
                    "Aleman"
                ],
                [
                    "Bjczvdlx",
                    "Artes_Visuales"
                ],
                [
                    "Yycaxjta",
                    "Biologia"
                ],
                [
                    "Oacufynm",
                    "Ciencias_Sociales"
                ],
                [
                    "Orvyxhyd",
                    "Consejo_de_Curso"
                ],
                [
                    "Xfyryhan",
                    "Educacion_Fisica"
                ],
                [
                    "Gvkndpxu",
                    "Fisica"
                ],
                [
                    "Ztyjwzin",
                    "G2"
                ],
                [
                    "Rlybywxl",
                    "G3"
                ],
                [
                    "Kgpidnxy",
                    "Geografia"
                ],
                [
                    "Ztyjwzin",
                    "Historia"
                ],
                [
                    "Qthqkwjq",
                    "Ingles"
                ],
                [
                    "Ncnqafso",
                    "Lenguaje"
                ],
                [
                    "Ekclmkxn",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IIIB": {
            "0": {},
            "1": [
                [
                    "Xrgtkdbt",
                    "Aleman"
                ],
                [
                    "Ycaeozob",
                    "Artes_Visuales"
                ],
                [
                    "Ybufanza",
                    "Biologia"
                ],
                [
                    "Eyygrfpx",
                    "Ciencias_Sociales"
                ],
                [
                    "Svixsrbd",
                    "Consejo_de_Curso"
                ],
                [
                    "Mjelvrnp",
                    "Educacion_Fisica"
                ],
                [
                    "Suahrayh",
                    "Fisica"
                ],
                [
                    "Kbksxvdi",
                    "G2"
                ],
                [
                    "Mmbudkeu",
                    "G3"
                ],
                [
                    "Mfrsyvvt",
                    "Geografia"
                ],
                [
                    "Wrbjwpou",
                    "Historia"
                ],
                [
                    "Mbkhrirw",
                    "Ingles"
                ],
                [
                    "Oueurwlr",
                    "Lenguaje"
                ],
                [
                    "Yokgsgdf",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IIIC": {
            "0": {},
            "1": [
                [
                    "Yicoxcly",
                    "Aleman"
                ],
                [
                    "Ulvuyjza",
                    "Artes_Visuales"
                ],
                [
                    "Dtqrwfpf",
                    "Biologia"
                ],
                [
                    "Bstpquhk",
                    "Ciencias_Sociales"
                ],
                [
                    "Ekclmkxn",
                    "Consejo_de_Curso"
                ],
                [
                    "Kgpidnxy",
                    "Educacion_Fisica"
                ],
                [
                    "Vokwrssi",
                    "Fisica"
                ],
                [
                    "Noayogmf",
                    "G2"
                ],
                [
                    "Jxlritwl",
                    "G3"
                ],
                [
                    "Izdefgii",
                    "Geografia"
                ],
                [
                    "Dkcpfgmz",
                    "Historia"
                ],
                [
                    "Ipgxqoqq",
                    "Ingles"
                ],
                [
                    "Rlybywxl",
                    "Lenguaje"
                ],
                [
                    "Bstpquhk",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IIID": {
            "0": {},
            "1": [
                [
                    "Ukpzxoex",
                    "Aleman"
                ],
                [
                    "Fjmedzyi",
                    "Artes_Visuales"
                ],
                [
                    "Cdajgsjh",
                    "Biologia"
                ],
                [
                    "Zhlczlpq",
                    "Ciencias_Sociales"
                ],
                [
                    "Dwsfwtcu",
                    "Consejo_de_Curso"
                ],
                [
                    "Cdajgsjh",
                    "Educacion_Fisica"
                ],
                [
                    "Dwsfwtcu",
                    "Fisica"
                ],
                [
                    "Igijmzip",
                    "G2"
                ],
                [
                    "Cdajgsjh",
                    "G3"
                ],
                [
                    "Nipudbji",
                    "Geografia"
                ],
                [
                    "Fpqpcfbq",
                    "Historia"
                ],
                [
                    "Xulhdtye",
                    "Ingles"
                ],
                [
                    "Upmsvroi",
                    "Lenguaje"
                ],
                [
                    "Dwivygdq",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IVA": {
            "0": {},
            "1": [
                [
                    "Yiqzsxsm",
                    "Aleman"
                ],
                [
                    "Vkmfgwym",
                    "Artes_Visuales"
                ],
                [
                    "Pwekysoi",
                    "Biologia"
                ],
                [
                    "Cjntorhr",
                    "Ciencias_Sociales"
                ],
                [
                    "Orvyxhyd",
                    "Consejo_de_Curso"
                ],
                [
                    "Ncnqafso",
                    "Educacion_Fisica"
                ],
                [
                    "Orvyxhyd",
                    "Fisica"
                ],
                [
                    "Nncolmnk",
                    "G2"
                ],
                [
                    "Hgcsbhrt",
                    "G3"
                ],
                [
                    "Svixsrbd",
                    "Geografia"
                ],
                [
                    "Weofvsvu",
                    "Historia"
                ],
                [
                    "Jumijrpx",
                    "Ingles"
                ],
                [
                    "Dwivygdq",
                    "Lenguaje"
                ],
                [
                    "Cdinnylg",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IVB": {
            "0": {},
            "1": [
                [
                    "Mlvafpyt",
                    "Aleman"
                ],
                [
                    "Xfhyxhmf",
                    "Artes_Visuales"
                ],
                [
                    "Jjjbjxan",
                    "Biologia"
                ],
                [
                    "Fkkvumii",
                    "Ciencias_Sociales"
                ],
                [
                    "Yiqzsxsm",
                    "Consejo_de_Curso"
                ],
                [
                    "Kbksxvdi",
                    "Educacion_Fisica"
                ],
                [
                    "Xulhdtye",
                    "Fisica"
                ],
                [
                    "Zhlczlpq",
                    "G2"
                ],
                [
                    "Vccyqwgt",
                    "G3"
                ],
                [
                    "Qmxargmc",
                    "Geografia"
                ],
                [
                    "Ylbruxtg",
                    "Historia"
                ],
                [
                    "Qthqkwjq",
                    "Ingles"
                ],
                [
                    "Peyaycgc",
                    "Lenguaje"
                ],
                [
                    "Yiqzsxsm",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IVC": {
            "0": {},
            "1": [
                [
                    "Izhnrdcv",
                    "Aleman"
                ],
                [
                    "Ycaeozob",
                    "Artes_Visuales"
                ],
                [
                    "Dwivygdq",
                    "Biologia"
                ],
                [
                    "Onyodhku",
                    "Ciencias_Sociales"
                ],
                [
                    "Orvyxhyd",
                    "Consejo_de_Curso"
                ],
                [
                    "Lhguzsdp",
                    "Educacion_Fisica"
                ],
                [
                    "Upmsvroi",
                    "Fisica"
                ],
                [
                    "Nipudbji",
                    "G2"
                ],
                [
                    "Sllrohmp",
                    "G3"
                ],
                [
                    "Cigviwln",
                    "Geografia"
                ],
                [
                    "Oacufynm",
                    "Historia"
                ],
                [
                    "Ukpzxoex",
                    "Ingles"
                ],
                [
                    "Igijmzip",
                    "Lenguaje"
                ],
                [
                    "Qthqkwjq",
                    "Matematicas"
                ]
            ],
            "M": []
        },
        "IVD": {
            "0": {},
            "1": [
                [
                    "Ncnqafso",
                    "Aleman"
                ],
                [
                    "Xfhyxhmf",
                    "Artes_Visuales"
                ],
                [
                    "Ybufanza",
                    "Biologia"
                ],
                [
                    "Mmbudkeu",
                    "Ciencias_Sociales"
                ],
                [
                    "Fjmedzyi",
                    "Consejo_de_Curso"
                ],
                [
                    "Xrgtkdbt",
                    "Educacion_Fisica"
                ],
                [
                    "Atzgrmcj",
                    "Fisica"
                ],
                [
                    "Yicoxcly",
                    "G2"
                ],
                [
                    "Ktalejxl",
                    "G3"
                ],
                [
                    "Fpqpcfbq",
                    "Geografia"
                ],
                [
                    "Oacufynm",
                    "Historia"
                ],
                [
                    "Yycaxjta",
                    "Ingles"
                ],
                [
                    "Lhguzsdp",
                    "Lenguaje"
                ],
                [
                    "Zpijftra",
                    "Matematicas"
                ]
            ],
            "M": []
        }
    },
    "ramos_por_curso": {
        "1A": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "1B": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "1C": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "1D": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "2A": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "2B": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "2C": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "2D": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "3A": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "3B": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "3C": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "3D": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "4A": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "4B": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "4C": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "4D": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "5A": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "5B": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "5C": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "5D": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "6A": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "6B": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "6C": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "6D": {
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Educacion_Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 7,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Naturales": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Taller_Comprension_Lectora": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "7A": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "7B": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "7C": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "7D": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "8A": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "8B": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "8C": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "8D": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IA": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IB": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IC": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "ID": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIA": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIB": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIC": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IID": {
            "Matematicas": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Orientacion": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Religion": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Aleman": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Lenguaje": {
                "modulos_semanales": 6,
                "maximo_modulos_diarios": 2
            },
            "Tecnologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Quimica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Historia": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Musica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIIA": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIIB": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIIC": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IIID": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IVA": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IVB": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IVC": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        },
        "IVD": {
            "Lenguaje": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Matematicas": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Historia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 2
            },
            "Ciencias_Sociales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Artes_Visuales": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Educacion_Fisica": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            },
            "Consejo_de_Curso": {
                "modulos_semanales": 1,
                "maximo_modulos_diarios": 1
            },
            "Ingles": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 1
            },
            "Geografia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "Biologia": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G2": {
                "modulos_semanales": 4,
                "maximo_modulos_diarios": 2
            },
            "Aleman": {
                "modulos_semanales": 5,
                "maximo_modulos_diarios": 2
            },
            "Fisica": {
                "modulos_semanales": 3,
                "maximo_modulos_diarios": 1
            },
            "G3": {
                "modulos_semanales": 2,
                "maximo_modulos_diarios": 2
            }
        }
    },
    "carga_profesores": {
        "Apkctzml": {
            "1": [
                [
                    "6D",
                    "Lenguaje"
                ],
                [
                    "7D",
                    "Matematicas"
                ],
                [
                    "8A",
                    "Fisica"
                ],
                [
                    "IIC",
                    "Ingles"
                ]
            ]
        },
        "Artfsbvj": {
            "1": [
                [
                    "1C",
                    "Aleman"
                ],
                [
                    "2A",
                    "Matematicas"
                ],
                [
                    "3A",
                    "Orientacion"
                ],
                [
                    "3A",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "6A",
                    "Religion"
                ],
                [
                    "ID",
                    "Musica"
                ],
                [
                    "IIB",
                    "Biologia"
                ]
            ]
        },
        "Atkvuhru": {
            "1": [
                [
                    "3D",
                    "Tecnologia"
                ],
                [
                    "6A",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "7A",
                    "Matematicas"
                ],
                [
                    "7C",
                    "Matematicas"
                ],
                [
                    "7C",
                    "Biologia"
                ]
            ]
        },
        "Atzgrmcj": {
            "1": [
                [
                    "1A",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "1C",
                    "Artes_Visuales"
                ],
                [
                    "3B",
                    "Orientacion"
                ],
                [
                    "6B",
                    "Orientacion"
                ],
                [
                    "8C",
                    "Musica"
                ],
                [
                    "8D",
                    "Educacion_Fisica"
                ],
                [
                    "IB",
                    "Religion"
                ],
                [
                    "IIA",
                    "Biologia"
                ],
                [
                    "IID",
                    "Fisica"
                ],
                [
                    "IVD",
                    "Fisica"
                ]
            ]
        },
        "Bjczvdlx": {
            "1": [
                [
                    "1D",
                    "Religion"
                ],
                [
                    "3C",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "8A",
                    "Ingles"
                ],
                [
                    "IB",
                    "Historia"
                ],
                [
                    "IIB",
                    "Aleman"
                ],
                [
                    "IIIA",
                    "Artes_Visuales"
                ]
            ]
        },
        "Bsgruzbz": {
            "1": [
                [
                    "2C",
                    "Tecnologia"
                ],
                [
                    "3D",
                    "Matematicas"
                ],
                [
                    "7C",
                    "Orientacion"
                ],
                [
                    "7D",
                    "Fisica"
                ],
                [
                    "ID",
                    "Matematicas"
                ]
            ]
        },
        "Bstpquhk": {
            "1": [
                [
                    "2D",
                    "Ciencias_Naturales"
                ],
                [
                    "7B",
                    "Quimica"
                ],
                [
                    "IA",
                    "Matematicas"
                ],
                [
                    "IIC",
                    "Fisica"
                ],
                [
                    "IIIC",
                    "Matematicas"
                ],
                [
                    "IIIC",
                    "Ciencias_Sociales"
                ]
            ]
        },
        "Btutuqlu": {
            "1": [
                [
                    "6C",
                    "Historia"
                ],
                [
                    "8A",
                    "Biologia"
                ],
                [
                    "IIB",
                    "Musica"
                ]
            ]
        },
        "Bzbkyeqh": {
            "1": [
                [
                    "1A",
                    "Matematicas"
                ],
                [
                    "1A",
                    "Religion"
                ],
                [
                    "3D",
                    "Religion"
                ],
                [
                    "5A",
                    "Ingles"
                ],
                [
                    "7A",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Cdajgsjh": {
            "1": [
                [
                    "4B",
                    "Ciencias_Naturales"
                ],
                [
                    "4D",
                    "Lenguaje"
                ],
                [
                    "IB",
                    "Orientacion"
                ],
                [
                    "IIID",
                    "Educacion_Fisica"
                ],
                [
                    "IIID",
                    "Biologia"
                ],
                [
                    "IIID",
                    "G3"
                ]
            ]
        },
        "Cdinnylg": {
            "1": [
                [
                    "2B",
                    "Musica"
                ],
                [
                    "IA",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Matematicas"
                ],
                [
                    "IVA",
                    "Matematicas"
                ]
            ]
        },
        "Cdnujdgy": {
            "1": [
                [
                    "3C",
                    "Ciencias_Naturales"
                ]
            ]
        },
        "Cigviwln": {
            "1": [
                [
                    "4D",
                    "Artes_Visuales"
                ],
                [
                    "5B",
                    "Musica"
                ],
                [
                    "6D",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "7A",
                    "Quimica"
                ],
                [
                    "8C",
                    "Orientacion"
                ],
                [
                    "IVC",
                    "Geografia"
                ]
            ]
        },
        "Cjntorhr": {
            "1": [
                [
                    "2A",
                    "Orientacion"
                ],
                [
                    "2B",
                    "Aleman"
                ],
                [
                    "2C",
                    "Aleman"
                ],
                [
                    "6B",
                    "Tecnologia"
                ],
                [
                    "8D",
                    "Quimica"
                ],
                [
                    "IVA",
                    "Ciencias_Sociales"
                ]
            ]
        },
        "Dkcpfgmz": {
            "1": [
                [
                    "3B",
                    "Ciencias_Naturales"
                ],
                [
                    "3B",
                    "Tecnologia"
                ],
                [
                    "IIIC",
                    "Historia"
                ]
            ]
        },
        "Dlrlhevn": {
            "1": [
                [
                    "2A",
                    "Aleman"
                ],
                [
                    "7D",
                    "Lenguaje"
                ],
                [
                    "8D",
                    "Aleman"
                ],
                [
                    "ID",
                    "Religion"
                ]
            ]
        },
        "Dtqrwfpf": {
            "1": [
                [
                    "5C",
                    "Tecnologia"
                ],
                [
                    "8B",
                    "Aleman"
                ],
                [
                    "IA",
                    "Biologia"
                ],
                [
                    "IC",
                    "Historia"
                ],
                [
                    "IIIC",
                    "Biologia"
                ]
            ]
        },
        "Dwivygdq": {
            "1": [
                [
                    "3B",
                    "Lenguaje"
                ],
                [
                    "3D",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "IIID",
                    "Matematicas"
                ],
                [
                    "IVA",
                    "Lenguaje"
                ],
                [
                    "IVC",
                    "Biologia"
                ]
            ]
        },
        "Dwsfwtcu": {
            "1": [
                [
                    "1C",
                    "Orientacion"
                ],
                [
                    "7A",
                    "Religion"
                ],
                [
                    "8B",
                    "Quimica"
                ],
                [
                    "8B",
                    "Biologia"
                ],
                [
                    "IB",
                    "Ingles"
                ],
                [
                    "IIC",
                    "Tecnologia"
                ],
                [
                    "IIC",
                    "Educacion_Fisica"
                ],
                [
                    "IIID",
                    "Consejo_de_Curso"
                ],
                [
                    "IIID",
                    "Fisica"
                ]
            ]
        },
        "Eamagaxo": {
            "1": [
                [
                    "1D",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "3D",
                    "Musica"
                ],
                [
                    "IB",
                    "Musica"
                ],
                [
                    "IIB",
                    "Tecnologia"
                ]
            ]
        },
        "Eieyagjc": {
            "1": [
                [
                    "1A",
                    "Aleman"
                ],
                [
                    "6D",
                    "Musica"
                ],
                [
                    "7A",
                    "Aleman"
                ],
                [
                    "8D",
                    "Religion"
                ],
                [
                    "IIB",
                    "Historia"
                ]
            ]
        },
        "Ekclmkxn": {
            "1": [
                [
                    "4A",
                    "Ciencias_Naturales"
                ],
                [
                    "4B",
                    "Matematicas"
                ],
                [
                    "4C",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "IIA",
                    "Ingles"
                ],
                [
                    "IIIA",
                    "Matematicas"
                ],
                [
                    "IIIC",
                    "Consejo_de_Curso"
                ]
            ]
        },
        "Enctmbwa": {
            "1": [
                [
                    "2A",
                    "Lenguaje"
                ],
                [
                    "2D",
                    "Artes_Visuales"
                ],
                [
                    "8B",
                    "Religion"
                ],
                [
                    "IIC",
                    "Historia"
                ]
            ]
        },
        "Eyygrfpx": {
            "1": [
                [
                    "3C",
                    "Matematicas"
                ],
                [
                    "4C",
                    "Educacion_Fisica"
                ],
                [
                    "7C",
                    "Musica"
                ],
                [
                    "8D",
                    "Biologia"
                ],
                [
                    "IC",
                    "Quimica"
                ],
                [
                    "IID",
                    "Religion"
                ],
                [
                    "IIIB",
                    "Ciencias_Sociales"
                ]
            ]
        },
        "Fjmedzyi": {
            "1": [
                [
                    "4A",
                    "Historia"
                ],
                [
                    "4C",
                    "Religion"
                ],
                [
                    "4D",
                    "Tecnologia"
                ],
                [
                    "6A",
                    "Artes_Visuales"
                ],
                [
                    "7A",
                    "Ingles"
                ],
                [
                    "IIID",
                    "Artes_Visuales"
                ],
                [
                    "IVD",
                    "Consejo_de_Curso"
                ]
            ]
        },
        "Fkkvumii": {
            "1": [
                [
                    "2D",
                    "Aleman"
                ],
                [
                    "7A",
                    "Lenguaje"
                ],
                [
                    "IVB",
                    "Ciencias_Sociales"
                ]
            ]
        },
        "Fpqpcfbq": {
            "1": [
                [
                    "5A",
                    "Tecnologia"
                ],
                [
                    "5B",
                    "Tecnologia"
                ],
                [
                    "6A",
                    "Orientacion"
                ],
                [
                    "6C",
                    "Orientacion"
                ],
                [
                    "7C",
                    "Tecnologia"
                ],
                [
                    "7C",
                    "Fisica"
                ],
                [
                    "8D",
                    "Tecnologia"
                ],
                [
                    "IID",
                    "Musica"
                ],
                [
                    "IIID",
                    "Historia"
                ],
                [
                    "IVD",
                    "Geografia"
                ]
            ]
        },
        "Fswbqxvq": {
            "1": [
                [
                    "3A",
                    "Religion"
                ],
                [
                    "4C",
                    "Lenguaje"
                ],
                [
                    "4C",
                    "Historia"
                ],
                [
                    "8C",
                    "Lenguaje"
                ]
            ]
        },
        "Gksjyzam": {
            "1": [
                [
                    "1B",
                    "Aleman"
                ],
                [
                    "5C",
                    "Musica"
                ]
            ]
        },
        "Gvkndpxu": {
            "1": [
                [
                    "1B",
                    "Lenguaje"
                ],
                [
                    "5B",
                    "Orientacion"
                ],
                [
                    "8A",
                    "Tecnologia"
                ],
                [
                    "IIA",
                    "Religion"
                ],
                [
                    "IIC",
                    "Religion"
                ],
                [
                    "IIIA",
                    "Fisica"
                ]
            ]
        },
        "Hbgzrbec": {
            "1": [
                [
                    "3C",
                    "Tecnologia"
                ],
                [
                    "5A",
                    "Lenguaje"
                ],
                [
                    "IB",
                    "Matematicas"
                ],
                [
                    "ID",
                    "Tecnologia"
                ],
                [
                    "IIA",
                    "Musica"
                ]
            ]
        },
        "Hcaebpbd": {
            "1": [
                [
                    "4D",
                    "Historia"
                ],
                [
                    "8A",
                    "Religion"
                ],
                [
                    "IIB",
                    "Ingles"
                ],
                [
                    "IIC",
                    "Lenguaje"
                ]
            ]
        },
        "Hgcsbhrt": {
            "1": [
                [
                    "5B",
                    "Aleman"
                ],
                [
                    "7D",
                    "Biologia"
                ],
                [
                    "8D",
                    "Matematicas"
                ],
                [
                    "IIB",
                    "Religion"
                ],
                [
                    "IVA",
                    "G3"
                ]
            ]
        },
        "Igijmzip": {
            "1": [
                [
                    "6D",
                    "Ciencias_Naturales"
                ],
                [
                    "IA",
                    "Ingles"
                ],
                [
                    "IIID",
                    "G2"
                ],
                [
                    "IVC",
                    "Lenguaje"
                ]
            ]
        },
        "Ilcmctde": {
            "1": [
                [
                    "2D",
                    "Musica"
                ],
                [
                    "4D",
                    "Musica"
                ],
                [
                    "6A",
                    "Musica"
                ],
                [
                    "6C",
                    "Lenguaje"
                ],
                [
                    "6C",
                    "Aleman"
                ]
            ]
        },
        "Ipgxqoqq": {
            "1": [
                [
                    "5B",
                    "Matematicas"
                ],
                [
                    "5D",
                    "Tecnologia"
                ],
                [
                    "7B",
                    "Lenguaje"
                ],
                [
                    "IID",
                    "Biologia"
                ],
                [
                    "IIIC",
                    "Ingles"
                ]
            ]
        },
        "Izdefgii": {
            "1": [
                [
                    "3C",
                    "Musica"
                ],
                [
                    "5B",
                    "Geografia"
                ],
                [
                    "7B",
                    "Fisica"
                ],
                [
                    "IIIC",
                    "Geografia"
                ]
            ]
        },
        "Izhnrdcv": {
            "1": [
                [
                    "2D",
                    "Orientacion"
                ],
                [
                    "5A",
                    "Orientacion"
                ],
                [
                    "5D",
                    "Lenguaje"
                ],
                [
                    "IIC",
                    "Aleman"
                ],
                [
                    "IVC",
                    "Aleman"
                ]
            ]
        },
        "Izxqvpvk": {
            "1": [
                [
                    "6C",
                    "Tecnologia"
                ]
            ]
        },
        "Jjjbjxan": {
            "1": [
                [
                    "3B",
                    "Aleman"
                ],
                [
                    "4A",
                    "Musica"
                ],
                [
                    "8A",
                    "Aleman"
                ],
                [
                    "IVB",
                    "Biologia"
                ]
            ]
        },
        "Jumijrpx": {
            "1": [
                [
                    "1D",
                    "Artes_Visuales"
                ],
                [
                    "2C",
                    "Lenguaje"
                ],
                [
                    "3B",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "8C",
                    "Aleman"
                ],
                [
                    "IVA",
                    "Ingles"
                ]
            ]
        },
        "Jxlritwl": {
            "1": [
                [
                    "5B",
                    "Religion"
                ],
                [
                    "8A",
                    "Historia"
                ],
                [
                    "IIC",
                    "Matematicas"
                ],
                [
                    "IIIC",
                    "G3"
                ]
            ]
        },
        "Kbksxvdi": {
            "1": [
                [
                    "5A",
                    "Historia"
                ],
                [
                    "IIA",
                    "Matematicas"
                ],
                [
                    "IIB",
                    "Quimica"
                ],
                [
                    "IIIB",
                    "G2"
                ],
                [
                    "IVB",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Kdfpngqg": {
            "1": [
                [
                    "4A",
                    "Educacion_Fisica"
                ],
                [
                    "IA",
                    "Tecnologia"
                ]
            ]
        },
        "Kgpidnxy": {
            "1": [
                [
                    "1D",
                    "Orientacion"
                ],
                [
                    "3A",
                    "Musica"
                ],
                [
                    "4A",
                    "Lenguaje"
                ],
                [
                    "7B",
                    "Biologia"
                ],
                [
                    "IIIA",
                    "Geografia"
                ],
                [
                    "IIIC",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Ktalejxl": {
            "1": [
                [
                    "2A",
                    "Tecnologia"
                ],
                [
                    "2C",
                    "Matematicas"
                ],
                [
                    "5A",
                    "Ciencias_Naturales"
                ],
                [
                    "6D",
                    "Aleman"
                ],
                [
                    "IVD",
                    "G3"
                ]
            ]
        },
        "Kvqamngw": {
            "1": [
                [
                    "5C",
                    "Matematicas"
                ],
                [
                    "6A",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Lenguaje"
                ]
            ]
        },
        "Lhguzsdp": {
            "1": [
                [
                    "4C",
                    "Matematicas"
                ],
                [
                    "ID",
                    "Lenguaje"
                ],
                [
                    "IVC",
                    "Educacion_Fisica"
                ],
                [
                    "IVD",
                    "Lenguaje"
                ]
            ]
        },
        "Lhhvlhbs": {
            "1": [
                [
                    "2C",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "2D",
                    "Taller_Comprension_Lectora"
                ]
            ]
        },
        "Lkmhjlav": {
            "1": [
                [
                    "1D",
                    "Matematicas"
                ],
                [
                    "2B",
                    "Religion"
                ],
                [
                    "5D",
                    "Ingles"
                ],
                [
                    "IIA",
                    "Fisica"
                ]
            ]
        },
        "Lwrkdqhz": {
            "1": [
                [
                    "5C",
                    "Orientacion"
                ],
                [
                    "7C",
                    "Educacion_Fisica"
                ],
                [
                    "ID",
                    "Quimica"
                ],
                [
                    "IID",
                    "Ingles"
                ]
            ]
        },
        "Mbkhrirw": {
            "1": [
                [
                    "5C",
                    "Lenguaje"
                ],
                [
                    "8A",
                    "Orientacion"
                ],
                [
                    "IID",
                    "Quimica"
                ],
                [
                    "IIIB",
                    "Ingles"
                ]
            ]
        },
        "Mfrsyvvt": {
            "1": [
                [
                    "2C",
                    "Artes_Visuales"
                ],
                [
                    "3C",
                    "Aleman"
                ],
                [
                    "6B",
                    "Educacion_Fisica"
                ],
                [
                    "8B",
                    "Ingles"
                ],
                [
                    "IB",
                    "Educacion_Fisica"
                ],
                [
                    "IIIB",
                    "Geografia"
                ]
            ]
        },
        "Mjelvrnp": {
            "1": [
                [
                    "5B",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Musica"
                ],
                [
                    "IIA",
                    "Aleman"
                ],
                [
                    "IIIB",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Mlvafpyt": {
            "1": [
                [
                    "1A",
                    "Tecnologia"
                ],
                [
                    "6C",
                    "Ciencias_Naturales"
                ],
                [
                    "ID",
                    "Aleman"
                ],
                [
                    "IVB",
                    "Aleman"
                ]
            ]
        },
        "Mmbudkeu": {
            "1": [
                [
                    "1C",
                    "Educacion_Fisica"
                ],
                [
                    "2B",
                    "Orientacion"
                ],
                [
                    "3A",
                    "Artes_Visuales"
                ],
                [
                    "5A",
                    "Musica"
                ],
                [
                    "5C",
                    "Educacion_Fisica"
                ],
                [
                    "IIIB",
                    "G3"
                ],
                [
                    "IVD",
                    "Ciencias_Sociales"
                ]
            ]
        },
        "Nbvukocd": {
            "1": [
                [
                    "1B",
                    "Ciencias_Naturales"
                ],
                [
                    "3B",
                    "Matematicas"
                ],
                [
                    "5A",
                    "Geografia"
                ],
                [
                    "8C",
                    "Historia"
                ],
                [
                    "IC",
                    "Orientacion"
                ]
            ]
        },
        "Ncnqafso": {
            "1": [
                [
                    "1A",
                    "Ciencias_Naturales"
                ],
                [
                    "2B",
                    "Ciencias_Naturales"
                ],
                [
                    "5D",
                    "Musica"
                ],
                [
                    "IIIA",
                    "Lenguaje"
                ],
                [
                    "IVA",
                    "Educacion_Fisica"
                ],
                [
                    "IVD",
                    "Aleman"
                ]
            ]
        },
        "Nipudbji": {
            "1": [
                [
                    "1A",
                    "Historia"
                ],
                [
                    "IIID",
                    "Geografia"
                ],
                [
                    "IVC",
                    "G2"
                ]
            ]
        },
        "Nncolmnk": {
            "1": [
                [
                    "4B",
                    "Historia"
                ],
                [
                    "5A",
                    "Matematicas"
                ],
                [
                    "6C",
                    "Artes_Visuales"
                ],
                [
                    "7C",
                    "Religion"
                ],
                [
                    "IVA",
                    "G2"
                ]
            ]
        },
        "Noayogmf": {
            "1": [
                [
                    "5C",
                    "Ingles"
                ],
                [
                    "IIIC",
                    "G2"
                ]
            ]
        },
        "Nolmbzqj": {
            "1": [
                [
                    "2A",
                    "Educacion_Fisica"
                ],
                [
                    "3A",
                    "Matematicas"
                ],
                [
                    "5D",
                    "Orientacion"
                ],
                [
                    "IIA",
                    "Tecnologia"
                ],
                [
                    "IIA",
                    "Historia"
                ]
            ]
        },
        "Oacufynm": {
            "1": [
                [
                    "1B",
                    "Tecnologia"
                ],
                [
                    "2C",
                    "Ciencias_Naturales"
                ],
                [
                    "7B",
                    "Educacion_Fisica"
                ],
                [
                    "IA",
                    "Educacion_Fisica"
                ],
                [
                    "IID",
                    "Educacion_Fisica"
                ],
                [
                    "IIIA",
                    "Ciencias_Sociales"
                ],
                [
                    "IVC",
                    "Historia"
                ],
                [
                    "IVD",
                    "Historia"
                ]
            ]
        },
        "Onyodhku": {
            "1": [
                [
                    "4D",
                    "Ciencias_Naturales"
                ],
                [
                    "6B",
                    "Aleman"
                ],
                [
                    "7A",
                    "Tecnologia"
                ],
                [
                    "IID",
                    "Historia"
                ],
                [
                    "IVC",
                    "Ciencias_Sociales"
                ]
            ]
        },
        "Orvyxhyd": {
            "1": [
                [
                    "1C",
                    "Ciencias_Naturales"
                ],
                [
                    "3A",
                    "Educacion_Fisica"
                ],
                [
                    "7D",
                    "Quimica"
                ],
                [
                    "8B",
                    "Orientacion"
                ],
                [
                    "8D",
                    "Orientacion"
                ],
                [
                    "IIA",
                    "Orientacion"
                ],
                [
                    "IIIA",
                    "Consejo_de_Curso"
                ],
                [
                    "IVA",
                    "Consejo_de_Curso"
                ],
                [
                    "IVA",
                    "Fisica"
                ],
                [
                    "IVC",
                    "Consejo_de_Curso"
                ]
            ]
        },
        "Oueurwlr": {
            "1": [
                [
                    "5B",
                    "Ingles"
                ],
                [
                    "6D",
                    "Religion"
                ],
                [
                    "8C",
                    "Fisica"
                ],
                [
                    "IIIB",
                    "Lenguaje"
                ]
            ]
        },
        "Peyaycgc": {
            "1": [
                [
                    "2B",
                    "Artes_Visuales"
                ],
                [
                    "2D",
                    "Lenguaje"
                ],
                [
                    "3A",
                    "Tecnologia"
                ],
                [
                    "IVB",
                    "Lenguaje"
                ]
            ]
        },
        "Pfqfrspa": {
            "1": [
                [
                    "3C",
                    "Religion"
                ],
                [
                    "4D",
                    "Religion"
                ],
                [
                    "5D",
                    "Educacion_Fisica"
                ],
                [
                    "7D",
                    "Tecnologia"
                ],
                [
                    "IC",
                    "Biologia"
                ],
                [
                    "IIC",
                    "Orientacion"
                ],
                [
                    "IID",
                    "Aleman"
                ]
            ]
        },
        "Pwekysoi": {
            "1": [
                [
                    "1D",
                    "Historia"
                ],
                [
                    "2C",
                    "Orientacion"
                ],
                [
                    "3D",
                    "Aleman"
                ],
                [
                    "4D",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "5C",
                    "Religion"
                ],
                [
                    "7A",
                    "Historia"
                ],
                [
                    "IVA",
                    "Biologia"
                ]
            ]
        },
        "Pxymekhf": {
            "1": [
                [
                    "1A",
                    "Musica"
                ],
                [
                    "4D",
                    "Aleman"
                ],
                [
                    "5D",
                    "Religion"
                ],
                [
                    "IC",
                    "Ingles"
                ],
                [
                    "IIA",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Qmxargmc": {
            "1": [
                [
                    "3C",
                    "Artes_Visuales"
                ],
                [
                    "5D",
                    "Matematicas"
                ],
                [
                    "7D",
                    "Musica"
                ],
                [
                    "IC",
                    "Aleman"
                ],
                [
                    "IVB",
                    "Geografia"
                ]
            ]
        },
        "Qthqkwjq": {
            "1": [
                [
                    "1B",
                    "Educacion_Fisica"
                ],
                [
                    "5D",
                    "Artes_Visuales"
                ],
                [
                    "IIIA",
                    "Ingles"
                ],
                [
                    "IVB",
                    "Ingles"
                ],
                [
                    "IVC",
                    "Matematicas"
                ]
            ]
        },
        "Rlybywxl": {
            "1": [
                [
                    "4D",
                    "Orientacion"
                ],
                [
                    "5B",
                    "Historia"
                ],
                [
                    "6D",
                    "Orientacion"
                ],
                [
                    "7B",
                    "Musica"
                ],
                [
                    "8B",
                    "Educacion_Fisica"
                ],
                [
                    "IB",
                    "Fisica"
                ],
                [
                    "ID",
                    "Orientacion"
                ],
                [
                    "IIC",
                    "Quimica"
                ],
                [
                    "IIIA",
                    "G3"
                ],
                [
                    "IIIC",
                    "Lenguaje"
                ]
            ]
        },
        "Sgnzggdl": {
            "1": [
                [
                    "7D",
                    "Historia"
                ],
                [
                    "IB",
                    "Lenguaje"
                ]
            ]
        },
        "Skzvkdfn": {
            "1": [
                [
                    "4B",
                    "Aleman"
                ],
                [
                    "7C",
                    "Aleman"
                ]
            ]
        },
        "Sllrohmp": {
            "1": [
                [
                    "5C",
                    "Historia"
                ],
                [
                    "7A",
                    "Musica"
                ],
                [
                    "IVC",
                    "G3"
                ]
            ]
        },
        "Suahrayh": {
            "1": [
                [
                    "1D",
                    "Musica"
                ],
                [
                    "8B",
                    "Historia"
                ],
                [
                    "IID",
                    "Matematicas"
                ],
                [
                    "IIIB",
                    "Fisica"
                ]
            ]
        },
        "Svixsrbd": {
            "1": [
                [
                    "4D",
                    "Matematicas"
                ],
                [
                    "6C",
                    "Educacion_Fisica"
                ],
                [
                    "6C",
                    "Musica"
                ],
                [
                    "7B",
                    "Religion"
                ],
                [
                    "8B",
                    "Tecnologia"
                ],
                [
                    "IIIB",
                    "Consejo_de_Curso"
                ],
                [
                    "IVA",
                    "Geografia"
                ]
            ]
        },
        "Tiifkdsx": {
            "1": [
                [
                    "1B",
                    "Matematicas"
                ],
                [
                    "1C",
                    "Lenguaje"
                ],
                [
                    "4B",
                    "Tecnologia"
                ],
                [
                    "5A",
                    "Educacion_Fisica"
                ],
                [
                    "6B",
                    "Musica"
                ]
            ]
        },
        "Tqeiwlki": {
            "1": [
                [
                    "8B",
                    "Lenguaje"
                ],
                [
                    "8C",
                    "Religion"
                ],
                [
                    "IIA",
                    "Quimica"
                ],
                [
                    "IIB",
                    "Matematicas"
                ]
            ]
        },
        "Trnctbzf": {
            "1": [
                [
                    "2D",
                    "Matematicas"
                ],
                [
                    "3D",
                    "Lenguaje"
                ],
                [
                    "4C",
                    "Artes_Visuales"
                ],
                [
                    "5B",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Txhbhqio": {
            "1": [
                [
                    "6B",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "7D",
                    "Aleman"
                ],
                [
                    "8B",
                    "Matematicas"
                ],
                [
                    "IIA",
                    "Lenguaje"
                ]
            ]
        },
        "Ukpzxoex": {
            "1": [
                [
                    "4A",
                    "Artes_Visuales"
                ],
                [
                    "5A",
                    "Aleman"
                ],
                [
                    "IID",
                    "Tecnologia"
                ],
                [
                    "IIID",
                    "Aleman"
                ],
                [
                    "IVC",
                    "Ingles"
                ]
            ]
        },
        "Ulvuyjza": {
            "1": [
                [
                    "2A",
                    "Religion"
                ],
                [
                    "4B",
                    "Religion"
                ],
                [
                    "4C",
                    "Tecnologia"
                ],
                [
                    "6B",
                    "Historia"
                ],
                [
                    "7C",
                    "Ingles"
                ],
                [
                    "8C",
                    "Tecnologia"
                ],
                [
                    "IIIC",
                    "Artes_Visuales"
                ]
            ]
        },
        "Upmsvroi": {
            "1": [
                [
                    "6D",
                    "Matematicas"
                ],
                [
                    "7A",
                    "Fisica"
                ],
                [
                    "IIID",
                    "Lenguaje"
                ],
                [
                    "IVC",
                    "Fisica"
                ]
            ]
        },
        "Uskngdik": {
            "1": [
                [
                    "1B",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "1C",
                    "Tecnologia"
                ],
                [
                    "2D",
                    "Religion"
                ],
                [
                    "3C",
                    "Historia"
                ],
                [
                    "4C",
                    "Musica"
                ],
                [
                    "6A",
                    "Tecnologia"
                ],
                [
                    "6D",
                    "Tecnologia"
                ],
                [
                    "7A",
                    "Orientacion"
                ],
                [
                    "7A",
                    "Biologia"
                ],
                [
                    "8D",
                    "Fisica"
                ]
            ]
        },
        "Uvpdhdwa": {
            "1": [
                [
                    "1C",
                    "Religion"
                ],
                [
                    "3C",
                    "Orientacion"
                ],
                [
                    "4A",
                    "Matematicas"
                ],
                [
                    "4A",
                    "Religion"
                ],
                [
                    "6D",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Uzkjwjne": {
            "1": [
                [
                    "1C",
                    "Matematicas"
                ],
                [
                    "3A",
                    "Lenguaje"
                ],
                [
                    "3D",
                    "Historia"
                ],
                [
                    "4B",
                    "Musica"
                ],
                [
                    "8D",
                    "Musica"
                ]
            ]
        },
        "Vccyqwgt": {
            "1": [
                [
                    "2B",
                    "Historia"
                ],
                [
                    "2C",
                    "Educacion_Fisica"
                ],
                [
                    "5D",
                    "Ciencias_Naturales"
                ],
                [
                    "6A",
                    "Aleman"
                ],
                [
                    "ID",
                    "Biologia"
                ],
                [
                    "IVB",
                    "G3"
                ]
            ]
        },
        "Vdlrplrh": {
            "1": [
                [
                    "5A",
                    "Artes_Visuales"
                ],
                [
                    "8D",
                    "Ingles"
                ],
                [
                    "IC",
                    "Tecnologia"
                ],
                [
                    "IIB",
                    "Educacion_Fisica"
                ],
                [
                    "IIC",
                    "Biologia"
                ]
            ]
        },
        "Vkmfgwym": {
            "1": [
                [
                    "1D",
                    "Lenguaje"
                ],
                [
                    "2A",
                    "Artes_Visuales"
                ],
                [
                    "3A",
                    "Aleman"
                ],
                [
                    "6A",
                    "Educacion_Fisica"
                ],
                [
                    "IVA",
                    "Artes_Visuales"
                ]
            ]
        },
        "Vokwrssi": {
            "1": [
                [
                    "2B",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "7D",
                    "Religion"
                ],
                [
                    "IA",
                    "Aleman"
                ],
                [
                    "ID",
                    "Historia"
                ],
                [
                    "ID",
                    "Ingles"
                ],
                [
                    "IIIC",
                    "Fisica"
                ]
            ]
        },
        "Vvfythjg": {
            "1": [
                [
                    "2B",
                    "Educacion_Fisica"
                ],
                [
                    "2C",
                    "Historia"
                ],
                [
                    "5C",
                    "Artes_Visuales"
                ],
                [
                    "6B",
                    "Artes_Visuales"
                ],
                [
                    "7D",
                    "Educacion_Fisica"
                ],
                [
                    "IC",
                    "Fisica"
                ]
            ]
        },
        "Weofvsvu": {
            "1": [
                [
                    "3B",
                    "Musica"
                ],
                [
                    "3C",
                    "Educacion_Fisica"
                ],
                [
                    "3D",
                    "Ciencias_Naturales"
                ],
                [
                    "6D",
                    "Artes_Visuales"
                ],
                [
                    "IVA",
                    "Historia"
                ]
            ]
        },
        "Wrbjwpou": {
            "1": [
                [
                    "1A",
                    "Orientacion"
                ],
                [
                    "2A",
                    "Historia"
                ],
                [
                    "3B",
                    "Historia"
                ],
                [
                    "IB",
                    "Tecnologia"
                ],
                [
                    "IIB",
                    "Lenguaje"
                ],
                [
                    "IID",
                    "Orientacion"
                ],
                [
                    "IIIB",
                    "Historia"
                ]
            ]
        },
        "Wrvitfwn": {
            "1": [
                [
                    "2B",
                    "Lenguaje"
                ],
                [
                    "2D",
                    "Educacion_Fisica"
                ],
                [
                    "6C",
                    "Matematicas"
                ],
                [
                    "7C",
                    "Historia"
                ]
            ]
        },
        "Wsaytkdx": {
            "1": [
                [
                    "8A",
                    "Quimica"
                ]
            ]
        },
        "Wumylfsy": {
            "1": [
                [
                    "2D",
                    "Tecnologia"
                ],
                [
                    "8A",
                    "Matematicas"
                ],
                [
                    "8A",
                    "Musica"
                ],
                [
                    "IIB",
                    "Orientacion"
                ],
                [
                    "IIIA",
                    "Aleman"
                ]
            ]
        },
        "Wvmqroil": {
            "1": [
                [
                    "5C",
                    "Geografia"
                ],
                [
                    "6B",
                    "Matematicas"
                ],
                [
                    "6B",
                    "Ciencias_Naturales"
                ],
                [
                    "8C",
                    "Educacion_Fisica"
                ],
                [
                    "IA",
                    "Historia"
                ]
            ]
        },
        "Wywsbftg": {
            "1": [
                [
                    "5C",
                    "Aleman"
                ],
                [
                    "7B",
                    "Matematicas"
                ],
                [
                    "8C",
                    "Matematicas"
                ]
            ]
        },
        "Xfhyxhmf": {
            "1": [
                [
                    "1D",
                    "Educacion_Fisica"
                ],
                [
                    "2D",
                    "Historia"
                ],
                [
                    "3B",
                    "Religion"
                ],
                [
                    "4D",
                    "Educacion_Fisica"
                ],
                [
                    "8B",
                    "Fisica"
                ],
                [
                    "IIB",
                    "Fisica"
                ],
                [
                    "IVB",
                    "Artes_Visuales"
                ],
                [
                    "IVD",
                    "Artes_Visuales"
                ]
            ]
        },
        "Xfyryhan": {
            "1": [
                [
                    "2A",
                    "Musica"
                ],
                [
                    "3A",
                    "Historia"
                ],
                [
                    "3D",
                    "Educacion_Fisica"
                ],
                [
                    "4B",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "7C",
                    "Quimica"
                ],
                [
                    "7D",
                    "Ingles"
                ],
                [
                    "IA",
                    "Orientacion"
                ],
                [
                    "ID",
                    "Fisica"
                ],
                [
                    "IIIA",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Xrgtkdbt": {
            "1": [
                [
                    "2A",
                    "Ciencias_Naturales"
                ],
                [
                    "3A",
                    "Ciencias_Naturales"
                ],
                [
                    "3D",
                    "Orientacion"
                ],
                [
                    "4C",
                    "Orientacion"
                ],
                [
                    "6B",
                    "Religion"
                ],
                [
                    "IIIB",
                    "Aleman"
                ],
                [
                    "IVD",
                    "Educacion_Fisica"
                ]
            ]
        },
        "Xtknjgfi": {
            "1": [
                [
                    "1C",
                    "Musica"
                ],
                [
                    "2B",
                    "Tecnologia"
                ],
                [
                    "5C",
                    "Ciencias_Naturales"
                ],
                [
                    "6B",
                    "Lenguaje"
                ],
                [
                    "8D",
                    "Lenguaje"
                ]
            ]
        },
        "Xulhdtye": {
            "1": [
                [
                    "4A",
                    "Tecnologia"
                ],
                [
                    "7B",
                    "Tecnologia"
                ],
                [
                    "IA",
                    "Fisica"
                ],
                [
                    "IIID",
                    "Ingles"
                ],
                [
                    "IVB",
                    "Fisica"
                ]
            ]
        },
        "Xwmgnbka": {
            "1": [
                [
                    "1D",
                    "Tecnologia"
                ],
                [
                    "3C",
                    "Lenguaje"
                ],
                [
                    "4C",
                    "Aleman"
                ],
                [
                    "7B",
                    "Orientacion"
                ],
                [
                    "8D",
                    "Historia"
                ]
            ]
        },
        "Ybufanza": {
            "1": [
                [
                    "1D",
                    "Ciencias_Naturales"
                ],
                [
                    "IB",
                    "Quimica"
                ],
                [
                    "IIIB",
                    "Biologia"
                ],
                [
                    "IVD",
                    "Biologia"
                ]
            ]
        },
        "Ycaeozob": {
            "1": [
                [
                    "1A",
                    "Artes_Visuales"
                ],
                [
                    "3B",
                    "Educacion_Fisica"
                ],
                [
                    "7B",
                    "Ingles"
                ],
                [
                    "8C",
                    "Ingles"
                ],
                [
                    "IA",
                    "Quimica"
                ],
                [
                    "IIIB",
                    "Artes_Visuales"
                ],
                [
                    "IVC",
                    "Artes_Visuales"
                ]
            ]
        },
        "Ychzycdi": {
            "1": [
                [
                    "6D",
                    "Historia"
                ],
                [
                    "7C",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Religion"
                ],
                [
                    "IID",
                    "Lenguaje"
                ]
            ]
        },
        "Yicoxcly": {
            "1": [
                [
                    "2C",
                    "Religion"
                ],
                [
                    "6A",
                    "Matematicas"
                ],
                [
                    "7D",
                    "Orientacion"
                ],
                [
                    "IIIC",
                    "Aleman"
                ],
                [
                    "IVD",
                    "G2"
                ]
            ]
        },
        "Yiqzsxsm": {
            "1": [
                [
                    "1A",
                    "Educacion_Fisica"
                ],
                [
                    "5A",
                    "Religion"
                ],
                [
                    "6C",
                    "Religion"
                ],
                [
                    "6C",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "8C",
                    "Biologia"
                ],
                [
                    "IVA",
                    "Aleman"
                ],
                [
                    "IVB",
                    "Matematicas"
                ],
                [
                    "IVB",
                    "Consejo_de_Curso"
                ]
            ]
        },
        "Ylbruxtg": {
            "1": [
                [
                    "4B",
                    "Educacion_Fisica"
                ],
                [
                    "5D",
                    "Geografia"
                ],
                [
                    "8B",
                    "Musica"
                ],
                [
                    "IA",
                    "Religion"
                ],
                [
                    "IB",
                    "Aleman"
                ],
                [
                    "IVB",
                    "Historia"
                ]
            ]
        },
        "Yokgsgdf": {
            "1": [
                [
                    "7B",
                    "Historia"
                ],
                [
                    "IIIB",
                    "Matematicas"
                ]
            ]
        },
        "Yycaxjta": {
            "1": [
                [
                    "1B",
                    "Historia"
                ],
                [
                    "2A",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "5D",
                    "Historia"
                ],
                [
                    "7B",
                    "Aleman"
                ],
                [
                    "IIIA",
                    "Biologia"
                ],
                [
                    "IVD",
                    "Ingles"
                ]
            ]
        },
        "Zcnkzivy": {
            "1": [
                [
                    "1B",
                    "Musica"
                ],
                [
                    "1B",
                    "Artes_Visuales"
                ],
                [
                    "4A",
                    "Orientacion"
                ],
                [
                    "4B",
                    "Orientacion"
                ],
                [
                    "4B",
                    "Lenguaje"
                ],
                [
                    "4C",
                    "Ciencias_Naturales"
                ],
                [
                    "8C",
                    "Quimica"
                ]
            ]
        },
        "Zhlczlpq": {
            "1": [
                [
                    "1C",
                    "Historia"
                ],
                [
                    "5B",
                    "Artes_Visuales"
                ],
                [
                    "6A",
                    "Ciencias_Naturales"
                ],
                [
                    "8A",
                    "Educacion_Fisica"
                ],
                [
                    "IA",
                    "Musica"
                ],
                [
                    "IB",
                    "Biologia"
                ],
                [
                    "IIID",
                    "Ciencias_Sociales"
                ],
                [
                    "IVB",
                    "G2"
                ]
            ]
        },
        "Zjszbjef": {
            "1": [
                [
                    "1A",
                    "Lenguaje"
                ],
                [
                    "1B",
                    "Religion"
                ],
                [
                    "3D",
                    "Artes_Visuales"
                ],
                [
                    "4A",
                    "Aleman"
                ],
                [
                    "6A",
                    "Historia"
                ]
            ]
        },
        "Zpijftra": {
            "1": [
                [
                    "1B",
                    "Orientacion"
                ],
                [
                    "1D",
                    "Aleman"
                ],
                [
                    "8A",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Educacion_Fisica"
                ],
                [
                    "IVD",
                    "Matematicas"
                ]
            ]
        },
        "Ztyjwzin": {
            "1": [
                [
                    "2B",
                    "Matematicas"
                ],
                [
                    "4B",
                    "Artes_Visuales"
                ],
                [
                    "IIC",
                    "Musica"
                ],
                [
                    "IIIA",
                    "Historia"
                ],
                [
                    "IIIA",
                    "G2"
                ]
            ]
        },
        "Zxozenmu": {
            "1": [
                [
                    "1C",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "2C",
                    "Musica"
                ],
                [
                    "3B",
                    "Artes_Visuales"
                ],
                [
                    "4A",
                    "Taller_Comprension_Lectora"
                ],
                [
                    "5B",
                    "Ciencias_Naturales"
                ],
                [
                    "5D",
                    "Aleman"
                ],
                [
                    "ID",
                    "Educacion_Fisica"
                ]
            ]
        }
    },
    "multiples_cursos": [

    ],
    "multiples_profesores": [

    ],
    "asignaciones_vetadas": [

    ],
    "asignaciones_fijadas": [

    ],
    "combinaciones_vetadas": [
        
    ]
}

x = requests.post(url, json = myobj)
final = x.text

final = final.replace('\\u00e1', 'á')
final = final.replace('\\u00e9', 'é')
final = final.replace('\\u00ed', 'í')
final = final.replace('\\u00f3', 'ó')
final = final.replace('\\u00fa', 'ú')
final = final.replace('\\u00c1', 'Á')
final = final.replace('\\u00c9', 'É')
final = final.replace('\\u00cd', 'Í')
final = final.replace('\\u00d3', 'Ó')
final = final.replace('\\u00da', 'Ú')
final = final.replace('\\u00f1', 'ñ')
final = final.replace('\\u00d1', 'Ñ')

print(final)
res = json.loads(final)
print(res)