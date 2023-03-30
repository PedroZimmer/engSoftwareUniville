

package AtividadeIMC;

import java.util.Scanner;

public class MainIMC{

    public static void main(String[] args){
        Scanner leitor = new Scanner(System.in);
        System.out.printf("bota o nome");
        String nome = leitor.nextLine();
        Pessoa p = new Pessoa(nome, 1.75, 800, "M", 18);
        System.out.println(p);
        Resultado r = new Resultado();
        System.out.println(r.resultado(p));




    }



}