
a = float(input("Introduce el lado a: "))
b = float(input("Introduce el lado b: "))
c = float(input("Introduce el lado c: "))
tipo=""
while a + b <= c or a + c <= b or b + c <= a:
    print("No es un triángulo")
    a = float(input("Introduce el lado a: "))
    b = float(input("Introduce el lado b: "))
    c = float(input("Introduce el lado c: "))




if a == b == c:
    tipo= "equilátero"
elif a == b or b == c or a == c:
    tipo= "isósceles"
else:
    tipo= "escaleno"
print("Es ", tipo)

