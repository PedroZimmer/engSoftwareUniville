package TRABALHO2;

public class Gastos {

    private String DataGastos;
    private double ValorGastos;
    private String TipoGastos;
    private String FormaPagamento;

    public Gastos(String dataGastos, double valorGastos, TiposGastos tipoGastos, FormaPagamento formaPagamento) {
        DataGastos = dataGastos;
        ValorGastos = valorGastos;
        TipoGastos = String.valueOf(tipoGastos);
        FormaPagamento = String.valueOf(formaPagamento);
    }

    public String getDataGastos() {
        return DataGastos;
    }

    public double getValorGastos() {
        return ValorGastos;
    }

    public String getTipoGastos() {
        return TipoGastos;
    }

    public String getFormaPagamento() {
        return FormaPagamento;
    }

}


