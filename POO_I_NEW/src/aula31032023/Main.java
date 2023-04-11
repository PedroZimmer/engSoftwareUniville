
package aula31032023;
public class Main {

    public static void main(String[] args) {

        Ponto p1 = new Ponto(-1, 2);
        Ponto p2 = new Ponto(3, 4);
        Ponto p3 = new Ponto(-1, 2);
        System.out.println("É igual? P1 == P2: " + p1.equals(p2));
        System.out.println("É igual? P1 == P3: " + p1.equals(p3));
        zerarPonto(p1);
        System.out.println("P1: " + p1);





    }


    public static void zerarPonto(Ponto p) {
        p.setX(0);
        p.setY(0);
    }
}