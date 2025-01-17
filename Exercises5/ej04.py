
class Coche:
    def __init__(self):
        self.tiempo=0
        self.distancia=0
        self.velocidad=0

    def acelerar(self, incremento_velocidad):
        self.velocidad+=incremento_velocidad

    def decelerar(self, decremento_velocidad):
        self.velocidad-=decremento_velocidad

    def actualizar(self, tiempo):
        self.tiempo+=tiempo
        self.distancia+= (self.velocidad*tiempo)

    def consultar_tiempo(self):
        return self.tiempo

    def consultar_distancia(self):
        return self.distancia

    def consultar_velocidad_actual(self):
        return self.velocidad

    def consultar_velocidad_media(self):
        if self.tiempo>0:
            return (self.distancia/self.tiempo)
        else:
            return None


def main():
    print("Tu coche está inicialmente parado")
    coche=Coche()


    while True:
        print("")
        print("1. Acelerar")
        print("2. Decelerar")
        print("3. Actualizar")
        print("4. Consultar")
        print("5. Salir")
        opción=int(input("Elige una opción: "))
        if opción==5:
            break
        if opción==1:
            coche.acelerar(float(input("Introduce cuántos km/h quieres acelerar: ")))
        elif opción==2:
            coche.decelerar(float(input("Introduce cuántos km/h quieres decelerar:  ")))
        elif opción==3:
            coche.actualizar(float(input("Introduce cuántas horas han pasado: ")))
        else:
            print(f"El tiempo trascurrido es {coche.consultar_tiempo(): .2f} h")
            print(f"La distancia recorrida es {coche.consultar_distancia(): .2f} km")
            print(f"La velocidad actual es {coche.consultar_velocidad_actual(): .2f} km/h")
            if coche.tiempo>0:
              print(f"La velocidad media es {coche.consultar_velocidad_media(): .2f} km/h")
            else:
                print("No puedo calcular la velocidad media si no ha trascurrido tiempo")
    print("¡Adiós!")


main()