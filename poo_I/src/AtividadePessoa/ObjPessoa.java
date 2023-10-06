package AtividadePessoa;

public class ObjPessoa {

    public void Pessoa(String nome, String sobrenome){
        setNome(nome);
        setSobrenome(sobrenome);

    }

    private String nome;
    private String sobrenome;

    public String getNome(){
        return nome;
    }

    public String getSobrenome(){
        return sobrenome;
    }

    public void setNome(String x){
        this.nome = x;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public String getNomeCompleto(String nome, String sobrenome){
        String nomeCompleto = nome + " " + sobrenome;
        return nomeCompleto;
    }
}
