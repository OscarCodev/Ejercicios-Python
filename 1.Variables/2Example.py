'''
Necesitamos una aplicación que calcule la media
aritmética de dos notas enteras. Hay que tener
en cuenta que la media puede contener decimales
'''

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))

media = (nota1 + nota2) / 2.0 # dividir entre 2.0 convierte el tipo de dato de "media" a float

print(type(media))
print(f'La media aritmetica es {media}')