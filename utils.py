import numpy as np


def crear_tablero():
    """
        Función para crear los 2 tableros del juego hundir la flota.
        Crea un tablero de 10x10 en el que las casillas son "_".
    """
    tablero = np.full((10,10), "_")
    return tablero

def crear_barco(eslora):
    """
        Función utilizada para crear los barcos.
        crea una fila de "O" del tamaño de cada barco.
    """
    barco = np.full((eslora,1), "O")
    return barco

def colocar_barco(barco, tablero):
    """
        Función utilizada para colocar los barcos de forma aleatoria.
        Se crea la variable eslora dentro de la función, para que calcule la longitud de cada barco.
        Se utiliza el bucle while para que se ejecuten las condiciones siguientes mientras haya barcos que colocar.
        Se crean las variables de posición, fila y columna para que se decidan las posiciones al azar.
        2 condiciones if: una para las posiciones horizontales y otra para las verticales. 
        Mismo funcionamiento, cambia si se centra en las filas o en las columnas.
        Comprueba que se cumplen las condicines de tamaño de tablero, barco y que las casillas están vacías con np.all

    """
    eslora = barco.shape[0]
    libre = True
    while libre:
        posicion = np.random.choice(["H", "V"])
        fila = np.random.randint(0,9)
        columna = np.random.randint(0,9)
        
        if posicion == "H" and columna + eslora <= 10 and np.all(tablero[fila, columna: columna+eslora]=="_"):
                tablero[fila, columna: columna+eslora] = "O"
                libre = False
        if posicion == "V" and fila + eslora <= 10 and np.all(tablero[fila: fila+eslora, columna] == "_"):   
                tablero[fila: fila+eslora, columna] = "O"
                libre = False

def colocar_barcos(lista_barcos, tablero):
    """
        Recorre la lista de barcos creada y ejecuta la función colocar barcos con todos.
    """
    for barco in lista_barcos:
        colocar_barco(barco, tablero)
    return tablero

def disparar(tablero, fila, columna):
    """
        Función para comprobar si en esa fila y columna hay barco o no, 
        si hay barco sustituye la letra "O" por una "X" e imprime un mensaje de "tocado".
        Si no hay barco, sustituye la "_" por una "A", imprime el mensaje de "agua".
    """
    if tablero[fila, columna] == "O":
        print("Tocado")
        tablero[fila, columna] = "X"
    else:
        print("Agua!")
        tablero[fila,columna] = "A"
    return tablero

def jugar(tablero_jugador, tablero_rival):
    """
        Función jugar: Sistema de turnos para jugar.
        Se define el turno de Jugador y que continua es True.
        A partir de ahí, se utiliza un bucle while, mientras continua sea True, si el turno es del jugador,
        imprime un mensaje indicando el turno y lanza 2 inputs para que introduzcamos la fila y columna a la que dispara.
        Llamas a la función disparar para que se ejecute y si no hay barco, cambia el turno al rival.
        Se repite el proceso con el rival, las filas y columnas son elegidas de manera aleatoria y se imprimen.
        Con np.any() comprobamos si quedan barcos, si no quedan, se acaba el juego.
        Imprime mensaje si se ha ganado o perdido.
    """
    print("Empieza el juego!")

    turno = "jugador"
    continua = True
    while continua == True:
        if turno == "jugador":
            print("Tu turno")
            fila = int(input("Elige una fila de 0 a 9:"))
            columna = int(input("Elige una columna de 0 a 9:"))
            tablero_rival = disparar(tablero_rival, fila, columna)
            if tablero_rival[fila,columna] == "A":
                turno = "rival"
            print("Tablero rival")
            print(tablero_rival)
        else:
            print("Turno rival")
            fila = np.random.randint(0,9)
            columna = np.random.randint(0,9)
            print("Fila: ", fila, "Columna: ", columna)
            tablero_jugador = disparar(tablero_jugador, fila, columna)
            if tablero_jugador[fila, columna] == "A":
                turno = "jugador"
            print("Tablero jugador")
            print(tablero_jugador)
        
        if not np.any(tablero_jugador == "O"):
            print("Lo siento, has perdido. Vuelve a intentarlo!")
            continua = False
        elif not np.any(tablero_rival == "O"):
            print("Has ganado!!")
            continua = False



