USE MinhaCaixa

CREATE VIEW VClientesIdade
AS
SELECT ClienteNome,
    DATEDIFF(YEAR, ClienteNascimento,
    GETDATE()) AS Idade
FROM dbo.Clientes;

SELECT * FROM VClientesIdade