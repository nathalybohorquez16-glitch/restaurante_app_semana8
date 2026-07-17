from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []


    def registrar_producto(self, producto: Producto) -> bool:

        for elemento in self.productos:
            if elemento.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True


    def listar_productos(self) -> None:

        for producto in self.productos:
            print(producto.mostrar_informacion())


    def registrar_cliente(self, cliente: Cliente) -> bool:

        for elemento in self.clientes:
            if elemento.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True


    def listar_clientes(self) -> None:

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
