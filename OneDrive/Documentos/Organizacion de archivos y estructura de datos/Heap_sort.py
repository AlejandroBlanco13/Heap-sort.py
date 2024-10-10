# Función para reorganizar la lista como un max-heap
def heapify(arr, n, i):
    # Inicializar el nodo más grande como la raíz
    largest = i
    # Índices de los hijos izquierdo y derecho
    left = 2 * i + 1
    right = 2 * i + 2

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        # Llamar recursivamente a heapify
        heapify(arr, n, largest)

# Función principal de Heap Sort
def heap_sort(arr):
    n = len(arr)

    # Construir el max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer cada elemento uno por uno del heap
    for i in range(n - 1, 0, -1):
        # Mover la raíz al final del array
        arr[i], arr[0] = arr[0], arr[i]
        # Llamar a heapify para reducir el heap
        heapify(arr, i, 0)

# Función para mostrar los resultados
def mostrar_resultado(arr):
    print("Lista original:", arr)
    heap_sort(arr)
    print("Lista ordenada:", arr)

# Pruebas con dos listas diferentes
lista1 = [12, 11, 13, 5, 6, 7]
lista2 = [4, 10, 3, 5, 1, 15, 6]

print("Prueba con la primera lista:")
mostrar_resultado(lista1.copy())  # Usamos .copy() para no modificar la lista original

print("\nPrueba con la segunda lista:")
mostrar_resultado(lista2.copy())