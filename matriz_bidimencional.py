# Programa 2: Ordenación de Fila en Matriz Bidimensional

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]  # Intercambio

def mostrar_matriz(m):
    for fila in m:
        print(fila)

# Matriz 3x3
matriz_ordenar = [
    [30, 10, 25],
    [50, 15, 40],
    [70, 5, 60]
]

print("Matriz original:")
mostrar_matriz(matriz_ordenar)

# Selección de fila
fila_a_ordenar = int(input("Ingrese el número de la fila a ordenar (0-2): "))
if 0 <= fila_a_ordenar < 3:
    bubble_sort(matriz_ordenar[fila_a_ordenar])
    print("\nMatriz con la fila ordenada:")
    mostrar_matriz(matriz_ordenar)
else:
    print("Número de fila inválido.")
