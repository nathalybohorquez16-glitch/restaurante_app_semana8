from modelos.producto import Producto


class Bebida(Producto):

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamaño: str,
        envase: str
    ):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño = tamaño
        self.envase = envase

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Bebida: {self.nombre} | "
            f"Tamaño: {self.tamaño} | "
            f"Envase: {self.envase} | "
            f"Precio: ${self.precio}"
        )
