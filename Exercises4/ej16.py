
def es_dígito(c):
    return c in "1234567890"


def secuencias_dígitos(cadena):
    secuencias = []
    secuencia_actual = ""
    
    for char in cadena:
        if es_dígito(char): 
            secuencia_actual += char  
        else:
            if secuencia_actual:  
                secuencias.append(secuencia_actual) 
                secuencia_actual = ""  
    
    if secuencia_actual:  
        secuencias.append(secuencia_actual)
    
    return secuencias

def main():
    cadena = input("Introduce una cadena: ")
    secuencias = secuencias_dígitos(cadena)
    print("La lista de secuencias obtenida es", secuencias)


main()