package br.servicos;

import br.atividade02.entidades.Retangulo;
import br.atividade02.servicos.RetanguloService;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class RetanguloTest {

    @Test
    public void testCalculateArea() {

        //cenario
        Retangulo retangulo = new Retangulo(10, 20);
        RetanguloService retanguloService = new RetanguloService();

        //acao
        double test = retanguloService.calculateArea(retangulo.getWidth(), retangulo.getHeight());

        //verificacao
        assertEquals(200.0, test, 0.01);

    }
}