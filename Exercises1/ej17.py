import math
a11=float(input("Introduce a: "))
b11=float(input("Introduce b: "))
c11=float(input("Introduce c: "))
raiz=((b11**2)-(4*a11*c11))
print("x1 = ", (-b11+(math.sqrt(raiz)))/(2*a11) )
print("x2 = ", (-b11-(math.sqrt(raiz)))/(2*a11) )
