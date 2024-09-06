def seleccion(arr):
    # Recorremos todos los elementos del arreglo
    for i in range(len(arr)):
        # Inicializamos el índice del mínimo como el índice actual
        min_idx = i
        
        # Buscamos el elemento más pequeño en el resto del arreglo
        for j in range(i + 1, len(arr)):
            # Si encontramos un elemento menor que el actual mínimo
            if arr[j] < arr[min_idx]:
                # Actualizamos el índice del mínimo
                min_idx = j
        
        # Intercambiamos el elemento en el índice actual con el elemento más pequeño encontrado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # Retornamos el arreglo ordenado
    return arr

# Lista de ejemplo
lista = [64, 25, 12, 22, 11]

# Imprimimos el resultado del algoritmo de selección
print(seleccion(lista))
