#Creacion de un dicicionario con informacion persona
informacion_personal = {
    "nombre": "Coraline",
    "edad": 23,
    "ciudad": "Amabato",
    "profesion": "Veterinaria"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "loja"

# Agregar una nueva clave-valor para "telefono" si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "1234567890"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)

