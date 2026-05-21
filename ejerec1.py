"""
Hacer una funcion recursiva que pedira una 
lista y un numero N y retornara la suma de los 
N ultimos numeros
[2,4,6,3] y N = 2  -> Resultado = 6+3=9
"""

def sumaulti(lista, n): 
    if n == 0: 
        return 0 
    return lista[-1] + sumaulti(lista[:-1], n - 1) 

lista = [8, 7, 0, 7] 
n = 2 
print(sumaulti(lista, n))