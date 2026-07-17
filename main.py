from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


restaurante = Restaurante()


def menu() -> None:

    while True:

        print("\n================================")
        print("     SISTEMA DE RESTAURANTE")
        print("================================")
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("--------------------------------")
        print("4. Listar productos")
        print("5. Listar clientes")
        print("--------------------------------")
        print("6. Salir")


        opcion = input("Seleccione una opción: ")


        if opcion == "1":

            codigo = input("Código del producto: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))

            producto = Producto(
                codigo,
                nombre,
                categoria,
                precio
            )

            if restaurante.registrar_producto(producto):
                print("Producto registrado correctamente")
            else:
                print("El código ya existe")


        elif opcion == "2":

            codigo = input("Código de bebida: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            tamaño = input("Tamaño: ")
            envase = input("Tipo de envase: ")

            bebida = Bebida(
                codigo,
                nombre,
                "Bebida",
                precio,
                tamaño,
                envase
            )

            if restaurante.registrar_producto(bebida):
                print("Bebida registrada correctamente")
            else:
                print("El código ya existe")


        elif opcion == "3":

            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            cliente = Cliente(
                identificacion,
                nombre,
                correo
            )

            if restaurante.registrar_cliente(cliente):
                print("Cliente registrado correctamente")
            else:
                print("La identificación ya existe")


        elif opcion == "4":

            restaurante.listar_productos()


        elif opcion == "5":

            restaurante.listar_clientes()


        elif opcion == "6":

            print("Programa finalizado")
            break


        else:

            print("Opción inválida")


menu()
