package DesafiosGPT.Clientes;


import java.util.ArrayList;

//deve ser feito uma ARRAY  de pedidos para cada cliente
public class Pedido {

    public Pedido(Cliente cliente, Produto produto, int quantidade){
        setCliente(cliente);
        //setProduto(produto);
        setQuantidade(quantidade);

        this.produtos.add(produto);


    }

    private Cliente cliente;
    private ArrayList<Produto> produtos = new ArrayList<Produto>();
    private int quantidade;

    public void setCliente(Cliente cliente){
        this.cliente = cliente;
    }



    public void addtProduto(Produto produto, int quantidade){
        if(produto.getEstoqueProduto() >= quantidade){
            this.produtos.add(produto);
            produto.setEstoque(produto.getEstoqueProduto() - quantidade);

        //this.produtos.add(produto);
    } else {
        System.out.println("Não há estoque suficiente");
    }
    }


    public void setQuantidade(int quantidade){
        this.quantidade = quantidade;
    }

    public String toString(){
        String saida = "Cliente: " + cliente.getNome() + "\n";
        for(Produto p : produtos){
            saida += "Produto: " + p.getNomeProduto() + "\n";
            saida += "Preço: " + p.getPrecoProduto() + "\n";
            saida += "Quantidade: " + quantidade + "\n";
            saida += "Total: " + (p.getPrecoProduto() * quantidade) + "\n";
        }
        return saida;
    }



}
