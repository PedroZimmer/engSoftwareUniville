package Heranca.Aula_10_05_2023.Calculadora;

public class Main {

    public static void main(String[] args) {


        CalculadoraPadrao calc = new CalculadoraPadrao();

        calc.somar(10, 5);
        calc.subtrair(10, 5);
        calc.multiplicar(10, 5);
        calc.dividir(10, 5);

        CalculadoraAvancada calcAvancada = new CalculadoraAvancada();

        calcAvancada.somar(10, 5);
        calcAvancada.subtrair(10, 5);
        calcAvancada.multiplicar(10, 5);
        calcAvancada.dividir(10, 5);
        calcAvancada.potencia(10, 5);
        calcAvancada.raiz(9);
        calcAvancada.log(10);
        calcAvancada.seno(10);
        calcAvancada.cosseno(10);
        calcAvancada.tangente(10);
        calcAvancada.fatorial(10);


    }
}
