'''
 Implementar un programa que pida por teclado
 un número decimal e indique si es un número 
 casi-cero, que son aquellos, positivos o negativos,
 que se acercan a 0 por menos de 1 unidad, aunque 
 curiosamente el 0 no se considera un número casi-cero.
 Ejemplos de números casi-cero son el 0.3, el -0.99 o el
 0.123. Y números que no se consideran casi-ceros son:
 el 12.3, el 0 o el -1. 
'''

#Pedimos el numero
num = float(input("Ingrese un numero real positivo o negativo: "))

#Un numero casi cero cumple que es mayor que -1, que es menor que 1 y que no es 0
if( -1 < num and num < 1 and num != 0 ):
    esUnCasiCero = True 
else:
    esUnCasiCero = False

#Mostramos el resultado
print(f'¿ El numero {num} es un casi cero ? {esUnCasiCero}')