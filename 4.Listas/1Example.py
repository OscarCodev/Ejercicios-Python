'''
 Las listas nos sirven para almacenar muchos valores, por ejemplo 
 podriamos tener listas que almacenen: frutas, usuarios, edades,
 estaturas, etc. Una vez que tenemos esos datos podemos procesarlos
 podemos obtener la cantidad total de frutas, la cantidad de usarios
 mayores de edad, las edades mas longevas, o la estatura mas alta.

 Ejercicio:
 Escribe un programa que recorra una lista de números y calcule 
 la suma de todos sus elementos. 
'''


numeros = [2, 4, 6, 8, 10] #lista de números
suma = 0 #variable acumuladora

for numero in numeros:
    suma += numero

print("La suma de los números es:", suma)