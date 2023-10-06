package Colecoes.ListaExercicios.Atv01.entities;

import java.text.DecimalFormat;

public class Points {


    private Long points;

    DecimalFormat df = new DecimalFormat("#,###");

    public Points() {
    }

    public Points(Long points) {
        this.points = points;
    }

    public Long getPoints() {
        return points;
    }

    @Override
    public String toString() {
        return df.format(points);
    }
}
