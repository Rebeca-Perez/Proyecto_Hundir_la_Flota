import numpy as np
from utils import crear_tablero, crear_barco, colocar_barco, colocar_barcos, disparar, jugar
import variable



tablero_jugador = crear_tablero()
tablero_rival = crear_tablero()


tablero_jugador = colocar_barcos(variable.barcos_jugador, tablero_jugador)
tablero_rival = colocar_barcos(variable.barcos_rival, tablero_rival)

print("tablero jugador")
print(tablero_jugador)

print("tablero rival")
print(tablero_rival)


jugar(tablero_jugador, tablero_rival)



