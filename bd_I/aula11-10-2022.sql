USE MinhaCaixa

SELECT ClienteNome + ' ' + ClienteSobrenome
 + '/' + CAST(ClienteRendaAnual AS CHAR(10)) AS NomeCompleto FROM Clientes



 SELECT ClienteNome + ' ' + ClienteSobrenome
 + '/' + CONVERT(CHAR(10), ClienteRendaAnual) AS NomeCompleto
  FROM Clientes

USE MinhaCaixa

  SELECT ClienteNascimento,
  DATENAME(MONTH,ClienteNascimento) AS MES,
  YEAR(ClienteNascimento) as ANO,
  DATENAME(MONTH,ClienteNascimento) + '/'+
  CAST(YEAR(ClienteNascimento) AS CHAR(4)) as MESANO
  FROM Clientes



SELECT YEAR(GETDATE())

DECLARE @ANO INT
SET @ANO = (SELECT YEAR(GETDATE()))
SELECT @ANO AS ANO

DECLARE @ANO2 CHAR(4)
SET @ANO2 = (SELECT (YEAR(GETDATE())))
SELECT @ANO2 AS ANO2