#6)	Faça um programa que carregue uma matriz 3 x 4, calcule e mostre:
#a.	A quantidade de elementos pares
#b.	A soma dos elementos ímpares
#c.	A média de todos os elementos

matriz = [[0]*4 for i in range(3)]
cont = 1
for i in range(3):
    for j in range(4):
        matriz[i][j] = cont
        cont += 1
print(matriz)        
contpar = 0
somaimpar = 0
somatotal = 0
for i in range(3):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            contpar += 1
        else:
            somaimpar += matriz[i][j]
        somatotal += matriz[i][j]
print("Qtd de nº pares:", contpar)
print("Soma dos impares:", somaimpar)
print("Média:", somatotal/12)
        