'''
Escribir una aplicación que indique cuántas
cifras tiene un número entero introducido por
teclado, que estará comprendido entre 0 y 99999

Por ejemplo: 
9 -> tiene 1 cifra
10 -> tiene 2 cifras
100 -> tiene 3 cifras
1000 -> tiene 4 cifras
.
.

'''

numero = int(input("Ingrese un número: "))

if(numero < 10):
    print('Tiene 1 cifra')
elif(numero < 100):
    print('Tiene 2 cifras')
elif(numero < 1000):
    print('Tiene 3 cifras')
elif(numero < 10000):
    print('Tiene 4 cifras')
elif(numero < 100000):
    print('Tiene 5 cifras')