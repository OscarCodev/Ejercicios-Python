'''
 Basandonos en la logica del archivo '5Example.py' de la carpeta
 '3.Bucles' hacer una funcion que reciba como argumento un numero
 e imprima un triangulo de asteriscos.
'''

#Definimos nuestra funcion
def dibujarTriangulo(num):
    for valor in range(1, num + 1):
        print('*' * valor) 

#Utilizamos nuestra funcion
dibujarTriangulo(4)
dibujarTriangulo(5)
dibujarTriangulo(6)

