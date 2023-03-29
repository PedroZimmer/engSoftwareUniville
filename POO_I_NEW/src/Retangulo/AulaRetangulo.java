package Retangulo;

import Retangulo.Retangulo;

public class AulaRetangulo{
    public static void main(String[] args) {
        Retangulo r = new Retangulo(100, 50);
        System.out.println("altura"+ r.getAltura());
        r.setAltura(100);
        r.setBase(100);
        System.out.println("altura"+ r.getAltura());
        System.out.println("É um quadrado?" + r.isQuadrado());
        System.out.println("Area= " + r.getArea());
        System.out.println(r);
    }
}
