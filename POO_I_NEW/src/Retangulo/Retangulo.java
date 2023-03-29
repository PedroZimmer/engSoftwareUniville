package Retangulo;


public class Retangulo {

    public Retangulo(int altura, int base){
        setAltura(altura);
        setBase(base);

    }
    private int altura;
    private int base;

    public int getAltura(){
        return altura;
    }

    public int getBase(){
        return base;
    }

    public void setAltura(int x) {
        this.altura = x;
    }

    public void setBase(int x){
        this.base = x;
    }

    public String isQuadrado(){
        if (altura == base){
            return "Sim";
        }
        else {
            return "Não";
        }}

    public int getArea(){
        return altura * base;
    }

    public int getPerimetro(){
        return altura* + base*2;
    }

    public String toString(){
        return "Retangulo.Retangulo = {Altura= " + altura + "base=" + base;
    }

}
