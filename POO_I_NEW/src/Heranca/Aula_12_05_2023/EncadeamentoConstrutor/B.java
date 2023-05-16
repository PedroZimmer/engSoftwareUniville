package Aula_12_05_2023.EncadeamentoConstrutor;

public class B extends A{

    public B() {
        super(10);
        System.out.println("Construtor B()");
    }

    public B(int x) {
        super(10, 20);
        System.out.println("Construtor B(int x)");
    }

    public B(int x, int y) {
        System.out.println("Construtor B(int x, int y)");
    }

}
