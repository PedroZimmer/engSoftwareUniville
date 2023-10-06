package TRABALHO2;

public class Ganhos {

    private String DataGanhos;
    private double ValorGanhos;

    private TiposGanhos tipo;


    public Ganhos(String dataGanhos, double valorGanhos, TiposGanhos tipoGanhos) {
        DataGanhos = dataGanhos;
        ValorGanhos = valorGanhos;
        tipo = tipoGanhos;
    }

    public double getValorGanhos() {
        return ValorGanhos;
    }

    public TiposGanhos getTipoGanhos() {
        return tipo;
    }

    public String getDataGanhos() {
        return DataGanhos;
    }


}
