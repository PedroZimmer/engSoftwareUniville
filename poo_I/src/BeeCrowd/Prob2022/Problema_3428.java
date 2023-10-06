package BeeCrowd.Prob2022;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Problema_3428 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
//        HashMap<Integer,Integer> alturas = new HashMap<>();
        ArrayList<Integer> lista = new ArrayList<>();
        // <NUMERO DO BALAO, ALTURA DO BALAO>

        System.out.println("qtd baloes:");
        int numBaloes = sc.nextInt();

        System.out.println("alturas:");
        for (int i=0; i < numBaloes; i++) {
            lista.add(sc.nextInt());
        }

        int x = 0;
        int flechas = 0;
        int estourados = 0;


        while (estourados < numBaloes) {
            estourados++;
            int balao = 0;

            int i = 0;
            while (true) {

                if (lista.get( i + 1 ) == lista.get(balao) - 1 ) {
                    estourados++;
                    balao = i;
                    lista.remove(0);
//                    i = 0;
                }
                i++;


            }


        }
        System.out.println(flechas);



    }
}
