def insercion(arr):
    # Contador para operaciones
    operaciones = 0
    
    # Recorremos desde el segundo elemento hasta el final del arreglo
    for i in range(1, len(arr)):
        # Guardamos el elemento actual (clave) que queremos insertar en la parte ordenada
        key = arr[i]
        # Inicializamos j al índice del elemento anterior al actual
        j = i - 1
        # Movemos los elementos de la parte ordenada que son mayores que la clave
        # hacia una posición adelante para hacer espacio
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            operaciones += 1  # Contar cada operación de intercambio
        # Colocamos la clave en la posición correcta
        arr[j + 1] = key
        if j + 1 != i:  # Asegurarse de contar el movimiento de la clave también
            operaciones += 1
    
    # Mostrar las operaciones necesarias
    print(f"Operaciones necesarias: {operaciones}")
    return arr

# Lista de ejemplo
lista = [4, 3, 2, 10, 12, 1, 5]

# Imprimimos el resultado del algoritmo de inserción
print(insercion(lista))
