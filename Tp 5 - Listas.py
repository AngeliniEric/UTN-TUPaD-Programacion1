#Tp 5 - Listas

#Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja
notas = [["Juan",7] , ["Eric",10] , ["Franco",6] , ["Florencia",4] , ["Julieta",9] , ["Josefina",8] , ["Salvador",5] , ["Gonzalo",10] ,["Julian",6] , ["Melina",3] ]
total=0
for i in range (len(notas)):
    print(notas[i])
    total = total + notas[i][1]
promedio = total / len(notas)
print(f"El promedio es de {promedio}")
notamax = notas[0][1]
notamin = notas[0][1]
for j in range (1, len(notas)):
    if notas[j][1] > notamax:
        notamax = notas[j][1]
    if notas[j][1] < notamin:
        notamin = notas[j][1]
print(f"Nota mas alta: {notamax}")
print(f"Nota mas baja: {notamin}")

print("-----------------------------------------------")
#Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
for i in range(5):
    prod = input(F"Ingrese el producto n°{i+1}: ")
    productos.append(prod)

ordenados = sorted(productos)
print("Productos ordenados: ")
for i in range(5):
    print(f"-{ordenados[i]}" )

eliminar = input("Ingrese el producto a eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
ordenados = sorted(productos)
print("Productos actuales: ")
for i in range(len(ordenados)):
    print(f"-{ordenados[i]}" )    

print("-----------------------------------------------")
#Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista

import random
numeros = []
pares = []
impares = []
for i in range(15):
    x = random.randint(1,100)
    numeros.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f"Cantidad de numeros pares: {len(pares)}")
print(f"Cantidad de numeros impares: {len(impares)}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")

print("-----------------------------------------------")
#Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
nuevosdatos = []
for i in range(len(datos)):
    if datos[i] not in nuevosdatos:
        nuevosdatos.append(datos[i])
print(f"Lista original: {datos}")        
print(f"Lista sin repetidos: {nuevosdatos}")

print("-----------------------------------------------")
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada

estudiantes = ["Julian", "Julieta", "Franco", "Paula", "Damian", "Maria", "Lucas", "Sofia"]
op = 1
while op > 0 and op < 4:
    print("-----------------------------------------------")
    print("1- Agregar estudiante")
    print("2- Eliminar estudiante")
    print("3- Mostrar lista")
    print("4- Salir")
    op = int(input("Ingrese una opcion -> "))
    print("-----------------------------------------------")
    if op == 1:
        nuevo = input("Ingrese el nombre del estudiante: ")
        estudiantes.append(nuevo)
    elif op == 2:
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        estudiantes.remove(eliminar)
    elif op == 3:
        print(f"Estudiantes: {estudiantes}")

#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).
listaoriginal = [1,2,3,4,5,6,7]
listarotada = []
for i in range(7):
    listarotada.append(listaoriginal[i-1])
print(f"Lista rotada: {listarotada}")    

print("-----------------------------------------------")
#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#•Calcular el promedio de las mínimas y el de las máximas.
#•Mostrar en qué día se registró la mayor amplitud térmica.
temp = [[8,20],[10,22],[5,19],[7,18],[9,19],[11,21],[13,23]]
dia = [ ["Lunes"],["Martes"],["Miercoles"],["Jueves"],["Viernes"],["Sabado"],["Domingo"] ]
prommin = 0
prommax = 0
for i in range(7):
    prommin = prommin + temp[i][0]
    prommax = prommax + temp[i][1]
prommin = prommin / 7
prommax = prommax / 7
print(f"Promedio temperatura minima: {prommin}.")
print(f"Promedio temperatura maxima: {prommax}")
amplitud = 0
mayoramp = dia[0]
for i in range(7):
    x = temp[i][1] - temp[i][0]
    if x > amplitud:
        amplitud = x
        mayoramp = dia[i]
print(f"Dia de mayor amplitud: {mayoramp} ")

print("-----------------------------------------------")
#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#•Mostrar el promedio de cada estudiante.
#•Mostrar el promedio de cada materia.
matrizx = [["Eric",8,7,10],["Gonzalo",6,8,8],["Julieta",4,9,9],["Josefina",5,6,7],["Martin",10,4,6]]

for i in range(5):
    prom = ( matrizx[i][1] + matrizx[i][2] + matrizx[i][3] ) / 3
    print(f"Promedio de {matrizx[i][0]}: {prom}")
print("--------------------")
promarq = 0
prommat = 0
promprog = 0
for i in range(5):
    promarq = promarq + matrizx[i][1]
    prommat = prommat + matrizx[i][2]
    promprog = promprog + matrizx[i][3]
promarq = promarq / 5
prommat = prommat / 5
promprog = promprog / 5
print(f"Promedio de Arquitectura y S.O.: {promarq}")
print(f"Promedio de matematica: {prommat}")
print(f"Promedio de programacion: {promprog}")

print("-----------------------------------------------")
#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#•Inicializarlo con guiones "-" representando casillas vacías.
#•Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#•Mostrar el tablero después de cada jugada.
tateti = [ ["-","-","-"] , ["-","-","-"] , ["-","-","-"] ]

for i in range(3):
    print(f"{tateti[i][0]} {tateti[i][1]} {tateti[i][2]}")
jugadas = 0
print("Para elegir el lugar del tablero tenes que indicar primero la fila y despues la columna, es decir que el centro seria 1-1.")
while jugadas < 9 :
    if jugadas % 2 == 0:
        print("Turno del jugador 1.")
        fila=int(input("Elige en que fila poner tu X"))
        columna=int(input("Elige en que columna poner tu X"))
        tateti[fila][columna] = "X"
    else:
        print("Turno del jugador 2.")
        fila=int(input("Elige en que fila poner tu O"))
        columna=int(input("Elige en que columna poner tu O"))
        tateti[fila][columna] = "O"
    jugadas = jugadas + 1
    for i in range(3):
        print(f"{tateti[i][0]} {tateti[i][1]} {tateti[i][2]}")
print("Juego terminado. ")

print("-----------------------------------------------")
#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#•Mostrar el total vendido por cada producto.
#•Mostrar el día con mayores ventas totales.
#•Indicar cuál fue el producto más vendido en la semana.

mat = [
    [10,15,14,8,4,9,11] ,
    [6,8,7,5,4,9,9],
    [20,25,24,25,28,26,18],
    [2,1,3,0,1,1,2]
]
ventas = [0,0,0,0]
for i in range(7):
    ventas[0] = ventas[0] + mat[0][i]
    ventas[1] = ventas[1] + mat[1][i]
    ventas[2] = ventas[2] + mat[2][i]
    ventas[3] = ventas[3] + mat[3][i]
print(f"Ventas del producto 1: {ventas[0]}")
print(f"Ventas del producto 2: {ventas[1]}")
print(f"Ventas del producto 3: {ventas[2]}")
print(f"Ventas del producto 4: {ventas[3]}")
masvendido = 0
prodmasvend = 0
for i in range(4):
    if ventas[i] > masvendido:
        masvendido = ventas[i]
        prodmasvend = i + 1
print(f"El mas vendido fue el producto {prodmasvend}")
