#1)	Faça um programa que carregue uma matriz 3 x 3 com números reais...
#e receba um valor, número digitado pelo usuário, calcule e mostre...
#a matriz resultante da multiplicação do número digitado por elemento da matriz.

matriz = [[0]*3 for i in range(3)]
cont = 1
for i in range(3):
    for j in range(3):
        matriz[i][j] = cont
        cont += 1
print(matriz)
num = int(input("Insira um número..."))
for i in range(3):
    for j in range(3):
        matriz[i][j] *= num
print("Nova matriz:\n",matriz)


