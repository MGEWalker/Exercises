	.data
vector:	.word 2, 4, 6, 3, 10, 1, 4,   
n_elements:	.word 7                         
n:	.word 5                          
result:	.word 0                           

	.text

main:	ldr r1, =vector        
    	ldr r2, =n_elements     
    	ldr r2, [r2]             
    	ldr r3, =n      
    	ldr r3, [r3]             
    	ldr r4, =result          
    	mov r5, #0               
	ldr r0, [r1]
	cmp r0, r3               
    	bgt increment
	sub r2, r2, #1          
loop:	cmp r2, #0               
    	beq done                 
	add r1, #4
    	ldr r0, [r1]         
    	cmp r0, r3               
    	bgt increment             

next_element:	sub r2, r2, #1          
    		b loop                   

increment:	add r5, r5, r0           
    		b next_element           

done:	str r5, [r4]             
stop:	wfi             
