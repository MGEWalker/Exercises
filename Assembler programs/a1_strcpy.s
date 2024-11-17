
@-------------@
@ZONA DE DATOS@
@-------------@

	.data
a1:	.asciz "Hola,"
b1:	.asciz "-----"

ori:	.asciz "Original:"
sob:	.asciz "Sobrescrita:"

@------------------@
@PROGRAMA INVOCADOR@
@------------------@

	.text
main:
	mov r0, #0 @ columna
	mov r1, #0 @ fila
	ldr r2, =ori
	bl printString

	mov r0, #13 @ columna
	mov r1, #0 @ fila
	ldr r2, =b1
	bl printString

	ldr r0, =a1
	ldr r1, =b1
	bl strcpy

	mov r0, #0 @ columna
	mov r1, #1 @ fila
	ldr r2, =sob
	bl printString

	mov r0, #13 @ columna
	mov r1, #1 @ fila
	ldr r2, =b1
	bl printString
	wfi

@----------------------------------------------------------------@
@SUBRUTINA STRCPY: COPIA UNA CADENA EN OTRA CON LA MISMA LONGITUD@  
@----------------------------------------------------------------@

@ Entrada: r0: Dirección de la cadena a
@          r1: Dirección de la cadena b

strcpy:
		push {r4-r7, lr}	@guardar los registros y la dirección de vuelta
strcpy1:
		ldrb r2, [r0]		@cargar en r2 el elemento (byte) de la primera cadena
		cmp r2, #0		@comprobar si el elemento es 0, lo que quiere decir que es último de la cadena
		beq finalisando		@si el elemento es 0 acaba el bucle, se produce el salto
		strb r2, [r1]		@escribe en memoria, indicada por la dirección del elemento de la segunda cadena, el contenido de r2; un byte de A
     		add r0, #1		@incrementa la dirección de la primera cadena, para apuntar al siguiente byte
		add r1, #1		@incrementa la dirección de la segunda cadena, para apuntar al siguiente byte
		b strcpy1		@repite el bucle
finalisando:	pop {r4-r7, pc}		@retorna el flujo a donde fue invocado y libera los registros guardados
		.end		
