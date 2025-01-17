def leer_alturas():
   altura = input('Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...\nAltura en '
                  'metros en el punto kilométrico 0: ')
   lista = []
   i = 0
   while altura != '':
       lista.append(int(altura))
       i += 1
       altura = input(f'Altura en metros en el punto kilométrico {i}: ')
   return lista




def mostrar_tramo(nº, inicio, longitud, desnivel):
   print(f'Tramo de subida número {nº}:')
   print(f'  Entre los puntos kilométricos {inicio} y {inicio + longitud}')
   print(f'  Longitud de {longitud} km')
   print(f'  Desnivel de {desnivel} m')




def mostrar_tramos_subida(alturas):
   if len(alturas) < 2:
       print("Recorrido no válido, con menos de dos puntos")
       return


   tramo = 0
   en_tramo = False
   inicio = 0
   desnivel_acumulado = 0
   for i in range(len(alturas) - 1):
       if alturas[i + 1] > alturas[i]:
           if not en_tramo:
               en_tramo = True
               inicio = i
           desnivel_acumulado += alturas[i + 1] - alturas[i]
       else:
           if en_tramo:
               tramo += 1
               longitud = i - inicio
               mostrar_tramo(tramo, inicio, longitud, desnivel_acumulado)
               en_tramo = False
               desnivel_acumulado = 0
   if en_tramo:
       tramo += 1
       longitud = len(alturas) - 1 - inicio
       mostrar_tramo(tramo, inicio, longitud, desnivel_acumulado)
   if tramo == 0:
       print("Ningún kilómetro es de subida")



def main():
    lista_alturas = leer_alturas()
    if len(lista_alturas) >= 2:
       print(f'Lista de alturas: {lista_alturas}')
    mostrar_tramos_subida(lista_alturas)

main()

