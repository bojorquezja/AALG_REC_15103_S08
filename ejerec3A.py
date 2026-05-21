def invertir(x):
    if len(x) == 1:
        return x
    else:
        return invertir(x[1:]) + x[0]

n=input("Ingrese una cadena de texto: ")
print("Cadena de texto invertida:", invertir(n))