USE MinhaCaixa

SELECT * FROM Clientes -- todas as linhas e colunas

SELECT ClienteNome FROM Clientes -- todas as linhas e apenas a coluna ClienteNome

SELECT ClienteNome, ClienteSobreNome FROM Clientes -- todas as linhas e apenas as colunas ClienteNome e ClienteSobreNome

SELECT * FROM Clientes WHERE ClienteSexo = 'M' AND ClienteBairro = 'CENTRO' -- todas as linhas e colunas onde o sexo é masculino e o bairro é centro

SELECT * FROM Clientes WHERE ClienteSexo = 'M' AND (ClienteBairro = 'CENTRO' OR ClienteBairro = 'BOM RETIRO')
AND ClienteEstadoCivil = 'S' -- todas as linhas e colunas onde o sexo é masculino e o bairro é centro ou bom retiro e o estado civil é solteiro

