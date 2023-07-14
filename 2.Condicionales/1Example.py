'''
 Diseñar una aplicación que solicite un número
 e indique si es par o impar.
'''

#Pedimos un numero al usuario
num = int(input('Ingrese un numero: '))

#esPar cambiara a true o false dependiendo de la condicion
if(num % 2 == 0):
    esPar = True
else:
    esPar = False
     
# un codigo equivalente para hacer la misma condicion y evitar las lineas 9 hasta la 12 es este:
# esPar = True if (num % 2 == 0) else False

#Mostramos el resultado
print(f'¿ El numero {num} es par ? {esPar}')
