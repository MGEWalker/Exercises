angulo= float(input("Introduce un ángulo (en grados): "))

if angulo==0:
    print("Nulo")
elif angulo<90:
    print("Agudo")
elif angulo==90:
    print("Recto")
elif angulo<180:
    print("Obtuso")
elif angulo==180:
    print("Llano")
elif angulo<360:
    print("Cóncavo")
else:
    print("Completo")