package Heranca.Aula_17_05_2023.ExercicioMouse;

public class Bluetooth extends Mouse{


    public Bluetooth(String name, String brand) {
        super(name, brand);
    }

    public void connect() {
        System.out.println("Connect");
    }

    public void disconnect() {
        System.out.println("Disconnect");
    }



}
