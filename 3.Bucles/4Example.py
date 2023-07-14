'''
    Realizar el juego el número secreto, que consiste en acertar un número desconocido
    (generado aleatoriamente entre 1 y 100). Para ello se leen por teclado una serie de
    números, para los que se indica: <<es un numero mayor>> o <<es un numero menor>>, 
    segun sea mayor o menor con respecto al número secreto. El proceso termina cuando 
    el usuario acierta o cuando se rinde (intruduciendo un -1).
'''

import random

#generamos un numero aleatorio entre 1 y 100 y lo almacenamos en la variable numeroAleatorio
numeroAleatorio = random.randint(1, 100) 

#inicializamos el numero del usuario porque no sabemos aun que numero introdujo
numeroDelUsuario = 0
print("Se ha generado un numero aleatorio entre 1 y 100 ¿Cual sera? 🤔🤐💡")

#mientras el numero del usuario sea diferente de -1 y diferente del numeroAleatorio 
#seguiremos ejecutando el codigo interno del while y haciendo las respectivas verificaciones
while((numeroDelUsuario != -1) and (numeroDelUsuario != numeroAleatorio)):
    numeroDelUsuario = int(input("Ingrese su prediccion: "))
    if (numeroAleatorio < numeroDelUsuario):
        print('Es un numero menor')
    else:
        print('Es un numero mayor')


#luego que el usario ha salido del bucle porque ha acertado o se ha rendido 
#debemos especificarlo y mostrarle algo en consecuencia
if(numeroDelUsuario == numeroAleatorio):
    print(f'En hora buena, Felicitaciones el numero aleatorio era {numeroAleatorio} 💐💐💐')
else:
    print('Para otra vez sera PIPIPI ☹️ 😭')


