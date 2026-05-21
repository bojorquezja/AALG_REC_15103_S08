"""
invertir una cadena de texto usando una funcion recursiva

abc -> cba
"""
def cadena(texto):
    if len(texto) <= 1:
        return texto
    return cadena(texto[1:]) + texto[0]



original = "abcdfghijklmnopqrstuvwxyz"

resultado = cadena(original)

print(f"{original} - {resultado}") 