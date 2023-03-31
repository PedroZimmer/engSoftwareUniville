package DesafiosGPT.Clientes;

public class Cliente {

    public Cliente(String nome){
        setNome(nome);

    }
    private String nome;
    public void setNome(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return nome;
    }
    
}
