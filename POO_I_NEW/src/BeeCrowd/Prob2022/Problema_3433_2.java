package BeeCrowd.Prob2022;

import java.util.ArrayList;
import java.util.Scanner;

public class Problema_3433_2 {




    private static ArrayList<Integer> putInArray(String linha) {
        String LISTA[] = linha.split(" ");
        ArrayList<Integer> lista = new ArrayList<>();
        for(String X : LISTA ){
            Integer num = Integer.parseInt(X);
            if (num > 10) {
                num = 10;
            }
            lista.add(num);
        }
        return lista;
    }

    private static int soma(ArrayList<Integer> lista) {
        int soma = 0;
        for (int X : lista) {
            soma += X;
        }
        return soma;
    }

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        System.out.println("Rodadas:");
        int RODADA = sc.nextInt();

        System.out.println("João:");
        int joao = sc.nextInt(); int joao2 = sc.nextInt();
        if (joao > 10){ joao = 10;} if (joao2 > 10) {joao2 = 10;}
        int somaJoao = joao + joao2;

        System.out.println("Maria:");
        int maria = sc.nextInt(); int maria2 = sc.nextInt();
        if (maria > 10){ maria = 10;} if (maria2 > 10) {maria2 = 10;}
        int somaMaria = maria + maria2;

        System.out.println("Comuns:");
        sc.nextLine();
        String COMUNS1 = sc.nextLine();
        ArrayList<Integer> COMUNS = putInArray(COMUNS1);
        if (COMUNS.contains(5)) {
            System.out.println("tem");
        } else {
            System.out.println("n tem");
        }






    }
}
