"""
Tarea Semana 12: Reserva de un asiento en sala de cine
Unidad 3. Arreglos N-Dimensionales
Tema 3.2.2. Iteracion sobre arreglos multidimensionales utilizando bucles anidados
 
Autor: EDINSON GONZALO PEREZ CASTILLO
Descripcion: Programa que gestiona la reserva de un asiento en una sala de
cine de 3 filas por 4 columnas. La sala se representa con una matriz
(lista de listas), donde 0 significa asiento libre y 1 significa
asiento reservado.
"""
 
# Dimensiones de la sala de cine
NUM_FILAS = 3
NUM_COLUMNAS = 4
 
# 1. Crear la matriz "asientos" con todos los valores en 0 (todos libres)
# Se arma fila por fila con un bucle para evitar que las filas
# terminen apuntando a la misma lista en memoria
asientos = []
for i in range(NUM_FILAS):
    fila_nueva = [0] * NUM_COLUMNAS
    asientos.append(fila_nueva)
 
# 2. Pedir al usuario la fila y la columna del asiento a reservar
# Se valida que el valor ingresado este dentro del rango permitido
fila = int(input(f"Ingrese fila (0 a {NUM_FILAS - 1}): "))
while fila < 0 or fila >= NUM_FILAS:
    print("Fila fuera de rango, intente de nuevo.")
    fila = int(input(f"Ingrese fila (0 a {NUM_FILAS - 1}): "))
 
columna = int(input(f"Ingrese columna (0 a {NUM_COLUMNAS - 1}): "))
while columna < 0 or columna >= NUM_COLUMNAS:
    print("Columna fuera de rango, intente de nuevo.")
    columna = int(input(f"Ingrese columna (0 a {NUM_COLUMNAS - 1}): "))
 
# 3. Marcar el asiento como reservado (valor 1)
# Mejora opcional: avisar si el asiento ya estaba reservado
if asientos[fila][columna] == 1:
    print(f"El asiento ({fila}, {columna}) ya estaba reservado.")
else:
    asientos[fila][columna] = 1
    print(f"Asiento ({fila}, {columna}) reservado con exito.")
 
# 4. Mostrar la matriz completa en formato de tabla con bucles anidados
print("\nEstado de la sala:")
for i in range(NUM_FILAS):
    for j in range(NUM_COLUMNAS):
        # end=" " evita el salto de linea para imprimir toda la fila junta
        print(asientos[i][j], end=" ")
    # Salto de linea al terminar de recorrer cada fila
    print()
 