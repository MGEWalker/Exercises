
def procesar_test():
    nombre_fichero = input("Introduce el nombre de un fichero de test: ")

    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
        plantilla = lineas[0].strip()

        for linea in lineas[1:]:
            partes = linea.strip().split('#')
            dni = partes[0]
            respuestas = partes[1]
            print(f"El alumno con DNI {dni} ha respondido {respuestas}")

        print(f"Un alumno perfecto habría respondido {plantilla}")

procesar_test()
