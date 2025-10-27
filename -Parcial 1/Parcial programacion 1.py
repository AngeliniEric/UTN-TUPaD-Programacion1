#Examen Parcial – Programación 1 - Angelini Eric

titulos = []
ejemplares = []
opcion = True
while opcion == True:
    print("\n")
    print("======= Menú principal =======")
    print("\n")
    print("1- Ingresar títulos")
    print("2- Ingresar ejemplares")
    print("3- Mostrar catálogo")
    print("4- Consultar disponibilidad")
    print("5- Listar agotados")
    print("6- Agregar título")
    print("7- Actualizar ejemplares")
    print("8- Salir")
    print("\n")
    print("==============================")
    print("\n")

    op = input("Ingrese una opción: ")
    if not op.isdigit() or int(op) < 1 or int(op) > 8:
        print("Opción invalida. ")
        continue
    op = int(op)
    match op:
        case 1:
            titulonuevo = input("Ingrese un nuevo título: ").strip()
            if titulonuevo in titulos:
                (print("Título existente."))
                input("Presione Enter para volver al menú. ")
            elif titulonuevo == "":
                print("Título vacio.")
                input("Presione Enter para volver al menú. ")
            else:
                titulos.append(titulonuevo)
                ejemplares.append(0)
                print("Título agregado!")
                input("Presione Enter para volver al menú. ")
        
        case 2:
            for i in range(len(titulos)):
                cantidad = input(f"Ingrese la cantidad que desea agregar para {titulos[i]}: ")
                if not cantidad.isdigit() or int(cantidad) < 0:
                    print("Debe ingresar un número positivo o cero.")
                else:
                    ejemplares[i] = ejemplares[i] + int(cantidad)
            input("Presione Enter para volver al menú. ")
        
        case 3:

            if len(titulos) == 0:
                print("Catálogo vacío.")
                input("Presione Enter para volver al menú. ")
            else:
                print("Catálogo: ")
                for i in range(len(titulos)):
                    print(f"Titulo: {titulos[i]} --> Ejemplares: {ejemplares[i]}.")
                input("Presione Enter para volver al menú. ")

        case 4:
            buscar = input("Ingrese el título: ").strip()
            if buscar in titulos:
                indice = titulos.index(buscar)
                print(f"Cantidad de ejemplares de {titulos[indice]}: {ejemplares[indice]}")
            elif buscar == "":
                print("Debe ingresar un título. ")
            else:
                print("Título inexistente. ")
            input("Presione Enter para volver al menú. ")

        case 5: 
            if len(titulos) == 0:
                print("Catálogo vacío. ")
            else:
                sinstock = False
                print("Títulos sin stock: ")
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        print(f"-{titulos[i]}")
                        sinstock = True
                if sinstock == False:
                    print("No hay. Todos los títulos tienen stock. ")
            input("Presione Enter para volver al menú. ")

        case 6:
            titulonuevo = input("Ingrese un nuevo título: ").strip()
            if titulonuevo == "":
                print("El título no puede estar vacío.")
            elif titulonuevo in titulos:
                print("Ese título ya existe en el catálogo.")
            else:
                cantidad = input("Ingrese la cantidad de ejemplares: ")
                if not cantidad.isdigit() or int(cantidad) < 0:
                    print("Debe ingresar un número entero positivo o cero.")
                else:
                    titulos.append(titulonuevo)
                    ejemplares.append(int(cantidad))
                    print("Título y ejemplares agregados!")
            input("Presione Enter para volver al menú. ")

        case 7:
            if len(titulos) == 0:
                print("Catálogo vacío. ")
            else:
                print("Elija el libro que desea modificar.")
                for i in range(len(titulos)):
                    print(f"{i+1}) {titulos[i]}. ")
                print("\n")
                modificar = input("Opcion --> ")
                if not modificar.isdigit() or int(modificar) < 1 or int(modificar) > len(titulos):
                    print("Opción invalida. ")
                else:
                    modificar = int(modificar)
                    print(f"Título a modificar: {titulos[modificar-1]}")
                    print("¿Prestamo o devolución? ")
                    print("1) Prestamo ")
                    print("2) Devolución ")
                    pod = input("Opción --> ")
                    if not pod.isdigit() or int(pod) < 1 or int(pod) > 2:
                        print("Opción invalida. ")
                    else:
                        pod = int(pod)
                        if pod == 1:
                            if ejemplares[modificar-1] == 0:
                                print("No hay stock disponible para prestar. ")
                            else:
                                ejemplares[modificar-1] = ejemplares[modificar-1] - 1
                                print(f"Cantidad actual de ejemplares de {titulos[modificar-1]}: {ejemplares[modificar-1]}")
                        elif pod == 2:
                            ejemplares[modificar-1] = ejemplares[modificar-1] + 1
                            print(f"Cantidad actual de ejemplares de {titulos[modificar-1]}: {ejemplares[modificar-1]}")
            input("Presione Enter para volver al menú. ")

        case 8: 
            opcion = False


