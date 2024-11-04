def es_triángulo(a,b,c):
    if a>=b+c or b>=a+c or c>=a+b :
        return False
    else:
        return True
def tipo_triángulo(a,b,c):
    if es_triángulo(a,b,c)== True:
        if a == b == c:
            tipo = "equilátero"
        elif a == b or b == c or a == c:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        return (f'{tipo}')
    else:
        return None

lado1 = float(input("Introduce el lado a: "))
lado2 = float(input("Introduce el lado b: "))
lado3 = float(input("Introduce el lado c: "))
while tipo_triángulo(lado1, lado2, lado3)==None:
    print("No es un triángulo")
    lado1 = float(input("Introduce el lado a: "))
    lado2 = float(input("Introduce el lado b: "))
    lado3 = float(input("Introduce el lado c: "))
print (f'Es {tipo_triángulo(lado1, lado2, lado3)}')
