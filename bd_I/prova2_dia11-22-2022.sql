--escreva uma consulta que mostre o nome e sobrenome do cliente (concatenados), e se o cliente for homem, mostre Sr. e se for mulher Sra. na frente do nome/sobrenome.
USE MinhaCaixa


SELECT CASE WHEN ClienteSexo = 'M'
THEN 'Sr. ' + ClienteNome + ' ' + ClienteSobrenome 
ELSE 'Sra. ' + ClienteNome + ' ' + ClienteSobrenome
END AS NomeCompleto FROM Clientes;




--Escreva uma consulta SQL que retorne o resultado abaixo com todos os bairros e quantidade de clientes de cada um:

USE MinhaCaixa

SELECT ClienteBairro,
COUNT(ClienteBairro) AS QuantidadeClientes
FROM Clientes GROUP BY ClienteBairro;


--Faça uma consulta que mostre o nome do cliente, o nome da agência, o bairro da agência e o número do cartão de crédito, somente para os clientes em que a conta foi aberta a partir de 2010. Caso ele não tenha cartão de crédito, mostre o telefone do cliente para contato. 

USE MinhaCaixa


SELECT Clientes.ClienteNome, Agencias.AgenciaNome, Agencias.AgenciaBairro, CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCredito.CartaoCodigo IS NOT NULL
    THEN 'TEM CONTA' ELSE ClienteTelefone
END AS 'SITUACAO'
FROM Clientes, Agencias, CartaoCredito, Contas
WHERE (Contas.ContaAbertura) > '2010-01-01'

SELECT Clientes.ClienteNome, Agencias.AgenciaNome, Agencias.AgenciaBairro, CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCodigo IS NULL
    THEN ClienteTelefone ELSE 'TEM Cartao' END AS 'SITUACAO'
FROM Clientes, Agencias, CartaoCredito

SELECT Clientes.ClienteNome, CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCodigo IS NULL THEN
ClienteTelefone ELSE 'NÃO LIGAR' END AS 'SITUACAO'
FROM Clientes
FULL OUTER JOIN CartaoCredito
    ON (Clientes.ClienteCodigo=CartaoCredito.ClienteCodigo)



SELECT * FROM CartaoCredito








--criar uma consulta que motre um ranking com as 10 idades que tem a melhor renda

SELECT ClienteNascimento, ClienteRendaAnual,
DATEDIFF(YEAR, ClienteNascimento, GETDATE()) AS Idade
FROM Clientes
ORDER BY ClienteRendaAnual DESC


SELECT TOP 10 YEAR(GETDATE()) - YEAR(ClienteNascimento) AS idade, Clientes.ClienteRendaAnual as Renda
FROM Clientes

SELECT ClienteNome,ClienteSobrenome, (ClienteRendaAnual / 5.36) AS Dolar, (ClienteRendaAnual / 5.51) AS Euro FROM Clientes;


--quais os 5 bairros que tem as piores rendas

SELECT top 5 Clientes.ClienteBairro, SUM(Clientes.ClienteRendaAnual) AS RendaTotal FROM Clientes
GROUP by Clientes.ClienteBairro ORDER by 2



--Faça uma consulta que mostre o nome do cliente, o nome da agência, o bairro da agência e o número do cartão de crédito, somente para os clientes em que a conta foi aberta a partir de 2010. Caso ele não tenha cartão de crédito, mostre o telefone do cliente para contato. 
 SELECT Clientes.ClienteNome, Agencias.AgenciaNome, Agencias.AgenciaBairro, CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCodigo IS NULL
    THEN ClienteTelefone ELSE 'TEM Cartao' END AS 'SITUACAO'
FROM Clientes, Agencias, CartaoCredito
WHERE (Clientes.ClienteCodigo=CartaoCredito.ClienteCodigo)