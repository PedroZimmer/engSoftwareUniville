package DesafiosGPT.Clientes;

public class Produto {

    private String nome;
    private double preco;
    private int estoque;

    public Produto(String nome, double preco, int estoque){
        setNome(nome);
        setPreco(preco);
        setEstoque(estoque);
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setPreco(double x){
        this.preco = x;
    }

    public void setEstoque(int x){
        this.estoque = x;
    }

    public String getNomeProduto(){
        return nome;
    }

    public double getPrecoProduto(){
        return preco;
    }

    public int getEstoqueProduto(){
        return estoque;
    }



}
