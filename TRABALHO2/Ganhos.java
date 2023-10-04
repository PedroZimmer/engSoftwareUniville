package TRABALHO2;

public class Ganhos {

    private String DataGanhos;
    private double ValorGanhos;
    private String TipoGanhos;


    public Ganhos(String dataGanhos, double valorGanhos, TiposGanhos tipoGanhos) {
        DataGanhos = dataGanhos;
        ValorGanhos = valorGanhos;
        TipoGanhos = String.valueOf(tipoGanhos);
    }

    public double getValorGanhos() {
        return ValorGanhos;
    }

    public String getTipoGanhos() {
        return TipoGanhos;
    }

    public String getDataGanhos() {
        return DataGanhos;
    }

    public void setValorGanhos(double valorGanhos) {
        ValorGanhos = valorGanhos;
    }

    public void setTipoGanhos(String tipoGanhos) {
        TipoGanhos = tipoGanhos;
    }

    public void setDataGanhos(String dataGanhos) {
        DataGanhos = dataGanhos;
    }


}
