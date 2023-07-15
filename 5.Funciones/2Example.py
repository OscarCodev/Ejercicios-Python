'''
 Basandonos en el archivo '3Example.py' de la carpeta '1.Variables'
 crear dos funciones una que retorne la longitud de una circunferencia
 y otra funcion que retorne el area de la circunferencia. 

 Las funciones se deberan llamar:
 longitudCircunferencia()
 areaCircunferencia()

 Ambas reciben el redio como argumento
'''

import math

#definimos las funciones

def longitudCircunferencia(radio):
    pi = math.pi
    longitud = 2 * pi * radio
    return longitud


def areaCircunferencia(radio):
    pi = math.pi
    areaCircunferencia = pi * (radio ** 2)
    return areaCircunferencia

#Ahora que tenemos nuestra funciones podemos hallar las longitudes
#y areas de los radios que deseemos sin necesidad de preocuparnos
#por como era el algoritmo o formula, ya sabemos que las funciones 
#que creamos nos retornaran los valores que esperamos

#Invocamos a las funciones y almacenamos su valor de retorno en variables
longitud1 = longitudCircunferencia(10)
longitud2 = longitudCircunferencia(20)
longitud3 = longitudCircunferencia(40)
longitud4 = longitudCircunferencia(50)

area1 = areaCircunferencia(10)
area2 = areaCircunferencia(20)
area3 = areaCircunferencia(30)
area4 = areaCircunferencia(40)

