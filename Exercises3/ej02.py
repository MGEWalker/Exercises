def es_triángulo(a,b,c):
    if a>=b+c or b>=a+c or c>=a+b :
        return False
    else:
        return True

lado1 = float(input("Introduce el número a: "))
lado2 = float(input("Introduce el número b: "))
lado3 = float(input("Introduce el número c: "))

if (es_triángulo(lado1, lado2, lado3))==True :
    print("Es un triángulo")
else:
    print("No es un triángulo")