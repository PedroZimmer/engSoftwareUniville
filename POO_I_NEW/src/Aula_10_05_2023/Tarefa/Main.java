package Aula_10_05_2023.Tarefa;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Getters getters = new Getters();

        Scanner input = new Scanner(System.in);


        int opcao = getters.opcao(); // 1- Retangulo 2- Circulo

        //criar sistema de verificacao de opcao
        while (opcao != 1 && opcao != 2){
            System.out.println("Opção inválida, digite novamente: ");
            opcao = input.nextInt();
        }

        if (opcao == 1){
            double base = getters.setBaseRetangulo();
            double altura = getters.setAlturaRetangulo();
            Retangulo retangulo = new Retangulo(base, altura);
            retangulo.obterArea();
        }

        if (opcao == 2){
            double raio = getters.setRaioCirculo();
            Circulo circulo = new Circulo(raio);
            circulo.obterArea();
        }

    }

}
