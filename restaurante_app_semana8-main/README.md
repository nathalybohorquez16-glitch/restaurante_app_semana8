# Restaurante App — Semana 9

## Información del estudiante

**Nombre:** Daniela Gomez

## Descripción del proyecto

Este proyecto corresponde a la Semana 9 de la asignatura Programación Orientada a Objetos.

El sistema `restaurante_app` permite administrar productos y usuarios de un restaurante mediante un programa interactivo ejecutado desde consola.

El proyecto continúa el desarrollo realizado en semanas anteriores y mantiene una arquitectura modular basada en modelos, servicios y un archivo principal de ejecución.

## Funcionalidades principales

El sistema permite:

* Registrar productos.
* Buscar productos mediante su código.
* Actualizar productos.
* Eliminar productos.
* Listar productos registrados.
* Registrar usuarios.
* Listar usuarios.
* Mostrar las categorías únicas de los productos.
* Evitar códigos de productos duplicados.
* Evitar identificaciones de usuarios duplicadas.
* Validar valores numéricos para los precios.
* Manejar errores de entrada mediante excepciones.

## Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

## Responsabilidad de los componentes

### modelos/producto.py

Contiene la clase `Producto`, que representa los productos del restaurante.

Cada producto contiene:

* Código.
* Nombre.
* Categoría.
* Precio.

### modelos/usuario.py

Contiene la clase `Usuario`, que representa de forma general a las personas registradas en el sistema.

Cada usuario contiene:

* Identificación.
* Nombre.
* Correo electrónico.

### servicios/restaurante.py

Contiene la clase `Restaurante`, encargada de administrar las colecciones y las operaciones principales del sistema.

Entre sus responsabilidades se encuentran:

* Registrar productos.
* Buscar productos.
* Actualizar productos.
* Eliminar productos.
* Listar productos.
* Registrar usuarios.
* Listar usuarios.
* Obtener categorías únicas.

La administración de las colecciones se mantiene dentro de este servicio para evitar que `main.py` modifique directamente las listas internas.

### main.py

Es el punto de entrada del programa.

Se encarga de:

* Mostrar el menú.
* Solicitar información mediante `input()`.
* Crear objetos `Producto` y `Usuario`.
* Utilizar los métodos proporcionados por `Restaurante`.
* Mostrar los resultados al usuario.
* Coordinar las opciones mediante funciones y un diccionario de acciones.

## Estructuras de datos utilizadas

### Lista — `list`

Las listas se utilizan para almacenar las colecciones dinámicas del sistema.

En `Restaurante` se utilizan:

```python
self.productos: list[Producto] = []
self.usuarios: list[Usuario] = []
```

La lista de productos permite registrar, buscar, actualizar, eliminar y listar objetos `Producto`.

La lista de usuarios permite registrar y listar objetos `Usuario`.

### Tupla — `tuple`

La tupla se utiliza para representar las opciones disponibles del menú principal.

```python
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
```

Se utiliza una tupla porque las opciones del menú representan información estable durante la ejecución del programa.

### Diccionario — `dict`

El diccionario relaciona cada opción del menú con la función que debe ejecutarse.

```python
ACCIONES_MENU: dict[str, Callable[[], None]]
```

Por ejemplo:

```text
"1" → registrar_producto
"2" → buscar_producto
"3" → actualizar_producto
```

Esta estructura permite organizar las acciones del menú de manera clara y evita concentrar toda la lógica en una cadena extensa de condicionales.

### Conjunto — `set`

El conjunto se utiliza para obtener las categorías de productos sin elementos duplicados.

```python
categorias: set[str] = set()
```

Cada categoría se agrega al conjunto y, debido a las características de esta estructura, una categoría repetida solamente aparece una vez.

Por ejemplo, si existen productos de las categorías:

```text
Comida
Comida
Bebida
Postre
```

el conjunto permite obtener:

```text
Comida
Bebida
Postre
```

## Ejecución del programa

Para ejecutar el sistema se debe abrir el proyecto en Visual Studio Code y ejecutar el archivo:

```text
main.py
```

También puede ejecutarse desde la terminal mediante:

```bash
python main.py
```

El programa mostrará un menú interactivo:

```text
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Mostrar categorías
9. Salir
```

## Validaciones

El sistema incorpora validaciones para evitar problemas durante la ejecución.

Entre ellas:

* No permite registrar productos con códigos repetidos.
* No permite registrar usuarios con identificaciones repetidas.
* No permite precios negativos.
* Controla entradas no numéricas para los precios mediante `ValueError`.
* Informa al usuario cuando un producto no existe.
* Informa cuando no existen productos, usuarios o categorías registradas.

## Importancia de seleccionar una estructura de datos adecuada

La selección de una estructura de datos depende de la necesidad que se desea resolver.

Las listas son adecuadas para administrar colecciones dinámicas de productos y usuarios. La tupla permite conservar información estable como las opciones del menú. El diccionario facilita relacionar cada opción con una función específica del sistema. Finalmente, el conjunto permite obtener categorías únicas sin duplicados.

Utilizar cada estructura de acuerdo con su propósito permite desarrollar un programa más organizado, comprensible y eficiente.

## Autor

**Daniela Gomez**

**Asignatura:** Programación Orientada a Objetos

**Actividad:** Tarea Semana 9 — Estructuras de datos aplicadas al proyecto restaurante_app
