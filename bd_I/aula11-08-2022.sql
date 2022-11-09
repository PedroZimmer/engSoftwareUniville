USE MinhaCaixa


SET DATEFORMAT YMD
SET LANGUAGE PORTUGUESE


SELECT YEAR(GETDATE()) --CURRENT



------------------------

SET DATEFORMAT YMD

SELECT * FROM Movimentos
WHERE MovimentoData = '2022/06/30'


----------------------

SELECT DATENAME(MONTH,(MovimentoData))
FROM Movimentos

---------------------

SELECT ClienteNome,
YEAR(ClienteNascimento) AS ANO,
DATENAME(MONTH,ClienteNascimento) AS MES,
DATEPART(yyyy,ClienteNascimento) AS ANO2,
DATEPART(WEEK,ClienteNascimento) AS ANO3,
DATENAME(MONTH,(DATEPART(mm,ClienteNascimento))) AS ANO4
FROM Clientes


-------------------

SELECT EOMONTH(GETDATE()) AS 'ULTIMO DIA MES'
SELECT DATEADD(day,1,GETDATE())
SELECT DATEADD(month,-1,GETDATE())


-------------------

SELECT ClienteNome, 
year(GETDATE()) - year(ClienteNascimento) as IDADE
FROM Clientes