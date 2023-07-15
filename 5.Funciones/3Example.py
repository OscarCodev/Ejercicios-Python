'''
 Basandonos en el archivo '1Example.py' de la carpeta '3.Bucles'
 crear una funcion que reciba un numero como argumento e imprima
 la tabla de multiplicar de ese numero. Utilizar cualquier bucle.

 Diferencia entre retornar e imprimir.

 Las funciones tambien nos sirven para agrupar codigo o modularizar
 nuestro proyecto
'''

def tablaMultiplicar(numero):
    for contador in range(1, 11): 
        print(f'{contador} x {numero} = {contador * numero}')
    

#Como nuestra funcion ya imprime las tablas y no los retorna, 
#no es necesario almacenarlos en variables 

#Simplemente las llamamos y generamos las tablas de los numeros 
#que deseemos y veremos el resultado en consola

tablaMultiplicar(10)

tablaMultiplicar(25)

tablaMultiplicar(30)