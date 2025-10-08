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
    print("Contacto inexistente. \n")
    