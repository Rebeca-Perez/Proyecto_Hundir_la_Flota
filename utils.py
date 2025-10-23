import numpy as np


def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero

def crear_barco(eslora):
    barco = np.full((eslora,1), "O")
    return barco

def colocar_barco(barco, tablero):
    eslora = barco.shape[0]
    while True:
        posicion = np.random.choice(["H", "V"])
        fila = np.random.randint(0,9)
        columna = np.random.randint(0,9)
        
        if posicion == "H" and columna + eslora <= 10:
            libre = True
            for c in range(columna, columna + eslora):
                if tablero[fila, c] == "X":
                    libre = False
                    break
            if libre:
                tablero[fila, columna: columna+eslora] = "O"
                return tablero
        if posicion == "V" and fila + eslora <= 10:
            libre = True
            for f in range(fila, fila + eslora):
                if tablero[f, columna] == "X":
                    libre = False
                    break
            if libre:    
                tablero[fila: fila+eslora, columna] = "O"
                return tablero

def colocar_barcos(lista_barcos, tablero):
    for barco in lista_barcos:
        colocar_barco(barco, tablero)
    return tablero

def disparar(tablero, fila, columna):
    if tablero[fila, columna] == "O":  #utils
        print("tocado")
        tablero[fila, columna] = "X"
    else:
        print("Agua!")
        tablero[fila,columna] = "A"
    return tablero

def jugar(tablero_jugador, tablero_rival):
    turno = "jugador"
    continua = True
    while continua == True:
        if turno == "jugador":
            print("Tu turno")
            fila = int(input("Elige una fila de 0 a 9:"))
            columna = int(input("Elige una columna de 0 a 9:"))
            tablero = disparar(tablero_rival, fila, columna)
            if tablero_rival[fila,columna] == "A":
                turno = "rival"
        else:
            print("Turno rival")
            fila = np.random.randint(0,9)
            columna = np.random.randint(0,9)
            print(fila, columna)
            tablero_jugador = disparar(tablero_jugador, fila, columna)
            if tablero_jugador[fila, columna] == "A":
                turno = "jugador"



