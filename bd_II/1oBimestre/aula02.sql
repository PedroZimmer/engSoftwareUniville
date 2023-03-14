USE MinhaCaixa


CREATE FUNCTION DtsMinutos
        (@min int, @dti datetime, @dtf datetime)

RETURNS @tbl TABLE (dt datetime)
AS
BEGIN
    WHILE @dti <= @dtf
    BEGIN
        INSERT INTO @tbl(dt) VALUES (@dti)
        SET @dti = DATEADD(MINUTE, @min,@dti)
    END
    RETURN
END


SELECT * FROM DtsMinutos(1,GETDATE(),GETDATE()+1)





CREATE FUNCTION clienteApos(@dt datetime)
RETURNS TABLE
AS
RETURN (SELECT * FROM Clientes WHERE ClienteNascimento >= @dt)

select * from clientes
    INNER join 
        clienteApos('1980-01-01') as fn
            on clientes.ClienteNascimento 
                    =fn.ClienteNascimento
