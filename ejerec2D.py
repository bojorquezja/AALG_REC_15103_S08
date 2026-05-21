def promedio(lista):
    return promN(lista, len(lista)-1, 0)
        
def promN(lista, n, acc):
    if n == 0:
        return (acc + lista[n] ) / len(lista)
    else:
        acc += lista[n]
        return promN(lista, n - 1, acc)


miLista = [2.0, 4.0, 6.0, 4.0]
resultado = promedio(miLista)
print(f"el promedio de la lista es: {resultado}")