package AtividadeIMC;

public class Resultado {

    public String resultado(Pessoa p){
        IMC imc = new IMC();
        double resultado = imc.calcular(p);
        if(resultado < 18.5){
            return "Abaixo do peso";
        }else if(resultado >= 18.5 && resultado <= 24.9){
            return "Peso normal";
        }else if(resultado >= 25 && resultado <= 29.9){
            return "Sobrepeso";
        }else if(resultado >= 30 && resultado <= 34.9){
            return "Obesidade grau 1";
        }else if(resultado >= 35 && resultado <= 39.9){
            return "Obesidade grau 2";
        }else{
            return "Obesidade grau 3";
        }
    }
}
