package BeeCrowd.Prob2016;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BeeCrowd2235 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a == b || a == c || c == b) {
            System.out.println("S");
        } else if (a == c + b || b == a + c || c == b + a ){
            System.out.println("S");
        } else {
            System.out.println("N");
        }
    }
}
