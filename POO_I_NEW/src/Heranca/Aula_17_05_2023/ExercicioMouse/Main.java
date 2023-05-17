package Heranca.Aula_17_05_2023.ExercicioMouse;

public class Main {

    public static void main(String[] args){

        Mouse mouse1;

        Optico mouse2;

        Bluetooth mouse3;

        mouse1 = new Mouse("Mouse 1", "Razer");

        mouse2 = new Optico("Mouse 2", "Redragon");

        mouse2.click();



    }

}
