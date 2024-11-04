def todos_dígitos(cadena):
    posibles="0123456789"
    nodigit=0
    for i in range (0, len(cadena)):
        if cadena[i]  not in posibles:
         nodigit+=1
    if nodigit==0:
        return True
    return False

cadena1=input("Introduce una cadena de caracteres: ")
if todos_dígitos(cadena1):
    print("Todos los caracteres son dígitos")
else:
    print("No todos los caracteres son dígitos")
