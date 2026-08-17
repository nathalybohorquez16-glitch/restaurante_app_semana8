from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for elemento in self.productos:
            if elemento.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(producto.mostrar_informacion())

    def registrar_usuario(self, usuario: Usuario) -> bool:
        for elemento in self.usuarios:
            if elemento.identificacion == usuario.identificacion:
                return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> None:
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        for usuario in self.usuarios:
            print(usuario.mostrar_informacion())

    def obtener_categorias(self) -> set[str]:
        categorias: set[str] = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias
