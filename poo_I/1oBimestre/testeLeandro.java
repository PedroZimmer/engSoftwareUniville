import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



public class testeLeandro {


    public static void main (String[] args) {


        List<Integer> arestas = new ArrayList<Integer>();
        
        //Declara variáveis como inteiro
            int a, b, c;
        
        //Entrada de dados
            Scanner entrada = new Scanner(System.in);
            System.out.println("Digite o valor da aresta A: ");
            a = entrada.nextInt();
            System.out.println("Digite o valor da aresta B: ");
            b = entrada.nextInt();
            System.out.println("Digite o valor da aresta C: ");
            c = entrada.nextInt();
            
            arestas.add((int) a);
            arestas.add((int) b);
            arestas.add((int) c);

        //Ordena com sort()
            
            arestas.sort(null);
        
        //Processamento
            if (arestas.get(0) + arestas.get(1) < arestas.get(2)) {
                System.out.println("Não é um triangulo");
            } else if (arestas[0] == arestas[1] && arestas[1] == arestas[2]) {
                System.out.println("Triangulo equilatero");
            } else if (arestas[0] == arestas[1] || arestas[1] == arestas[2] || arestas[0] == arestas[2]) {
                System.out.println("Triangulo isosceles");
            } else {
                System.out.println("Triangulo escaleno");
            }
        }

}




