
USE Universidade;
--criar procedure para inserir alunos na tabela alunos

create procedure inserir_aluno
@nome varchar(50)
AS
BEGIN
    INSERT ALUNOS VALUES (@nome);
END

exec inserir_aluno 'Robertin';

SELECT * FROM ALUNOS


-------------------------------------------------------------------

--criar procedure para cadastrar cursos

create procedure cadastrar_curso
@curso char(3),
@nome varchar(50)
AS
BEGIN
    INSERT CURSOS VALUES (@curso, @nome);
END

exec cadastrar_curso 'ADS', 'Análise e Desenvolvimento de Sistemas';


---------------------------------------------------------------------

--procedure para PROFESSOR

create procedure cadastrar_professor
@nome varchar(50)
AS
BEGIN
    INSERT PROFESSOR VALUES (@nome);
END

EXEC cadastrar_professor 'Dornel';

---------------------------------------------------------------------



--procedure para MATERIAS

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

EXEC cadastrar_materia 'XYZ', 'Orientação a objetos', 80, 'ENG', 1;

SELECT * FROM MATERIAS 

DELETE FROM MATERIAS WHERE SIGLA = 'BDA'


---------------------------------------------------------------------

--Procedure para matrricula

