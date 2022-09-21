matriz = [[0] * 4 for i in range(4)]
cont= 1
soma1 = 0 
produto1 = 1
somatotal = 0
cont2 = 0
proddiag = 1
for i in range(4):
    for j in range(4):
        matriz[i][j] = cont
        cont += 1
for i in range(4):
    for j in range(4):
        if i == 0:
            produto1 *= matriz[0][j]
        somatotal += matriz[i][j]
        if i == j:
            diagonal = matriz[i][j]
            proddiag *= diagonal
    soma1 += matriz[i][0]
    
print(matriz)
print("Soma da 1a coluna:", soma1)
print("Produto da 1a linha:", produto1)
print("Soma total:", somatotal)                        
print("Produto da diagonal", proddiag)