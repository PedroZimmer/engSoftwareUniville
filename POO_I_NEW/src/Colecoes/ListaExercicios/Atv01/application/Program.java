package Colecoes.ListaExercicios.Atv01.application;

import Colecoes.ListaExercicios.Atv01.entities.Player;
import Colecoes.ListaExercicios.Atv01.entities.Points;

import java.util.ArrayList;
import java.util.Locale;

public class Program {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        //Preciso de uma arrayList com os nomes dos objetos players

        ArrayList<Player> players = new ArrayList<>();

        players.add(new Player("ABC", new Points(100000000L)));
        players.add(new Player("DEF", new Points(100000L)));
        players.add(new Player("GHI", new Points(1000000L)));
        players.add(new Player("JKL", new Points(10000000L)));

         for (Player player : players) {
             System.out.println(player);
         }

    }
}
