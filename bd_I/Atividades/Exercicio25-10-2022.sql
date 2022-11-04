
-- 1. 

USE MinhaCaixa
CREATE TABLE Feriados (nomeFeriado VARCHAR(50), dataFeriado DATE);

INSERT INTO Feriados VALUES ('Ano Novo', '2022-01-01');
INSERT INTO Feriados VALUES ('Carnaval', '2022-02-15');
INSERT INTO Feriados VALUES ('Carnaval', '2022-02-16');
INSERT INTO Feriados VALUES ('Sexta-feira Santa', '2022-04-15');
INSERT INTO Feriados VALUES ('Tiradentes', '2022-04-21');
INSERT INTO Feriados VALUES ('Dia do Trabalho', '2022-05-01');
INSERT INTO Feriados VALUES ('Corpus Christi', '2022-06-03');
INSERT INTO Feriados VALUES ('Independência do Brasil', '2022-09-07');
INSERT INTO Feriados VALUES ('Nossa Senhora Aparecida', '2022-10-12');
INSERT INTO Feriados VALUES ('Finados', '2022-11-02');
INSERT INTO Feriados VALUES ('Proclamação da República', '2022-11-15');
INSERT INTO Feriados VALUES ('Natal', '2022-12-25');
SELECT * FROM Feriados;

--2 

SELECT * FROM Clientes
SELECT * FROM CartaoCredito
SELECT * FROM Contas

SELECT ClienteNome, AgenciaCodigo, ContaNumero, clientes.ClienteCodigo, contas.ClienteCodigo FROM Clientes, Contas WHERE Clientes.ClienteCodigo=Contas.ClienteCodigo;

INSERT INTO CartaoCredito (AgenciaCodigo, ContaNumero, ClienteCodigo, CartaoCodigo, CartaoLimite, CartaoExpira,CartaoCodigoSeguranca)
VALUES (1, '173475-0', 1, '1234-7894-4561-1325', 10000, '2022-31-12', '123');

-- 3

