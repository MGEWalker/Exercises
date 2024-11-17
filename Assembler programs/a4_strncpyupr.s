
@-------------@
@ZONA DE DATOS@
@-------------@

	.data
a1:	.asciz "Esta es una cadena!"
b1:	.asciz "$$$$$$$"
	.balign 4
n1:	.word 7

a2:	.asciz "Esta es otra cadena!"
b2:	.asciz "$$$$$$$$$$$$$$$$$$$$$$$$"
	.balign 4
n2:	.word 24

ori:	.asciz "Original:"
res:    .asciz "Copia:"

@------------------@
@PROGRAMA INVOCADOR@
@------------------@

	.text
main:
	mov r0, #0 @ columna
	mov r1, #0 @ fila
	ldr r2, =ori
	bl printString

	mov r0, #10 @ columna
	mov r1, #0 @ fila
	ldr r2, =a1
	bl printString

	ldr r0, =a1
	ldr r1, =b1
	ldr r2, =n1
	ldr r2, [r2]
	bl strncpyupr

	mov r0, #0 @ columna
	mov r1, #1 @ fila
	ldr r2, =res
	bl printString

	mov r0, #10 @ columna
	mov r1, #1 @ fila
	ldr r2, =b1
	bl printString


	mov r0, #0 @ columna
	mov r1, #3 @ fila
	ldr r2, =ori
	bl printString

	mov r0, #10 @ columna
	mov r1, #3 @ fila
	ldr r2, =a2
	bl printString

	ldr r0, =a2
	ldr r1, =b2
	ldr r2, =n2
	ldr r2, [r2]
	bl strncpyupr

	mov r0, #0 @ columna
	mov r1, #4 @ fila
	ldr r2, =res
	bl printString

	mov r0, #10 @ columna
	mov r1, #4 @ fila
	ldr r2, =b2
	bl printString

	wfi


@---------------------------------------------@
@SUBRUTINA UPR: DEVULVE UNA LETRA EN MAYÚSCULA@          
@---------------------------------------------@

@ Entrada: r3: Carácter a procesar
@ Salida:  r3: El carácter, convertido a mayúsculas si era una letra

upr:

	push {r4-r7, lr}       @apila los registros de r4 a r7 y la dirección de retorno

 	cmp     r3, #97        @ Comparar el carácter con 'a' (ASCII 97)
	blt    NoConvertir     @ Si el carácter es menor que 'a', saltar a NoConvertir
	cmp     r3, #122       @ Comparar el carácter con 'z' (ASCII 122)
	bgt     NoConvertir    @ Si el carácter es mayor que 'z', saltar a NoConvertir
			       @ Si el carácter está entre 'a' y 'z', convertirlo a mayúscula
	sub     r3, r3, #32    @ Restar 32 para convertir a mayúscula (diferencia entre 'a' y 'A')

NoConvertir:
    			       @ Aquí r0 contiene el carácter convertido o no, según corresponda
    	pop {r4-r7, pc}        @desapila r4 hasta r7, y la dirección de retorno sobreescribe el pc


@----------------------------------------------------------------------------------------@
@SUBRUTINA STRCPYUPR: COPIA UNA CADENA EN OTRA CON DISTINTA LONGITUD PASANDO A MAYÚSCULAS@  
@----------------------------------------------------------------------------------------@

@ Entrada: r0: Dirección de la cadena a
@          r1: Dirección de la cadena b
@          r2: máximo de caracteres a copiar
strncpyupr:
		push {r4-r7, lr}	@apila de r4 hasta r7, y la dirección de retorno
		mov r4, r0		@copia r0 en r4
		mov r5, r1		@copia r1 en r5
		mov r6, r2		@copia r2 en r6

strcpy1:	cmp r6, #0		@analiza la condición de si se ha copiado el máximo de caractéres
		beq afinando		@si se cumple, salta al final
		ldrb r7, [r4]		@cargar en r2 el elemento (byte) de la primera cadena
		cmp r7, #0		@comprobar si el elemento es 0, lo que quiere decir que es último de la cadena
		beq afinando	        @si el elemento es 0 acaba el bucle, se produce el salto
		mov r3, r7		@carga el en r3 del la letra que se quiere convertir
		bl upr			@pasa el control a la subrutina  upr, que solo modifica el reristro r3.
		mov r7, r3		@devuleve el resultado de r3 a r7
		strb r7, [r5]		@escribe en memoria, indicada por la dirección del elemento de la segunda cadena, el contenido de r2; un byte de A
     		add r4, #1		@incrementa la dirección de la primera cadena, para apuntar al siguiente byte
		add r5, #1		@incrementa la dirección de la segunda cadena, para apuntar al siguiente byte
		sub r6, r6, #1		@decrementa el max. de carac.
		b strcpy1		@retorno al principio del bucle



afinando: 	mov r7, #0		@ r7<-0
		strb r7,  [r5]		@escribe al final de la cadena un 0
		pop {r4-r7, pc}		@devulve el control y datos a donde fue invocado

	.end				@fin
