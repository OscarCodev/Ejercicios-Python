'''
    Este programa engloba los 5 conceptos principales de la programacion:
    -variables
    -condicionales
    -bucles
    -listas
    -funciones

    Hice este trabajo cuando estaba llevando el curso de algoritmos con el 
    profesor Montes. 

    Primero ejecutalo

    Si quieres entedenderlo empiza a analizarlo desde la linea 332
    veras que es un bucle, el cual contiene opciones y esas opciones
    simplemente estan llamando funciones. Esas funciones estan definidas
    en la parte superior del bucle.

    Todo comenzó con un menu interactivo :) 😊😊

'''

import random

# Funciones Presentacion y opciones
def presentacion():
    variable = "◼◼◼◼◼◼◼◼◼◼◼◼◼⬜⬜⬜◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼"

    print(variable)
    print("◼ Bienvenid@ al Menú Interactivo ◼")
    
def opciones():
    print(" ")
    print("▶ Selecciona una opcion:")
    print("1.Halla tu peso en un planeta 🪐")
    print("2️.Halla tu indice de masa corporal 🧬")
    print("3️.Juega a adivinar colores 🐣 ")
    print("4️.Grafica la figura que escojas 🌀")
    print("5️.Piedra, Papel o Tijera ⛄")
    print("6️.salir")
    print(" ")

# Funciones de los Programas 
def programa_01():
    print("    Escoge el Planeta: ")
    print("    1️.Marte ")
    print("    2️.Jupiter")
    print("    3️.Saturno")

    planeta_escogido = input("    => ") 

    if planeta_escogido == "1" or planeta_escogido == "marte":
        peso = int(input("    Introduce tu peso: "))
        peso_marte = (peso // 10) * 4
        print(f"    Tu peso en Marte es { peso_marte} kg")

    elif planeta_escogido == "2" or planeta_escogido == "jupiter":
        peso = int(input("    Introduce tu peso: "))
        peso_jupiter = (peso // 10) * 25

        print(f"    Tu peso en Jupiter es {peso_jupiter} kg")

    elif planeta_escogido == "3" or planeta_escogido == "saturno":
        peso = int(input("      Introduce tu peso: "))
        peso_saturno = (peso // 10) * 10 

        print(f"    Tu peso en Saturno es {peso_saturno} kg")

def programa_02():
    peso = int(input("    Introduce tu peso: "))
    altura = float(input("    Introduce tu altura: "))

    indice_masa = peso // altura**2 

    print(f"    Tu indice de masa corporal es de {indice_masa} puntos")

    if indice_masa <= 18:
        print("    Delgades 🤷‍♂️")
    elif indice_masa <= 25:
        print("    Tu IDC es saludable 👩🧑")
    elif indice_masa <= 100:
        print("    Alerta Sobrepeso 👩‍⚕️") 

def programa_03():
    print("    Escoge uno de estos cinco colores")
    print("    y veremos si la maquina tambien lo escogio")
    print("    🟡, 🔴, 🟢, 🔵, 🟣")


    color = random.choice(["amarillo","rojo","verde","azul","morado"])
    
    de_nuevo = True 

    while de_nuevo == True:

        opcion = input("    Ingrese un color: ")

        if color == opcion:
            print(f"    La maquina escogio el color {color}")
            print("    Bien hecho")
            de_nuevo = False 
        else:
            if color == "amarillo":
                
                print("    PISTA: en el trigo y en el limon, en el desierto y en el sol, adivina quien soy")

            elif color == "rojo":
                
                print("    PISTA: estoy en la sangre y no en el agua. Brillo en el fuego y no en la leña ")

            elif color == "verde":
                
                print("    PISTA: aveces en el mar, tambien en la selva y en tus mismo ojos puedo estar")

            elif color == "azul":
            
                print("    PISTA: violeta, amarillo, naranja, rojo, verde y añil,¿Cuál es el color que falta? \nEstá en el arcoiris")
                
            elif color == "morado":
                
                print("    PISTA: tienen el color de aquellas redonditas y dulces como la miel, que se pisan y \npisan y luego a beber ")

def programa_04():
    print("    Escoge que quieres graficar en pantalla: ")
    def sub_opciones ():
        print("    1.Enojado")
        print("    2.Monkey")
        print("    3.Meme")
        print("    4.PacMan")
        print("    5.Mario Bros")
        print("    6.Mujer")
        print("    7.Salir de la graficadora")

    # Dibujos
    def dibujo_01():
        print("""
        ────────▓▓▓▓▓▓▓────────────▒▒▒▒▒▒
        ──────▓▓▒▒▒▒▒▒▒▓▓────────▒▒░░░░░░▒▒
        ────▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓────▒▒░░░░░░░░░▒▒▒
        ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒
        ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
        ──▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
        ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒
        ▓▓▒▒▒▒▒▒░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒
        ▓▓▒▒▒▒▒▒▀▀▀▀▀███▄▄▒▒▒░░░▄▄▄██▀▀▀▀▀░░░░░░▒
        ▓▓▒▒▒▒▒▒▒▄▀████▀███▄▒░▄████▀████▄░░░░░░░▒
        ▓▓▒▒▒▒▒▒█──▀█████▀─▌▒░▐──▀█████▀─█░░░░░░▒
        ▓▓▒▒▒▒▒▒▒▀▄▄▄▄▄▄▄▄▀▒▒░░▀▄▄▄▄▄▄▄▄▀░░░░░░░▒
        ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
        ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
        ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀░░░░░░░░░░░░░░▒
        ────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒
        ─────▓▓▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▄░░░░░░░░▒▒
        ──────▓▓▒▒▒▒▒▒▒▄▀▀▀▀▀▀▀▀▀▀▀▄░░░░░▒▒
        ───────▓▓▒▒▒▒▒▀▒▒▒▒▒▒░░░░░░░▀░░░▒▒
        ────────▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒
        ──────────▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒
        ───────────▓▓▒▒▒▒▒▒▒▒░░░░░░░▒▒
        ─────────────▓▓▒▒▒▒▒▒░░░░░▒▒
        ───────────────▓▓▒▒▒▒░░░░▒▒
        ────────────────▓▓▒▒▒░░░▒▒
        ──────────────────▓▓▒░▒▒
        ───────────────────▓▒░▒
        ────────────────────▓▒
        """)

    def dibujo_02():
        print("""
        ───────────▄██████████████▄
        ───────▄████░░░░░░░░█▀────█▄
        ──────██░░░░░░░░░░░█▀──────█▄
        ─────██░░░░░░░░░░░█▀────────█▄
        ────██░░░░░░░░░░░░█──────────██
        ───██░░░░░░░░░░░░░█──────██──██
        ──██░░░░░░░░░░░░░░█▄─────██──██
        ─████████████░░░░░░██────────██
        ██░░░░░░░░░░░██░░░░░█████████████
        ██░░░░░░░░░░░██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
        ██░░░░░░░░░░░██░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
        ─▀███████████▒▒▒▒█▓▓▓███████████▀
        ────██▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓█
        ─────██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓█
        ──────█████▒▒▒▒▒▒▒▒▒▒██████████
        ─────────▀███████████▀
        """)

    def dibujo_03():
        print("""
        ░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░
        ░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░
        ░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░
        ░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░
        ░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░
        ░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░
        ░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░
        █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█
        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█
        █░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█
        █░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█
        █░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█
        █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█
        ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░
        ░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░
        ░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░
        ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░
        ░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░
        """)
        
    def dibujo_04():
        print("""

        ──▒▒▒▒▒▒───▄████▄
        ─▒─▄▒─▄▒──███▄█▀
        ─▒▒▒▒▒▒▒─▐████──█─█
        ─▒▒▒▒▒▒▒──█████▄
        ─▒─▒─▒─▒───▀████▀

        """)

    def dibujo_05():
        print("""
            
        ______██████████████
        -____██▓▓▓▓▓▓▓▓▓ M ▓████
        -__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
        -__██████░░░░██░░██████
        ██░░░░████░░██░░░░░░░░██
        ██░░░░████░░░░██░░░░░░██
        -__████░░░░░░██████████
        -__██░░░░░░░░░░░░░██
        _____██░░░░░░░░░██
        -______██░░░░░░██
        -____██▓▓████▓▓▓█
        -_██▓▓▓▓▓▓████▓▓█
        ██▓▓▓▓▓▓███░░███░
        -__██░░░░░░███████
        -____██░░░░███████
        -______██████████
        -_____██▓▓▓▓▓▓▓▓▓██
        -_____█████████████

        """)

    def dibujo_06():
        print("""
        _________________________$$$$$$$________________
        ________________________$$$$$$$$$$______________
        ________________________$$$$$$$$$$$_____________
        _________________________$$$$$$$$$$$$$$_________
        __________________________$$$$$$$$$$$___________
        _____________________________$$$$$$$$$$$$$______
        ___________________________$$$$$$$$$$___________
        _________________________$$$$$$$$$$$$$$$________
        ________________$$$______$$$$$$$$$$$$$$_________
        ______________$$$$$$$$_____$$$$$$__$$$$$________
        _____________$$$$$$$$$$_____$$$$____$$$$$_______
        ___________$$$$$$_$$$$$$$$__$$$$______$$$$______
        __________$$$$$_____$$$$$$$$_$$$$_______$$$_____
        ________$$$$$_________$$$$$$$$$$$$_______$$$____
        _______$$$_____________$$$$$$$$$$$________$$$___
        _____$$$________________$$$$$$$$$$________$$$$$$
        __$$$$$$__________________$$$$$$$_______________

        """)

    while True:
        sub_opciones()
        opcion = input("> ")

        if opcion == "1":
            dibujo_01()

        elif opcion == "2":
            dibujo_02()

        elif opcion == "3":
            dibujo_03()

        elif opcion == "4":
            dibujo_04()

        elif opcion == "5":
            dibujo_05()

        elif opcion == "6":
            dibujo_06()

        elif opcion == "7":
            break
      
def programa_05():

    def jugar():
        usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
        computadora = random.choice(['pi', 'pa', 'ti'])

        if usuario == computadora:
            print(f"La computadora escogio {computadora}")
            return '¡Empate!'

        if ganó_el_jugador(usuario, computadora):
            print(f"La computadora escogio {computadora}")
            return '¡Ganaste!'

        return '¡Perdiste!'


    def ganó_el_jugador(jugador, oponente):
        # Retornar True (verdadero) si gana el jugador.
        # Piedra gana a Tijera (pi > ti).
        # Tijera gana a Papel (ti > pa).
        # Papel gana a Piedra (pa > pi).
        if ((jugador == 'pi' and oponente == 'ti')
            or (jugador == 'ti' and oponente == 'pa')
            or (jugador == 'pa' and oponente == 'pi')):
            return True
        else:
            return False


        
        
    print(jugar())



#Invocando a la funcion presentación
presentacion()

#Menú Interactivo

while True:
    opciones()

    opcion = input("> ")
    
    if opcion == "1":
        programa_01()

    elif opcion == "2":
        programa_02()

    elif opcion == "3":
        programa_03()

    elif opcion == "4":
        programa_04()

    elif opcion == "5":
        programa_05()

    elif opcion == "6":
        print("Hasta pronto 🖐🏻")
        print(" ")
        break
    else:
        print("🚫  Comando no reconocido, pruebe otra opcion ")
        print(" ")
