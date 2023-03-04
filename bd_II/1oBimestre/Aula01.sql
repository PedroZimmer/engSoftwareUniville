USE MinhaCaixa

SELECT ClienteNome, dbo.fnretorna(ClienteNascimento) AS ANO FROM Clientes

CREATE FUNCTION fnretorna(@data datetime)

RETURNS int
AS
    BEGIN
    DECLARE @ano int
    SET @ano = YEAR(@data)

        RETURN @ano
END


-------

SELECT ClienteNome, dbo.fnretornaidade(ClienteNascimento) AS Idade FROM Clientes

CREATE FUNCTION fnretornaidade(@data datetime)

RETURNS int
AS 
    BEGIN
    DECLARE @idade int
    SET @idade = YEAR(GETDATE()) - YEAR(@data)

        RETURN @idade 
END

