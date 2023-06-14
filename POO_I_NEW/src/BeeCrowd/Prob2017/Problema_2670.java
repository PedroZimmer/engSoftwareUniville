package BeeCrowd.Prob2017;

import java.util.Scanner;

public class Problema_2670 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int PRIMEIRO = sc.nextInt();
        int SEGUNDO = sc.nextInt();
        int TERCEIRO = sc.nextInt();

        int oMenorTempo = (SEGUNDO * 2)+(TERCEIRO * 4);

        if (oMenorTempo > (PRIMEIRO * 2)+(TERCEIRO * 2)) {
            oMenorTempo = (PRIMEIRO * 2)+(TERCEIRO * 2);
        }
        if (oMenorTempo > (PRIMEIRO * 4)+(SEGUNDO * 2)) {
            oMenorTempo = (PRIMEIRO * 4)+(SEGUNDO * 2);
        }
        System.out.println(oMenorTempo);
    }
}

