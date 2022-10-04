'''
3.	Elabore uma função que retorne um vetor com os três primeiros números perfeitos.
Sabe-se que um número é perfeito quando é igual à soma de seus divisores (exceto ele mesmo).
Exemplo: os divisores de 6 são: 1 , 2 e 3, e 1+2+3 = 6, logo 6 é perfeito.
'''

def funcao():
    perfeitos = []
    for i in range(1, 1000):
        lista = []
        for j in range(1,1000):
            if i > j:
                if i % j == 0:
                    lista.append(j)
        if sum(lista) == i:
            perfeitos.append(i)
    return perfeitos
print(funcao())