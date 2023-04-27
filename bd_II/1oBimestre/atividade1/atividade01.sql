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


------------------------------------------------------------------------------

CREATE PROCEDURE sp_CadastraNotas
	(
		@MATRICULA INT,
		@CURSO CHAR(3),
		@MATERIA CHAR(3),
		@PERLETIVO CHAR(4),
		@NOTA FLOAT,
		@FALTA INT,
		@BIMESTRE INT
	)
	AS
BEGIN

		IF @BIMESTRE = 1
		    BEGIN

                UPDATE MATRICULA
                SET Nota1 = @NOTA,
                    Falta1 = @FALTA,
                    TOTALPONTOS = @NOTA,
                    TOTALFALTAS = @FALTA,
                    MEDIA = @NOTA
                WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;
		    END

        ELSE 
        
        IF @BIMESTRE = 2
            BEGIN

                UPDATE MATRICULA
                SET Nota2 = @NOTA,
                    Falta2 = @FALTA,
                    TOTALPONTOS = @NOTA + Nota1,
                    TOTALFALTAS = @FALTA + Falta1,
                    MEDIA = (@NOTA + Nota1) / 2
                WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;
            END

        ELSE 
        
        IF @BIMESTRE = 3
            BEGIN

                UPDATE MATRICULA
                SET Nota3 = @NOTA,
                    Falta3 = @FALTA,
                    TOTALPONTOS = @NOTA + Nota1 + Nota2,
                    TOTALFALTAS = @FALTA + Falta1 + Falta2,
                    MEDIA = (@NOTA + Nota1 + Nota2) / 3
                WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;
            END

        ELSE 
        
        IF @BIMESTRE = 4
            BEGIN

                DECLARE @RESULTADO VARCHAR(50),
                        @FREQUENCIA FLOAT,
                        @MEDIAFINAL FLOAT,
                        @CARGAHORA INT 
                
                SET @CARGAHORA = (
                    SELECT CARGAHORARIA FROM MATERIAS 
                    WHERE       SIGLA = @MATERIA
                            AND CURSO = @CURSO)

                UPDATE MATRICULA
                SET Nota4 = @NOTA,
                    Falta4 = @FALTA,
                    TOTALPONTOS = @NOTA + Nota1 + Nota2 + Nota3,
                    TOTALFALTAS = @FALTA + Falta1 + Falta2 + Falta3,
                    MEDIA = (@NOTA + Nota1 + Nota2 + Nota3) / 4,
                    MEDIAFINAL = (@NOTA + Nota1 + Nota2 + Nota3) / 4,
                    PERCFREQ = 100 -( ((@FALTA + Falta1 + Falta2 + Falta3)*@CARGAHORA )/100)

                    --RESULTADO
                    ,RESULTADO = 
                    CASE 
                        WHEN ((@NOTA + Nota1 + Nota2 + Nota3) / 4) >= 7 
                            AND (100 -( ((@FALTA + Falta1 + Falta2 + Falta3)*@CARGAHORA )/100))>=75
                        THEN 'APROVADO'
                        
                        WHEN ((@NOTA + Nota1 + Nota2 + Nota3) / 4) >= 3 
                            AND (100 -( ((@FALTA + Falta1 + Falta2 + Falta3)*@CARGAHORA )/100))>=75 
                        THEN 'EXAME' 
                        
                        ELSE 'REPROVADO'
                    
                    END

                        WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;


            END
        ELSE 
        
        IF @BIMESTRE = 5

            BEGIN

                UPDATE MATRICULA
                SET NOTAEXAME = @NOTA,
                --FALTA CALCULAR O RESULTADO PÓS EXAME
				
					
				RESULTADO = 
				CASE WHEN (@NOTA + MEDIAFINAL) / 2 >= 5 THEN 'APROVADO'

				ELSE 'REPROVADO'
				END			
				
				WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;
                
            END

		SELECT * FROM MATRICULA	WHERE MATRICULA = @MATRICULA
END



--------------------------------------------------------------------------------

EXEC inserir_aluno 'Rodrigo Rodrigues';
EXEC inserir_aluno 'Leandro Lopes';

EXEC cadastrar_curso 'ENG', 'Engenharia de Software';
GO

EXEC cadastrar_professor 'Rodrigo Dornel';
EXEC cadastrar_professor 'Leanderson André';

EXEC cadastrar_materia 'POO', 'Orientação a objetos', 80, 'ENG', 2;
EXEC cadastrar_materia 'BDA', 'Banco de dados', 80, 'ENG', 1;

EXEC cadastrar_matricula @matricula = 1, @curso = 'ENG';
EXEC cadastrar_matricula @matricula = 2, @curso = 'ENG';



EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 7.0, @FALTA = 1, @BIMESTRE = 1;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 8.0, @FALTA = 1, @BIMESTRE = 2;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 1.0, @FALTA = 1, @BIMESTRE = 3;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 1.0, @FALTA = 1, @BIMESTRE = 4;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 9.0, @FALTA = 0, @BIMESTRE = 5;



EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 7.0, @FALTA = 1, @BIMESTRE = 1;
EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 8.0, @FALTA = 1, @BIMESTRE = 2;
EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 9.0, @FALTA = 1, @BIMESTRE = 3;
EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'POO', @PERLETIVO = '2023', @NOTA = 10.0, @FALTA = 1, @BIMESTRE = 4;

EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 7.0, @FALTA = 1, @BIMESTRE = 1;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 8.0, @FALTA = 1, @BIMESTRE = 2;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 9.0, @FALTA = 1, @BIMESTRE = 3;
EXEC sp_CadastraNotas @MATRICULA = 1, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 10.0, @FALTA = 1, @BIMESTRE = 4;

EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 7.0, @FALTA = 1, @BIMESTRE = 1;
EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 8.0, @FALTA = 1, @BIMESTRE = 2;
EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 9.0, @FALTA = 1, @BIMESTRE = 3;
EXEC sp_CadastraNotas @MATRICULA = 2, @CURSO = 'ENG', @MATERIA = 'BDA', @PERLETIVO = '2023', @NOTA = 10.0, @FALTA = 1, @BIMESTRE = 4;




SELECT * FROM MATRICULA
SELECT * FROM ALUNOS
SELECT * FROM CURSOS
SELECT * FROM MATERIAS
SELECT * FROM PROFESSOR
GO