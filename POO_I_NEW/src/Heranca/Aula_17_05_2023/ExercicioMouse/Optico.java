package Heranca.Aula_17_05_2023.ExercicioMouse;

public class Optico extends Mouse{

    private String dpi;

    public Optico(String name, String brand) {
        super(name, brand);
    }

    public void changeDpi(String dpi) {
        this.dpi = dpi;
    }

    public String getDpi() {
        return dpi;
    }

}
