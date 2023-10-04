package br.servicos;

import static br.utils.DataUtils.adicionarDias;

import java.security.Provider.Service;
import java.util.Date;

import org.junit.Assert;
import org.junit.Test;

import br.entidades.Filme;
import br.entidades.Locacao;
import br.entidades.Usuario;
import br.utils.DataUtils;

public class LocacaoService {
	
	public Locacao alugarFilme(Usuario usuario, Filme filme) throws Exception {
		
		if (filme.getEstoque() == 0 ) {
			throw new Exception("Filme sem estoque");
		}
		
		Locacao locacao = new Locacao();
		locacao.setFilme(filme);
		locacao.setUsuario(usuario);
		locacao.setDataLocacao(new Date());
		locacao.setValor(filme.getPrecoLocacao());

		//Entrega no dia seguinte
		Date dataEntrega = new Date();
		dataEntrega = adicionarDias(dataEntrega, 1);
		locacao.setDataRetorno(dataEntrega);
		
		//Salvando a locacao...	
		//TODO adicionar método para salvar
		
		return locacao;
	}
	
	public static void main(String[] args) {
							
	}
	
}