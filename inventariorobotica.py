
inventario = []

def registrar_componente():
    print("\n--- REGISTRAR COMPONENTE ---")

    id_componente = input("Ingrese el ID del componente: ")

    repetido = False

    for componente in inventario:
        if componente["id"] == id_componente:
            repetido = True

    if repetido:
        print("Error: Este ID ya existe.")
    else:
        nombre = input("Ingrese el nombre: ")
        categoria = input("Ingrese la categoria: ")

        try:
            stock = int(input("Ingrese la cantidad disponible: "))
            precio = float(input("Ingrese el precio unitario: "))

            if stock < 0 or precio < 0:
                print("Error: Los valores no pueden ser negativos.")
            else:
                nuevo_componente = {
                    "id": id_componente,
                    "nombre": nombre,
                    "categoria": categoria,
                    "stock": stock,
                    "precio_unitario": precio
                }

                inventario.append(nuevo_componente)

                print("Componente registrado correctamente.")

        except ValueError:
            print("Error: Ingrese valores numericos validos.")


def mostrar_inventario():
    print("\n--- INVENTARIO COMPLETO ---")

    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        for componente in inventario:
            print("-------------------------")
            print("ID:", componente["id"])
            print("Nombre:", componente["nombre"])
            print("Categoria:", componente["categoria"])
            print("Stock:", componente["stock"])
            print("Precio:", componente["precio_unitario"])


def filtrar_categoria():
    print("\n--- FILTRAR POR CATEGORIA ---")

    categoria_buscar = input("Ingrese la categoria: ")
    encontrado = False

    for componente in inventario:
        if componente["categoria"].lower() == categoria_buscar.lower():
            print("-------------------------")
            print("ID:", componente["id"])
            print("Nombre:", componente["nombre"])
            print("Categoria:", componente["categoria"])
            print("Stock:", componente["stock"])
            print("Precio:", componente["precio_unitario"])

            encontrado = True

    if encontrado == False:
        print("No se encontraron componentes en esa categoria.")


def actualizar_stock():
    print("\n--- ACTUALIZAR STOCK ---")

    id_buscar = input("Ingrese el ID del componente: ")
    encontrado = False

    for componente in inventario:
        if componente["id"] == id_buscar:
            encontrado = True

            print("Componente:", componente["nombre"])
            print("Stock actual:", componente["stock"])

            print("1. Agregar unidades")
            print("2. Restar unidades")

            opcion = input("Seleccione una opcion: ")

            try:
                cantidad = int(input("Ingrese la cantidad: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")

                elif opcion == "1":
                    componente["stock"] += cantidad
                    print("Stock actualizado correctamente.")
                    print("Nuevo stock:", componente["stock"])

                elif opcion == "2":
                    if componente["stock"] >= cantidad:
                        componente["stock"] -= cantidad
                        print("Stock actualizado correctamente.")
                        print("Nuevo stock:", componente["stock"])
                    else:
                        print("Error: No hay suficiente stock.")

                else:
                    print("Opcion no valida.")

            except ValueError:
                print("Error: Ingrese un numero entero.")

            break

    if encontrado == False:
        print("No se encontro ningun componente con ese ID.")


while True:

    print("\n================================")
    print(" INVENTARIO - LABORATORIO ROBOTICA")
    print("================================")
    print("1. Registrar componente")
    print("2. Mostrar inventario")
    print("3. Filtrar por categoria")
    print("4. Actualizar stock")
    print("5. Salir")
    print("================================")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_componente()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        filtrar_categoria()

    elif opcion == "4":
        actualizar_stock()

    elif opcion == "5":
        print("Gracias por utilizar el sistema.")
        break

    else:
        print("Opcion incorrecta. Intente nuevamente.")
