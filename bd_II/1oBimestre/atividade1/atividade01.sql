    -- USE master;
	-- ALTER DATABASE Universidade SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
	-- GO
	-- DROP DATABASE Universidade;
	-- GO
	-- USE master;
	-- CREATE DATABASE Universidade;
	-- GO

	SELECT * FROM Universidade


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
                SET Nota3 = @NOTA,
                    Falta4 = @FALTA,
                    TOTALPONTOS = @NOTA + Nota1 + Nota2 + Nota3,
                    TOTALFALTAS = @FALTA + Falta1 + Falta2 + Falta3,
                    MEDIA = (@NOTA + Nota1 + Nota2 + Nota3) / 4,
                    MEDIAFINAL = (@NOTA + Nota1 + Nota2 + Nota3) / 4,
                    PERCFREQ = 100 -( ((@FALTA + Falta1 + Falta2 + Falta3)*@CARGAHORA )/100)
                        WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;


            END
            

		SELECT * FROM MATRICULA	WHERE MATRICULA = @MATRICULA
END
GO

EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
                      @CURSO = 'ENG',      -- char(3)
                      @MATERIA = 'BDA',    -- char(3)
                      @PERLETIVO = '2023', -- char(4)
                      @NOTA = 7.0,         -- float
                      @FALTA = 2,
                      @BIMESTRE = 4;      -- int
GO
EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
                      @CURSO = 'ENG',      -- char(3)
                      @MATERIA = 'BDA',    -- char(3)
                      @PERLETIVO = '2023', -- char(4)
                      @NOTA = 7.0,         -- float
                      @FALTA = 2,
                      @BIMESTRE = 2;      -- int
GO
EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
                      @CURSO = 'ENG',      -- char(3)
                      @MATERIA = 'BDA',    -- char(3)
                      @PERLETIVO = '2023', -- char(4)
                      @NOTA = 7.0,         -- float
                      @FALTA = 2,
                      @BIMESTRE = 3;      -- int
GO
EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
                      @CURSO = 'ENG',      -- char(3)
                      @MATERIA = 'BDA',    -- char(3)
                      @PERLETIVO = '2023', -- char(4)
                      @NOTA = 7.0,         -- float
                      @FALTA = 2,
                      @BIMESTRE = 4;      -- int             
GO