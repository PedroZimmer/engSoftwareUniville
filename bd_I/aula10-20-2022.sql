SELECT ClienteNome, ContaTipo,
contas.ClienteCodigo, clientes.ClienteCodigo
FROM Clientes, Contas 
WHERE Clientes.ClienteCodigo=Contas.ClienteCodigo


SELECT ClienteNome, ContaTipo,
contas.ClienteCodigo, clientes.ClienteCodigo
FROM Clientes
    INNER JOIN Contas ON (Clientes.ClienteCodigo=Contas.ClienteCodigo)
    LEFT JOIN Movimentos ON (Contas.ContaNumero=Movimentos.ContaNumero)


USE MinhaCaixa


SELECT Clientes.ClienteNome, CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCodigo IS NULL THEN
ClienteTelefone ELSE 'NÃO LIGAR' END AS 'SITUACAO'
FROM Clientes
LEFT JOIN CartaoCredito
    ON (Clientes.ClienteCodigo=CartaoCredito.ClienteCodigo)