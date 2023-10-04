package br.exemplo.servicos;

import static org.junit.Assert.assertNotEquals;

import org.junit.Assert;
import org.junit.Test;

import br.exemplo.entidades.Usuario;

public class AssertTest {
		
	@Test
	public void teste() {
		Assert.assertEquals(1, 1);
		Assert.assertEquals(0.8, 0.8, 0.01);
		Assert.assertEquals("bola", "bola");
		//Assert.assertEquals("bola", "Bola");
	
		assertNotEquals("bola","casa");
		
		Assert.assertTrue("bola".equalsIgnoreCase("Bola"));
		
		
		Usuario u1 = new Usuario("Usuario 1");
		Usuario u2 = new Usuario("Usuario 1");
		
		Assert.assertEquals(u1, u2);
	}

}
