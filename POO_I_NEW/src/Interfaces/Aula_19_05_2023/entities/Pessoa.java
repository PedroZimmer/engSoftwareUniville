package Interfaces.Aula_19_05_2023.entities;

public class Pessoa  implements Deletavel{


    @Override
    public void deletar() {
        System.out.println("Deletando pessoa");
    }


}
