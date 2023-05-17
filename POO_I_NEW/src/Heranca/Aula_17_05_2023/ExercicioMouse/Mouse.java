package Heranca.Aula_17_05_2023.ExercicioMouse;

public class Mouse {

    private String name;
    private String brand;

    public Mouse(String name, String brand) {
        this.name = name;
        this.brand = brand;
    }


    public void click() {
        System.out.println("Click");
    }

    public void doubleClick() {
            System.out.println("Double Click");
        }

    public void scroll() {
            System.out.println("Scroll");
        }

    public void drag() {
            System.out.println("Drag");
        }


}
