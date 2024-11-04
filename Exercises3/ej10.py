
def sumar_divisores_propios(x):
    suma_de_divisores=0
    for i in range (1, x):
        if x%i==0:
            suma_de_divisores +=i
    return suma_de_divisores

def son_amigos(primero,segundo):
    if sumar_divisores_propios(primero)==segundo and sumar_divisores_propios(segundo)==primero:
        return True
    return False

numA=int(input(" Introduce un número entero a: "))
numB=int(input(" Introduce un número entero b: "))
if son_amigos(numA,numB):
    print("Los dos números son amigos")
else:
    print("Los dos números no son amigos")

condición=str(input("¿Seguimos comprobando amistades (S/N)?"))
while condición=="S":

    numA = int(input(" Introduce un número entero a: "))
    numB = int(input(" Introduce un número entero b: "))
    if son_amigos(numA, numB):
        print("Los dos números son amigos")
    else:
        print("Los dos números no son amigos")
    condición=str(input("¿Seguimos comprobando amistades (S/N)?"))
print(" ¡Adiós!")