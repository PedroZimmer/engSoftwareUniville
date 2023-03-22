import java.util.Scanner;

public class exercicio1 {
    public static void main(String[] args) {
                
    System.out.println("Insira um ano:");
    Scanner entrada = new Scanner(System.in);
    int ano  = entrada.nextInt();
    entrada.close();
    if (ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0) {
        System.out.println("O ano " + ano + " é bissexto");
    } else {
        System.out.println("O ano " + ano + " não é bissexto");
    }
    }
    }