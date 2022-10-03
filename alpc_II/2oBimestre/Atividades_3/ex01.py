'''
1.	Faça um programa contendo uma função que receba dois números positivos por parâmetro e retorne a soma dos N números inteiros existentes entre eles.
'''

def funcao(num1,num2):
    if num1 > num2:
        num1,num2 = num2,num1
    soma = 0
    for i in range(num1,num2):
        soma += i
    return soma

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

respota = funcao(num1,num2)
print(respota)