#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Mayor de edad")


#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")


#Ejercicio 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par" )
else:
    print("Por favor, ingrese un numero par")


#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")


#Ejercicio 5
contrasena = len(input("Ingrese su contraseña: "))
if contrasena >= 8 and contrasena <= 14:
    print("Ha ignresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres ")


#Ejercicio 6
from statistics import mean, median, mode
import random
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo")
if media < mediana and mediana < moda:
    print("Sesgo negativo")
if media == mediana and mediana == moda:
    print("No hay sesgo")


#Ejercicio 7
palabra = input("Ingrese una palabra: ")
ultimaletra = palabra[-1]
if ultimaletra == "a" or ultimaletra == "e" or ultimaletra == "i" or ultimaletra == "o" or ultimaletra == "u":
    print(f"{palabra}!")


#Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 si quiere su nombre en mayusculas" "\n" "Ingrese 2 si quiere su nombre en minusculas: " "\n" "Ingrese 3 si queire su nombre con la primer letra en mayuscula: "))
if opcion == 1:
    print(nombre.upper())
if opcion == 2:
    print(nombre.lower())
if opcion == 3:
    nombre = nombre.lower()
    print(nombre.title())   


#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    prinf("Muy leve")
if magnitud >= 3 and magnitud < 4:
    print("Leve")
if magnitud >= 4 and magnitud < 5:
    print("Moderado")   
if magnitud >= 5 and magnitud < 6:
    print("Fuerte")
if magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
if magnitud >= 7:
    print("Extremo")


#Ejercicio 10
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = input("Ingrese el mes (1-12): ")
dia = int(input("Ingrese el dia (1-31): "))
if hemisferio == "N":
    if (mes == "12" and dia >= 21) or (mes == "1") or (mes == "2") or (mes == "3" and dia < 20):
        print("Invierno")
    if (mes == "3" and dia >= 20) or (mes == "4") or (mes == "5") or (mes == "6" and dia < 21):
        print("Primavera")
    if (mes == "6" and dia >= 21) or (mes == "7") or (mes == "8") or (mes == "9" and dia < 22):
        print("Verano")
    if (mes == "9" and dia >= 22) or (mes == "10") or (mes == "11") or (mes == "12" and dia < 21):
        print("Otoño")
if hemisferio == "S":
    if (mes == "6" and dia >= 21) or (mes == "7") or (mes == "8") or (mes == "9" and dia < 22):
        print("Invierno")
    if (mes == "9" and dia >= 22) or (mes == "10") or (mes == "11") or (mes == "12" and dia < 21):
        print("Primavera")
    if (mes == "12" and dia >= 21) or (mes == "1") or (mes == "2") or (mes == "3" and dia < 20):
        print("Verano")
    if (mes == "3" and dia >= 20) or (mes == "4") or (mes == "5") or (mes == "6" and dia < 21):
        print("Otoño")  
