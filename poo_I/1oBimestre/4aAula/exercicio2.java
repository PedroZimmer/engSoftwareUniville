import java.util.Scanner;

public class exercicio2 {
    
    public static void main(String[] args) {
    
    System.out.println("Insira um numero positivo:");
    Scanner entrada = new Scanner(System.in);
    int x = 0;
    while (x < 1) {
        int numero  = entrada.nextInt();
        if (numero > 0){
            x = 1;
            int fibonaci = 0;
            int a = 1;
            int b = 0;
            while (fibonaci < numero) {
                
                b = fibonaci + a;
                a = fibonaci;
                fibonaci = b;
                System.out.println(fibonaci);
                

            }
        } else {
            System.out.println("Insira um numero positivo:");
        }


    }

    entrada.close();

    }


}
