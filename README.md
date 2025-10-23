# Proyecto_Hundir_la_Flota
![imagen](hundir-la-flota-juego-de-mesa.jpg)

---

Versión en Python del clásico juego **Hundir la flota**. 
El jugador y el rival colocan sus barcos en un tablero de 10x10 y se enfrentan.

---
## Librerías utilizadas

- NumPy

## Reglas básicas del juego

- Cada jugador (tú y el rival controlado por el ordenador) tiene un tablero de 10x10.

- Los barcos se colocan aleatoriamente en el tablero.

- Los barcos tienen las siguientes longitudes:

    + 1 barco de 4 casillas

    + 2 barcos de 3 casillas

    + 3 barcos de 2 casillas

- En cada turno:

    + Introduces la fila y columna (de 0 a 9) donde quieres disparar.

    + Si aciertas, se marca con una X.

    + Si fallas, se marca con una A.

Gana el primero que hunda todos los barcos del oponente.

## Funcionalidades principales

#### utils.py

Contiene todas las funciones que gestionan la lógica del juego.

#### variables.py

Define las flotas iniciales de jugador y rival

#### main.py

Ejecuta el flujo principal del juego:

+ Crea los tableros.

+ Coloca los barcos.

+ Muestra ambos tableros.

+ Inicia la partida con jugar().

### Autor: Rebeca Pérez
