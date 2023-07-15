'''
Escribe un programa que recorra una lista de números y muestre 
únicamente los números pares. Puedes utilizar un bucle for y la 
operación de módulo (%) para determinar si un número es par.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'lista original: {numeros}')

for numero in numeros:
    if numero % 2 == 0: #filtramos los números pares
        print(numero)