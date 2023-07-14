'''
    Utilizando la idea del archivo "2.Example.py" de la carpeta "1.Variables"
    hacer un programa que pida notas hasta que el usuario introduzca una nota
    negativa. El programa debe mostrar la media aritmetica de todas las notas
    introducidas. 
'''

nota = 0 #inicializamos con 0 porque aun no sabemos la nota que introducira el usuario
contador = 0 #utilizaremos este contador para dividir y hallar la media aritmetica
acumuladorDeNotas = 0 #sera el encargado de almacenar las sumas de las notas


while( nota >= 0): #mientras la nota no sea negativa ejecutamos el codigo interno repetidas veces
    nota = int(input('Introduzca una nota: ')) 
    if(nota > 0): # solo acumulamos las notas y  aumentamos el contador si la nota es positiva
        acumuladorDeNotas += nota #acumulamos las sumas de las notas
        contador += 1 


#una vez que hemos salido del bucle (cuando se coloca una nota negativa):
#el acumuladorDeNotas contendra la suma de todas las notas introducidas
#y el contador tendra algun valor, en este caso la cantidad de notas positivas que se halla introducido

#ahora solo procesamos para mostrar el resultado
media = acumuladorDeNotas / contador
print(f'🫡 La media aritmetica de todas las notas introducidas es: {media}')
