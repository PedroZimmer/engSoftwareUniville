-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.


CREATE DATABASE CLIENTES_2

USE CLIENTES_2

CREATE TABLE CLIENTES
(
    ID_CLIENTE INT IDENTITY(1,1) PRIMARY KEY,
    NOME VARCHAR(50) NOT NULL,
    CPF VARCHAR(11) NOT NULL,
    ENDERECO VARCHAR(50) NOT NULL,
    CIDADE VARCHAR(50) NOT NULL,
    TELEFONE VARCHAR(11) NOT NULL
)

CREATE TABLE PRODUTOS
(
    ID_PRODUTO INT IDENTITY(1,1) PRIMARY KEY,
    NOME VARCHAR(50) NOT NULL,
    DESCRICAO VARCHAR(50) NOT NULL,
    PRECO DECIMAL(10,2) NOT NULL,
    QUANTIDADE INT NOT NULL
)

CREATE TABLE PEDIDOS
(
    ID_PEDIDO INT IDENTITY(1,1) PRIMARY KEY,
    ID_CLIENTE INT NOT NULL,
    DATA_PEDIDO DATETIME NOT NULL,
    DATA_ENTREGA DATETIME NOT NULL,
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE)
)

SELECT * FROM CLIENTES
SELECT * FROM PRODUTOS
SELECT * FROM PEDIDOS

INSERT INTO CLIENTES (NOME, CPF, ENDERECO, CIDADE, TELEFONE) VALUES ('JOAO', '12345678901', 'PIRIRI', 'GUARACITY', '123456789')
INSERT INTO CLIENTES (NOME, CPF, ENDERECO, CIDADE, TELEFONE) VALUES ('MARIA', '12345678902', 'PORORO', 'JARAS', '123456780')
INSERT INTO PRODUTOS (NOME, DESCRICAO, PRECO, QUANTIDADE) VALUES ('MONITOR', '4K', 10.00, 10)
INSERT INTO PRODUTOS (NOME, DESCRICAO, PRECO, QUANTIDADE) VALUES ('MOUSEPAD', 'GRANDE', 20.00, 20)
INSERT INTO PEDIDOS (ID_CLIENTE, DATA_PEDIDO, DATA_ENTREGA) VALUES (1, '2020-01-01', '2020-01-02')
INSERT INTO PEDIDOS (ID_CLIENTE, DATA_PEDIDO, DATA_ENTREGA) VALUES (2, '2020-01-01', '2020-01-02')


SELECT * FROM CLIENTES
SELECT * FROM PRODUTOS
SELECT * FROM PEDIDOS

UPDATE CLIENTES SET NOME = 'JOAO DA UNIVILLE' WHERE ID_CLIENTE = 1

