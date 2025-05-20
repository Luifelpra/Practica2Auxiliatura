```mermaid
classDiagram
    class Producto {
        -nombre: String
        -precio: float
        +mostrar_info() void
    }

    class CarritoCompras {
        -productos: List~Producto~
        +agregar_producto(Producto) void
        +mostrar_carrito() void
    }

    CarritoCompras o--  Producto