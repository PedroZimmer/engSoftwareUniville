

package DesafiosGPT.Clientes;

import java.util.Scanner;

public class Main {

    public static void main(String[] args){

        Scanner leitor = new Scanner(System.in);

        Cliente c1 = new Cliente("Pedro");
        Cliente c2 = new Cliente("João");
        Produto p1 = new Produto("Arroz", 10.00, 10);
        Produto p2 = new Produto("Feijão", 5.00, 10);
        Pedido ped1 = new Pedido(c2, p1, 2);
        System.out.println(ped1.toString());
        System.out.println("Sobrou " + p1.getEstoqueProduto() + " unidades de " + p1.getNomeProduto());



    }

}