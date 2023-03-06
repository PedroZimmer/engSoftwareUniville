

import java.util.Scanner;

public class EntradadeDados {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite um número: ");
        String numero = entrada.nextLine(); // nextInt() para números inteiros e nextFloat() para números decimais (float) nextLine para String
        System.out.println("O número digitado foi: " + numero);
        entrada.close();
    }
}