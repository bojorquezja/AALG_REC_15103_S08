"""
Hacer una funcion recursiva que devuelva el promedio
de una lista de numeros
[2,4,6,4] -> 16/4 = 4
"""
def suma(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma(lista[1:])

def promedio(lista):
    return suma(lista) / len(lista)

numeros = [8, 7, 8, 4]

print("Promedio:", promedio(numeros))