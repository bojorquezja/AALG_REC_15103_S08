def suma(lista, n): 
    if n == 0: 
        return 0 
    else: 
        return lista[-n] + suma(lista, n - 1) 
    
numeros = [12, 10, 2, 11, 6, 5] 
print("La lista es:", numeros) 
n = int(input("Ingresa el valor de N: ")) 
print("La suma de los ultimos",n,"números es =>", suma(numeros, n))