	.data
A:	.word 2
B:	.word 1
RES:	.space 

	.text
main:	ldr r0, =A
	ldr r0, [r0]

	ldr r1, =B
	ldr r1, [r1]

	ldr r3, =RES

	cmp r0, r1
	bge salto
	sub r1, r1, r0
	b escrib

salto:	sub r1, r0, r1

escrib: str r1, [r3]

stop: 	wfi
