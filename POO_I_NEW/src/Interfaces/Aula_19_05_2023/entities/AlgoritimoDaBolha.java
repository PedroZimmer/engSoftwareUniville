package Interfaces.Aula_19_05_2023.entities;

public class AlgoritimoDaBolha {



    public int[] ordenar(int[] vetor) {


        for (int i = 0; i < vetor.length; i++) {


            for (int j = 0; j < vetor.length; i++) {

                if (vetor[i] > vetor[j]) {

                    int aux = vetor[i];
                    vetor[i] = vetor[j];
                    vetor[j] = aux;

                }
            }
        }


        return vetor;

    }
}
