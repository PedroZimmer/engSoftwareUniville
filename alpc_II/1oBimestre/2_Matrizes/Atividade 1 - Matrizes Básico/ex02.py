#2)	Ler uma matriz A de duas dimensões com 7 linhas e 7 colunas.
#Ao final apresentar o total de elementos pares existentes dentro da matriz.

matriz = [[0] * 7 for i in range(7)]
cont = 1
contapar = 0
for i in range(7):
    for j in range(7):
        matriz[i][j] = cont
        cont += 1
        if matriz[i][j] % 2 == 0:
            contapar += 1
        else:
            pass
print(matriz)
print("Total de pares:", contapar)