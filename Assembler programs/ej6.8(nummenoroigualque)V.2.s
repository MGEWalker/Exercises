	.data
vector: .word 5, 3, 5, 5, 8, 12, 12, 15, 12
dim:	.word 9
dato1:	.word 5
res1:	.word 0
	
		.text
		@------------------@
		@Programa Invocador@
		@------------------@

primera:	ldr r0, =vector
		ldr r1, =dim
		ldr r1, [r1]
		ldr r2, =dato1
		ldr r2, [r2]
		bl nummenoroigualque
		ldr r3, =res1
		str r0, [r3]


stop:		wfi
		
		@---------@
		@Subrutina@
		@---------@

nummenoroigualque: 	mov r3, #0
nummenoroigualque1:	cmp r1, #0
			beq fin
			ldr r3, [r0]
			cmp r3, r2
			bgt sigue
				add r4, r4, #1
sigue:			add r0, #4
			sub r1, #1
			b nummenoroigualque1

fin:			mov r0, r4
			mov pc, lr	
			.end
