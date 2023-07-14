'''
    Pedir tres numeros y mostrarlos ordenados
    de mayor a menor.
    Si ingresamos:
    1  4  0
    deberia mostrar:
    4  1  0
    probar todos los casos posibles
'''

#Pedimos los 3 numeros al usuario
a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))

#Vamos a plantear tantos condicionales como casos existen con tres numeros
if(a > b and b > c):
    print(a, b, c)
elif(a > c and c > b):
    print(a, c, b)
elif(b > a and a > c):
    print(b, a, c)
elif(b > c and c > a):
    print(b, c, a)
elif(c > a and a > b):
    print(c, a, b)
elif(c > b and b > a):
    print(c, b, a)

# ¿Habra una forma de hacer mas corto el algoritmo?