#2)	Faça um programa que receba as vendas semanais (de um mês) de cinco vendedores...
# de uma loja e armazene essas vendas em uma matriz. Calcule e mostre:
#a.	O total de vendas do mês de cada vendedor
#b.	O total de vendas de cada semana (todos os vendedores juntos)
#c.	O total de vendas do mês


matriz = [[0] * 4 for i in range(5)]
#print(matriz)
totalmes = []
somasemana = [0] * 4
for i in range(5):
    somai = 0
    print("<<Vendedor: ", i+1,">>")
    for j in range(4):
        print("Insira o nº de vendas da semana:", j+1)
        numvendas = int(input())
        matriz[i][j] = numvendas
        somai += matriz[i][j]
        if j == 3:
            totalmes.append(somai)
        somasemana[j] += numvendas
total = 0        
for i in range(5):
    print("\nVendedor", i+1,"- Total de vendas:", totalmes[i])
for u in range(4):
    print("Semana",u,":",somasemana[u])
    total += somasemana[u]
print("Total de vendas:", total)
