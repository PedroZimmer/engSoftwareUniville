package BeeCrowd.Prob2015;

import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class Problema_1936 {

    private static int fatorial(int num) {
        int x = 1;
        for (int i = 1; i <= num; i++) {
            x *= i;
        }
        return x;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> fatoriais = new Stack<>();


        int num = sc.nextInt();

        int i = 1;
        int x = 0;
        while (x < Math.pow(10,5)) {
            x = fatorial(i);
            fatoriais.push(x);
            i++;
        }

        int cont = 0;
        while (num != 0) {
            int xx = fatoriais.pop();
            if (xx <= num) {
                num -= xx;
                cont += 1;
                while (xx <= num) {
                    num -= xx;
                    cont += 1;
                }
            }
        }
        System.out.println(cont);
    }
}
