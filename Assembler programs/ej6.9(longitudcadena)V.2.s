		.data
cadena1:	.asciz "abcd"
		.balign 4
cadena2:	.asciz "abcde"
		.balign 4 
res1:		.word 0
		.balign 4 
res2:		.word 0
res:		.word 0
	
		.text
		@------------------@
		@Programa Invocador@
		@------------------@

primera:	ldr r0, =cadena1
		bl longitudcadena
		ldr r2, =res1
		str r0, [r2]

	
segunda:	ldr r0, =cadena2
		bl longitudcadena
		ldr r2, =res2
		str r0, [r2]

final:		ldr r0, =res1
		ldr r0, [r0]
		ldr r1, =res2
		ldr r1, [r1]
		ldr r2, =res
		cmp r0, r1
		bgt op2
			mov r3, #2
			str r3, [r2]
		b end
op2:		mov r3, #1
		str r3, [r2]
end:		wfi
		
		@---------@
		@Subrutina@
		@---------@

longitudcadena:		mov r2, #0
			mov r3, #0
longitudcadena1:	ldrb r2, [r0]
			cmp r2, #0
			beq fin
			add r0, #1
			add r3, r3, #1
			b longitudcadena1			
fin:		mov r0, r3
		mov pc, lr	
		.end
