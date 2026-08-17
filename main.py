from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante()


# Tupla: contiene las opciones estables del menú
OPCIONES_MENU: tuple[str, ...] = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
)


def registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:
        precio = float(input("Precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("El precio debe ser un número válido.")
        return

    producto = Producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("El código del producto ya existe.")


def buscar_producto() -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        print("\nProducto encontrado:")
        print(producto.mostrar_informacion())
    else:
        print("No se encontró ningún producto con ese código.")


def actualizar_producto() -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No se encontró ningún producto con ese código.")
        return

    print("Producto actual:")
    print(producto.mostrar_informacion())

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:
        precio = float(input("Nuevo precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("El precio debe ser un número válido.")
        return

    if restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    ):
        print("Producto actualizado correctamente.")
    else:
        print("No fue posible actualizar el producto.")


def eliminar_producto() -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("No se encontró ningún producto con ese código.")


def listar_productos() -> None:
    print("\n--- LISTA DE PRODUCTOS ---")
    restaurante.listar_productos()


def registrar_usuario() -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("La identificación ya existe.")


def listar_usuarios() -> None:
    print("\n--- LISTA DE USUARIOS ---")
    restaurante.listar_usuarios()


def mostrar_categorias() -> None:
    print("\n--- CATEGORÍAS DE PRODUCTOS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No hay categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


# Diccionario: relaciona cada opción con la función correspondiente
ACCIONES_MENU: dict[str, callable] = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias
}


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías")
    print("9. Salir")


def menu() -> None:
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion not in OPCIONES_MENU:
            print("Opción inválida.")
            continue

        if opcion == "9":
            print("Programa finalizado.")
            break

        accion = ACCIONES_MENU[opcion]
        accion()


if __name__ == "__main__":
    menu()
