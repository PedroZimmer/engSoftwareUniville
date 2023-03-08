

public class contador {
    public static void main(String args[]){
        int contador = 0;
        while(contador < 10) {
            System.out.println("Repetiu" +contador);
            contador++;
        }

        for(int i = 0; i < 10; i++) {
            System.out.println("Repetiu"+ i);
        }

        //laço reversivo
        for(int i = 10; i > 0; i--) {
            System.out.println("Repetiu" +i);
        }

        
    }
}
    