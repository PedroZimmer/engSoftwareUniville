USE Universidade;
GO


-------------------------------------------------------------------------------------------

create procedure cadastrar_curso
@curso char(3),
@nome varchar(50)
AS
BEGIN
    INSERT CURSOS VALUES (@curso, @nome);
END
GO
-------------------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------------------
create procedure cadastrar_professor
@nome varchar(50)
AS
BEGIN
    INSERT PROFESSOR VALUES (@nome);
END
GO
-------------------------------------------------------------------------------------------

create procedure inserir_aluno
@nome varchar(50)
AS
BEGIN
    INSERT ALUNOS VALUES (@nome);
END
GO


-------------------------------------------------------------------------------------------

--Procedure para matrricula

-- INSERT MATRICULA
-- (
--         MATRICULA,
--         CURSO,
--         MATERIA,
--         PROFESSOR,
--         PERLETIVO

-- )
-- SELECT 1 AS MATRICULA, CURSO, SIGLA,PROFESSOR, -- ESSE "1" É A MATRICULA DO ALUNO, NO CASO EU TO INSERINDO NA TABELA MATRICULA CADA MATERIA EM QUE O ALUNO ESTA MATRICULADO
--     YEAR(GETDATE()) FROM MATERIAS WHERE CURSO ='ENG'
-- GO


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




-- NEM FUDENDO QUE FUNCIONOUUUUUUUU PORRA PROFESSOR TMJ

---------------------------------------------------------------------



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
                        WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;


            END
            

		SELECT * FROM MATRICULA	WHERE MATRICULA = @MATRICULA
END
GO

-------------------------------------------------------------------------------



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
                SET N1 = @NOTA,
                    F1 = @FALTA,
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
                SET N2 = @NOTA,
                    F2 = @FALTA,
                    TOTALPONTOS = @NOTA + N1,
                    TOTALFALTAS = @FALTA + F1,
                    MEDIA = (@NOTA + N1) / 2
                WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;
            END

        ELSE 
        
        IF @BIMESTRE = 3
            BEGIN

                UPDATE MATRICULA
                SET N3 = @NOTA,
                    F3 = @FALTA,
                    TOTALPONTOS = @NOTA + N1 + N2,
                    TOTALFALTAS = @FALTA + F1 + F2,
                    MEDIA = (@NOTA + N1 + N2) / 3
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
                SET N4 = @NOTA,
                    F4 = @FALTA,
                    TOTALPONTOS = @NOTA + N1 + N2 + N3,
                    TOTALFALTAS = @FALTA + F1 + F2 + F3,
                    MEDIA = (@NOTA + N1 + N2 + N3) / 4,
                    MEDIAFINAL = (@NOTA + N1 + N2 + N3) / 4,
                    PERCFREQ = 100 -( ((@FALTA + F1 + F2 + F3)*@CARGAHORA )/100)

                    --RESULTADO
                    ,RESULTADO = 
                    CASE 
                        WHEN ((@NOTA + N1 + N2 + N3) / 4) >= 7 
                            AND (100 -( ((@FALTA + F1 + F2 + F3)*@CARGAHORA )/100))>=75
                        THEN 'APROVADO'
                        
                        WHEN ((@NOTA + N1 + N2 + N3) / 4) >= 3 
                            AND (100 -( ((@FALTA + F1 + F2 + F3)*@CARGAHORA )/100))>=75 
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
                SET NOTAEXAME = @NOTA
                --FALTA CALCULAR O RESULTADO PÓS EXAME
                WHERE MATRICULA = @MATRICULA
                    AND CURSO = @CURSO
                    AND MATERIA = @MATERIA
                    AND PERLETIVO = @PERLETIVO;
            END

		SELECT * FROM MATRICULA	WHERE MATRICULA = @MATRICULA
END
