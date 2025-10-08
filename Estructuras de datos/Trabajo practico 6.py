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
for i in range(1):
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
print(f"Registro completo: {datos_alumnos}")
