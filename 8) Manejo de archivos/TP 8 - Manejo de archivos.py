# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Teclado,20000,7\n")
    archivo.write("Mouse,12000,10\n")
    archivo.write("Joystick,30000,3\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt","r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        linea = linea.split(",")
        print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt","a") as archivo:
    nombre = input("Ingrese el nombre del nuevo producto: ")
    precio = input(f"Ingrese el valor de {nombre}: $")
    cantidad = input(f"Ingrese la cantidad de {nombre}: ")
    archivo.write(f"{nombre},{precio},{cantidad}\n")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

productos = []
with open("productos.txt","r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        linea = linea.split(",")
        producto = {"nombre": linea[0],"precio":linea[1],"cantidad":linea[2]}
        productos.append(producto)

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

encontrado = False
nombre = input("Ingrese el nombre del producto que desea buscar: ")
for producto in productos:
    if nombre == producto["nombre"]:
        print(f"Producto: {nombre} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")
        encontrado = True
if encontrado == False:
    print("Producto no encontrado. ")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

print("\nLista actualizada:\n")
with open("productos.txt","w") as archivo:
    for linea in productos:
        archivo.write(f"{linea["nombre"]},{linea["precio"]},{linea["cantidad"]}\n")
        print(f"{linea["nombre"]},{linea["precio"]},{linea["cantidad"]}")
