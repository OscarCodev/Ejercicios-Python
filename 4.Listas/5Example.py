'''
    Primero ejecuta este programa e interactua con el, luego estudia el código
    veras que es sencillo.

    Este programa nos ayudara a entender los distintos métodos que se
    pueden aplicar a una lista.

    a.Crea un menu interactivo que muestre las siguientes opciones: 
      1.Inicializar lista con 3 numeros
      2.Añadir elemento
      3.Eliminar elemento
      4.Ordenar lista
      5.Obtener longitud
      6.Salir
    
    b.La lista sera de numeros
    c.Cada vez que el usario seleccione una opcion mostrar la lista
      modificada a excepcion de la opcion 6.

    Tarea: Añadir mas opciones al menu como la de eliminar la lista, 
    unir otra lista, y otra que muestre el numero mas grande de toda 
    la lista
'''

lista = [] #creamos nuestra lista en este caso no contiene ningun elemento

opcion = 0 #inicializamos la opcion que valla a poner el usuario

while(opcion != 6): #mientras el usario no seleccione la opcion 6
    print('')
    print('📝📝 ListApp 📝📝') #Nombramos asi a nuestra aplicación
    print('1.Inicializar lista con 3 numeros')
    print('2.Añadir elemento')
    print('3.Eliminar elemento')
    print('4.Ordenar lista')
    print('5.Obtener longitud')
    print('6.Salir')

    opcion = int(input('Seleccione una opción: '))


    if(opcion == 1):
        lista = [4,1,10] #Creamos la lista con tres elementos
        print(lista)

    elif(opcion == 2):
        valorIngresar = int(input('¿Qué número desea agregar? '))
        lista.append(valorIngresar)
        print(lista)

    elif(opcion == 3):
        valorEliminar = int(input('¿Qué número desea eliminar? '))
        lista.remove(valorEliminar)
        print(lista)

    elif(opcion == 4):
        lista.sort()
        print(lista)

    elif(opcion == 5):
        longitud = len(lista)
        print(f'La longitud actual de la lista es {longitud} items')
        print(lista)

    elif(opcion == 6):
        print('Hasta pronto !!')
    else:
        print('Opción invalida')