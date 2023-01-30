import requests

url = 'http://localhost:8000/test2'
myobj = {
    "dias": [
        "Lunes","Martes","Miércoles","Jueves","Viernes"
    ],
    "modulos": [
        1,2,3,4,5,6,7,8,9,10
    ],
    "ramos_con_modulos_seguidos": [
        "Educación_Física", "Artes_Visuales", "Tecnología"
    ],
    "combinaciones": [
        [1,2],
        [2,3],
        [4,5],
        [6,7],
        [8,9]
    ],
    "horarios": {
        "1A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "1B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "1C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "1D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "2D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "3D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "4D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "5D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "6D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8],
            "Miércoles": [1,2,3,4,5,6,7,8],
            "Jueves": [1,2,3,4,5,6,7,8], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "7D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8A": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8B": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8C": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "8D": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "ID": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IID": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIIA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIIB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIIC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IIID": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVA": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVB": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVC": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        },
        "IVD": {
            "Lunes": [1,2,3,4,5,6,7],
            "Martes": [1,2,3,4,5,6,7,8,9],
            "Miércoles": [1,2,3,4,5,6,7,8,9,10],
            "Jueves": [1,2,3,4,5,6,7,8,9], 
            "Viernes": [1,2,3,4,5,6,7]
        }
    },
    "profesores_por_curso": {
        "1A": {
            "1": [
                [
                    "Eieyagjc",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Pxymekhf",
                    "M\u00fasica"
                ],
                [
                    "Wrbjwpou",
                    "Orientaci\u00f3n"
                ],
                [
                    "Bzbkyeqh",
                    "Religi\u00f3n"
                ],
                [
                    "Atzgrmcj",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Mlvafpyt",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "1B": {
            "1": [
                [
                    "Gksjyzam",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Zcnkzivy",
                    "M\u00fasica"
                ],
                [
                    "Zpijftra",
                    "Orientaci\u00f3n"
                ],
                [
                    "Zjszbjef",
                    "Religi\u00f3n"
                ],
                [
                    "Uskngdik",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Oacufynm",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "1C": {
            "1": [
                [
                    "Artfsbvj",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Xtknjgfi",
                    "M\u00fasica"
                ],
                [
                    "Dwsfwtcu",
                    "Orientaci\u00f3n"
                ],
                [
                    "Uvpdhdwa",
                    "Religi\u00f3n"
                ],
                [
                    "Zxozenmu",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Uskngdik",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "1D": {
            "1": [
                [
                    "Zpijftra",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Suahrayh",
                    "M\u00fasica"
                ],
                [
                    "Kgpidnxy",
                    "Orientaci\u00f3n"
                ],
                [
                    "Bjczvdlx",
                    "Religi\u00f3n"
                ],
                [
                    "Eamagaxo",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Xwmgnbka",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "2A": {
            "1": [
                [
                    "Dlrlhevn",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Xfyryhan",
                    "M\u00fasica"
                ],
                [
                    "Cjntorhr",
                    "Orientaci\u00f3n"
                ],
                [
                    "Ulvuyjza",
                    "Religi\u00f3n"
                ],
                [
                    "Yycaxjta",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Ktalejxl",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "2B": {
            "1": [
                [
                    "Cjntorhr",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Cdinnylg",
                    "M\u00fasica"
                ],
                [
                    "Mmbudkeu",
                    "Orientaci\u00f3n"
                ],
                [
                    "Lkmhjlav",
                    "Religi\u00f3n"
                ],
                [
                    "Vokwrssi",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Xtknjgfi",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "2C": {
            "1": [
                [
                    "Cjntorhr",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Zxozenmu",
                    "M\u00fasica"
                ],
                [
                    "Pwekysoi",
                    "Orientaci\u00f3n"
                ],
                [
                    "Yicoxcly",
                    "Religi\u00f3n"
                ],
                [
                    "Lhhvlhbs",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Bsgruzbz",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "2D": {
            "1": [
                [
                    "Fkkvumii",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Ilcmctde",
                    "M\u00fasica"
                ],
                [
                    "Izhnrdcv",
                    "Orientaci\u00f3n"
                ],
                [
                    "Uskngdik",
                    "Religi\u00f3n"
                ],
                [
                    "Lhhvlhbs",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Wumylfsy",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "3A": {
            "1": [
                [
                    "Vkmfgwym",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Kgpidnxy",
                    "M\u00fasica"
                ],
                [
                    "Artfsbvj",
                    "Orientaci\u00f3n"
                ],
                [
                    "Fswbqxvq",
                    "Religi\u00f3n"
                ],
                [
                    "Artfsbvj",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Peyaycgc",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "3B": {
            "1": [
                [
                    "Jjjbjxan",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Weofvsvu",
                    "M\u00fasica"
                ],
                [
                    "Atzgrmcj",
                    "Orientaci\u00f3n"
                ],
                [
                    "Xfhyxhmf",
                    "Religi\u00f3n"
                ],
                [
                    "Jumijrpx",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Dkcpfgmz",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "3C": {
            "1": [
                [
                    "Mfrsyvvt",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Izdefgii",
                    "M\u00fasica"
                ],
                [
                    "Uvpdhdwa",
                    "Orientaci\u00f3n"
                ],
                [
                    "Pfqfrspa",
                    "Religi\u00f3n"
                ],
                [
                    "Bjczvdlx",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Hbgzrbec",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "3D": {
            "1": [
                [
                    "Pwekysoi",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Eamagaxo",
                    "M\u00fasica"
                ],
                [
                    "Xrgtkdbt",
                    "Orientaci\u00f3n"
                ],
                [
                    "Bzbkyeqh",
                    "Religi\u00f3n"
                ],
                [
                    "Dwivygdq",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Atkvuhru",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "4A": {
            "1": [
                [
                    "Zjszbjef",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Jjjbjxan",
                    "M\u00fasica"
                ],
                [
                    "Zcnkzivy",
                    "Orientaci\u00f3n"
                ],
                [
                    "Uvpdhdwa",
                    "Religi\u00f3n"
                ],
                [
                    "Zxozenmu",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Xulhdtye",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "4B": {
            "1": [
                [
                    "Skzvkdfn",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Uzkjwjne",
                    "M\u00fasica"
                ],
                [
                    "Zcnkzivy",
                    "Orientaci\u00f3n"
                ],
                [
                    "Ulvuyjza",
                    "Religi\u00f3n"
                ],
                [
                    "Xfyryhan",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Tiifkdsx",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "4C": {
            "1": [
                [
                    "Xwmgnbka",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Uskngdik",
                    "M\u00fasica"
                ],
                [
                    "Xrgtkdbt",
                    "Orientaci\u00f3n"
                ],
                [
                    "Fjmedzyi",
                    "Religi\u00f3n"
                ],
                [
                    "Ekclmkxn",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Ulvuyjza",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "4D": {
            "1": [
                [
                    "Pxymekhf",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Ilcmctde",
                    "M\u00fasica"
                ],
                [
                    "Rlybywxl",
                    "Orientaci\u00f3n"
                ],
                [
                    "Pfqfrspa",
                    "Religi\u00f3n"
                ],
                [
                    "Pwekysoi",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Fjmedzyi",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "5A": {
            "1": [
                [
                    "Ukpzxoex",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Nbvukocd",
                    "Geograf\u00eda"
                ],
                [
                    "Kbksxvdi",
                    "Historia"
                ],
                [
                    "Bzbkyeqh",
                    "Ingl\u00e9s"
                ],
                [
                    "Hbgzrbec",
                    "Lenguaje"
                ],
                [
                    "Nncolmnk",
                    "Matem\u00e1ticas"
                ],
                [
                    "Mmbudkeu",
                    "M\u00fasica"
                ],
                [
                    "Izhnrdcv",
                    "Orientaci\u00f3n"
                ],
                [
                    "Yiqzsxsm",
                    "Religi\u00f3n"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "5B": {
            "1": [
                [
                    "Hgcsbhrt",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Izdefgii",
                    "Geograf\u00eda"
                ],
                [
                    "Rlybywxl",
                    "Historia"
                ],
                [
                    "Oueurwlr",
                    "Ingl\u00e9s"
                ],
                [
                    "Mjelvrnp",
                    "Lenguaje"
                ],
                [
                    "Ipgxqoqq",
                    "Matem\u00e1ticas"
                ],
                [
                    "Cigviwln",
                    "M\u00fasica"
                ],
                [
                    "Gvkndpxu",
                    "Orientaci\u00f3n"
                ],
                [
                    "Jxlritwl",
                    "Religi\u00f3n"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "5C": {
            "1": [
                [
                    "Wywsbftg",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Wvmqroil",
                    "Geograf\u00eda"
                ],
                [
                    "Sllrohmp",
                    "Historia"
                ],
                [
                    "Noayogmf",
                    "Ingl\u00e9s"
                ],
                [
                    "Mbkhrirw",
                    "Lenguaje"
                ],
                [
                    "Kvqamngw",
                    "Matem\u00e1ticas"
                ],
                [
                    "Gksjyzam",
                    "M\u00fasica"
                ],
                [
                    "Lwrkdqhz",
                    "Orientaci\u00f3n"
                ],
                [
                    "Pwekysoi",
                    "Religi\u00f3n"
                ],
                [
                    "Dtqrwfpf",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "5D": {
            "1": [
                [
                    "Zxozenmu",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Ylbruxtg",
                    "Geograf\u00eda"
                ],
                [
                    "Yycaxjta",
                    "Historia"
                ],
                [
                    "Lkmhjlav",
                    "Ingl\u00e9s"
                ],
                [
                    "Izhnrdcv",
                    "Lenguaje"
                ],
                [
                    "Qmxargmc",
                    "Matem\u00e1ticas"
                ],
                [
                    "Ncnqafso",
                    "M\u00fasica"
                ],
                [
                    "Nolmbzqj",
                    "Orientaci\u00f3n"
                ],
                [
                    "Pxymekhf",
                    "Religi\u00f3n"
                ],
                [
                    "Ipgxqoqq",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "6A": {
            "1": [
                [
                    "Vccyqwgt",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Ilcmctde",
                    "M\u00fasica"
                ],
                [
                    "Fpqpcfbq",
                    "Orientaci\u00f3n"
                ],
                [
                    "Artfsbvj",
                    "Religi\u00f3n"
                ],
                [
                    "Atkvuhru",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Uskngdik",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "6B": {
            "1": [
                [
                    "Onyodhku",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Tiifkdsx",
                    "M\u00fasica"
                ],
                [
                    "Atzgrmcj",
                    "Orientaci\u00f3n"
                ],
                [
                    "Xrgtkdbt",
                    "Religi\u00f3n"
                ],
                [
                    "Txhbhqio",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Cjntorhr",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "6C": {
            "1": [
                [
                    "Ilcmctde",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Svixsrbd",
                    "M\u00fasica"
                ],
                [
                    "Fpqpcfbq",
                    "Orientaci\u00f3n"
                ],
                [
                    "Yiqzsxsm",
                    "Religi\u00f3n"
                ],
                [
                    "Yiqzsxsm",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Izxqvpvk",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "6D": {
            "1": [
                [
                    "Ktalejxl",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "Eieyagjc",
                    "M\u00fasica"
                ],
                [
                    "Rlybywxl",
                    "Orientaci\u00f3n"
                ],
                [
                    "Oueurwlr",
                    "Religi\u00f3n"
                ],
                [
                    "Cigviwln",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "Uskngdik",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "7A": {
            "1": [
                [
                    "Eieyagjc",
                    "Alem\u00e1n"
                ],
                [
                    "Uskngdik",
                    "Biolog\u00eda"
                ],
                [
                    "Bzbkyeqh",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Upmsvroi",
                    "F\u00edsica"
                ],
                [
                    "Pwekysoi",
                    "Historia"
                ],
                [
                    "Fjmedzyi",
                    "Ingl\u00e9s"
                ],
                [
                    "Fkkvumii",
                    "Lenguaje"
                ],
                [
                    "Atkvuhru",
                    "Matem\u00e1ticas"
                ],
                [
                    "Sllrohmp",
                    "M\u00fasica"
                ],
                [
                    "Uskngdik",
                    "Orientaci\u00f3n"
                ],
                [
                    "Cigviwln",
                    "Qu\u00edmica"
                ],
                [
                    "Dwsfwtcu",
                    "Religi\u00f3n"
                ],
                [
                    "Onyodhku",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "7B": {
            "1": [
                [
                    "Yycaxjta",
                    "Alem\u00e1n"
                ],
                [
                    "Kgpidnxy",
                    "Biolog\u00eda"
                ],
                [
                    "Oacufynm",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Izdefgii",
                    "F\u00edsica"
                ],
                [
                    "Yokgsgdf",
                    "Historia"
                ],
                [
                    "Ycaeozob",
                    "Ingl\u00e9s"
                ],
                [
                    "Ipgxqoqq",
                    "Lenguaje"
                ],
                [
                    "Wywsbftg",
                    "Matem\u00e1ticas"
                ],
                [
                    "Rlybywxl",
                    "M\u00fasica"
                ],
                [
                    "Xwmgnbka",
                    "Orientaci\u00f3n"
                ],
                [
                    "Bstpquhk",
                    "Qu\u00edmica"
                ],
                [
                    "Svixsrbd",
                    "Religi\u00f3n"
                ],
                [
                    "Xulhdtye",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "7C": {
            "1": [
                [
                    "Skzvkdfn",
                    "Alem\u00e1n"
                ],
                [
                    "Atkvuhru",
                    "Biolog\u00eda"
                ],
                [
                    "Lwrkdqhz",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Fpqpcfbq",
                    "F\u00edsica"
                ],
                [
                    "Wrvitfwn",
                    "Historia"
                ],
                [
                    "Ulvuyjza",
                    "Ingl\u00e9s"
                ],
                [
                    "Ychzycdi",
                    "Lenguaje"
                ],
                [
                    "Atkvuhru",
                    "Matem\u00e1ticas"
                ],
                [
                    "Eyygrfpx",
                    "M\u00fasica"
                ],
                [
                    "Bsgruzbz",
                    "Orientaci\u00f3n"
                ],
                [
                    "Xfyryhan",
                    "Qu\u00edmica"
                ],
                [
                    "Nncolmnk",
                    "Religi\u00f3n"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "7D": {
            "1": [
                [
                    "Txhbhqio",
                    "Alem\u00e1n"
                ],
                [
                    "Hgcsbhrt",
                    "Biolog\u00eda"
                ],
                [
                    "Vvfythjg",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Bsgruzbz",
                    "F\u00edsica"
                ],
                [
                    "Sgnzggdl",
                    "Historia"
                ],
                [
                    "Xfyryhan",
                    "Ingl\u00e9s"
                ],
                [
                    "Dlrlhevn",
                    "Lenguaje"
                ],
                [
                    "Apkctzml",
                    "Matem\u00e1ticas"
                ],
                [
                    "Qmxargmc",
                    "M\u00fasica"
                ],
                [
                    "Yicoxcly",
                    "Orientaci\u00f3n"
                ],
                [
                    "Orvyxhyd",
                    "Qu\u00edmica"
                ],
                [
                    "Vokwrssi",
                    "Religi\u00f3n"
                ],
                [
                    "Pfqfrspa",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "8A": {
            "1": [
                [
                    "Jjjbjxan",
                    "Alem\u00e1n"
                ],
                [
                    "Btutuqlu",
                    "Biolog\u00eda"
                ],
                [
                    "Zhlczlpq",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Apkctzml",
                    "F\u00edsica"
                ],
                [
                    "Jxlritwl",
                    "Historia"
                ],
                [
                    "Bjczvdlx",
                    "Ingl\u00e9s"
                ],
                [
                    "Zpijftra",
                    "Lenguaje"
                ],
                [
                    "Wumylfsy",
                    "Matem\u00e1ticas"
                ],
                [
                    "Wumylfsy",
                    "M\u00fasica"
                ],
                [
                    "Mbkhrirw",
                    "Orientaci\u00f3n"
                ],
                [
                    "Wsaytkdx",
                    "Qu\u00edmica"
                ],
                [
                    "Hcaebpbd",
                    "Religi\u00f3n"
                ],
                [
                    "Gvkndpxu",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "8B": {
            "1": [
                [
                    "Dtqrwfpf",
                    "Alem\u00e1n"
                ],
                [
                    "Dwsfwtcu",
                    "Biolog\u00eda"
                ],
                [
                    "Rlybywxl",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Xfhyxhmf",
                    "F\u00edsica"
                ],
                [
                    "Suahrayh",
                    "Historia"
                ],
                [
                    "Mfrsyvvt",
                    "Ingl\u00e9s"
                ],
                [
                    "Tqeiwlki",
                    "Lenguaje"
                ],
                [
                    "Txhbhqio",
                    "Matem\u00e1ticas"
                ],
                [
                    "Ylbruxtg",
                    "M\u00fasica"
                ],
                [
                    "Orvyxhyd",
                    "Orientaci\u00f3n"
                ],
                [
                    "Dwsfwtcu",
                    "Qu\u00edmica"
                ],
                [
                    "Enctmbwa",
                    "Religi\u00f3n"
                ],
                [
                    "Svixsrbd",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "8C": {
            "1": [
                [
                    "Jumijrpx",
                    "Alem\u00e1n"
                ],
                [
                    "Yiqzsxsm",
                    "Biolog\u00eda"
                ],
                [
                    "Wvmqroil",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Oueurwlr",
                    "F\u00edsica"
                ],
                [
                    "Nbvukocd",
                    "Historia"
                ],
                [
                    "Ycaeozob",
                    "Ingl\u00e9s"
                ],
                [
                    "Fswbqxvq",
                    "Lenguaje"
                ],
                [
                    "Wywsbftg",
                    "Matem\u00e1ticas"
                ],
                [
                    "Atzgrmcj",
                    "M\u00fasica"
                ],
                [
                    "Cigviwln",
                    "Orientaci\u00f3n"
                ],
                [
                    "Zcnkzivy",
                    "Qu\u00edmica"
                ],
                [
                    "Tqeiwlki",
                    "Religi\u00f3n"
                ],
                [
                    "Ulvuyjza",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "8D": {
            "1": [
                [
                    "Dlrlhevn",
                    "Alem\u00e1n"
                ],
                [
                    "Eyygrfpx",
                    "Biolog\u00eda"
                ],
                [
                    "Atzgrmcj",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Uskngdik",
                    "F\u00edsica"
                ],
                [
                    "Xwmgnbka",
                    "Historia"
                ],
                [
                    "Vdlrplrh",
                    "Ingl\u00e9s"
                ],
                [
                    "Xtknjgfi",
                    "Lenguaje"
                ],
                [
                    "Hgcsbhrt",
                    "Matem\u00e1ticas"
                ],
                [
                    "Uzkjwjne",
                    "M\u00fasica"
                ],
                [
                    "Orvyxhyd",
                    "Orientaci\u00f3n"
                ],
                [
                    "Cjntorhr",
                    "Qu\u00edmica"
                ],
                [
                    "Eieyagjc",
                    "Religi\u00f3n"
                ],
                [
                    "Fpqpcfbq",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IA": {
            "1": [
                [
                    "Vokwrssi",
                    "Alem\u00e1n"
                ],
                [
                    "Dtqrwfpf",
                    "Biolog\u00eda"
                ],
                [
                    "Oacufynm",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Xulhdtye",
                    "F\u00edsica"
                ],
                [
                    "Wvmqroil",
                    "Historia"
                ],
                [
                    "Igijmzip",
                    "Ingl\u00e9s"
                ],
                [
                    "Cdinnylg",
                    "Lenguaje"
                ],
                [
                    "Bstpquhk",
                    "Matem\u00e1ticas"
                ],
                [
                    "Zhlczlpq",
                    "M\u00fasica"
                ],
                [
                    "Xfyryhan",
                    "Orientaci\u00f3n"
                ],
                [
                    "Ycaeozob",
                    "Qu\u00edmica"
                ],
                [
                    "Ylbruxtg",
                    "Religi\u00f3n"
                ],
                [
                    "Kdfpngqg",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IB": {
            "1": [
                [
                    "Ylbruxtg",
                    "Alem\u00e1n"
                ],
                [
                    "Zhlczlpq",
                    "Biolog\u00eda"
                ],
                [
                    "Mfrsyvvt",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Rlybywxl",
                    "F\u00edsica"
                ],
                [
                    "Bjczvdlx",
                    "Historia"
                ],
                [
                    "Dwsfwtcu",
                    "Ingl\u00e9s"
                ],
                [
                    "Sgnzggdl",
                    "Lenguaje"
                ],
                [
                    "Hbgzrbec",
                    "Matem\u00e1ticas"
                ],
                [
                    "Eamagaxo",
                    "M\u00fasica"
                ],
                [
                    "Cdajgsjh",
                    "Orientaci\u00f3n"
                ],
                [
                    "Ybufanza",
                    "Qu\u00edmica"
                ],
                [
                    "Atzgrmcj",
                    "Religi\u00f3n"
                ],
                [
                    "Wrbjwpou",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IC": {
            "1": [
                [
                    "Qmxargmc",
                    "Alem\u00e1n"
                ],
                [
                    "Pfqfrspa",
                    "Biolog\u00eda"
                ],
                [
                    "Zpijftra",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Vvfythjg",
                    "F\u00edsica"
                ],
                [
                    "Dtqrwfpf",
                    "Historia"
                ],
                [
                    "Pxymekhf",
                    "Ingl\u00e9s"
                ],
                [
                    "Kvqamngw",
                    "Lenguaje"
                ],
                [
                    "Cdinnylg",
                    "Matem\u00e1ticas"
                ],
                [
                    "Mjelvrnp",
                    "M\u00fasica"
                ],
                [
                    "Nbvukocd",
                    "Orientaci\u00f3n"
                ],
                [
                    "Eyygrfpx",
                    "Qu\u00edmica"
                ],
                [
                    "Ychzycdi",
                    "Religi\u00f3n"
                ],
                [
                    "Vdlrplrh",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "ID": {
            "1": [
                [
                    "Mlvafpyt",
                    "Alem\u00e1n"
                ],
                [
                    "Vccyqwgt",
                    "Biolog\u00eda"
                ],
                [
                    "Zxozenmu",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Xfyryhan",
                    "F\u00edsica"
                ],
                [
                    "Vokwrssi",
                    "Historia"
                ],
                [
                    "Vokwrssi",
                    "Ingl\u00e9s"
                ],
                [
                    "Lhguzsdp",
                    "Lenguaje"
                ],
                [
                    "Bsgruzbz",
                    "Matem\u00e1ticas"
                ],
                [
                    "Artfsbvj",
                    "M\u00fasica"
                ],
                [
                    "Rlybywxl",
                    "Orientaci\u00f3n"
                ],
                [
                    "Lwrkdqhz",
                    "Qu\u00edmica"
                ],
                [
                    "Dlrlhevn",
                    "Religi\u00f3n"
                ],
                [
                    "Hbgzrbec",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IIA": {
            "1": [
                [
                    "Mjelvrnp",
                    "Alem\u00e1n"
                ],
                [
                    "Atzgrmcj",
                    "Biolog\u00eda"
                ],
                [
                    "Pxymekhf",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Lkmhjlav",
                    "F\u00edsica"
                ],
                [
                    "Nolmbzqj",
                    "Historia"
                ],
                [
                    "Ekclmkxn",
                    "Ingl\u00e9s"
                ],
                [
                    "Txhbhqio",
                    "Lenguaje"
                ],
                [
                    "Kbksxvdi",
                    "Matem\u00e1ticas"
                ],
                [
                    "Hbgzrbec",
                    "M\u00fasica"
                ],
                [
                    "Orvyxhyd",
                    "Orientaci\u00f3n"
                ],
                [
                    "Tqeiwlki",
                    "Qu\u00edmica"
                ],
                [
                    "Gvkndpxu",
                    "Religi\u00f3n"
                ],
                [
                    "Nolmbzqj",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IIB": {
            "1": [
                [
                    "Bjczvdlx",
                    "Alem\u00e1n"
                ],
                [
                    "Artfsbvj",
                    "Biolog\u00eda"
                ],
                [
                    "Vdlrplrh",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Xfhyxhmf",
                    "F\u00edsica"
                ],
                [
                    "Eieyagjc",
                    "Historia"
                ],
                [
                    "Hcaebpbd",
                    "Ingl\u00e9s"
                ],
                [
                    "Wrbjwpou",
                    "Lenguaje"
                ],
                [
                    "Tqeiwlki",
                    "Matem\u00e1ticas"
                ],
                [
                    "Btutuqlu",
                    "M\u00fasica"
                ],
                [
                    "Wumylfsy",
                    "Orientaci\u00f3n"
                ],
                [
                    "Kbksxvdi",
                    "Qu\u00edmica"
                ],
                [
                    "Hgcsbhrt",
                    "Religi\u00f3n"
                ],
                [
                    "Eamagaxo",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IIC": {
            "1": [
                [
                    "Izhnrdcv",
                    "Alem\u00e1n"
                ],
                [
                    "Vdlrplrh",
                    "Biolog\u00eda"
                ],
                [
                    "Dwsfwtcu",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Bstpquhk",
                    "F\u00edsica"
                ],
                [
                    "Enctmbwa",
                    "Historia"
                ],
                [
                    "Apkctzml",
                    "Ingl\u00e9s"
                ],
                [
                    "Hcaebpbd",
                    "Lenguaje"
                ],
                [
                    "Jxlritwl",
                    "Matem\u00e1ticas"
                ],
                [
                    "Ztyjwzin",
                    "M\u00fasica"
                ],
                [
                    "Pfqfrspa",
                    "Orientaci\u00f3n"
                ],
                [
                    "Rlybywxl",
                    "Qu\u00edmica"
                ],
                [
                    "Gvkndpxu",
                    "Religi\u00f3n"
                ],
                [
                    "Dwsfwtcu",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IID": {
            "1": [
                [
                    "Pfqfrspa",
                    "Alem\u00e1n"
                ],
                [
                    "Ipgxqoqq",
                    "Biolog\u00eda"
                ],
                [
                    "Oacufynm",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Atzgrmcj",
                    "F\u00edsica"
                ],
                [
                    "Onyodhku",
                    "Historia"
                ],
                [
                    "Lwrkdqhz",
                    "Ingl\u00e9s"
                ],
                [
                    "Ychzycdi",
                    "Lenguaje"
                ],
                [
                    "Suahrayh",
                    "Matem\u00e1ticas"
                ],
                [
                    "Fpqpcfbq",
                    "M\u00fasica"
                ],
                [
                    "Wrbjwpou",
                    "Orientaci\u00f3n"
                ],
                [
                    "Mbkhrirw",
                    "Qu\u00edmica"
                ],
                [
                    "Eyygrfpx",
                    "Religi\u00f3n"
                ],
                [
                    "Ukpzxoex",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "IIIA": {
            "1": [
                [
                    "Wumylfsy",
                    "Alem\u00e1n"
                ],
                [
                    "Bjczvdlx",
                    "Artes_Visuales"
                ],
                [
                    "Yycaxjta",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Gvkndpxu",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Ztyjwzin",
                    "Historia"
                ],
                [
                    "Qthqkwjq",
                    "Ingl\u00e9s"
                ],
                [
                    "Ncnqafso",
                    "Lenguaje"
                ],
                [
                    "Ekclmkxn",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IIIB": {
            "1": [
                [
                    "Xrgtkdbt",
                    "Alem\u00e1n"
                ],
                [
                    "Ycaeozob",
                    "Artes_Visuales"
                ],
                [
                    "Ybufanza",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Suahrayh",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Wrbjwpou",
                    "Historia"
                ],
                [
                    "Mbkhrirw",
                    "Ingl\u00e9s"
                ],
                [
                    "Oueurwlr",
                    "Lenguaje"
                ],
                [
                    "Yokgsgdf",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IIIC": {
            "1": [
                [
                    "Yicoxcly",
                    "Alem\u00e1n"
                ],
                [
                    "Ulvuyjza",
                    "Artes_Visuales"
                ],
                [
                    "Dtqrwfpf",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Vokwrssi",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Dkcpfgmz",
                    "Historia"
                ],
                [
                    "Ipgxqoqq",
                    "Ingl\u00e9s"
                ],
                [
                    "Rlybywxl",
                    "Lenguaje"
                ],
                [
                    "Bstpquhk",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IIID": {
            "1": [
                [
                    "Ukpzxoex",
                    "Alem\u00e1n"
                ],
                [
                    "Fjmedzyi",
                    "Artes_Visuales"
                ],
                [
                    "Cdajgsjh",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Dwsfwtcu",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Fpqpcfbq",
                    "Historia"
                ],
                [
                    "Xulhdtye",
                    "Ingl\u00e9s"
                ],
                [
                    "Upmsvroi",
                    "Lenguaje"
                ],
                [
                    "Dwivygdq",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IVA": {
            "1": [
                [
                    "Yiqzsxsm",
                    "Alem\u00e1n"
                ],
                [
                    "Vkmfgwym",
                    "Artes_Visuales"
                ],
                [
                    "Pwekysoi",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Orvyxhyd",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Weofvsvu",
                    "Historia"
                ],
                [
                    "Jumijrpx",
                    "Ingl\u00e9s"
                ],
                [
                    "Dwivygdq",
                    "Lenguaje"
                ],
                [
                    "Cdinnylg",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IVB": {
            "1": [
                [
                    "Mlvafpyt",
                    "Alem\u00e1n"
                ],
                [
                    "Xfhyxhmf",
                    "Artes_Visuales"
                ],
                [
                    "Jjjbjxan",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Xulhdtye",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Ylbruxtg",
                    "Historia"
                ],
                [
                    "Qthqkwjq",
                    "Ingl\u00e9s"
                ],
                [
                    "Peyaycgc",
                    "Lenguaje"
                ],
                [
                    "Yiqzsxsm",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IVC": {
            "1": [
                [
                    "Izhnrdcv",
                    "Alem\u00e1n"
                ],
                [
                    "Ycaeozob",
                    "Artes_Visuales"
                ],
                [
                    "Dwivygdq",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Upmsvroi",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Oacufynm",
                    "Historia"
                ],
                [
                    "Ukpzxoex",
                    "Ingl\u00e9s"
                ],
                [
                    "Igijmzip",
                    "Lenguaje"
                ],
                [
                    "Qthqkwjq",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "IVD": {
            "1": [
                [
                    "Ncnqafso",
                    "Alem\u00e1n"
                ],
                [
                    "Xfhyxhmf",
                    "Artes_Visuales"
                ],
                [
                    "Ybufanza",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "Atzgrmcj",
                    "F\u00edsica"
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
                    "Geograf\u00eda"
                ],
                [
                    "Oacufynm",
                    "Historia"
                ],
                [
                    "Yycaxjta",
                    "Ingl\u00e9s"
                ],
                [
                    "Lhguzsdp",
                    "Lenguaje"
                ],
                [
                    "Zpijftra",
                    "Matem\u00e1ticas"
                ]
            ]
        }
    },
    "ramos_por_curso": {
        "1A": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "1B": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "1C": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "1D": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "2A": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "2B": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "2C": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "2D": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "3A": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "3B": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "3C": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "3D": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "4A": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "4B": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "4C": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "4D": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "5A": {
            "Orientaci\u00f3n": 1,
            "Lenguaje": 6,
            "Ingl\u00e9s": 4,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Geograf\u00eda": 2,
            "Historia": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Religi\u00f3n": 2,
            "M\u00fasica": 2,
            "Artes_Visuales": 2,
            "Tecnolog\u00eda": 2
        },
        "5B": {
            "Orientaci\u00f3n": 1,
            "Lenguaje": 6,
            "Ingl\u00e9s": 4,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Geograf\u00eda": 2,
            "Historia": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Religi\u00f3n": 2,
            "M\u00fasica": 2,
            "Artes_Visuales": 2,
            "Tecnolog\u00eda": 2
        },
        "5C": {
            "Orientaci\u00f3n": 1,
            "Lenguaje": 6,
            "Ingl\u00e9s": 4,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Geograf\u00eda": 2,
            "Historia": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Religi\u00f3n": 2,
            "M\u00fasica": 2,
            "Artes_Visuales": 2,
            "Tecnolog\u00eda": 2
        },
        "5D": {
            "Orientaci\u00f3n": 1,
            "Lenguaje": 6,
            "Ingl\u00e9s": 4,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Geograf\u00eda": 2,
            "Historia": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Religi\u00f3n": 2,
            "M\u00fasica": 2,
            "Artes_Visuales": 2,
            "Tecnolog\u00eda": 2
        },
        "6A": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "6B": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "6C": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "6D": {
            "Orientaci\u00f3n": 1,
            "Educaci\u00f3n_F\u00edsica": 3,
            "Lenguaje": 7,
            "Matem\u00e1ticas": 6,
            "Alem\u00e1n": 6,
            "Ciencias_Naturales": 3,
            "Religi\u00f3n": 2,
            "Historia": 3,
            "Taller_Comprensi\u00f3n_Lectora": 1,
            "M\u00fasica": 2,
            "Tecnolog\u00eda": 2,
            "Artes_Visuales": 2
        },
        "7A": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "7B": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "7C": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "7D": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "8A": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "8B": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "8C": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "8D": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IA": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IB": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IC": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "ID": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IIA": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IIB": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IIC": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IID": {
            "Matem\u00e1ticas": 6,
            "Orientaci\u00f3n": 1,
            "Religi\u00f3n": 2,
            "Alem\u00e1n": 6,
            "Lenguaje": 6,
            "Tecnolog\u00eda": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Qu\u00edmica": 2,
            "Historia": 4,
            "Biolog\u00eda": 2,
            "F\u00edsica": 2,
            "Ingl\u00e9s": 4,
            "M\u00fasica": 2
        },
        "IIIA": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IIIB": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IIIC": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IIID": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IVA": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IVB": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IVC": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
        },
        "IVD": {
            "Lenguaje": 4,
            "Matem\u00e1ticas": 4,
            "Historia": 3,
            "Ciencias_Sociales": 2,
            "Artes_Visuales": 2,
            "Educaci\u00f3n_F\u00edsica": 2,
            "Consejo_de_Curso": 1,
            "Ingl\u00e9s": 4,
            "Geograf\u00eda": 3,
            "Biolog\u00eda": 3,
            "G2": 4,
            "Alem\u00e1n": 5,
            "F\u00edsica": 3,
            "G3": 2
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
                    "Matem\u00e1ticas"
                ],
                [
                    "8A",
                    "F\u00edsica"
                ],
                [
                    "IIC",
                    "Ingl\u00e9s"
                ]
            ]
        },
        "Artfsbvj": {
            "1": [
                [
                    "1C",
                    "Alem\u00e1n"
                ],
                [
                    "2A",
                    "Matem\u00e1ticas"
                ],
                [
                    "3A",
                    "Orientaci\u00f3n"
                ],
                [
                    "3A",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "6A",
                    "Religi\u00f3n"
                ],
                [
                    "ID",
                    "M\u00fasica"
                ],
                [
                    "IIB",
                    "Biolog\u00eda"
                ]
            ]
        },
        "Atkvuhru": {
            "1": [
                [
                    "3D",
                    "Tecnolog\u00eda"
                ],
                [
                    "6A",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "7A",
                    "Matem\u00e1ticas"
                ],
                [
                    "7C",
                    "Matem\u00e1ticas"
                ],
                [
                    "7C",
                    "Biolog\u00eda"
                ]
            ]
        },
        "Atzgrmcj": {
            "1": [
                [
                    "1A",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "1C",
                    "Artes_Visuales"
                ],
                [
                    "3B",
                    "Orientaci\u00f3n"
                ],
                [
                    "6B",
                    "Orientaci\u00f3n"
                ],
                [
                    "8C",
                    "M\u00fasica"
                ],
                [
                    "8D",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IB",
                    "Religi\u00f3n"
                ],
                [
                    "IIA",
                    "Biolog\u00eda"
                ],
                [
                    "IID",
                    "F\u00edsica"
                ],
                [
                    "IVD",
                    "F\u00edsica"
                ]
            ]
        },
        "Bjczvdlx": {
            "1": [
                [
                    "1D",
                    "Religi\u00f3n"
                ],
                [
                    "3C",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "8A",
                    "Ingl\u00e9s"
                ],
                [
                    "IB",
                    "Historia"
                ],
                [
                    "IIB",
                    "Alem\u00e1n"
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
                    "Tecnolog\u00eda"
                ],
                [
                    "3D",
                    "Matem\u00e1ticas"
                ],
                [
                    "7C",
                    "Orientaci\u00f3n"
                ],
                [
                    "7D",
                    "F\u00edsica"
                ],
                [
                    "ID",
                    "Matem\u00e1ticas"
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
                    "Qu\u00edmica"
                ],
                [
                    "IA",
                    "Matem\u00e1ticas"
                ],
                [
                    "IIC",
                    "F\u00edsica"
                ],
                [
                    "IIIC",
                    "Matem\u00e1ticas"
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
                    "Biolog\u00eda"
                ],
                [
                    "IIB",
                    "M\u00fasica"
                ]
            ]
        },
        "Bzbkyeqh": {
            "1": [
                [
                    "1A",
                    "Matem\u00e1ticas"
                ],
                [
                    "1A",
                    "Religi\u00f3n"
                ],
                [
                    "3D",
                    "Religi\u00f3n"
                ],
                [
                    "5A",
                    "Ingl\u00e9s"
                ],
                [
                    "7A",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Orientaci\u00f3n"
                ],
                [
                    "IIID",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IIID",
                    "Biolog\u00eda"
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
                    "M\u00fasica"
                ],
                [
                    "IA",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Matem\u00e1ticas"
                ],
                [
                    "IVA",
                    "Matem\u00e1ticas"
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
                    "M\u00fasica"
                ],
                [
                    "6D",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "7A",
                    "Qu\u00edmica"
                ],
                [
                    "8C",
                    "Orientaci\u00f3n"
                ],
                [
                    "IVC",
                    "Geograf\u00eda"
                ]
            ]
        },
        "Cjntorhr": {
            "1": [
                [
                    "2A",
                    "Orientaci\u00f3n"
                ],
                [
                    "2B",
                    "Alem\u00e1n"
                ],
                [
                    "2C",
                    "Alem\u00e1n"
                ],
                [
                    "6B",
                    "Tecnolog\u00eda"
                ],
                [
                    "8D",
                    "Qu\u00edmica"
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
                    "Tecnolog\u00eda"
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
                    "Alem\u00e1n"
                ],
                [
                    "7D",
                    "Lenguaje"
                ],
                [
                    "8D",
                    "Alem\u00e1n"
                ],
                [
                    "ID",
                    "Religi\u00f3n"
                ]
            ]
        },
        "Dtqrwfpf": {
            "1": [
                [
                    "5C",
                    "Tecnolog\u00eda"
                ],
                [
                    "8B",
                    "Alem\u00e1n"
                ],
                [
                    "IA",
                    "Biolog\u00eda"
                ],
                [
                    "IC",
                    "Historia"
                ],
                [
                    "IIIC",
                    "Biolog\u00eda"
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
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "IIID",
                    "Matem\u00e1ticas"
                ],
                [
                    "IVA",
                    "Lenguaje"
                ],
                [
                    "IVC",
                    "Biolog\u00eda"
                ]
            ]
        },
        "Dwsfwtcu": {
            "1": [
                [
                    "1C",
                    "Orientaci\u00f3n"
                ],
                [
                    "7A",
                    "Religi\u00f3n"
                ],
                [
                    "8B",
                    "Qu\u00edmica"
                ],
                [
                    "8B",
                    "Biolog\u00eda"
                ],
                [
                    "IB",
                    "Ingl\u00e9s"
                ],
                [
                    "IIC",
                    "Tecnolog\u00eda"
                ],
                [
                    "IIC",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IIID",
                    "Consejo_de_Curso"
                ],
                [
                    "IIID",
                    "F\u00edsica"
                ]
            ]
        },
        "Eamagaxo": {
            "1": [
                [
                    "1D",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "3D",
                    "M\u00fasica"
                ],
                [
                    "IB",
                    "M\u00fasica"
                ],
                [
                    "IIB",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "Eieyagjc": {
            "1": [
                [
                    "1A",
                    "Alem\u00e1n"
                ],
                [
                    "6D",
                    "M\u00fasica"
                ],
                [
                    "7A",
                    "Alem\u00e1n"
                ],
                [
                    "8D",
                    "Religi\u00f3n"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "4C",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "IIA",
                    "Ingl\u00e9s"
                ],
                [
                    "IIIA",
                    "Matem\u00e1ticas"
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
                    "Religi\u00f3n"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "4C",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "7C",
                    "M\u00fasica"
                ],
                [
                    "8D",
                    "Biolog\u00eda"
                ],
                [
                    "IC",
                    "Qu\u00edmica"
                ],
                [
                    "IID",
                    "Religi\u00f3n"
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
                    "Religi\u00f3n"
                ],
                [
                    "4D",
                    "Tecnolog\u00eda"
                ],
                [
                    "6A",
                    "Artes_Visuales"
                ],
                [
                    "7A",
                    "Ingl\u00e9s"
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
                    "Alem\u00e1n"
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
                    "Tecnolog\u00eda"
                ],
                [
                    "5B",
                    "Tecnolog\u00eda"
                ],
                [
                    "6A",
                    "Orientaci\u00f3n"
                ],
                [
                    "6C",
                    "Orientaci\u00f3n"
                ],
                [
                    "7C",
                    "Tecnolog\u00eda"
                ],
                [
                    "7C",
                    "F\u00edsica"
                ],
                [
                    "8D",
                    "Tecnolog\u00eda"
                ],
                [
                    "IID",
                    "M\u00fasica"
                ],
                [
                    "IIID",
                    "Historia"
                ],
                [
                    "IVD",
                    "Geograf\u00eda"
                ]
            ]
        },
        "Fswbqxvq": {
            "1": [
                [
                    "3A",
                    "Religi\u00f3n"
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
                    "Alem\u00e1n"
                ],
                [
                    "5C",
                    "M\u00fasica"
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
                    "Orientaci\u00f3n"
                ],
                [
                    "8A",
                    "Tecnolog\u00eda"
                ],
                [
                    "IIA",
                    "Religi\u00f3n"
                ],
                [
                    "IIC",
                    "Religi\u00f3n"
                ],
                [
                    "IIIA",
                    "F\u00edsica"
                ]
            ]
        },
        "Hbgzrbec": {
            "1": [
                [
                    "3C",
                    "Tecnolog\u00eda"
                ],
                [
                    "5A",
                    "Lenguaje"
                ],
                [
                    "IB",
                    "Matem\u00e1ticas"
                ],
                [
                    "ID",
                    "Tecnolog\u00eda"
                ],
                [
                    "IIA",
                    "M\u00fasica"
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
                    "Religi\u00f3n"
                ],
                [
                    "IIB",
                    "Ingl\u00e9s"
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
                    "Alem\u00e1n"
                ],
                [
                    "7D",
                    "Biolog\u00eda"
                ],
                [
                    "8D",
                    "Matem\u00e1ticas"
                ],
                [
                    "IIB",
                    "Religi\u00f3n"
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
                    "Ingl\u00e9s"
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
                    "M\u00fasica"
                ],
                [
                    "4D",
                    "M\u00fasica"
                ],
                [
                    "6A",
                    "M\u00fasica"
                ],
                [
                    "6C",
                    "Lenguaje"
                ],
                [
                    "6C",
                    "Alem\u00e1n"
                ]
            ]
        },
        "Ipgxqoqq": {
            "1": [
                [
                    "5B",
                    "Matem\u00e1ticas"
                ],
                [
                    "5D",
                    "Tecnolog\u00eda"
                ],
                [
                    "7B",
                    "Lenguaje"
                ],
                [
                    "IID",
                    "Biolog\u00eda"
                ],
                [
                    "IIIC",
                    "Ingl\u00e9s"
                ]
            ]
        },
        "Izdefgii": {
            "1": [
                [
                    "3C",
                    "M\u00fasica"
                ],
                [
                    "5B",
                    "Geograf\u00eda"
                ],
                [
                    "7B",
                    "F\u00edsica"
                ],
                [
                    "IIIC",
                    "Geograf\u00eda"
                ]
            ]
        },
        "Izhnrdcv": {
            "1": [
                [
                    "2D",
                    "Orientaci\u00f3n"
                ],
                [
                    "5A",
                    "Orientaci\u00f3n"
                ],
                [
                    "5D",
                    "Lenguaje"
                ],
                [
                    "IIC",
                    "Alem\u00e1n"
                ],
                [
                    "IVC",
                    "Alem\u00e1n"
                ]
            ]
        },
        "Izxqvpvk": {
            "1": [
                [
                    "6C",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "Jjjbjxan": {
            "1": [
                [
                    "3B",
                    "Alem\u00e1n"
                ],
                [
                    "4A",
                    "M\u00fasica"
                ],
                [
                    "8A",
                    "Alem\u00e1n"
                ],
                [
                    "IVB",
                    "Biolog\u00eda"
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
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "8C",
                    "Alem\u00e1n"
                ],
                [
                    "IVA",
                    "Ingl\u00e9s"
                ]
            ]
        },
        "Jxlritwl": {
            "1": [
                [
                    "5B",
                    "Religi\u00f3n"
                ],
                [
                    "8A",
                    "Historia"
                ],
                [
                    "IIC",
                    "Matem\u00e1ticas"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "IIB",
                    "Qu\u00edmica"
                ],
                [
                    "IIIB",
                    "G2"
                ],
                [
                    "IVB",
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        },
        "Kdfpngqg": {
            "1": [
                [
                    "4A",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IA",
                    "Tecnolog\u00eda"
                ]
            ]
        },
        "Kgpidnxy": {
            "1": [
                [
                    "1D",
                    "Orientaci\u00f3n"
                ],
                [
                    "3A",
                    "M\u00fasica"
                ],
                [
                    "4A",
                    "Lenguaje"
                ],
                [
                    "7B",
                    "Biolog\u00eda"
                ],
                [
                    "IIIA",
                    "Geograf\u00eda"
                ],
                [
                    "IIIC",
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        },
        "Ktalejxl": {
            "1": [
                [
                    "2A",
                    "Tecnolog\u00eda"
                ],
                [
                    "2C",
                    "Matem\u00e1ticas"
                ],
                [
                    "5A",
                    "Ciencias_Naturales"
                ],
                [
                    "6D",
                    "Alem\u00e1n"
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
                    "Matem\u00e1ticas"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "ID",
                    "Lenguaje"
                ],
                [
                    "IVC",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "2D",
                    "Taller_Comprensi\u00f3n_Lectora"
                ]
            ]
        },
        "Lkmhjlav": {
            "1": [
                [
                    "1D",
                    "Matem\u00e1ticas"
                ],
                [
                    "2B",
                    "Religi\u00f3n"
                ],
                [
                    "5D",
                    "Ingl\u00e9s"
                ],
                [
                    "IIA",
                    "F\u00edsica"
                ]
            ]
        },
        "Lwrkdqhz": {
            "1": [
                [
                    "5C",
                    "Orientaci\u00f3n"
                ],
                [
                    "7C",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "ID",
                    "Qu\u00edmica"
                ],
                [
                    "IID",
                    "Ingl\u00e9s"
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
                    "Orientaci\u00f3n"
                ],
                [
                    "IID",
                    "Qu\u00edmica"
                ],
                [
                    "IIIB",
                    "Ingl\u00e9s"
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
                    "Alem\u00e1n"
                ],
                [
                    "6B",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "8B",
                    "Ingl\u00e9s"
                ],
                [
                    "IB",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IIIB",
                    "Geograf\u00eda"
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
                    "M\u00fasica"
                ],
                [
                    "IIA",
                    "Alem\u00e1n"
                ],
                [
                    "IIIB",
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        },
        "Mlvafpyt": {
            "1": [
                [
                    "1A",
                    "Tecnolog\u00eda"
                ],
                [
                    "6C",
                    "Ciencias_Naturales"
                ],
                [
                    "ID",
                    "Alem\u00e1n"
                ],
                [
                    "IVB",
                    "Alem\u00e1n"
                ]
            ]
        },
        "Mmbudkeu": {
            "1": [
                [
                    "1C",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "2B",
                    "Orientaci\u00f3n"
                ],
                [
                    "3A",
                    "Artes_Visuales"
                ],
                [
                    "5A",
                    "M\u00fasica"
                ],
                [
                    "5C",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "5A",
                    "Geograf\u00eda"
                ],
                [
                    "8C",
                    "Historia"
                ],
                [
                    "IC",
                    "Orientaci\u00f3n"
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
                    "M\u00fasica"
                ],
                [
                    "IIIA",
                    "Lenguaje"
                ],
                [
                    "IVA",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IVD",
                    "Alem\u00e1n"
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
                    "Geograf\u00eda"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "6C",
                    "Artes_Visuales"
                ],
                [
                    "7C",
                    "Religi\u00f3n"
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
                    "Ingl\u00e9s"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "3A",
                    "Matem\u00e1ticas"
                ],
                [
                    "5D",
                    "Orientaci\u00f3n"
                ],
                [
                    "IIA",
                    "Tecnolog\u00eda"
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
                    "Tecnolog\u00eda"
                ],
                [
                    "2C",
                    "Ciencias_Naturales"
                ],
                [
                    "7B",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IA",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IID",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Alem\u00e1n"
                ],
                [
                    "7A",
                    "Tecnolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "7D",
                    "Qu\u00edmica"
                ],
                [
                    "8B",
                    "Orientaci\u00f3n"
                ],
                [
                    "8D",
                    "Orientaci\u00f3n"
                ],
                [
                    "IIA",
                    "Orientaci\u00f3n"
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
                    "F\u00edsica"
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
                    "Ingl\u00e9s"
                ],
                [
                    "6D",
                    "Religi\u00f3n"
                ],
                [
                    "8C",
                    "F\u00edsica"
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
                    "Tecnolog\u00eda"
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
                    "Religi\u00f3n"
                ],
                [
                    "4D",
                    "Religi\u00f3n"
                ],
                [
                    "5D",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "7D",
                    "Tecnolog\u00eda"
                ],
                [
                    "IC",
                    "Biolog\u00eda"
                ],
                [
                    "IIC",
                    "Orientaci\u00f3n"
                ],
                [
                    "IID",
                    "Alem\u00e1n"
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
                    "Orientaci\u00f3n"
                ],
                [
                    "3D",
                    "Alem\u00e1n"
                ],
                [
                    "4D",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "5C",
                    "Religi\u00f3n"
                ],
                [
                    "7A",
                    "Historia"
                ],
                [
                    "IVA",
                    "Biolog\u00eda"
                ]
            ]
        },
        "Pxymekhf": {
            "1": [
                [
                    "1A",
                    "M\u00fasica"
                ],
                [
                    "4D",
                    "Alem\u00e1n"
                ],
                [
                    "5D",
                    "Religi\u00f3n"
                ],
                [
                    "IC",
                    "Ingl\u00e9s"
                ],
                [
                    "IIA",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "7D",
                    "M\u00fasica"
                ],
                [
                    "IC",
                    "Alem\u00e1n"
                ],
                [
                    "IVB",
                    "Geograf\u00eda"
                ]
            ]
        },
        "Qthqkwjq": {
            "1": [
                [
                    "1B",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "5D",
                    "Artes_Visuales"
                ],
                [
                    "IIIA",
                    "Ingl\u00e9s"
                ],
                [
                    "IVB",
                    "Ingl\u00e9s"
                ],
                [
                    "IVC",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "Rlybywxl": {
            "1": [
                [
                    "4D",
                    "Orientaci\u00f3n"
                ],
                [
                    "5B",
                    "Historia"
                ],
                [
                    "6D",
                    "Orientaci\u00f3n"
                ],
                [
                    "7B",
                    "M\u00fasica"
                ],
                [
                    "8B",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IB",
                    "F\u00edsica"
                ],
                [
                    "ID",
                    "Orientaci\u00f3n"
                ],
                [
                    "IIC",
                    "Qu\u00edmica"
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
                    "Alem\u00e1n"
                ],
                [
                    "7C",
                    "Alem\u00e1n"
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
                    "M\u00fasica"
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
                    "M\u00fasica"
                ],
                [
                    "8B",
                    "Historia"
                ],
                [
                    "IID",
                    "Matem\u00e1ticas"
                ],
                [
                    "IIIB",
                    "F\u00edsica"
                ]
            ]
        },
        "Svixsrbd": {
            "1": [
                [
                    "4D",
                    "Matem\u00e1ticas"
                ],
                [
                    "6C",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "6C",
                    "M\u00fasica"
                ],
                [
                    "7B",
                    "Religi\u00f3n"
                ],
                [
                    "8B",
                    "Tecnolog\u00eda"
                ],
                [
                    "IIIB",
                    "Consejo_de_Curso"
                ],
                [
                    "IVA",
                    "Geograf\u00eda"
                ]
            ]
        },
        "Tiifkdsx": {
            "1": [
                [
                    "1B",
                    "Matem\u00e1ticas"
                ],
                [
                    "1C",
                    "Lenguaje"
                ],
                [
                    "4B",
                    "Tecnolog\u00eda"
                ],
                [
                    "5A",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "6B",
                    "M\u00fasica"
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
                    "Religi\u00f3n"
                ],
                [
                    "IIA",
                    "Qu\u00edmica"
                ],
                [
                    "IIB",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "Trnctbzf": {
            "1": [
                [
                    "2D",
                    "Matem\u00e1ticas"
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
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        },
        "Txhbhqio": {
            "1": [
                [
                    "6B",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "7D",
                    "Alem\u00e1n"
                ],
                [
                    "8B",
                    "Matem\u00e1ticas"
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
                    "Alem\u00e1n"
                ],
                [
                    "IID",
                    "Tecnolog\u00eda"
                ],
                [
                    "IIID",
                    "Alem\u00e1n"
                ],
                [
                    "IVC",
                    "Ingl\u00e9s"
                ]
            ]
        },
        "Ulvuyjza": {
            "1": [
                [
                    "2A",
                    "Religi\u00f3n"
                ],
                [
                    "4B",
                    "Religi\u00f3n"
                ],
                [
                    "4C",
                    "Tecnolog\u00eda"
                ],
                [
                    "6B",
                    "Historia"
                ],
                [
                    "7C",
                    "Ingl\u00e9s"
                ],
                [
                    "8C",
                    "Tecnolog\u00eda"
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
                    "Matem\u00e1ticas"
                ],
                [
                    "7A",
                    "F\u00edsica"
                ],
                [
                    "IIID",
                    "Lenguaje"
                ],
                [
                    "IVC",
                    "F\u00edsica"
                ]
            ]
        },
        "Uskngdik": {
            "1": [
                [
                    "1B",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "1C",
                    "Tecnolog\u00eda"
                ],
                [
                    "2D",
                    "Religi\u00f3n"
                ],
                [
                    "3C",
                    "Historia"
                ],
                [
                    "4C",
                    "M\u00fasica"
                ],
                [
                    "6A",
                    "Tecnolog\u00eda"
                ],
                [
                    "6D",
                    "Tecnolog\u00eda"
                ],
                [
                    "7A",
                    "Orientaci\u00f3n"
                ],
                [
                    "7A",
                    "Biolog\u00eda"
                ],
                [
                    "8D",
                    "F\u00edsica"
                ]
            ]
        },
        "Uvpdhdwa": {
            "1": [
                [
                    "1C",
                    "Religi\u00f3n"
                ],
                [
                    "3C",
                    "Orientaci\u00f3n"
                ],
                [
                    "4A",
                    "Matem\u00e1ticas"
                ],
                [
                    "4A",
                    "Religi\u00f3n"
                ],
                [
                    "6D",
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        },
        "Uzkjwjne": {
            "1": [
                [
                    "1C",
                    "Matem\u00e1ticas"
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
                    "M\u00fasica"
                ],
                [
                    "8D",
                    "M\u00fasica"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "5D",
                    "Ciencias_Naturales"
                ],
                [
                    "6A",
                    "Alem\u00e1n"
                ],
                [
                    "ID",
                    "Biolog\u00eda"
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
                    "Ingl\u00e9s"
                ],
                [
                    "IC",
                    "Tecnolog\u00eda"
                ],
                [
                    "IIB",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IIC",
                    "Biolog\u00eda"
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
                    "Alem\u00e1n"
                ],
                [
                    "6A",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "7D",
                    "Religi\u00f3n"
                ],
                [
                    "IA",
                    "Alem\u00e1n"
                ],
                [
                    "ID",
                    "Historia"
                ],
                [
                    "ID",
                    "Ingl\u00e9s"
                ],
                [
                    "IIIC",
                    "F\u00edsica"
                ]
            ]
        },
        "Vvfythjg": {
            "1": [
                [
                    "2B",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IC",
                    "F\u00edsica"
                ]
            ]
        },
        "Weofvsvu": {
            "1": [
                [
                    "3B",
                    "M\u00fasica"
                ],
                [
                    "3C",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Orientaci\u00f3n"
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
                    "Tecnolog\u00eda"
                ],
                [
                    "IIB",
                    "Lenguaje"
                ],
                [
                    "IID",
                    "Orientaci\u00f3n"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "6C",
                    "Matem\u00e1ticas"
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
                    "Qu\u00edmica"
                ]
            ]
        },
        "Wumylfsy": {
            "1": [
                [
                    "2D",
                    "Tecnolog\u00eda"
                ],
                [
                    "8A",
                    "Matem\u00e1ticas"
                ],
                [
                    "8A",
                    "M\u00fasica"
                ],
                [
                    "IIB",
                    "Orientaci\u00f3n"
                ],
                [
                    "IIIA",
                    "Alem\u00e1n"
                ]
            ]
        },
        "Wvmqroil": {
            "1": [
                [
                    "5C",
                    "Geograf\u00eda"
                ],
                [
                    "6B",
                    "Matem\u00e1ticas"
                ],
                [
                    "6B",
                    "Ciencias_Naturales"
                ],
                [
                    "8C",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Alem\u00e1n"
                ],
                [
                    "7B",
                    "Matem\u00e1ticas"
                ],
                [
                    "8C",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "Xfhyxhmf": {
            "1": [
                [
                    "1D",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "2D",
                    "Historia"
                ],
                [
                    "3B",
                    "Religi\u00f3n"
                ],
                [
                    "4D",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "8B",
                    "F\u00edsica"
                ],
                [
                    "IIB",
                    "F\u00edsica"
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
                    "M\u00fasica"
                ],
                [
                    "3A",
                    "Historia"
                ],
                [
                    "3D",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "4B",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "7C",
                    "Qu\u00edmica"
                ],
                [
                    "7D",
                    "Ingl\u00e9s"
                ],
                [
                    "IA",
                    "Orientaci\u00f3n"
                ],
                [
                    "ID",
                    "F\u00edsica"
                ],
                [
                    "IIIA",
                    "Educaci\u00f3n_F\u00edsica"
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
                    "Orientaci\u00f3n"
                ],
                [
                    "4C",
                    "Orientaci\u00f3n"
                ],
                [
                    "6B",
                    "Religi\u00f3n"
                ],
                [
                    "IIIB",
                    "Alem\u00e1n"
                ],
                [
                    "IVD",
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        },
        "Xtknjgfi": {
            "1": [
                [
                    "1C",
                    "M\u00fasica"
                ],
                [
                    "2B",
                    "Tecnolog\u00eda"
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
                    "Tecnolog\u00eda"
                ],
                [
                    "7B",
                    "Tecnolog\u00eda"
                ],
                [
                    "IA",
                    "F\u00edsica"
                ],
                [
                    "IIID",
                    "Ingl\u00e9s"
                ],
                [
                    "IVB",
                    "F\u00edsica"
                ]
            ]
        },
        "Xwmgnbka": {
            "1": [
                [
                    "1D",
                    "Tecnolog\u00eda"
                ],
                [
                    "3C",
                    "Lenguaje"
                ],
                [
                    "4C",
                    "Alem\u00e1n"
                ],
                [
                    "7B",
                    "Orientaci\u00f3n"
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
                    "Qu\u00edmica"
                ],
                [
                    "IIIB",
                    "Biolog\u00eda"
                ],
                [
                    "IVD",
                    "Biolog\u00eda"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "7B",
                    "Ingl\u00e9s"
                ],
                [
                    "8C",
                    "Ingl\u00e9s"
                ],
                [
                    "IA",
                    "Qu\u00edmica"
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
                    "Religi\u00f3n"
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
                    "Religi\u00f3n"
                ],
                [
                    "6A",
                    "Matem\u00e1ticas"
                ],
                [
                    "7D",
                    "Orientaci\u00f3n"
                ],
                [
                    "IIIC",
                    "Alem\u00e1n"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "5A",
                    "Religi\u00f3n"
                ],
                [
                    "6C",
                    "Religi\u00f3n"
                ],
                [
                    "6C",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "8C",
                    "Biolog\u00eda"
                ],
                [
                    "IVA",
                    "Alem\u00e1n"
                ],
                [
                    "IVB",
                    "Matem\u00e1ticas"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "5D",
                    "Geograf\u00eda"
                ],
                [
                    "8B",
                    "M\u00fasica"
                ],
                [
                    "IA",
                    "Religi\u00f3n"
                ],
                [
                    "IB",
                    "Alem\u00e1n"
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
                    "Matem\u00e1ticas"
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
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "5D",
                    "Historia"
                ],
                [
                    "7B",
                    "Alem\u00e1n"
                ],
                [
                    "IIIA",
                    "Biolog\u00eda"
                ],
                [
                    "IVD",
                    "Ingl\u00e9s"
                ]
            ]
        },
        "Zcnkzivy": {
            "1": [
                [
                    "1B",
                    "M\u00fasica"
                ],
                [
                    "1B",
                    "Artes_Visuales"
                ],
                [
                    "4A",
                    "Orientaci\u00f3n"
                ],
                [
                    "4B",
                    "Orientaci\u00f3n"
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
                    "Qu\u00edmica"
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
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IA",
                    "M\u00fasica"
                ],
                [
                    "IB",
                    "Biolog\u00eda"
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
                    "Religi\u00f3n"
                ],
                [
                    "3D",
                    "Artes_Visuales"
                ],
                [
                    "4A",
                    "Alem\u00e1n"
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
                    "Orientaci\u00f3n"
                ],
                [
                    "1D",
                    "Alem\u00e1n"
                ],
                [
                    "8A",
                    "Lenguaje"
                ],
                [
                    "IC",
                    "Educaci\u00f3n_F\u00edsica"
                ],
                [
                    "IVD",
                    "Matem\u00e1ticas"
                ]
            ]
        },
        "Ztyjwzin": {
            "1": [
                [
                    "2B",
                    "Matem\u00e1ticas"
                ],
                [
                    "4B",
                    "Artes_Visuales"
                ],
                [
                    "IIC",
                    "M\u00fasica"
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
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "2C",
                    "M\u00fasica"
                ],
                [
                    "3B",
                    "Artes_Visuales"
                ],
                [
                    "4A",
                    "Taller_Comprensi\u00f3n_Lectora"
                ],
                [
                    "5B",
                    "Ciencias_Naturales"
                ],
                [
                    "5D",
                    "Alem\u00e1n"
                ],
                [
                    "ID",
                    "Educaci\u00f3n_F\u00edsica"
                ]
            ]
        }
    },
    "multiples_cursos": [

    ],
    "multiples_profesores": [

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