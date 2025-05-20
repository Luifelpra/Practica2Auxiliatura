```mermaid
classDiagram
    class Empleado {
        -nombre: String
        -apellido: String
        -salario_base: float
        -años_antigüedad: int
        +calcular_salario(): float
    }

    class Gerente {
        -departamento: String
        -bono_gerencial: float
        +calcular_salario(): float
    }

    class Desarrollador {
        -lenguaje_programación: String
        -horas_extras: int
        +calcular_salario(): float
    }

    Empleado <|-- Gerente
    Empleado <|-- Desarrollador
