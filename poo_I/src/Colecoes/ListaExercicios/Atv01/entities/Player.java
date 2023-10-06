package Colecoes.ListaExercicios.Atv01.entities;

import java.text.DecimalFormat;

public class Player {

    private String name;

    private Points points;

    DecimalFormat df = new DecimalFormat("#,###");


    public Player() {
    }

    public Player(String name, Points points) {
        this.name = name;
        this.points = points;
    }

    public String toString() {
        return name + " - " + df.format(points.getPoints());
    }

}
