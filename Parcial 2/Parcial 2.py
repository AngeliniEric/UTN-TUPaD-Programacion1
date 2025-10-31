import csv
import os

nombre_archivo = "catalogo.csv" 

def obtener_catalogo():
    catalogo = []

    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo,"w",newline="",encoding="utf-8")as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["titulo","cantidad"])
            escritor.writeheader()
            return catalogo

    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            cantidad = fila.get("cantidad")
            titulo = fila.get("titulo")

            if titulo and cantidad and cantidad.isdigit():
                catalogo.append({"titulo": titulo,"cantidad": int(cantidad)})
            else:
                print(f"Error: Fila con formato incorrecto: {fila}")
        return catalogo

def agregar_titulo(catalogo,titulo):
        catalogo.append(titulo)
        print("\nTítulo agregado!\n")

def existe_titulo(catalogo_actual,nombre):
    nombre_comparar = nombre.strip().lower()
    for libro in catalogo_actual:
        titulo_existente = libro["titulo"].strip().lower()
        if titulo_existente == nombre_comparar:
            return True
    return False

def mostrar_catalogo(catalogo):
    print("\n---------- Catálogo ----------\n")
    if not catalogo:
        print("Catálogo vacío. ")
        input("\nPresione Enter para volver al menú. ")
        return
    for fila in catalogo:
        print(f"{fila["titulo"]} - {fila["cantidad"]}")
    input("\nPresione Enter para volver al menú. ")

def guardar_catalogo(catalogo):
    with open(nombre_archivo,"w",newline="",encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=["titulo","cantidad"])
        escritor.writeheader()
        escritor.writerows(catalogo)
    print("\n¡Catálogo actualizado! ")

def validar_cantidad(mensaje):
    while True:
        x = input(mensaje)
        if x.isdigit():
            cant = int(x)
            if cant >=0:
                return cant
            else: 
                print("Error: Debe ingresar una cantidad positiva o 0.")
        else:
            print("Error: Debe ingresar una cantidad positiva o 0. ")

def nuevo_titulo(catalogo_actual):
            print("\n---------- Nuevo título ----------\n")
            nombre = input("Ingrese el título: ").strip()
            if not nombre:
                print("\nError: El título no puede estar vacío. ")
                input("\nPresione Enter para volver al menú. ")
                return
            
            if existe_titulo(catalogo_actual,nombre):
                print(f"\nError: El título {nombre} ya existe. ")
                input("\nPresione Enter para volver al menú. ")
                return
            
            cantidad = validar_cantidad("Ingrese la cantidad de ejemplares: ")
            titulo = {"titulo":nombre,"cantidad":cantidad}
            agregar_titulo(catalogo_actual,titulo)
            guardar_catalogo(catalogo_actual)
            input("\nPresione Enter para volver al menú. ")

def ingresar_titulos(catalogo_actual):
    print("\n---------- Ingresar títulos ----------\n")
    libros_nuevos = validar_cantidad("Ingrese la cantidad de nuevos títulos que desea agregar: ")
    for i in range (libros_nuevos):
        nuevo_titulo(catalogo_actual)

def buscar_libro(catalogo_actual,nombre):
    nombre_buscar = nombre.strip().lower()
    for libro in catalogo_actual:
        titulo = libro["titulo"].strip().lower()
        if titulo == nombre_buscar:
            return libro
    return None

def modificar_ejemplares(catalogo_actual):
    print("\n---------- Ingresar ejemplares ----------\n")
    
    if not catalogo_actual:
        print("El catálogo está vacío.")
        input("\nPresione Enter para volver al menú. ")
        return
    
    nombre = input("Ingrese el título al que desea agregar ejemplares: ").strip()
    if not nombre:
        print("\nEl título no puede estar vacío. ")
        input("\nPresione Enter para volver al menú. ")
        return
    
    libro = buscar_libro(catalogo_actual,nombre)
    if libro:
        print(f"Libro encontrado!\nNombre: {libro["titulo"]} - Ejemplares: {libro["cantidad"]}\n")
        agregar = validar_cantidad("Ingrese la cantidad de ejemplares que desea agregar: ")
        if agregar > 0:
            libro["cantidad"] += agregar
            print("\nEjemplares agregados con exito!")
            print(f"Ahora {libro["titulo"]} tiene {libro["cantidad"]} ejemplares. ")
            guardar_catalogo(catalogo_actual)
        else:
            print("No se agregaron ejemplares!")
    else:
        print("El título no se encuentra en el catálogo. ")
    input("\nPresione Enter para volver al menú. ")

def consultar_disponibilidad(catalogo_actual):
    print("\n---------- Consultar disponibilidad ----------\n")
    
    if not catalogo_actual:
        print("El catálogo está vacío.")
        input("\nPresione Enter para volver al menú. ")
        return
    
    nombre = input("Ingrese el título que desea consultar: ").strip()
    if not nombre:
        print("El título no puede estar vacío. ")
        input("\nPresione Enter para volver al menú. ")
        return
    
    libro = buscar_libro(catalogo_actual,nombre)
    if libro:
        print(f"\nLibro encontrado!\nNombre: {libro["titulo"]} - Ejemplares: {libro["cantidad"]}\n")
    else:
        print(f"\nNo se encontró el título {nombre}")
    input("\nPresione Enter para volver al menú. ")

def listar_agotados(catalogo_actual):
    print("\n---------- Listar agotados ----------\n")

    if not catalogo_actual:
        print("Catálogo vacío. ")
        input("\nPresione Enter para volver al menú. ")
        return
    else:
        sinstock = False

    for libro in catalogo_actual:
        if libro["cantidad"] == 0:
            print(f"{libro["titulo"]} - Agotado!")
            sinstock = True

    if not sinstock:
        print("Todos los libros tienen stock! ")
        
    input("\nPresione Enter para volver al menú. ")

def actualizar_ejemplares(catalogo_actual):
    print("\n---------- Actualizar ejemplares ----------\n")

    if not catalogo_actual:
        print("Catálogo vacío. ")
        input("\nPresione Enter para volver al menú. ")
        return
    else:
        sinstock = False

    nombre = input("Ingrese el título que desea actualizar: ")
    if not nombre:
        print("Error: Título vacío. ")
        input("\nPresione Enter para volver al menú. ")
        return

    libro = buscar_libro(catalogo_actual,nombre)
    if not libro:
        print("Título no encontrado. ")
        input("\nPresione Enter para volver al menú. ")
        return
    
    print("\n---------- Préstamo o devolución ----------\n")
    print("1) Préstamo. ")
    print("2) Devolución. ")
    opcion = input("\nIngrese una de las opciones ---> ")
    if opcion == "1":
        if libro["cantidad"] > 0:
            libro["cantidad"]-= 1
            print("\nPréstamo confirmado! ")
            guardar_catalogo(catalogo_actual)
        else:
            print("\nError: No hay ejemplares disponibles para prestar! ")

    elif opcion == "2":
        libro["cantidad"]+= 1
        print("\nDevolución confirmada! ")
        guardar_catalogo(catalogo_actual)

    else:
        print("Opción inválida!")
        input("\nPresione Enter para volver al menú. ")
        return
    
    input("\nPresione Enter para volver al menú. ")



catalogo = obtener_catalogo()

menu = True
while menu == True:


    print("\n---------- Biblioteca escolar ----------\n")
    print("1) Ingresar títulos. ")
    print("2) Ingresar ejemplares. ")
    print("3) Mostrar catálogo. ")
    print("4) Consultar disponibilidad. ")
    print("5) Listar agotados. ")
    print("6) Agregar título. ")
    print("7) Actualizar ejemplares. ")
    print("8) Salir. ")
    op = input("\nIngrese una de las opciones ---> ")

    match op:
        
        case "1":
            ingresar_titulos(catalogo)

        case "2":
            modificar_ejemplares(catalogo)

        case "3":
            mostrar_catalogo(catalogo)

        case "4":
            consultar_disponibilidad(catalogo)

        case "5":
            listar_agotados(catalogo)

        case "6":
            nuevo_titulo(catalogo)

        case "7":
            actualizar_ejemplares(catalogo)

        case "8":

            menu = False
        
        case _:
            print("\nOpción inválida! Seleccione una opción correcta. ")
            input("\nPresione Enter para volver al menú. ")
            
