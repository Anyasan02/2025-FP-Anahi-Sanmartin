# Programa 1: Búsqueda en Matriz Bidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición si lo encuentra
    return None  # Retorna None si no está

# Matriz 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Solicitar valor a buscar
valor_buscar = int(input("Ingrese el valor a buscar en la matriz: "))
resultado = buscar_valor(matriz, valor_buscar)

if resultado:
    print(f"Valor encontrado en la posición: {resultado}")
else:
    print("Valor no encontrado en la matriz.")
