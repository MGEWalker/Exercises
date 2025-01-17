class Cuenta:
    def __init__(self, saldo):
        self.saldo=saldo

    def ingresar(self, importe ):
        self.saldo+=importe

    def reintegrar(self, importe):
        self.saldo-=importe

    def consultar_saldo(self):
        return self.saldo


def main():
    saldo_inicial=float(input("Introduce cuántos euros quieres como saldo inicial de tu cuenta: "))
    mi_cuenta=Cuenta(saldo_inicial)

    while True:
        print("")
        print("1. Hacer un ingreso")
        print("2. Pedir un reintegro")
        print("3. Consultar el saldo")
        print("4. Salir")
        opción=int(input("Elige una opción: "))
        if opción==4:
            break
        if opción==1:
            mi_cuenta.ingresar(float(input("Introduce cuántos euros quieres ingresar: ")))
        elif opción==2:
            mi_cuenta.reintegrar(float(input("Introduce cuántos euros quieres que se te reintegren: ")))
        else:
            print(f"El saldo actual es {mi_cuenta.consultar_saldo(): .2f} euros")

    print("¡Adiós!")


main()