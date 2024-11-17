	.data
vector: .word 5, 3, 8, 5, 6, 8, 10, 4, 8, 7, 5, 7
dim:	.word 12
dato1:	.word 7
dato2:	.word 8
res1:	.word 0
res2:	.word 0
resfin:	.word 0
	
		.text
		@------------------@
		@Programa Invocador@
		@------------------@

primera:	ldr r0, =vector
		ldr r1, =dim
		ldr r1, [r1]
		ldr r2, =dato1
		ldr r2, [r2]
		bl numigualque
		ldr r3, =res1
		str r0, [r3]

segunda:	ldr r0, =vector
		ldr r1, =dim
		ldr r1, [r1]
		ldr r2, =dato2
		ldr r2, [r2]
		bl numigualque
		ldr r3, =res2
		str r0, [r3]

final:		ldr r0, =res1
		ldr r0, [r0]
		ldr r1, =res2
		ldr r1, [r1]
		ldr r2, =resfin
		add r0, r0, r1
		str r0, [r2]

stop:		wfi
		
		@---------@
		@Subrutina@
		@---------@

numigualque: 	mov r4, #0
numigualque1:	cmp r1, #0
		beq fin
		ldr r3, [r0]
		cmp r3, r2
		bne sigue
			add r4, r4, #1
sigue:		add r0, #4
		sub r1, #1
		b numigualque1

fin:		mov r0, r4
		mov pc, lr	
		.end
