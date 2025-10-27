#Ejercicio 1
for i in range(101):
    print(i)

#Ejercicio 2
n = input("Ingrese un numero: ")
digitos = len(n)
print(f"El numero tiene {digitos} digitos")

#Ejercicio 3
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
suma = 0
if n1 > n2:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1
for i in range(menor+1, mayor):
    suma += i
print(f"La suma de los numeros entre {menor} y {mayor} es: {suma}")

#Ejercicio 4
n = int(input("Ingrese un numero: "))
suma = 0
while n != 0:
    suma += n
    print(f"Valor acumulado: {suma}")
    n = int(input("Ingrese otro numero (0 para terminar): "))

#Ejercicio 5
import random
numero_aleatorio = random.randint(0, 9) 
n = int(input("Ingrese un numero entre 0 y 9:  "))
intentos = 1
while n != numero_aleatorio:
    intentos += 1
    n = int(input("Intente nuevamente: "))
print(f"Adivinaste, el numero era {numero_aleatorio}. Cantidad de intentos: {intentos} ")

#Ejercicio 6
for i in range(100, 0, -2):
    print(i)

#Ejercicio 7
n = int(input("Ingrese un numero positivo: "))
total = 0
for i in range(0,n):
    total += i
print(f"Suma de los numeros entre 0 y {n}: {total}")

#Ejercicio 8
par = 0
impar = 0
pos = 0
neg = 0
for i in range(100):
    n =int(input("Ingrese un numero: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
print(f"Cantidad de numeros pares: {par}")
print(f"Cantidad de numeros impares: {impar}")
print(f"Cantidad de numeros positivos: {pos}")  
print(f"Cantidad de numeros negativos: {neg}")

#Ejercicio 9
cant = 100
suma = 0
for i in range(cant):
    n = int(input("Ingrese un numero: "))
    suma += n
media = suma / cant
print(f"La media es: {media}")

#Ejercicio 10
n = int(input("Ingrese el numero a invertir: "))
invertido = 0
while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10 
print(f"Numero invertido: {invertido}")