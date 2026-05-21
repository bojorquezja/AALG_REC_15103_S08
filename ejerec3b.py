def invertir_cadena(cadena):
    if len(cadena) == 0:
        return "" 
    else:
        letra_actual = cadena[0] 
        letra_siguiente = invertir_cadena(cadena[1:])
        return letra_siguiente + letra_actual

texto = "abc"
resultado = invertir_cadena(texto)
print(f" abc ---> {resultado}")