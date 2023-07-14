'''
Diseñar una aplicación que calcule la longitud
y el área de una circunferencia. Para ello, el
usuario debe introducir el radio (que puede 
contener decimales). Recordamos:
    longitud = 2*PI*radio
    area = PI*(radio**2)
'''


#PI es una constante, la declaramos
PI = 3.14 # tambien pudimos asignarle math.pi previa importacion del modulo math

#pedimos el radio y cambiamos su type a float:
radio = float(input("Ingrese el radio: "))

#procesamos a partir del radio dado:
longitud = 2 * PI * radio
area = PI * (radio**2)

#mostramos los resultados
print(f'La longitud es: {longitud}')
print(f'El area es: {area}')
