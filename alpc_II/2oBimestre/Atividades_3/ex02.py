'''
2.	Faça um programa contendo uma função que retorne 1 se o número digitado for positivo ou 0 se for negativo.

'''



def funcao(num):
    if num > 0:
        return 1
    if num < 0:
        return 0
    
num = int(input("Digite um número: "))

respota = funcao(num)
print(respota)