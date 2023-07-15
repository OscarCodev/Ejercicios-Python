'''
    Crear una funcion que reciba una lista de numeros como argumento
    y devuelva una nueva lista que contenga solamente los numeros pares. 
'''

#Definimos nuestra funcion
def filtrarPares(lista):

    listaFiltrada = []

    for numero in lista: #recorremos numero en la lista pasada como argumento
        if numero % 2 == 0: #si el numero es par lo añadimos a la lista filtrada
            listaFiltrada.append(numero)
    
    return listaFiltrada #retornamos la lista filtrada


#Antes de utilizar nuestra funcion crearemos 2 listas de numeros

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [10,11,12,13,14,15,16]

#utilizamos nuestras funciones para filtrar los pares y los imprimimos directamente
print(filtrarPares(lista1))
print(filtrarPares(lista2))

'''
    Tambien pudimos almacenar los resultados en variables: 
    listaFiltrada1 = filtrarPares(lista1)
    listaFiltrada2 = filtrarPares(lista2)

    y despues imprimirlos:
    print(listaFiltrada1)
    print(listaFiltrada2)

    Hacer eso ayuda en la legibilidad del codigo. 

    :) OscarCodev <3 
'''