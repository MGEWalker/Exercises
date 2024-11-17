
@-------------@
@ZONA DE DATOS@
@-------------@

	.data
a:	.asciz "Hola, Mundo!"
b:	.asciz "-"

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
	ldr r2, =a
	bl printString


	mov r0, #0 @ columna
	mov r1, #1 @ fila
	ldr r2, =res
	bl printString

	mov r5, #10 	@ columna inicial
	ldr r6, =a  	@ dirección de a
	ldr r7, =b  	@ dirección de b
m_w:	ldrb r0, [r6] 	@carga el caracter de la cadena a en r0
	cmp r0, #0    	@comprueba si es 0
	beq m_fw      	@si es 0 quiere decir que ha revisado toda la cadena, y termina el bucle
	bl upr       	@llama a la subrutina upr
	strb r0, [r7] 	@escribe en la dirección de b el caracter de r0
	mov r0, r5 	@ columna
	mov r1, #1 	@ fila
	ldr r2, =b    	@carga el caracter
	bl printString 	@llama a  la subrutina printString
	add r5, #1 	@aumenta el num. de columna
	add r6, #1 	@aumenta la dirección de a
	b m_w		@repite el bucle
m_fw:	wfi


@---------------------------------------------@
@SUBRUTINA UPR: DEVULVE UNA LETRA EN MAYÚSCULA@          
@---------------------------------------------@

@ Entrada: r0: Carácter a procesar
@ Salida:  r0: El carácter, convertido a mayúsculas si era una letra

upr:

	push {r4-r7, lr}       @apila los registros de r4 a r7 y la dirección de retorno

 	cmp     r0, #97        @ Comparar el carácter con 'a' (ASCII 97)
	blt    NoConvertir     @ Si el carácter es menor que 'a', saltar a NoConvertir
	cmp     r0, #122       @ Comparar el carácter con 'z' (ASCII 122)
	bgt     NoConvertir    @ Si el carácter es mayor que 'z', saltar a NoConvertir
			       @ Si el carácter está entre 'a' y 'z', convertirlo a mayúscula
	sub     r0, r0, #32    @ Restar 32 para convertir a mayúscula (diferencia entre 'a' y 'A')

NoConvertir:
    			       @ Aquí r0 contiene el carácter convertido o no, según corresponda
    	pop {r4-r7, pc}        @desapila r4 hasta r7, y la dirección de retorno sobreescribe el pc

	.end
