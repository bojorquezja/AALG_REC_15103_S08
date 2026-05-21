def promedio(lista, n):
    if n == 0:
        return 0
    else:
        numero_actual = lista[-n]
        numero_siguiente = promedio(lista, n - 1)
        suma = numero_actual + numero_siguiente
    if n == len(lista):
        return suma / len(lista)
    else:
        return suma

miLista = [2, 4, 6, 4]
resultado = promedio(miLista, len(miLista))
print(f"el promedio de la lista es: {resultado}")