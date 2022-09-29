'''
1)	Faça uma função que receba três números inteiros:
 a,b e c, onde a é maior que 1. A função deve somar todos os inteiros entre b e c que sejam divisíveis por a (inclusive b e c) e retornar o resultado para a função principal.
'''
def funcao(a:int, b:int, c:int):
    soma = 0
    for i in range(b,c):
        if i % a == 0:
            soma += i
    return soma
va = int(input("Digite o valor de A:"))
vb = int(input("Digite o valor de B:"))
vc = int(input("Digite o valor de C:"))
print(funcao(va,vb,vc))