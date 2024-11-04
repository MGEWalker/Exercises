cantidad= float(input("Introduce la cantidad de kWh: "))

precio_tramo1 = 0.05
precio_tramo2 = 0.07
precio_tramo3 = 0.10

if cantidad <= 100:
    importe = cantidad * precio_tramo1
else:
    importe = 100 * precio_tramo1
    cantidad -= 100


    if cantidad <= 150:
        importe += cantidad * precio_tramo2
    else:
        importe += 150 * precio_tramo2
        cantidad -= 150
        importe += cantidad * precio_tramo3

print(f"Importe: {importe:.2f} euros")