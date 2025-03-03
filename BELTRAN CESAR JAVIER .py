def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def search_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return i, j
    return None

# Definir la matriz 3x3
matrix = [
    [9, 5, 3],
    [4, 8, 1],
    [7, 2, 6]
]

# Mostrar la matriz original
print("Matriz original:")
for row in matrix:
    print(row)

# Búsqueda de un valor específico
valor_a_buscar = int(input("Ingrese el valor a buscar: "))
resultado = search_value(matrix, valor_a_buscar)

if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

# Ordenación de una fila específica
fila_a_ordenar = int(input("Ingrese el índice de la fila a ordenar (0-2): "))
if 0 <= fila_a_ordenar < len(matrix):
    matrix[fila_a_ordenar] = bubble_sort(matrix[fila_a_ordenar])
    print("\nMatriz con la fila ordenada:")
    for row in matrix:
        print(row)
else:
    print("Índice de fila no válido.")
