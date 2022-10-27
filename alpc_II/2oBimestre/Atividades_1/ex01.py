'''
1)	Faça uma função que receba três números inteiros:
 a,b e c, onde a é maior que 1. A função deve somar todos os inteiros entre b e c que sejam divisíveis por a (inclusive b e c) e retornar o resultado para a função principal.
'''
def funcao(valores):
    soma = 0
    a = valores[0]
    b = valores[1]
    c = valores[2]        
    for i in range(b,c):
        if i % a == 0:
            soma += i
    return soma
def inputs():
    a = int(input("Insira o valor de A: "))
    b = int(input("Insira o valor de B: "))
    c = int(input("Insira o valor de C: "))
    return [a,b,c]
resultado = (funcao(inputs()))
print("A soma dos valores é: ",resultado)