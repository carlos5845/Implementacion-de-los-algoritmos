def burbuja(arr):
    n = len(arr)
    # Recorremos todo el arreglo
    for i in range(n):
        # En cada iteración, la parte final del arreglo se vuelve más ordenada
        # por eso podemos reducir el rango del segundo bucle
        for j in range(0, n-i-1):
            # Comparamos elementos adyacentes y los intercambiamos si están en el orden incorrecto
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Lista de ejemplo
lista = [5, 2, 9, 1, 5, 6]

# Imprimimos el resultado del algoritmo de burbuja
print(burbuja(lista))
