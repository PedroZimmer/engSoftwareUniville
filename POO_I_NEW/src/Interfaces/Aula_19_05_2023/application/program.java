package Interfaces.Aula_19_05_2023.application;

import Interfaces.Aula_19_05_2023.entities.AlgoritimoDaBolha;
import Interfaces.Aula_19_05_2023.entities.Deletavel;
import Interfaces.Aula_19_05_2023.entities.Pessoa;

public class program {


    public static void main(String[] args) {

        Deletavel deletavel = new Pessoa();

        AlgoritimoDaBolha algoritimoDaBolha = new AlgoritimoDaBolha();


        int vetor[] = {5, 3, 2, 4, 7, 1, 0, 6};

        System.out.println(vetor.toString());
    }
}
