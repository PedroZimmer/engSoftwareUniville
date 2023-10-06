package BeeCrowd.Prob2022;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Problema_3432 {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String entrada = sc.nextLine();
        String linha[] = entrada.split(" ");
        if (linha.length > 8) {
            System.out.println("F");
            System.exit(0);
        }

        ArrayList<Integer> lista = new ArrayList<Integer>();
        for (String X : linha) {
            Integer num = Integer.parseInt(X);
            lista.add(num);
            if (num != 0 && num != 1) {
                System.out.println("F");
                System.exit(0);
            }
        }
        System.out.println("S");

    }

}
