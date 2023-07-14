'''
    Pedir por consola un número n y dibujar un triangulo de n elementos de lado,
    utilizando para ello asteriscos (*). Por ejemplo para n = 4,generara: 
    *
    **
    ***
    ****
'''

num = int(input('Ingrese un número: '))

for valor in range(1, num + 1):
    print('*' * valor)


'''
    Y si quisiera generar un triangulo invertido: 
    ****
    ***
    **
    *

    ¿Cómo lo haria?

    Pista: entender como funciona el range()
'''