USE MinhaCaixa;

-- exemplo 1
SELECT ClienteBairro, sum(MovimentoValor) AS Total
FROM
    Movimentos
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
GROUP BY ClienteBairro
ORDER BY ClienteBairro

--top 5 bairros com mais movimentações
SELECT TOP 5 ClienteBairro, sum(MovimentoValor) AS Total
FROM
    Movimentos
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
GROUP BY ClienteBairro
ORDER BY 2 DESC


SELECT ClienteBairro, COUNT(ClienteCodigo) AS Quantidade FROM Clientes
GROUP BY ClienteBairro
ORDER BY 2 DESC

SELECT 
ClienteBairro,
COUNT(ClienteCodigo) AS Quantidade,
SUM(ClienteRendaAnual) AS ClienteRendaAnual
FROM Clientes
GROUP BY ClienteBairro
ORDER BY 2 DESC


SELECT ClienteBairro, sum(MovimentoValor) AS Total,
count(Clientes.ClienteCodigo) as Quantidade
FROM 
    Movimentos
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
WHERE Clientes.ClienteCodigo > 1
GROUP BY ClienteBairro
HAVING count(Clientes.ClienteCodigo) > 200
ORDER BY 3 DESC


