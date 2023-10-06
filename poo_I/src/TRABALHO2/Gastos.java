package TRABALHO2;

public class Gastos {

    private String DataGastos;
    private double ValorGastos;
    private TiposGastos tipo;
    private FormaPagamento tipoPagamento;

    public Gastos(String dataGastos, double valorGastos, TiposGastos tipoGastos, FormaPagamento formaPagamento) {
        DataGastos = dataGastos;
        ValorGastos = valorGastos;
        tipo = tipoGastos;
        tipoPagamento = formaPagamento;
    }

    public String getDataGastos() {
        return DataGastos;
    }

    public double getValorGastos() {
        return ValorGastos;
    }

    public TiposGastos getTipoGastos() {
        return tipo;
    }

    public FormaPagamento getFormaPagamento() {
        return tipoPagamento;
    }

}


