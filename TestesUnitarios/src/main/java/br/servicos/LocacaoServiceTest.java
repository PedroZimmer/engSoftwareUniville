package br.servicos;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.fail;

import org.hamcrest.CoreMatchers;
import org.hamcrest.Matcher;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ErrorCollector;

import br.entidades.Filme;
import br.entidades.Locacao;
import br.entidades.Usuario;
import junit.framework.Assert;


public class LocacaoServiceTest {
	
	@Rule
	public ErrorCollector error = new ErrorCollector();
	
	
	@Test
	public void testeLocacao() {
		//cenario
		LocacaoService service = new LocacaoService();
		Usuario usuario = new Usuario("Usuario 1");
		Filme filme = new Filme("Filme 1", 2, 5.0);		
		
		//acao		
		Locacao locacao;
		try {
			locacao = service.alugarFilme(usuario, filme);
			
			//verificacao
			assertEquals(5.0, locacao.getValor(), 0.01);
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			fail("Não deveria lancar excecao");
		}
		
		
		
		

		
	}

}
