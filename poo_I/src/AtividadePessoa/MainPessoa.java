

package AtividadePessoa;

import java.util.Scanner;

public class MainPessoa{
    public static void main(String[] args){
        Scanner leitor = new Scanner(System.in);
        System.out.println("Insira o Nome");
        String nome = leitor.nextLine();
        System.out.println("Insira o sobrenome");
        String sobrenome = leitor.nextLine();
        ObjPessoa p = new ObjPessoa();
        p.setNome(nome);
        p.setSobrenome(sobrenome);
        System.out.println("Nome completo:" + p.getNomeCompleto(nome, sobrenome));
    }
}