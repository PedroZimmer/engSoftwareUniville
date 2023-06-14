package BeeCrowd.Prob2022;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Problema_3424 {


    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int NUMERO = sc.nextInt();
        if (!(NUMERO >= 1 && NUMERO <= Math.pow(10,5))) {
            System.exit(0);
        }
        sc.nextLine();
        String LETRAS = sc.nextLine();
        String List[] = LETRAS.split("");

        ArrayList<String> LISTA = new ArrayList<String>();
        for (String X: List) {
            LISTA.add(X);
        }

        int cont = 0;
        for (int i = 0 ; i < LISTA.size()-1; i++ ) {

            if (LISTA.get(i).equals("a")) {

                String letra = LISTA.get(i);
                String proxLetra = LISTA.get(i+1);

                int pos = i+1;

                if (letra.equals(proxLetra)) {
                    cont += 1;

                    while (letra.equals(proxLetra)) {
                        cont += 1;
                        if (pos < LISTA.size()-1) {
                            pos += 1;
                            proxLetra = LISTA.get((pos));
                        } else {
                            break;
                        }

                    }

                    i = pos-1;
                }


            }


        }System.out.println(cont);


    }
}
