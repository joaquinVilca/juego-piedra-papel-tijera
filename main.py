#un juego de piedra papel o tijera
#0 el usuario elige una opcion
#1 el programa elige una opcion
#2 se comparan las opciones
#3 se muestra el resultado
#4 se muestra el ganador
#5 se muestra el perdedor
import random as rd

def usuraioEleccion():
    print("""Elige tu arma:
    0. Piedra
    1. Papel
    2. Tijera
    """)
    opcionUsuario = int(input("Elige una opcion: "))
    return opcionUsuario

def programaEleccion():
    opcionPrograma = rd.randint(0,2)
    print(" ")
    if opcionPrograma == 0:
        print("El programa eligio piedra")
    elif opcionPrograma == 1:
        print("El programa eligio papel")
    elif opcionPrograma == 2:
        print("El programa eligio tijera")
    else:
        print("Opcion no valida. El programa entro en crisis, ganas por defecto")
    return opcionPrograma

def piedraPapelTijera(jugador0, jugador1):
    if jugador0 == 0 and jugador1 == 0:
        print("Empate, me. llevo una piedra")
    elif jugador0 == 0 and jugador1 == 1:
        print("Perdiste. El programa se rie de ti")
    elif jugador0 == 0 and jugador1 == 2:
        print("Ganaste la batalla")
    elif jugador0 == 1 and jugador1 == 0:
        print("Ganaste la batalla")
    elif jugador0 == 1 and jugador1 == 1:
        print("Empate, me. llevo un papel")
    elif jugador0 == 1 and jugador1 == 2:
        print("Perdiste. El programa se rie de ti")
    elif jugador0 == 2 and jugador1 == 0:
        print("Perdiste. El programa se rie de ti")
    elif jugador0 == 2 and jugador1 == 1:
        print("Ganaste la batalla")
    elif jugador0 == 2 and jugador1 == 2:
        print("Empate, meee ;-;. que quieres?")
    else:
        print("Opcion no valida, juega puto")

def run():
    jugador0 = usuraioEleccion()
    jugador1 = programaEleccion()
    print(" ")
    piedraPapelTijera(jugador0, jugador1)


if __name__ == '__main__':
    run()