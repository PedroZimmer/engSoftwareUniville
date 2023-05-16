package Aula_10_05_2023.Tarefa;

public class Retangulo extends Figura{

    private double base;
    private double altura;

    private double area;


    public Retangulo(double base, double altura){
        this.base = base;
        this.altura = altura;
    }

    @Override
    public void obterArea() {
        this.area = this.base * this.altura;
        System.out.println("A área do retangulo é: " + this.area);
    }

}
