
	@-------------@
	@ZONA DE DATOS@
	@-------------@
	
	.data
cadena1:	.asciz "Hola!"			@asignar y reservar los caracteres de la primera cadena a copiar
		.balign 4			@alinear la siguiente cadena por si la que le antecede no es múltiplo de 4
cadena2:	.asciz "$$$$$"			@asignar y reservar los caracteres de la segunda cadena, en la que se va a copiar
		.balign 4			@alinear
inicialfinal:	.asciz "Inicial/final: "	@guardar un mensaje para mostrarlo

	@------------------@
	@PROGRAMA INVOCADOR@
	@------------------@
@r0<- cadena primera, r1<- cadena segunda
@print en pantalla de la cadena previa y de la cadena resultado,la que se ha copiado
	
	.text
main:	
	ldr r2, =inicialfinal	@r2<- dirección del mensaje a mostrar
	mov r0, #1		@r0<- una separación horizontal de una casilla  para la pantalla LCD
	mov r1, #0		@r1<- una separación de 0 casillas verticalmente
	bl printString		@llama a la subrutina para hacer un print de la cadena, con las condiciones especificadas
	mov r0, #1		@r0<- una separación horizontal de una casilla  para la pantalla LCD
	mov r1, #1		@r1<- una separación de 1 casilla verticalmente
	ldr r2, =cadena2	@r2<- dirección del mensaje a mostrar
	bl printString		@llama a la subrutina para hacer un print de la cadena, con las condiciones especificadas
	ldr r0, =cadena1	@r0<- la dirección de la cadena a copiar
	ldr r1, =cadena2	@r1<- la dirección de la cadena en la que se quiere copiar
	bl strcpy		@llama a la subrutina para copiar A en B
	mov r0, #1		@r0<- una separación horizontal de una casilla  para la pantalla LCD
	mov r1, #2		@r1<- una separación de 2 casillas verticalmente
	ldr r2, =cadena2	@r2<- dirección del mensaje a mostrar, la cadena que acabamos de remplazar
	bl printString		@llama a la subrutina para hacer un print de la cadena, con las condiciones especificadas

stop:	wfi			@fin


@--------------------------------------------------------------@
@SUBRUTINA STRCPY: COPIA LA PRIMERA CADENA EN LA SEGUNDA CADENA@
@--------------------------------------------------------------@
@r0<- primera cadena a copiar
@r1<- segunda cadena, en la que copiar
@cadena copiada-> r0

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
		.end			@fin de la subrutina (no es necesario en este caso)
