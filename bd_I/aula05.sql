USE MinhaCaixa

-- SELCIONA OS 5 PRIMEIROS REGISTROS DA TABELA CLIENTE
SELECT TOP 5 * FROM Clientes


-- SELECT ORDEM ALFABETICA
SELECT * FROM Clientes
ORDER BY ClienteNome -- ASC (ASCENDETE - PADRÃO) DESC (DESCENDENTE)


-- SELECT 5 PRIMEIROS CLIENTES COM MENOR RENDA ANUAL
SELECT TOP 5 ClienteNome, ClienteRendaAnual 
FROM Clientes
ORDER BY ClienteRendaAnual ASC







SELECT ClienteNome AS Nome, ClienteRendaAnual, Contas.ContaNumero, ContaAbertura, Movimentos.MovimentoTipo
FROM Clientes AS Cli, Contas, Movimentos
WHERE Cli.ClienteCodigo = Contas.ClienteCodigo
AND Movimentos.ContaNumero = Contas.ContaNumero
AND Cli.ClienteCodigo = 1
AND Movimentos.MovimentoTipo = 1


SELECT * FROM Contas WHERE ClienteCodigo = 1



SELECT * FROM Clientes
WHERE ClienteNome LIKE 'J%' -- Comeca com 'J'

SELECT * FROM Clientes
WHERE ClienteNome LIKE '%J' -- Termina com 'J'