import java.util.Random;
import java.util.Scanner;

public class aula03{

    public static void main(String args[]) {
        Random gerador = new Random();
        Scanner leitor = new Scanner(System.in);
        int secreto = gerador.nextInt(10);
        //0->9 --- 10 não é incluido+


        while(true) {
            System.out.println("Digite um numero:");
            int i = leitor.nextInt();
            if(secreto == i) {
                System.out.println("Acertou!");
                break; //quebra o laço de repetição
            }
            System.out.println("Você errou!");
        }

    }
}

