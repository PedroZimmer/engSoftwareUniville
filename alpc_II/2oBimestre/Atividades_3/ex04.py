'''
4.	Crie uma função que receba como parâmetro um valor inteiro e positivo N e 
retorne o valor de S que é obtido pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

'''


def funcao(num):
    soma = 0
    for i in range(1,num+1):
        fatorial = i
        for j in range(1,i):
            fatorial *= j
        soma += 1/fatorial
    return soma + 1
        

num = int(input("Numero: "))

resposta = funcao(num)
print(resposta)