
@/!\ESTE PROGRAMA REESCRIBE LOS PRIMEROS ELEMENTOS DE LA MATRIZ/!\@
@/!\Un cambio para evitar esto es inicializar en subr1 r7 con un valor de 4*dimensión, después en porfinseacaba cambiar r4 por r7/!\@
@/!\Otra posible solución es en la línea 49 sustituir el almacenamiento en memoria con relativo al SP, y en pofinseacaba poner en r0 la dirección del SP y en r1 la dimensión de la matriz/!\@

		@-------------@
		@ZONA DE DATOS@
		@-------------@
    	.data

matriz: .word 1, 2, 3, 4   @ Matriz de ejemplo 2x2 para pruebas
n:      .word 2            @ Dimensión de la matriz (2x2 en este ejemplo)
max:    .word 0            @ Dirección para almacenar el máximo buscado

		@-----------------@
		@PROGRAMA INVOCADOR
		@-----------------@
	.text

main:	ldr r0, =matriz        @ r0 <- dirección de la matriz
    	ldr r1, =n             @ r1 <- dirección de la dimensión de la matriz
    	ldr r1, [r1]           @ r1 <- valor de la dimensión
    	bl subr1               @ Llamada a subr1 (busca el máximo en el vector de sumas)
    	ldr r2, =max           @ r2 <- dirección de max
    	str r0, [r2]           @ Almacena el máximo en max
stop:	wfi                    


@---------------------------------------------------------------------------@
@SUBRUTINA 1: CALCULA EL NÚMERO MÁXIMO DE LA SUMA DE LAS FILAS DE UNA MATRIZ@
@---------------------------------------------------------------------------@

@ Parámetros: r0 = matriz, r1 = dimensión (n)
@ Devuelve: r0 = máximo de las sumas de filas

subr1:
    	push {r4-r7, lr}      @guarda registros y enlace de retorno
	mov r4, r0	      @guardar en r4 la dirección del vector
	mov r5, r1	      @guardar en r5 las dimensiones para ir decrementando
	mov r6, r1	      @guardar en r6 la dimensión
	lsl r6, #2	      @cálculo para colocar en r6 el dato para añadir al incremento (4*dimensión)
	mov r8, r1	      @almacenar en r8 la dimensión para que no se altere

boocle: cmp r5, #0	      @comprobar si ya no quedan filas por calcular
	beq porfinseacaba     @dar el salto al final si ya no quedan filas por analizar, a porfinseacaba
	add r0, r4, r7	      @cálculo de la dirección de memoria de la que se quiere leer, para colocarlo en r0 para la subrutina
	mov r1, r8	      @poner en r1 ladimensión de la fila, para la subrutina 
	bl subr2	      @pasa el control a la subrutina 2
	str r0, [r4, r7]      @como el dato de salida está en r0, ese dato se almacena en la memoria con un desplazamientoel cual hace coincidir que se rescribe el primer dato de la fila
	sub r5, #1	      @decrementa la cantidad de filas que quedan por analizar
	add r7, r7, r6	      @el incremento se calcula como el aumento constante de 4*dimensión (r6)
	b boocle	      @repite el bucle


porfinseacaba:	mov r0, r4    @coloca en r0 la direccío primera del vector, que coincidirá con la de la matriz
		mov r2, r8    @copia la dimensión de la matriz en r2 para poder trabajar con ella
		mul r2, r2    @calcula la cantidad de elemtos de la matriz, ya que el rango del vector es el número de elementos de la matriz porque los resultados de las sumas de las filas sobrescriben el primer elemento de dicha fila
		mov r1, r2    @coloca en r1, la cantidad de elementos del vector
		bl subr3      @pasa el control a la subrutina 3, que devolverá el resultado en r0
		pop {r4-r7, pc}       @ Restaura registros y regresa


@----------------------------------------------------------@
@SUBRUTINA 2: CALCULA LA SUMA DE LOS ELEMENTOS DE UN VECTOR@
@----------------------------------------------------------@

@ Parámetros: r0 = dirección del vector, r1 = dimensión del vector
@ Devuelve: r0 = suma de los elementos


subr2:
    			push {r4-r7, lr}  @ Guarda registros y enlace de retorno
    			mov r3, #0        @ Inicializa la suma en 0

vector_sum_loop:	cmp r1, #0 	  @revisa si quedan elementos por tratar en el vector
			beq vamoacabando  @si no quedan, pasa a la última fase
    			ldr r2, [r0]      @ Carga el siguiente elemento del vector en r3 y avanza
			add r3, r3, r2	  @ añade el valor del elemento a la suma
			sub r1, r1, #1    @decrementa el número de elementos
			add r0, r0, #4	  @aumenta la direcciónde memoria de la que leer el dato
			b vector_sum_loop @repite el bucle

vamoacabando:		mov r0, r3	  @coloca en r0 el resultado de la suma de los elementos del vector
			pop {r4-r7, pc}   @ Restaura registros y regresa




@--------------------------------------------------------@
@SUBRUTINA 3: CALCULA EL ELEMENTO MÁS GRANDE DE UN VECTOR@
@--------------------------------------------------------@

@ Parámetros: r0 = dirección del vector, r1 = dimensión del vector
@ Devuelve: r0 =  el máximo valor de los elementos


subr3:
   		push {r4-r7, lr}   @ Guarda registros y enlace de retorno
		mov r3, #0   	   @r3<- 0

loopardo:    	cmp r1, #0	   @revisa si quedan elementos por tratar en el vector
		beq finalisando	   @si no quedan, pasa a la última fase
		ldr r2, [r0]       @ Carga el elemento del vector
		cmp r2, r3	   @compara el nuevo elemento con lo que es el actual máximo
		blt tero	   @salta si el nuevo elemento es menor
		mov r3, r2 	   @si el nuevo elemento es mayor, actualiza r3

tero:		sub r1, r1, #1	   @decrementa la cantidad de elemntos
		add r0, r0, #4	   @aumenta la dirección para leer un elemto del vector
		b loopardo	   @vuelve a ejecutar el bucle

finalisando:	mov r0, r3 	   @coloca en r0 el número más grande del vector
		pop {r4-r7, pc}	   @devuelve el flujo
