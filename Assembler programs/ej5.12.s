		.data
nota1:		.word 7             
nota2:		.word 5             
resultado:	.word 0               

aprobado:	.asciz "APROBADO"     
suspenso:	.asciz "SUSPENSO"     

mensaje_final:	.space 10             

		.text
main:	ldr r1, =nota1        
    	ldr r2, [r1]          
    	ldr r1, =nota2        
    	ldr r3, [r1]          

    	add r4, r2, r3        
    	lsr r4, r4, #1       

    	ldr r1, =resultado    
    	str r4, [r1]          

    	cmp r4, #5           
    	blt suspenso1          

    	ldr r1, =aprobado   
    	b copiar_mensaje

suspenso1:	ldr r1, =suspenso   

copiar_mensaje:	ldr r2, =mensaje_final       
    		mov r3, #0                   

copiar_loop:	ldrb r4, [r1, r3]            
    		strb r4, [r2, r3]            
    		add r3, r3, #1               
    		cmp r4, #0                   
    		bne copiar_loop              
stop:		wfi                   
