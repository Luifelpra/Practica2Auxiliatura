```mermaid
classDiagram
    class Parte {
        -nombre: String
        -peso: float
        +mostrar_info() void
    }

    class Avion {
        -modelo: String
        -fabricante: String
        -partes: List~Parte~
        +agregar_parte(Parte) void
        +mostrar_avion() void
    }

    Avion *--  Parte