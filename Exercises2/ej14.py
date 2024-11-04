importe_compra = float(input("Introduce el importe de la compra: "))
zona_envio = input("Introduce la zona de envío (A/B/C): ").upper()
socio = input("¿Eres socio (S/N)? ").upper()

gastos_envio = 0
importe_zonaB = 30
importe_zonaC = 69

if importe_compra <= 150:
    if socio == "S":
        base_gastos = 19
    else:
        base_gastos = 25
elif importe_compra <= 750:
    if socio == "S":
        base_gastos = 49
    else:
        base_gastos = 60
elif importe_compra <= 1500:
    if socio == "S":
        base_gastos = 89
    else:
        base_gastos = 120
else:
    if socio == "S":
        base_gastos = (6 * importe_compra) / 100
    else:
        base_gastos = (8 * importe_compra) / 100

if zona_envio == "B":
    gastos_envio = base_gastos + importe_zonaB
elif zona_envio == "C":
    gastos_envio = base_gastos + importe_zonaC
else:
    gastos_envio = base_gastos

print(f'Gastos de envío: {gastos_envio:.2f} euros')
