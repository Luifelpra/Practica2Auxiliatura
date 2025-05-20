```mermaid
classDiagram
    class Persona {
        -ci: String
        -nombre: String
        -apellido: String
        -celular: String
        -fechaNac: String
        +mostrar(): void
    }

    class Estudiante {
        -ru: String
        -fechaIngreso: String
        -semestre: int
    }

    class Docente {
        -nit: String
        -profesion: String
        -especialidad: String
    }

    Persona <|-- Estudiante
    Persona <|-- Docente
