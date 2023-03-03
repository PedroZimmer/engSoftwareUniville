// javac HelloWorld.java --release 8



//Meu primeiro programa em JAVA

public class HelloWorld{
    // Método que inicia o programa
    public static void main(String args[]) {
        // Tipo de dados
        int a = 10;//Inteiro
        long d = 10L;//Inteiro longo
        float b = 10.5f;//decimal
        double c = 10.5;//decimal (mais preciso) dar preferencia para o double
        boolean e = true;//true ou false
        char f = 'a';//caracter (aspas simples)

        //Operadores
        int soma = 10 + 10;
        int subtracao = 10 - 10;
        int multiplicacao = 10 * 10;
        int divisao = 10 / 10;
        int resto = 10 % 10;
        int incremento = 10;
        incremento++;
        int decremento = 10;
        decremento--;
        double potencia = Math.pow(10, 2);//10 elevado a 2

        int valorMaximo = 2147483647;
        int valorMaximoMaisUm = valorMaximo + 1;

        System.out.println("Hello World!");
        System.out.println("a = " + a);
        System.out.println("Valor maximo = " + valorMaximo);
        System.out.println("Valor maximo + 1 = " + valorMaximoMaisUm);
        
    }
}