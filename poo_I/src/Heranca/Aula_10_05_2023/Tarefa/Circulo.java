package Heranca.Aula_10_05_2023.Tarefa;

public class Circulo extends Figura{

    private double raio;

    private double area;

    public Circulo(double raio){
        this.raio = raio;
    }

    @Override
    public void obterArea(){
        this.area = Math.PI * Math.pow(this.raio, 2);
        System.out.println("A área do circulo é: " + this.area);
    }


}
