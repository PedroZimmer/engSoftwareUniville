package BeeCrowd.Prob2018;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;
import java.util.Stack;

public class Problema_2879 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> pilha = new Stack<>();
        // numero de jogadas
        int numJog = sc.nextInt();
        //onde fica o carro
        int x = 0;
        int cont = 0;
        for (int i = 0; i < numJog; i++) {
            x = sc.nextInt();
            pilha.push(x);
            if (x != 1) {
                cont += 1;
            }
        }
        System.out.println(cont);
    }

}