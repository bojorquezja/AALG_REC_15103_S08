def promedio(lista, i=0):
    if i == len(lista) - 1:
        return lista[i]
    else:
        return lista[i] + promedio(lista, i + 1)

num = [12, 24, 2, 6, 5]

rpta = promedio(num) / len(num)

print("La lista es:", num)

print("El promedio es:", rpta)