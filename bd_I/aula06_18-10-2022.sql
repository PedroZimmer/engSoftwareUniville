USE MinhaCaixa

SELECT ClienteNome, ClienteSexo,
CASE WHEN ClienteSexo = 'M' THEN 'Masculino'
     WHEN ClienteSexo = 'F' THEN 'Feminino'
ELSE 'nn' END AS Sexo,
ClienteEstadoCivil,
CASE WHEN ClienteEstadoCivil = 'S' THEN 'Solteiro'
     WHEN ClienteEstadoCivil = 'C' THEN 'Casado'
     WHEN ClienteEstadoCivil = 'D' THEN 'Divorciado'
     WHEN ClienteEstadoCivil = 'V' THEN 'Viúvo'
ELSE 'nn' END AS EstadoCivil    
FROM Clientes


--
SELECT ClienteNome, ClienteRendaAnual,
CASE WHEN ClienteRendaAnual >=0 AND
            ClienteRendaAnual <= 100000 THEN 'Rico'
ELSE 'Pobre' END AS 'CLASSE_CLIENTE'
FROM Clientes
ORDER BY ClienteRendaAnual DESC




--
SELECT ClienteNome, ClienteRendaAnual,
CASE WHEN 
    ClienteRendaAnual BETWEEN 0 AND 100000 
    
    THEN 'Rico'
ELSE 'Pobre' END AS 'CLASSE_CLIENTE'
FROM Clientes


--EXEMPLO 4
SELECT DISTINCT ClienteBairro FROM Clientes
ORDER BY ClienteBairro ASC

--EXEMPLO 5
SELECT ClienteNome, ClienteBairro FROM Clientes
WHERE ClienteBairro IN ('CENTRO', 'FLORESTA', 'ATIRADORES')

--EXEMPLO 6
SELECT ClienteNome, ClienteBairro FROM Clientes
WHERE ClienteBairro IN (SELECT ClienteNome FROM CartaoCredito) 

--EXEMPLO 7
SELECT * FROM Clientes WHERE ClienteNome = 'Jon'
UNION
SELECT * FROM Clientes WHERE ClienteNome = 'Jon'

--EXEMPLO 8
SELECT ClienteNome, ClienteSobrenome FROM Clientes WHERE ClienteNome = 'Jon'
UNION
SELECT ClienteSobrenome, ClienteNome FROM Clientes WHERE ClienteNome = 'Jon'



