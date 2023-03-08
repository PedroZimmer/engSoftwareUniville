import java.sql.SQLInvalidAuthorizationSpecException;
import java.util.Scanner;

import javax.sound.sampled.SourceDataLine;


public class desafioTabuada{
    public static void main(String args[]){

    Scanner leitor = new Scanner(System.in);
    System.out.println("Escolha a tabuada:");
    int z = 1; 

    while(z != 0) {

        int num = leitor.nextInt();
        if(num == 0){
            System.out.println("Escolhe um certo poha");
            
            z = 1;
        } else {
            for(int i = 1; i <11; i++) {
                System.out.println(num + "*" + i + "=" + i*num);
                System.out.println("Cabo");
            }
            break;
        }
    }
    
    }
}