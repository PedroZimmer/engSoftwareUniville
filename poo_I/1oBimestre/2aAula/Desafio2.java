import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Desafio2 {
    public static void main(String args[]) {

        List<Integer> triangulos = new ArrayList<Integer>();
 
        try (Scanner entrada1 = new Scanner(System.in)) {
            System.out.println("Digite o primeiro lado: ");
            double lado1 = entrada1.nextDouble();
            triangulos.add((int) lado1);
            System.out.println("Digite o segundo lado: ");
            double lado2 = entrada1.nextDouble();
            triangulos.add((int) lado2);
            System.out.println("Digite o terceiro lado: ");
            double lado3 = entrada1.nextDouble();
            triangulos.add((int)lado3);

            //ordenar lista
            triangulos.sort(null);
            System.out.println(triangulos);
            
            if (triangulos.get(0) + triangulos.get(1) > triangulos.get(2)) {
                System.out.println("É um triangulo");
                if (triangulos.get(0) == triangulos.get(1) && triangulos.get(1) == triangulos.get(2)) {
                    System.out.println("É um triangulo equilatero");
                } else if (triangulos.get(0) == triangulos.get(1) || triangulos.get(1) == triangulos.get(2)) {
                    System.out.println("É um triangulo isosceles");
                } else {
                    System.out.println("É um triangulo escaleno");
                }

            } else {
                System.out.println("Não é um triangulo");
            }
 
        }  

    }
}




// Escreva um programa q idetifique o tipo de triangulo 
