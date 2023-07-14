'''
Escribir una aplicación que pida el año actual
y el de nacimiento del usuario. Debe calcular 
su edad, suponiendo que en el año en curso el 
usuario ya ha cumplido años.
'''

#convertimos los dos inputs a enteros 
añoActual = int(input('Ingrese el año actual: '))
añoNacimiento = int(input('Ingrese el año de nacimiento: '))

edad = añoActual - añoNacimiento

print(f'Su edad es de {edad} años')