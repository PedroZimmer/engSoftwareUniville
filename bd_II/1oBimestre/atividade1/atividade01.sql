    USE master;
	ALTER DATABASE Universidade SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
	GO
	DROP DATABASE Universidade;
	GO
	USE master;
	CREATE DATABASE Universidade;
	GO



	USE Universidade;

	CREATE TABLE ALUNOS
	(
		MATRICULA INT NOT NULL IDENTITY
			CONSTRAINT PK_ALUNO PRIMARY KEY,
		NOME VARCHAR(50) NOT NULL
	);



	
	CREATE TABLE CURSOS
	(
		CURSO CHAR(3) NOT NULL
			CONSTRAINT PK_CURSO PRIMARY KEY,
		NOME VARCHAR(50) NOT NULL
	);


	
	CREATE TABLE PROFESSOR
	(
		PROFESSOR INT IDENTITY NOT NULL
			CONSTRAINT PK_PROFESSOR PRIMARY KEY,
		NOME VARCHAR(50) NOT NULL
	);
	



	CREATE TABLE MATERIAS
	(
		SIGLA CHAR(3) NOT NULL,
		NOME VARCHAR(50) NOT NULL,
		CARGAHORARIA INT NOT NULL,
		CURSO CHAR(3) NOT NULL,
		PROFESSOR INT
			CONSTRAINT PK_MATERIA
			PRIMARY KEY (
							SIGLA,
							CURSO,
							PROFESSOR
						)
			CONSTRAINT FK_CURSO
			FOREIGN KEY (CURSO) REFERENCES CURSOS (CURSO),
		CONSTRAINT FK_PROFESSOR
			FOREIGN KEY (PROFESSOR)
			REFERENCES PROFESSOR (PROFESSOR)
	);
	

	CREATE TABLE MATRICULA
	(
		MATRICULA INT,
		CURSO CHAR(3),
		MATERIA CHAR(3),
		PROFESSOR INT,
		PERLETIVO INT,
		Nota1 FLOAT,
		Nota2 FLOAT,
		Nota3 FLOAT,
		Nota4 FLOAT,
		TOTALPONTOS FLOAT,
		MEDIA FLOAT,
		Falta1 INT,
		Falta2 INT,
		Falta3 INT,
		Falta4 INT,
		TOTALFALTAS INT,
		PERCFREQ FLOAT,
		RESULTADO VARCHAR(20)
			CONSTRAINT PK_MATRICULA
			PRIMARY KEY (
							MATRICULA,
							CURSO,
							MATERIA,
							PROFESSOR,
							PERLETIVO
						),
		CONSTRAINT FK_ALUNOS_MATRICULA
			FOREIGN KEY (MATRICULA)
			REFERENCES ALUNOS (MATRICULA),
		CONSTRAINT FK_CURSOS_MATRICULA
			FOREIGN KEY (CURSO)
			REFERENCES CURSOS (CURSO),
		
		CONSTRAINT FK_PROFESSOR_MATRICULA
			FOREIGN KEY (PROFESSOR)
			REFERENCES PROFESSOR (PROFESSOR)
	);
	
ALTER TABLE MATRICULA ADD MEDIAFINAL FLOAT
GO
ALTER TABLE MATRICULA ADD NOTAEXAME FLOAT
GO
    


create procedure inserir_aluno
@nome varchar(50)
AS
BEGIN
    INSERT ALUNOS VALUES (@nome);
END
GO
-------------------------------------------------------------------

create procedure cadastrar_curso
@curso char(3),
@nome varchar(50)
AS
BEGIN
    INSERT CURSOS VALUES (@curso, @nome);
END
GO

---------------------------------------------------------------------

create procedure cadastrar_professor
@nome varchar(50)
AS
BEGIN
    INSERT PROFESSOR VALUES (@nome);
END
GO
---------------------------------------------------------------------

create procedure cadastrar_materia
@sigla char(3),
@nome varchar(50),
@cargahoraria int,
@curso char(3),
@professor int
AS
BEGIN
    INSERT MATERIAS VALUES (@sigla, @nome, @cargahoraria, @curso, @professor);
END
GO
---------------------------------------------------------------------

create procedure cadastrar_matricula
@matricula int,
@curso char(3)
-- @materia char(3),
-- @professor int,
-- @perletivo char(4)
AS
BEGIN
    INSERT MATRICULA
(
        MATRICULA,
        CURSO,
        MATERIA,
        PROFESSOR,
        PERLETIVO
)
    SELECT @matricula AS MATRICULA, CURSO, SIGLA,PROFESSOR, -- ESSE "1" É A MATRICULA DO ALUNO, NO CASO EU TO INSERINDO NA TABELA MATRICULA CADA MATERIA EM QUE O ALUNO ESTA MATRICULADO
    YEAR(GETDATE()) FROM MATERIAS WHERE CURSO = @curso;
END
GO

EXEC inserir_aluno 'Rodrigo Rodrigues';
EXEC inserir_aluno 'Leandro Lopes';
EXEC inserir_aluno 'Pedro Excel';

EXEC cadastrar_curso 'ENG', 'Engenharia de Software';
GO

EXEC cadastrar_professor 'Rodrigo Dornel';
EXEC cadastrar_professor 'Leanderson André';

EXEC cadastrar_materia 'POO', 'Orientação a objetos', 80, 'ENG', 2;
EXEC cadastrar_materia 'BDA', 'Banco de dados', 80, 'ENG', 1;

EXEC cadastrar_matricula @matricula = 1, @curso = 'ENG';
EXEC cadastrar_matricula @matricula = 2, @curso = 'ENG';
EXEC cadastrar_matricula @matricula = 3, @curso = 'ENG';


SELECT * FROM MATRICULA
SELECT * FROM ALUNOS
SELECT * FROM CURSOS
SELECT * FROM MATERIAS
SELECT * FROM PROFESSOR
GO