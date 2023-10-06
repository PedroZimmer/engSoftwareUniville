package aula31032023;

public class Ponto {

    private double x;
    private double y;

    public static double z = 0.; // atributo de classe (static) - pertence a classe

    public Ponto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }
}
