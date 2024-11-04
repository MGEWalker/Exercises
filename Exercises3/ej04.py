
def calcular_cadena_repetida(CadenaC, entero, CadenaS):
    return (str(CadenaC)+str(CadenaS))*(entero-1) + str(CadenaC)


cadena1= str(input("Introduce una cadena: "))
cadena2= str(input("Introduce un separador: "))
veces=int(input("Introduce un máximo de repeticiones: "))

for i in range (1, veces+1):
    print(f'{calcular_cadena_repetida(cadena1, i, cadena2)}')
