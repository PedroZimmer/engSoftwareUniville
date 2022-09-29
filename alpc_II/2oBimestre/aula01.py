
def minhaFuncao(num:int=0):
    print(num)
    if num < 100:
        minhaFuncao(num+1)
minhaFuncao(0)

def soma(num1:float, num2:float):
    resul = num1 + num2
    return resul

guardarresultado = soma(2,2)
print(guardarresultado)
