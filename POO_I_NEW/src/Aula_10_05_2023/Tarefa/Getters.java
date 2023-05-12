package Aula_10_05_2023.Tarefa;
import java.util.Scanner;

public class Getters {

    private String nome;
    private int opcao;
    private double base;
    private double altura;

    Scanner input = new Scanner(System.in);

    public int opcao(){
        System.out.println("Qual figura você quer utilizar? 1- Retangulo 2- Circulo");
        int opcao = input.nextInt();
        return opcao;
    }

    public double setBaseRetangulo(){
        System.out.println("Digite a base do retangulo: ");
        base = input.nextDouble();
        return base;
    }

    public double setAlturaRetangulo(){
        System.out.println("Digite a altura do retangulo: ");
        altura = input.nextDouble();
        return altura;
    }

    public double setRaioCirculo(){
        System.out.println("Digite o raio do circulo: ");
        double raio = input.nextDouble();
        return raio;
    }


}
