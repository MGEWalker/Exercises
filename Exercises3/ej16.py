posibles="0123456789"
nodigit=0
cadena=input("Introduce una cadena de caracteres: ")
for i in range (0, len(cadena)):
    if cadena[i]  not in posibles:
     nodigit+=1
if nodigit==0:
    print("Todos los caracteres son dígitos")
else:
    print("No todos los caracteres son dígitos")



