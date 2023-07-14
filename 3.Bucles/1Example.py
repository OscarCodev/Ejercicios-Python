'''
    Generar la tabla de multiplicar hasta el 10 de un
    numero que el usuario introduzca.

    Utilizar el bucle while y el for 

    Respecto al bucle while hacer uno que utilize un contador sin el break y
    hacer otro que utilize el break.

    En total generar 3 tablas de multiplicar.
'''

num = int(input('Ingrese un número: '))


#BUCLE WHILE CON CONTADOR
contadorA = 1
print('Tabla de multiplicar con el bucle while + contador')
while(contadorA <= 10): #ejecuta el codigo interno mientras contadorA sea menor o igual a 10
    print(f'{contadorA} x {num} = {contadorA * num}')
    contadorA += 1 #es lo mismo que escribir: contadorA = contadorA + 1



#BUCLE WHILE UTILIZANDO UN CONTADOR + BREAK
print('Tabla de multiplicar con el bucle while utilizando un contador + break')
contadorB = 1
while(True): #Notacion de bucle infinito
    print(f'{contadorB} x {num} = {contadorB * num}')
    contadorB += 1
    if(contadorB > 10): #hace posible salir del bucle infinito cuando el contadorB supera 10
        break



#BUCLE FOR
print('Tabla de multiplicar utilizando el bucle for')
for contadorC in range(1, 11): #range crea un objeto de rango que representa una secuencia de números desde 1 hasta 10 (el número final es excluido)
    print(f'{contadorC} x {num} = {contadorC * num}')


#¿Cual es la diferencia entre un bucle while y un bucle for?

# El bucle while evalúa la condición antes de cada iteración y, 
# si la condición sigue siendo verdadera, se ejecuta el bloque 
# de código dentro del bucle. 

# Un bucle for se utiliza para iterar sobre una secuencia de 
# elementos, como una lista, una cadena de caracteres, 
# un rango, entre otros.