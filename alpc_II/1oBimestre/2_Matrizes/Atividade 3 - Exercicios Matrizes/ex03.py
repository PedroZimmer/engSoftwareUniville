#3)	Faça um programa que carregue uma matriz 12 x 4 com os valores das vendas...
#de uma loja, onde cada linha representa um mês do ano e cada coluna...
#representa uma semana do mês. Calcule e mostre:
#a.	O total vendido em cada mês do ano, mostrando o nome do mês por extenso;
#b.	O total vendido em cada semana durante todo o ano;
#c.	O total vendido pela loja no ano.

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
matriz = [[0]*4 for i in range(12)]
cont = 10
totalmes = [0]*12
totalsemana = [0]*12
totalvendas = 0
for i in range(12):
    for j in range(4):
        matriz[i][j] = cont
        cont += 10
        if cont > 100:
            cont = 10
        totalmes[i] += matriz[i][j]
        totalsemana[j] += matriz[i][j]
        totalvendas += matriz[i][j]
print(matriz)
for i in range(12):
    print("Total de",meses[i],":",totalmes[i])
for i in range(4):
    print("Semana",i+1,":",totalsemana[i])
print("Total de vendas:", totalvendas)