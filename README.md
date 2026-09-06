# Reserva de un asiento en sala de cine

**Estudiante:** EDINSON GONZALO PEREZ CASTILLO
**Asignatura:** Programación — Unidad 3, Tema 3.2.2 (Iteración sobre arreglos multidimensionales)
**Tarea:** Semana 12

## Objetivo

Programa en Python que gestiona la reserva de asientos de una sala de cine de 3 filas por 4 columnas. La sala se representa como una matriz (lista de listas) donde `0` indica asiento libre y `1` indica asiento reservado. El programa aplica los conceptos de creación de matrices, acceso por índices de fila y columna, y recorrido con bucles anidados.

## ¿Qué hace el programa?

1. Crea la matriz `asientos` de 3x4 con todos los asientos libres (0).
2. Pide al usuario la fila (0 a 2) y la columna (0 a 3) del asiento a reservar, validando que estén en rango.
3. Marca el asiento como reservado (1), avisando si ya estaba ocupado.
4. Muestra el estado completo de la sala como una tabla, recorriendo la matriz con dos bucles anidados.

## Cómo ejecutarlo

Requiere Python 3 instalado.

```bash
python3 reserva_cine.py
```

Luego ingresar la fila y la columna cuando el programa las solicite.

### Ejemplo de ejecución

```
Ingrese fila (0 a 2): 1
Ingrese columna (0 a 3): 2
Asiento (1, 2) reservado con exito.

Estado de la sala:
0 0 0 0
0 0 1 0
0 0 0 0
```
