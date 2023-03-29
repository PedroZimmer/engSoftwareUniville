package AtividadeTriangulo;

public class ObjTriangulo{

    public void Triangulo(double base, double altura){
        setBase(base);
        setAltura(altura);
    }

    private double base;
    private double altura;

    public double getBase(){
        return base;
    }

    public double getAltura(){
        return altura;
    }

    public void setBase(double x){
        this.base = x;
    }

    public void setAltura(double x){
        this.altura = x;
    }

    public double getArea(double altura, double base){
        return altura*base/2;
    }


}

