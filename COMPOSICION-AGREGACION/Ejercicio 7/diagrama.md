```mermaid
classDiagram
    class Estudiante {
        -nombre: String
        -carrera: String
        -semestre: int
        +mostrar_info() void
    }

    class Universidad {
        -nombre: String
        -estudiantes: List~Estudiante~
        +agregar_estudiante(Estudiante) void
        +mostrar_universidad() void
    }

    Universidad  o--  Estudiante