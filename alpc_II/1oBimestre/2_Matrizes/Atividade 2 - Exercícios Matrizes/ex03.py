#3)	Faça um programa que receba o estoque atual de três produtos que estão armazenados...
#em quatro armazéns e coloque esses dados em uma matriz 5x3.
#Sendo que a última linha da matriz contém o custo de cada produto, calcule e mostre:
#a.	A quantidade de itens  armazenas em cada armazém
#b.	Qual o armazém possui maior estoque do produto 2;
#c.	Qual o armazém possui menor estoque
#d.	Qual o custo total de cada produto
#e.	Qual o custo total de cada armazém
matriz = [[0]*3 for i in range(5)]
maior = 0
qtditem = 0
qtdarmazem = [0] * 4
custoprod = [0] * 3
custoarm = [0] * 4
#PREÇOOOOO
cont = 10
for i in range(3): #PREÇOOOOO
    matriz[4][i] = cont
    cont += 10
#ESTOQUEEEEE
for i in range(3):
    print("<<Item", i+1,">>")
    for j in range(4):
        print("Insira a quantidade no armazém", j+1)
        qtditem = int(input())
        matriz[j][i] = qtditem
        #AAAA
        qtdarmazem[j] += qtditem
        #BBBB
        if i == 1:
            if qtditem > maior:
                maior = qtditem
                omaior = j+1
        #DDDDDDDDDDDDDDDD
        custoprod[i] += qtditem * matriz[4][i]
        #EEEEEEEEEEEEEEEE
        custoarm[j] += qtditem * matriz[4][i]
#CCCCCCC        
for i in range(4):
    if i == 0:
        menor = qtdarmazem[i]
        omenor = i
    if qtdarmazem[i] < menor:
        menor = qtditem
        omenor = i
print("\nMatriz ->\n", matriz)
print("\nA.")                
for i in range(4):
    print("Quantidade do armazém", i+1,"é:", qtdarmazem[i]) #Certo           
print("\nB. Maior estoque do produto 2:", omaior) #Certo
print("\nC. Armazém com menos estoque:", omenor+1, "com:", menor) #Certo
print("\nD.")
for i in range(3):
    print("Custo total do produto", i+1,"é de",custoprod[i]) #Certo
print("\nE.")
for i in range(4):
    print("Custo total do armazém", i+1,"é de",custoarm[i]) #Certo