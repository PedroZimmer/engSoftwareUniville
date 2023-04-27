


package TRABALHO2;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        TiposGanhos tiposGanhos1 = new TiposGanhos("Salário");
        TiposGanhos tiposGanhos2 = new TiposGanhos("Investimentos");
        TiposGanhos tiposGanhos3 = new TiposGanhos("Outros");
        TiposGastos tiposGastos1 = new TiposGastos("Alimentação");
        TiposGastos tiposGastos2 = new TiposGastos("Transporte");
        TiposGastos tiposGastos3 = new TiposGastos("Lazer");
        TiposGastos tiposGastos4 = new TiposGastos("Outros");

        Ganhos ganho1 = new Ganhos("01/01/2021", 100, tiposGanhos1);
        Ganhos ganho2 = new Ganhos("01/01/2021", 100, tiposGanhos2);
        Ganhos ganho3 = new Ganhos("01/01/2021", 100, tiposGanhos3);
        Gastos gasto1 = new Gastos("01/01/2021", 100, tiposGastos1, "Dinheiro");
        Gastos gasto2 = new Gastos("01/01/2021", 100, tiposGastos2, "Dinheiro");
        Gastos gasto3 = new Gastos("01/01/2021", 100, tiposGastos3, "Dinheiro");


        System.out.println("Menu de opções: ");
        System.out.println("1 - Cadastrar ganhos");
        System.out.println("2 - Cadastrar gastos");
        System.out.println("3 - Listar ganhos");
        System.out.println("4 - Listar gastos");
        System.out.println("5 - Relatório mensal");
        System.out.println("6 - Sair");
        System.out.println("Digite a opção desejada: ");
        Scanner scanner = new Scanner(System.in);
        int opcao = scanner.nextInt();


        if (opcao == 1) {
            System.out.println("Digite a data do ganho: ");
            String dataGanhos = scanner.next();
            System.out.println("Digite o valor do ganho: ");
            double valorGanhos = scanner.nextDouble();
            System.out.println("Digite o tipo do ganho: ");
            System.out.printf("1 - %s\n", tiposGanhos1.getTipoGanhos());
            System.out.printf("2 - %s\n", tiposGanhos2.getTipoGanhos());
            System.out.printf("3 - %s\n", tiposGanhos3.getTipoGanhos());
            int tipoGanhos = scanner.nextInt();
            

        }
    }
}