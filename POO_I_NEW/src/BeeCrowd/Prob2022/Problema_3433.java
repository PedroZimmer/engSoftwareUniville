package BeeCrowd.Prob2022;

import java.lang.invoke.StringConcatException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Problema_3433 {


    private static int META = 23;


    private static ArrayList<Integer> putInArray(String linha) {
        String LISTA[] = linha.split(" ");
        ArrayList<Integer> lista = new ArrayList<>();
        for(String X : LISTA ){
            Integer num = Integer.parseInt(X);
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

    private static ArrayList<Integer> subsEspeciais(ArrayList<Integer> lista) {

        for (int i = 0; i < lista.size(); i++) {
            Integer elemento = lista.get(i);
            if (elemento.equals(11) || elemento.equals(12) || elemento.equals(13)) {
                lista.set(i, 10);
            }
        }
        return lista;
    }

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        System.out.println("Rodadas:");
        int RODADA = sc.nextInt();

        System.out.println("João:");
        sc.nextLine();
        String joao1 = sc.nextLine();
        ArrayList<Integer> joao = putInArray(joao1);


        System.out.println("Maria:");
        String maria1 = sc.nextLine();
        ArrayList<Integer> maria = putInArray(maria1);

        System.out.println("Comuns:");
        String COMUNS1 = sc.nextLine();
        ArrayList<Integer> COMUNS = putInArray(COMUNS1);
        COMUNS = subsEspeciais(COMUNS);


        joao.addAll(COMUNS);
        joao = subsEspeciais(joao);
        int somaJoao = soma(joao);



        maria.addAll(COMUNS);
        maria = subsEspeciais(maria);
        int somaMaria = soma(maria);


        int resultado = 23 - somaMaria;
        System.out.println(resultado);


    }
}
