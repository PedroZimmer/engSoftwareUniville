package BeeCrowd.Prob2015;

import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Problema_1940 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int qtdJog = sc.nextInt();
        int qtdRodadas = sc.nextInt();

        HashMap<Integer,Integer> jogadores = new HashMap<>(){{
            for (int i=0; i<qtdJog; i++) {
                put(i, 0);
            }
        }};

        int cont = 0;
        int maior = 0;
        for (int i=0; i<qtdRodadas*qtdJog; i++) {
            int x = sc.nextInt();
            int y = jogadores.get(cont);
            jogadores.put(cont, x+y);
            if (jogadores.get(cont) >= jogadores.get(maior)) {
                maior = cont;
            }
            if (cont == qtdJog-1) {
                cont = 0;
            } else {
                cont++;
            }

        }
        maior += 1;
        System.out.println(maior);
    }
}