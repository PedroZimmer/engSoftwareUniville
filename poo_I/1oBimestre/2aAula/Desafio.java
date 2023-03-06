import java.util.Scanner;


public class Desafio {
    public static void main(String argds[]){

    Scanner entrada1 = new Scanner(System.in);
    System.out.println("Digite sua altura: ");
    double altura = entrada1.nextDouble();
    System.out.println("Digite sua largura: ");
    double largura = entrada1.nextDouble();
    
    double area = altura * largura;
    System.out.println("A area é de:" + area);


    if (area > 50) {
        System.out.println("A area é maior que 50");
    } else if (area < 50) {
        System.out.println("A area é menor que 50");
    } else {
        System.out.println("A area é igual a 50");
    }

}


