package AtividadeIMC;


    public class IMC {

        public double calcular(Pessoa p){
            double altura = p.getAltura();
            double peso = p.getPeso();
            double imc = peso / (altura * altura);
            return imc;
        }

}
