
@-------------@
@ZONA DE DATOS@
@-------------@

	.data
a1:	.asciz "Hola,"
b1:	.asciz "-----"

ori:	.asciz "Antes:"
res:    .asciz "Despues:"

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
	bl strcpyupr

	mov r0, #0 @ columna
	mov r1, #1 @ fila
	ldr r2, =res
	bl printString

	mov r0, #10 @ columna
	mov r1, #1 @ fila
	ldr r2, =b1
	bl printString

stop:	wfi


@---------------------------------------------@
@SUBRUTINA UPR: DEVULVE UNA LETRA EN MAYÚSCULA@          
@---------------------------------------------@

@ Entrada: r2: Carácter a procesar
@ Salida:  r2: El carácter, convertido a mayúsculas si era una letra
upr:
	push {r4-r7, lr}       @apila los registros de r4 a r7 y la dirección de retorno

 	cmp     r2, #97        @ Comparar el carácter con 'a' (ASCII 97)
	blt    NoConvertir     @ Si el carácter es menor que 'a', saltar a NoConvertir
	cmp     r2, #122       @ Comparar el carácter con 'z' (ASCII 122)
	bgt     NoConvertir    @ Si el carácter es mayor que 'z', saltar a NoConvertir
			       @ Si el carácter está entre 'a' y 'z', convertirlo a mayúscula
	sub     r2, r2, #32    @ Restar 32 para convertir a mayúscula (diferencia entre 'a' y 'A')

NoConvertir:
    			       @ Aquí r0 contiene el carácter convertido o no, según corresponda
    	pop {r4-r7, pc}        @desapila r4 hasta r7, y la dirección de retorno sobreescribe el pc




@----------------------------------------------------------------------------------------@
@SUBRUTINA STRCPYUPR: COPIA UNA CADENA EN OTRA CON LA MISMA LONGITUD PASANDO A MAYÚSCULAS@  
@----------------------------------------------------------------------------------------@

@ Entrada: r0: Dirección de la cadena a
@          r1: Dirección de la cadena b

strcpyupr:
		push {r4-r7, lr}	@guardar los registros y la dirección de vuelta
strcpy1:
		ldrb r2, [r0]		@cargar en r2 el elemento (byte) de la primera cadena
		cmp r2, #0		@comprobar si el elemento es 0, lo que quiere decir que es último de la cadena
		beq finalisando		@si el elemento es 0 acaba el bucle, se produce el salto
		bl upr			@pasa el control a la subrutina  upr, que solo modifica el reristro r2, por lo tanto, no es necesario guardar nada de otros registros.
		strb r2, [r1]		@escribe en memoria, indicada por la dirección del elemento de la segunda cadena, el contenido de r2; un byte de A
     		add r0, #1		@incrementa la dirección de la primera cadena, para apuntar al siguiente byte
		add r1, #1		@incrementa la dirección de la segunda cadena, para apuntar al siguiente byte
		b strcpy1		@repite el bucle
finalisando:	pop {r4-r7, pc}		@retorna el flujo a donde fue invocado y libera los registros guardados
		.end		
		
