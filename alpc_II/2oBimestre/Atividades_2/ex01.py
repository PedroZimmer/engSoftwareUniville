'''
1.	Faça uma função que receba dois vetores A e B de dez elementos inteiros, por parâmetro.
O procedimento deve determinar e mostrar um vetor C que contenha os elementos de A e B em ordem decrescente.
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def funcao(a, b):
    c = a + b
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i] > c[j]:
                c[i], c[j] = c[j], c[i]
    return c

print(funcao(a, b))

