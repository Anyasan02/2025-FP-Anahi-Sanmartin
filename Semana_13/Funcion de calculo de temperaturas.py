# Creación de una matriz 3D para almacenar los datos de las temperaturas
# Primera dimensión: Ciudades (Quito, Loja, Machala)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

temperaturas = [
    {"ciudad": "Quito", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 9},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 8},
            {"day": "Viernes", "temp": 9},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 11}
        ]
    ]},
    {"ciudad": "Loja", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 58},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 57},
            {"day": "Viernes", "temp": 57},
            {"day": "Sábado", "temp": 57},
            {"day": "Domingo", "temp": 56}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 56},
            {"day": "Jueves", "temp": 57},
            {"day": "Viernes", "temp": 59},
            {"day": "Sábado", "temp": 62},
            {"day": "Domingo", "temp": 65}
        ]
    ]},
    {"ciudad": "Machala", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 80},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 78}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 77},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 86},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 84},
            {"day": "Martes", "temp": 82},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 77}
        ]
    ]}
]

# Función para calcular el promedio de temperaturas por ciudad
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula el promedio de temperaturas de cada ciudad.

    :param temperaturas: Lista de diccionarios con los datos de las temperaturas.
    :return: Diccionario con las ciudades y su temperatura promedio.
    """
    promedios = {}

    for ciudad in temperaturas:
        total_temp = 0
        total_dias = 0

        for semana in ciudad["semanas"]:
            for dia in semana:
                total_temp += dia["temp"]
                total_dias += 1

        promedio_ciudad = total_temp / total_dias
        promedios[ciudad["ciudad"]] = round(promedio_ciudad, 2)

    return promedios

# Llamar a la función y mostrar los resultados
resultados = calcular_temperatura_promedio(temperaturas)

print("\nPromedio de temperaturas por ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°F")