

package AtividadeTriangulo;

import java.util.Scanner;

public class MainTriangulo {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        ObjTriangulo t = new ObjTriangulo();
        System.out.println("Digite a Base:");
        double base = leitor.nextDouble();
        System.out.println("Digite a Altura:");
        double altura = leitor.nextDouble();
        t.setBase(base);
        t.setAltura(altura);
        System.out.println(t.getBase());
        System.out.println("Area" + t.getArea(altura, base));

    }
}