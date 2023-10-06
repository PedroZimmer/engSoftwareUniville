package br.servicos;

import br.atividade01.entidades.Pessoa;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PessoaTest {
    //cenario
    Pessoa p1 = new Pessoa("Kleber", 20);
    Pessoa p2 = new Pessoa("Nelsinho", 25);
    @Test
    public void testGetNome() {




        //acao

        String nome1 = p1.getNome();
        String nome2 = p2.getNome();

        //verificacao

        assertEquals("Kleber", nome1);
        assertEquals("Nelsinho", nome2);

    }

    @Test
    public void testGetIdade() {

        //acao

        int idade1 = p1.getIdade();
        int idade2 = p2.getIdade();

        //verificacao

        assertEquals(20, idade1);
        assertEquals(25, idade2);


    }


}
