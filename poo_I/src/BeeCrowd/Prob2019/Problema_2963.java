package BeeCrowd.Prob2019;

import java.util.Scanner;
import java.util.Stack;

public class Problema_2963 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numCand = sc.nextInt();
        Boolean ganhou = Boolean.FALSE;
        int maior = 0;
        for (int i = 0; i < numCand; i++){
            int x = sc.nextInt();

            if (i == 0) {
                maior = x;
                ganhou = Boolean.TRUE;
            }
            if (x > maior) {
                ganhou = Boolean.FALSE;
            }
        }
        if (ganhou) {
            System.out.println("S");
        } else {
            System.out.println("N");
        }

    }
}
