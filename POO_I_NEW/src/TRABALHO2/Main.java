


package TRABALHO2;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        ArrayList<Ganhos> ganhos = new ArrayList<>();
        ArrayList<Gastos> gastos = new ArrayList<>();




        TiposGanhos tiposGanhos1 = new TiposGanhos("Salário");
        TiposGanhos tiposGanhos2 = new TiposGanhos("Investimentos");


        TiposGastos tiposGastos1 = new TiposGastos("Alimentação");
        TiposGastos tiposGastos2 = new TiposGastos("Transporte");
        TiposGastos tiposGastos3 = new TiposGastos("Lazer");


        FormaPagamento formaPagamento1 = new FormaPagamento("Dinheiro");
        FormaPagamento formaPagamento2 = new FormaPagamento("Cartão de crédito");
        FormaPagamento formaPagamento3 = new FormaPagamento("PIX");

        ganhos.add(new Ganhos("01/01/2021", 5000, tiposGanhos1));
        ganhos.add(new Ganhos("01/01/2021", 1000, tiposGanhos2));

        gastos.add(new Gastos("01/01/2021", 100, tiposGastos1, formaPagamento1));
        gastos.add(new Gastos("01/01/2021", 100, tiposGastos2, formaPagamento2));
        gastos.add(new Gastos("01/01/2021", 100, tiposGastos3, formaPagamento3));


        int fecharmenu = 0;
        while (fecharmenu != 1) {
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

            System.out.println("Digite a data do ganho: (dd/mm/aaaa)");
            scanner.nextLine();
            String dataGanhos = scanner.nextLine();

            System.out.println("Digite o valor do ganho: ");
            double valorGanhos = scanner.nextDouble();

            System.out.println("Digite o tipo do ganho: ");
            System.out.println("1 - Salário");
            System.out.println("2 - Investimentos");

            int tipo = scanner.nextInt();
            TiposGanhos x;
            switch (tipo) {
                case 1 -> x = tiposGanhos1;
                case 2 -> x = tiposGanhos2;
                default -> {
                    System.out.println("Opção inválida");
                    return;
                }
            }
            ganhos.add(new Ganhos(dataGanhos, valorGanhos, x));




        }
        if (opcao == 2) {

                System.out.println("Digite a data do gasto: (dd/mm/aaaa)");
                scanner.nextLine();
                String dataGastos = scanner.nextLine();

                System.out.println("Digite o valor do gasto: ");
                double valorGastos = scanner.nextDouble();

                System.out.println("Digite o tipo do gasto: ");
                System.out.println("1 - Alimentação");
                System.out.println("2 - Transporte");
                System.out.println("3 - Lazer");

                int tipo = scanner.nextInt();
                TiposGastos x;
                switch (tipo) {
                    case 1 -> x = tiposGastos1;
                    case 2 -> x = tiposGastos2;
                    case 3 -> x = tiposGastos3;
                    default -> {
                        System.out.println("Opção inválida");
                        return;
                    }
                }

                System.out.println("Digite a forma de pagamento: ");
                System.out.println("1 - Dinheiro");
                System.out.println("2 - Cartão de crédito");
                System.out.println("3 - PIX");

                int forma = scanner.nextInt();
                FormaPagamento y;
                switch (forma) {
                    case 1 -> y = formaPagamento1;
                    case 2 -> y = formaPagamento2;
                    case 3 -> y = formaPagamento3;
                    default -> {
                        System.out.println("Opção inválida");
                        return;
                    }
                }

                gastos.add(new Gastos(dataGastos, valorGastos, x, y));
        }
        if (opcao == 3) {
            for (Ganhos ganho : ganhos) {
                System.out.println("Data: " + ganho.getDataGanhos());
                System.out.println("Valor: " + ganho.getValorGanhos());
                System.out.println("Tipo: " + ganho.getTipoGanhos());
                System.out.println("---------------------");
        }
    }
        if (opcao == 4) {
            for (Gastos gasto : gastos) {
                System.out.println("Data: " + gasto.getDataGastos());
                System.out.println("Valor: " + gasto.getValorGastos());
                System.out.println("Tipo: " + gasto.getTipoGastos());
                System.out.println("Forma de pagamento: " + gasto.getFormaPagamento());
                System.out.println("---------------------");
            }
        }
        if (opcao == 5) {
            // Relatório mensal
            // escolher mes e ano

            System.out.println("Digite o mês: ");
            int mes = scanner.nextInt();
            System.out.println("Digite o ano: ");
            int ano = scanner.nextInt();
            double totalGanhos = 0;
            double totalGastos = 0;
            for (Ganhos ganho : ganhos) {
                String[] data = ganho.getDataGanhos().split("/");
                int mesGanho = Integer.parseInt(data[1]);
                int anoGanho = Integer.parseInt(data[2]);
                if (mesGanho == mes && anoGanho == ano) {
                    totalGanhos += ganho.getValorGanhos();
                }
            }
            for (Gastos gasto : gastos) {
                String[] data = gasto.getDataGastos().split("/");
                int mesGasto = Integer.parseInt(data[1]);
                int anoGasto = Integer.parseInt(data[2]);
                if (mesGasto == mes && anoGasto == ano) {
                    totalGastos += gasto.getValorGastos();
                }
            }
            System.out.println("Total de ganhos: " + totalGanhos);
            System.out.println("Total de gastos: " + totalGastos);
            System.out.println("Saldo: " + (totalGanhos - totalGastos));


        }
        if (fecharmenu == 0) {
            System.out.println("Deseja fechar o menu?");
            System.out.println("1 - Sim");
            System.out.println("2 - Não");
            int fechar = scanner.nextInt();
            if (fechar == 1) {
                fecharmenu = 1;
            }
        }
}}}