```mermaid
classDiagram
    class Habitacion {
        -nombre: String
        -tamano: float
        +mostrar_info() void
    }

    class Casa {
        -direccion: String
        -habitaciones: List~Habitacion~
        +agregar_habitacion(Habitacion) void
        +mostrar_casa() void
    }

    Casa  *--  Habitacion 