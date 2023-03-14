USE MinhaCaixa

SELECT ClienteTelefone,CHARINDEX('-', ClienteTelefone) FROM Clientes


SELECT CHARINDEX('(', ClienteTelefone),
        CHARINDEX(')', ClienteTelefone),
        CASE WHEN
        SUBSTRING(ClienteTelefone,
            CHARINDEX('(',ClienteTelefone)+1, 
            2
            ) = 0 THEN 'SP' END
FROM Clientes

SELECT CHARINDEX('(', ClienteTelefone),
       CHARINDEX(')', ClienteTelefone),
       CASE WHEN CHARINDEX('(', ClienteTelefone) > 0 -- verifica se há um parêntese de abertura
            AND CHARINDEX(')', ClienteTelefone) > 0 -- verifica se há um parêntese de fechamento
            AND SUBSTRING(ClienteTelefone, CHARINDEX('(', ClienteTelefone)+1, 2) = '11' -- verifica se os dois próximos caracteres são '11'
            THEN 'SP' -- retorna 'SP' se as condições forem atendidas
            ELSE NULL -- retorna NULL caso contrário
       END
FROM Clientes
WHERE CHARINDEX('(', ClienteTelefone) > 0 AND CHARINDEX(')', ClienteTelefone) > 0;



SELECT RTRIM(LTRIM(ClienteTelefone)),
ClienteTelefone,
ClienteNome,
UPPER(ClienteNome),
PATINDEX('%@%', ClienteEmail),
CONCAT(REPLICATE('@', 5),'DORNEL'),
DATALENGTH(ClienteNome),
FORMAT (ClienteNascimento, 'd' , 'en-US') AS 'US English Result',
FORMAT (12345, '##-###')
FROM Clientes