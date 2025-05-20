//3.Crea un POO de clases para modelar un avión y sus partes. El avión está compuesto por partes como el motor, las alas y el tren de aterrizaje. Si el avión se destruye, las partes también se destruyen.
//Parte<nombre, peso (en kg)Métodos: mostrar_info() (muestra el nombre y el peso de la parte)
//Avión<modelo, fabricante, partes (lista de objetos de tipo Parte)
//Métodos: agregar_parte(parte), mostrar_avión() (muestra el modelo, fabricante y la información de todas las partes)
//  a)Implementa las clases con sus constructores, getters y setters.
//  b)Crea un avión y agrega varias partes.
//  c)Muestra la información del avión y sus partes.
import java.util.ArrayList;
class Parte {
    private String nombre;
    private double peso;

    public Parte(String nombre, double peso) {
        this.nombre = nombre;
        this.peso = peso;
    }

    public void mostrarInfo() {
        System.out.println("Parte: " + nombre + ", Peso: " + peso + " kg");
    }
}

class Avion {
    private String modelo;
    private String fabricante;
    private ArrayList<Parte> partes;

    public Avion(String modelo, String fabricante) {
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.partes = new ArrayList<>();
    }

    public void agregarParte(Parte parte) {
        partes.add(parte);
    }

    public void mostrarAvion() {
        System.out.println("Modelo: " + modelo + ", Fabricante: " + fabricante);
        for (Parte p : partes) {
            p.mostrarInfo();
        }
    }

    public static void main(String[] args) {
        Avion avion = new Avion("A320", "Airbus");
        avion.agregarParte(new Parte("Motor", 1500));
        avion.agregarParte(new Parte("Ala", 800));
        avion.mostrarAvion();
    }
}
