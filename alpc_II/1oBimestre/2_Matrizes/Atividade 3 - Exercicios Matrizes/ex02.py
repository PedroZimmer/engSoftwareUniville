#1)	Faça um programa que leia um vetor V contendo 18 elementos.
#A seguir, distribua esses elementos em uma matriz 3x6.
#Ao final, mostre a matriz gerada.
vetor = [i for i in range(18)]
print(vetor)
matriz = [[0]*6 for i in range(3)]
cont = 0
for i in range(3):
    for j in range(6):
        matriz[i][j] = vetor[cont]
        cont += 1
print(matriz)