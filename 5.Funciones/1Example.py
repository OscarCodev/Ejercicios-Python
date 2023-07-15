'''
 Basandonos en el archivo '2Example.py' de la carpeta '1.Variables'
 crear una función que reutilice esa logica y devuelva la media aritmetica
 de dos números que se pasen como argumento:

 La función se debe llamar calcularMedia(num1, num2) la cual recibe dos
 argumentos num1 y num2

 El valor retornado por la función debe ser almacenado en una variable
 y luego debe ser imprimida

 Hallar la media aritmetica de estos valores:
 12, 20
 25, 45
 78, 90
'''

def calcularMedia(num1, num2):
    #Sumamos los dos argumentos recibidos y los dividimos entre 2.0
    media = (num1 + num2) / 2.0
    #Retornamos la media
    return media

#Una vez que hemos definido nuestra función hay que invocarla para usarla
resultado1 = calcularMedia(12, 20) #invocamos a la funcion y la almacenamos en resultado1
resultado2 = calcularMedia(25, 45)
resultado3 = calcularMedia(78, 90)

#Imprimimos los resultados
print(resultado1)
print(resultado2)
print(resultado2)

#En ves de crear 3 algoritmos iguales para calcular la media, solo 
#creamos una función que contiene la misma logica.

#Con esta idea es que se han creado muchas librerias o modulos que 
#basicamente reutilizan funcionalidades. La idea es que el programador
#disponga de estas funcionalidades (que esten disponibles para usarse). 



