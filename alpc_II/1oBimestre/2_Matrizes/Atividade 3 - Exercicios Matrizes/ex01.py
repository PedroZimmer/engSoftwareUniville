

matriz = [[0]*5 for i in range(4)]
somalinha = [0] * 4
somacoluna = [0] * 5
cont = 1
somatotal = 0
for i in range(4):
    for j in range(5):
        matriz[i][j] = cont
        cont += 1
        somalinha[i] += matriz[i][j]
        somacoluna[j] += matriz[i][j]
        somatotal += matriz[i][j]
print(matriz)
for i in range(4):
    print("Linha:",i+1,"-",somalinha[i])     
for i in range(5):
    print("Coluna:",i+1,"-",somacoluna[i])
print("Soma total:", somatotal)