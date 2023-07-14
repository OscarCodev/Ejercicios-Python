'''
Escribir un programa que pida una hora de la forma:
hora, minutos y segundos. El programa debe mostrar
la hora un segundo más tarde. Un ejemplo: 
hora actual [23:59:59] -> hora actual + 1 segundo [00:00:00]

Suponer que la hora introducida por el usuario es correcta
'''

hora = int(input('Introduzca una hora: '))
minutos = int(input('Introduca los minutos: '))
segundos = int(input('Introduca los segundos: '))

#Incrementamos los segundos
segundos += 1 # esta sintaxis es equivalente a: segundos = segundos + 1

#Procesamos - anidación de condicionales 
if(segundos > 59): #si los segundos superan 59
    segundos = 0 #los reiniciamos a cero
    minutos += 1 #incrementamos los minutos
    
    if(minutos > 59): #si los minutos superan 59
        minutos = 0 #los reiniciamos
        hora += 1 #incrementamos la hora
    
        if(hora > 23): #si la hora supera 23
            hora = 0 #reiniciamos la hora a 0

#Mostramos
print(f'Hora + 1 segundo:  {hora} : {minutos} : {segundos}')

