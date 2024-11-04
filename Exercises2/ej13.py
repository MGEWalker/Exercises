from math import ceil
veces = int(input("¿Cuántas veces prevés utilizar el gimnasio? "))
precio_tarjeta = 50
precio_bono = 20
precio_entrada = 3
coste_tarjeta = precio_tarjeta
print(f"Con tarjeta: {coste_tarjeta} euros.")

bonos_necesarios1= veces // 10
bonos_necesarios = ceil(veces / 10)                                                                  # Dividir el n�mero de usos entre 10 para saber cu�ntos bonos se requieren
coste_bonos_solo = bonos_necesarios * precio_bono
print(f"Con bonos ({bonos_necesarios}): {coste_bonos_solo} euros.")

entradas_extra = veces % 10                                                                     # Saber cu�ntas entradas individuales necesitar�a despu�s de agotar los bonos completos
coste_bonos_y_entradas = (bonos_necesarios1 * precio_bono) + (entradas_extra * precio_entrada)
print(f"Con bonos ({bonos_necesarios1}) y entradas ({entradas_extra}): {coste_bonos_y_entradas} euros.")

mejor_opcion= coste_tarjeta
if coste_bonos_solo < mejor_opcion:
    mejor_opcion = coste_bonos_solo
if coste_bonos_y_entradas < mejor_opcion:
    mejor_opcion = coste_bonos_y_entradas

if mejor_opcion == coste_tarjeta:
        recomendacion = "Recomendación: tarjeta."
elif mejor_opcion == coste_bonos_solo:
        recomendacion = f"Recomendación: bonos. "
else:
    recomendacion = f"Recomendación: bonos  y entradas."
print(recomendacion)
