#5)	Faça um programa que receba os preços de 20 produtos em cinco lojas diferentes e armazene-os em uma matriz 20x5.
#Desconsiderando empates, mostre o número do produto e o número da loja do produto mais caro.
qtdprod = 20 #QUANTIDADE DE PRODUTOSSSSSSSSSSSSSSS
qtdlojas = 5 #QUANTIDADE DE LOJAS
matriz = [[0]*qtdprod for i in range(qtdlojas)]
cont = 1
maior = 0
cont1 = 0
asmaioreslojas = []
osmaioresprodutos = []
amaiorloja = 0
omaiorprod = 0
for i in range(qtdlojas): #LINHA
    #print("Loja",i+1)
    for j in range(qtdprod): #COLUNA
        #print("Insira o preço do produto...",j+1)
        #matriz[i][j] = int(input())
        matriz[i][j] = cont 
        cont *= 2
        if cont > 500:
            cont = 32
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            amaiorloja = i
            omaiorprod = j
for i in range(qtdlojas): #LINHA
    for j in range(qtdprod): #COLUNA
        if maior == matriz[i][j]:
            cont1 += 1
            asmaioreslojas.append(i) #LOJAS
            osmaioresprodutos.append(j) #PRODUTOS
if cont1 > 1:
    print("Essas",cont1,"lojas tem o produto mais caro")
    for i in range(cont1):
        print("Loja:", asmaioreslojas[i]+1,"| Produto:", osmaioresprodutos[i]+1,"| Valor:", maior)
else:
    print("A loja", amaiorloja+1,"tem o produto:", omaiorprod+1,"custando:",maior)

#teste
