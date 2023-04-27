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

CREATE PROCEDURE cadastrar_notas
    (
        @MATRICULA INT,
        @CURSO CHAR(3),
        @PERIODOLETIVO CHAR(4),
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


-- CREATE PROCEDURE sp_CadastraNotas
-- 	(
-- 		@MATRICULA INT,
-- 		@CURSO CHAR(3),
-- 		@MATERIA CHAR(3),
-- 		@PERLETIVO CHAR(4),
-- 		@NOTA FLOAT,
-- 		@FALTA INT,
-- 		@BIMESTRE INT
-- 	)
-- 	AS
-- BEGIN

-- 		IF @BIMESTRE = 1
-- 		    BEGIN

--                 UPDATE MATRICULA
--                 SET Nota1 = @NOTA,
--                     Falta1 = @FALTA,
--                     TOTALPONTOS = @NOTA,
--                     TOTALFALTAS = @FALTA,
--                     MEDIA = @NOTA
--                 WHERE MATRICULA = @MATRICULA
--                     AND CURSO = @CURSO
--                     AND MATERIA = @MATERIA
--                     AND PERLETIVO = @PERLETIVO;
-- 		    END

--         ELSE 
        
--         IF @BIMESTRE = 2
--             BEGIN

--                 UPDATE MATRICULA
--                 SET Nota2 = @NOTA,
--                     Falta2 = @FALTA,
--                     TOTALPONTOS = @NOTA + Nota1,
--                     TOTALFALTAS = @FALTA + Falta1,
--                     MEDIA = (@NOTA + Nota1) / 2
--                 WHERE MATRICULA = @MATRICULA
--                     AND CURSO = @CURSO
--                     AND MATERIA = @MATERIA
--                     AND PERLETIVO = @PERLETIVO;
--             END

--         ELSE 
        
--         IF @BIMESTRE = 3
--             BEGIN

--                 UPDATE MATRICULA
--                 SET Nota3 = @NOTA,
--                     Falta3 = @FALTA,
--                     TOTALPONTOS = @NOTA + Nota1 + Nota2,
--                     TOTALFALTAS = @FALTA + Falta1 + Falta2,
--                     MEDIA = (@NOTA + Nota1 + Nota2) / 3
--                 WHERE MATRICULA = @MATRICULA
--                     AND CURSO = @CURSO
--                     AND MATERIA = @MATERIA
--                     AND PERLETIVO = @PERLETIVO;
--             END

--         ELSE 
        
--         IF @BIMESTRE = 4
--             BEGIN

--                 DECLARE @RESULTADO VARCHAR(50),
--                         @FREQUENCIA FLOAT,
--                         @MEDIAFINAL FLOAT,
--                         @CARGAHORA INT 
                
--                 SET @CARGAHORA = (
--                     SELECT CARGAHORARIA FROM MATERIAS 
--                     WHERE       SIGLA = @MATERIA
--                             AND CURSO = @CURSO)

--                 UPDATE MATRICULA
--                 SET Nota3 = @NOTA,
--                     Falta4 = @FALTA,
--                     TOTALPONTOS = @NOTA + Nota1 + Nota2 + Nota3,
--                     TOTALFALTAS = @FALTA + Falta1 + Falta2 + Falta3,
--                     MEDIA = (@NOTA + Nota1 + Nota2 + Nota3) / 4,
--                     MEDIAFINAL = (@NOTA + Nota1 + Nota2 + Nota3) / 4,
--                     PERCFREQ = 100 -( ((@FALTA + Falta1 + Falta2 + Falta3)*@CARGAHORA )/100)
--                         WHERE MATRICULA = @MATRICULA
--                     AND CURSO = @CURSO
--                     AND MATERIA = @MATERIA
--                     AND PERLETIVO = @PERLETIVO;


--             END
            

-- 		SELECT * FROM MATRICULA	WHERE MATRICULA = @MATRICULA
-- END
-- GO

-------------------------------------------------------------------------------

-- fazer execução de procedures

EXEC inserir_aluno 'Rodrigo Rodrigues';
EXEC inserir_aluno 'Leandro Lopes';
EXEC inserir_aluno 'Pedro Excel';

EXEC cadastrar_curso 'ENG', 'Engenharia de Software';
GO

EXEC cadastrar_professor 'Rodrigo Dornel';
EXEC cadastrar_professor 'Walter Coan';

EXEC cadastrar_materia 'POO', 'Orientação a objetos', 80, 'ENG', 1;
EXEC cadastrar_materia 'BDA', 'Banco de dados', 80, 'ENG', 1;

EXEC cadastrar_matricula @matricula = 1, @curso = 'ENG';
EXEC cadastrar_matricula @matricula = 2, @curso = 'ENG';
EXEC cadastrar_matricula @matricula = 3, @curso = 'ENG';


-- EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
--                       @CURSO = 'ENG',      -- char(3)
--                       @MATERIA = 'BDA',    -- char(3)
--                       @PERLETIVO = '2023', -- char(4)
--                       @NOTA = 7.0,         -- float
--                       @FALTA = 2,
--                       @BIMESTRE = 4;      -- int
-- GO
-- EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
--                       @CURSO = 'ENG',      -- char(3)
--                       @MATERIA = 'BDA',    -- char(3)
--                       @PERLETIVO = '2023', -- char(4)
--                       @NOTA = 7.0,         -- float
--                       @FALTA = 2,
--                       @BIMESTRE = 2;      -- int
-- GO
-- EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
--                       @CURSO = 'ENG',      -- char(3)
--                       @MATERIA = 'BDA',    -- char(3)
--                       @PERLETIVO = '2023', -- char(4)
--                       @NOTA = 7.0,         -- float
--                       @FALTA = 2,
--                       @BIMESTRE = 3;      -- int
-- GO
-- EXEC sp_CadastraNotas @MATRICULA = 1,      -- int
--                       @CURSO = 'ENG',      -- char(3)
--                       @MATERIA = 'BDA',    -- char(3)
--                       @PERLETIVO = '2023', -- char(4)
--                       @NOTA = 7.0,         -- float
--                       @FALTA = 2,
--                       @BIMESTRE = 4;      -- int             
-- GO