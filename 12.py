
from collections import deque

turno = deque(['X', 'O'])

tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def rotar_turno():
    turno.rotate()
    return turno[0]

def mostrar_tablero():
    print ("")
    for fila in tablero:
        print(fila) 

def procesar_posicion(posicion):
    fila, columna = posicion.split(',')
    return int(fila)-1, int(columna)-1

def posicion_correcta(posicion):
    if 0 <= 2 and 0 <= posicion[1] <= 2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
        return False

def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador

def ha_ganado(jugador):
    if tablero[0] == [jugador, jugador, jugador] or tablero[1] == [jugador, jugador, jugador] or tablero[2] == [jugador, jugador, jugador]:
        return True
    elif tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] == jugador:
        return True
    elif tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == jugador:
        return True
    elif tablero[0][2] == jugador and tablero[1][2] == jugador and tablero[2][2] == jugador:
        return True
    elif tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    elif tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    else:
        return False

def juego():
    mostrar_tablero()
    jugador = rotar_turno()
    while True:
        posicion = input(f"Juega {jugador}. Elige una posicion: ").upper()
        if posicion == 'SALIR':
            break

        
        try:
            posicion_l = procesar_posicion(posicion)
        except:
            print(f'Error, posicion {posicion} no valida')
            continue    
        if posicion_correcta(posicion_l):
            print("Posicion correcta")
            actualizar_tablero(posicion_l, jugador)
            mostrar_tablero()
            if ha_ganado(jugador):
                print(f'Ganador {jugador}')
                break
            jugador = rotar_turno()
        else:
            print("Posicion incorrecta")
        
        
juego()