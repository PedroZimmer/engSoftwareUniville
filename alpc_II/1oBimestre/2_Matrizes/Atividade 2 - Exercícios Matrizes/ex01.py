#1)	Faça um programa que carregue uma matriz 3x5 com números inteiros,
# calcule e mostre a quantidade de elementos entre 15 e 20.

matriz = [[0] * 5 for i in range(5)]
cont = 10
cont2 = 0
for i in range(3):
    for j in range(5):
        matriz[i][j] = cont
        cont += 1
        if matriz[i][j] >= 15 and matriz[i][j] <= 20:
            cont2 += 1
print(matriz)
print("Números entre 15 e 20(inclusos):", cont2)