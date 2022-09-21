#1)	Faça um programa para ler e imprimir uma matriz 2 × 4 de números inteiros.

matriz = [[0] * 4 for i in range(4)] #VERIFICAR ESSA POHA DE """""4'"""" AQUI *(&AQUI@!!!!!!!!!!!!!!!!%!&¨!%&!%!&¨!
for i in range(2):
    for j in range(4):
        print("Insira o valor da linha %d e coluna %s" % (i,j))
        matriz[i][j] = int(input())
print(matriz)
for i in range(2):
    for j in range(4):
        print("Linha: %d Coluna: %s Valor:" % (i,j))
        print(matriz[i][j])