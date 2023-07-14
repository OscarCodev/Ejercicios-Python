'''
    Generar las tablas de multiplicar, de todos 
    los numeros hasta el 10.   
'''

#Anidación de bucles
for counterA in range(1, 11): #bucle externo
    print(f'Tabla de multiplicar del numero {counterA}')

    for counterB in range(1, 11): #bucle interno
        print(f'{counterA} * {counterB} = {counterA * counterB}')

#Analizando el código:
#Por cada vez que el bucle externo se ejecute, el bucle interno se ejecutara 10 veces




