

public class triangulo {

private double lado1;
private double lado2;
private double lado3;

public triangulo(double lado1, double lado2, double lado3) {
    this.lado1 = lado1;
    this.lado2 = lado2;
    this.lado3 = lado3;
    
}

public double calcularArea() {
    double p = (lado1 + lado2 + lado3)/2;
    double area = Math.sqrt(p*(p-lado1)*(p-lado2)*(p-lado3)); //Math.sqrt = raiz quadrada
    return area;
}

public double calcularPerimetro() {
    double perimetro = lado1 + lado2 + lado3;
    return perimetro;

}

public static void main(String[] args) {
    triangulo triangulo = new triangulo(3, 4, 5);
    double area = triangulo.calcularArea();
    double perimetro = triangulo.calcularPerimetro();
    System.out.println("Area: " + area);
    System.out.println("Perimetro: " + perimetro);
}
}
