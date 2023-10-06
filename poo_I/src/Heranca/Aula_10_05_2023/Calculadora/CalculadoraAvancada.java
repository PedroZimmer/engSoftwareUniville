package Heranca.Aula_10_05_2023.Calculadora;

public class CalculadoraAvancada extends CalculadoraPadrao{

    public void potencia(int a, int b) {
        System.out.println(Math.pow(a, b));
    }

    public void raiz(int a) {
        System.out.println(Math.sqrt(a));
    }

    public void log(int a) {
        System.out.println(Math.log(a));
    }

    public void seno(int a) {
        System.out.println(Math.sin(a));
    }

    public void cosseno(int a) {
        System.out.println(Math.cos(a));
    }

    public void tangente(int a) {
        System.out.println(Math.tan(a));
    }

    public void fatorial(int a) {
        int fatorial = 1;
        for (int i = 1; i <= a; i++) {
            fatorial *= i;
        }
        System.out.println(fatorial);
    }
}
