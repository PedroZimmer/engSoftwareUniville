package br.servicos;

import org.junit.Assert;
import org.junit.Test;

public class AssertTest {

    @Test
    public void teste() {
        Assert.assertEquals(1,1);
        Assert.assertEquals(0.5123,0.5120,0.0003); //o delta é a margem de erro
        Assert.assertEquals(Math.PI,3.14,0.01);
        Assert.assertEquals("bola","bola","bolas");



    }


}
