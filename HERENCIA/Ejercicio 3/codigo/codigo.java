//3.Definir las clases:
//Persona <ci, nombre, apellido, celular, fecha_Nac>Estudiante (heredado de persona) <ru, fecha_Ingreso, semestre> Docente (heredado de persona) <nit, profesión, especialidad>
// a)Diseñar el diagrama UML de las clases anteriores.
//  b)Implementa las clases con sus constructores, datos por defecto y mostrar.
//  c)Mostrar los estudiantes mayores de 25 años.
//  d)Mostrar al docente que tiene la profesión de “Ingeniero”, es del sexo masculino y es el mayor de todos.
//  e)Mostrar a los estudiantes y docentes que tienen el mismo apellido
import java.time.LocalDate;
import java.time.Period;
import java.util.*;

class Persona {
    protected String ci, nombre, apellido, celular;
    protected LocalDate fechaNac;

    public Persona(String ci, String nombre, String apellido, String celular, String fechaNac) {
        this.ci = ci;
        this.nombre = nombre;
        this.apellido = apellido;
        this.celular = celular;
        this.fechaNac = LocalDate.parse(fechaNac);
    }

    public void mostrar() {
        System.out.println(nombre + " " + apellido + ", CI: " + ci + ", Cel: " + celular + ", Nac: " + fechaNac);
    }

    public int edad() {
        return Period.between(fechaNac, LocalDate.now()).getYears();
    }

    public String getApellido() {
        return apellido;
    }
}

class Estudiante extends Persona {
    private String ru, fechaIngreso;
    private int semestre;

    public Estudiante(String ci, String nombre, String apellido, String celular, String fechaNac,
                      String ru, String fechaIngreso, int semestre) {
        super(ci, nombre, apellido, celular, fechaNac);
        this.ru = ru;
        this.fechaIngreso = fechaIngreso;
        this.semestre = semestre;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("RU: " + ru + ", Ingreso: " + fechaIngreso + ", Semestre: " + semestre);
    }
}

class Docente extends Persona {
    private String nit, profesion, especialidad;

    public Docente(String ci, String nombre, String apellido, String celular, String fechaNac,
                   String nit, String profesion, String especialidad) {
        super(ci, nombre, apellido, celular, fechaNac);
        this.nit = nit;
        this.profesion = profesion;
        this.especialidad = especialidad;
    }

    public String getProfesion() {
        return profesion;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("NIT: " + nit + ", Profesión: " + profesion + ", Especialidad: " + especialidad);
    }
}

public class Main {
    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("123", "Luis", "Perez", "77777777", "2000-04-15", "RU01", "2020-01-10", 5);
        Estudiante e2 = new Estudiante("124", "Ana", "Gomez", "77777778", "1995-03-12", "RU02", "2019-01-10", 7);
        Docente d1 = new Docente("456", "Carlos", "Perez", "77777779", "1970-08-01", "NIT01", "Ingeniero", "Sistemas");
        Docente d2 = new Docente("457", "Jose", "Gomez", "77777780", "1980-07-22", "NIT02", "Licenciado", "Matemática");

        List<Estudiante> estudiantes = Arrays.asList(e1, e2);
        List<Docente> docentes = Arrays.asList(d1, d2);

        // Mostrar estudiantes > 25 años
        for (Estudiante e : estudiantes) {
            if (e.edad() > 25) {
                System.out.println("Estudiante mayor de 25 años:");
                e.mostrar();
            }
        }

        // Docente ingeniero más viejo
        Docente mayor = null;
        for (Docente d : docentes) {
            if (d.getProfesion().equalsIgnoreCase("Ingeniero")) {
                if (mayor == null || d.edad() > mayor.edad()) {
                    mayor = d;
                }
            }
        }
        if (mayor != null) {
            System.out.println("Docente Ingeniero más viejo:");
            mayor.mostrar();
        }

        // Estudiantes y docentes con el mismo apellido
        for (Estudiante e : estudiantes) {
            for (Docente d : docentes) {
                if (e.getApellido().equalsIgnoreCase(d.getApellido())) {
                    System.out.println("Coincidencia de apellido:");
                    e.mostrar();
                    d.mostrar();
                }
            }
        }
    }
}
