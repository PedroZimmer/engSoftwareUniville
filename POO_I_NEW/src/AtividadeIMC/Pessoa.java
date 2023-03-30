package AtividadeIMC;

public class Pessoa {

    public Pessoa(String nome, double altura, double peso, String sexo, int idade){
        setNome(nome);
        setAltura(altura);
        setPeso(peso);
        setSexo(sexo);
        setIdade(idade);
    }

    private String nome;
    private double altura;
    private double peso;
    private String sexo;
    private int idade;


    public void setNome(String x){
        this.nome = x;
    }

    public void setAltura(double x){
        this.altura = x;
    }

    public void setPeso(double x){
        this.peso = x;
    }

    public void setSexo(String x){
        this.sexo = x;

    }

    public void setIdade(int x){
        this.idade = x;
    }

    public String getNome(){
        return nome;
    }

    public double getAltura(){
        return altura;
    }

    public double getPeso(){
        return peso;
    }

    public String getSexo(){
        return sexo;
    }

    public int getIdade(){
        return  idade;
    }

    public String toString(){
        return " Nome: " + nome + " Altura: " + altura + " Peso: " + peso + " Sexo: " + sexo + " Idade: " + idade;
    }
}

