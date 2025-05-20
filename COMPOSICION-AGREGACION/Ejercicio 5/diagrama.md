```mermaid
classDiagram
    class Jugador {
        -nombre: String
        -numero: int
        -posicion: String
        +mostrar_info() void
    }

    class Portero {
        -habilidad: String
        +mostrar_info() void
    }

    class Defensa {
        -habilidad: String
        +mostrar_info() void
    }

    class Mediocampista {
        -habilidad: String
        +mostrar_info() void
    }

    class Delantero {
        -habilidad: String
        +mostrar_info() void
    }

    class Equipo {
        -nombre: String
        -jugadores: List~Jugador~
        +agregar_jugador(Jugador) void
        +mostrar_equipo() void
    }

    Jugador <|-- Portero
    Jugador <|-- Defensa
    Jugador <|-- Mediocampista
    Jugador <|-- Delantero

    Equipo  o--  Jugador 