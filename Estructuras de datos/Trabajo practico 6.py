print("\n")
print("Trabajo práctico 6: Estructuras de datos. \n ")
# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {"Banana":1200,"Ananá":2500,"Melón":3000,"Uva":1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"Ejercicio 1: {precios_frutas} \n")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(f"Ejercicio 2: {precios_frutas} \n")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

frutas = list(precios_frutas.keys())
print(f"Ejercicio 3: {frutas} \n")

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

print("Ejercicio 4: \n")
agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ahora ingrese el número de teléfono: ")
    print("\n")
    agenda[nombre] = numero 
buscar = input("Buscar contacto: ")
if buscar in agenda:
    print(f"Número de teléfono: {agenda[buscar]}")
else:
    print("Contacto inexistente. ")
print("\n")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

print("Ejercicio 5: \n")
frase = input("Ingrese una frase: ")
frase = frase.lower()
palabras = frase.split()
palabras_unicas = set(palabras)
print(f"Palabras unicas: {palabras_unicas}")
palabra_cantidad = {}
for palabra in palabras:
    if palabra in palabra_cantidad:
        palabra_cantidad[palabra] += 1
    else: 
        palabra_cantidad[palabra] = 1
print(f"{palabra_cantidad}")
print("\n")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

print("Ejercicio 6: \n")
datos_alumnos = {}
for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno n°{i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} de {alumno}: "))
        notas.append(nota)
    tupla_notas = tuple(notas)
    datos_alumnos[alumno] = tupla_notas
for nombre, notas in datos_alumnos.items():
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es de: {promedio}")
print("\n")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

print("Ejercicio 7: \n")
parcial1 = {7,12,24,31,47,52,66,79,88,95}
parcial2 = {7,15,22,31,44,52,66,71,84,95}
ambos = parcial1 & parcial2 
print(f"Alumnos que aprobaron ambos parciales: {ambos}")
solo_uno = parcial1 ^ parcial2 
print(f"Alumnos que aprobaron solo uno de los parciales: {solo_uno}")
al_menos_uno = parcial1 | parcial2
print(f"Aprobaron al menos un parcial: {al_menos_uno}")
print("\n")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

print("Ejercicio 8: \n")
inventario = {"mouse": 7, "teclado": 9, "monitor": 2, "joystick": 18, "auriculares": 24}
bucle = True
while bucle == True:
    print("======= Menú principal ======= \n")
    print("1) Consultar stock. ")
    print("2) Agregar stock. ")
    print("3) Agregar un nuevo producto. ")
    print("4) Salir. \n")
    opcion = int(input("Ingrese una de las opciones ---> "))

    match opcion: 
        case 1:
            buscar = input("Ingrese el producto que desea consultar: ")
            if buscar in inventario:
                print(f"Stock de {buscar}: {inventario[buscar]}")
            else:
                print("Producto inexistente. ")
            input("\nPresione Enter para volver al menú. ")
        
        case 2: 
            buscar = input("Ingrese el producto al que desea agregar stock: ")
            if buscar in inventario:
                stock = int(input("Ingrese la cantidad de stock a sumar: "))
                inventario[buscar] += stock
                print(f"Stock actual de {buscar}: {inventario[buscar]}")
            else:
                print("Producto inexistente. ")
            input("\nPresione Enter para volver al menú. ") 

        case 3:
            buscar = input("Ingrese el nuevo producto: ")
            if buscar in inventario:
                print("Producto ya existente. ")   
            else:
                inventario[buscar] = 0
                print(f"Producto {buscar} agregado correctamente! ")
            input("\nPresione Enter para volver al menú. ")
        
        case 4:
            print("Hasta pronto! ")
            bucle = False
print("\n")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

print("Ejercicio 9: \n")
agenda = { 
    ("lunes" , "18:00") : "Estudio" ,
    ("martes" , "20:00") : "Boxeo" , 
    ("miercoles" , "19:00") : "Fútbol" , 
    ("jueves" , "20:30") : "Piano" ,
    ("viernes" , "21:00") : "Cita"
    }

consulta = input("Ingrese el dia y horario que desea consultar: ")
consulta = consulta.split()
consulta = tuple(consulta)
if consulta in agenda:
    print(f"El {consulta} está ocupador por ---> {agenda[consulta]}")
else: 
    print(f"El {consulta} está libre. ")
print("\n")

