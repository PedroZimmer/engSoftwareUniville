'''Faça um programa que carregue uma matriz 12 x 4 com os valores das vendas de uma loja,
onde cada linha representa um mês do ano e cada coluna representa uma semana do mês.
Valide a entrada impedindo que sejam digitados valores negativos. (4.0)

Calcule e mostre:

a. O total vendido em cada mês do ano, mostrando nome do mês por extenso;

b. O total vendido pela loja no ano;

c. O mês em que houve o maior valor em vendas.'''

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
matriz = [[0]*4 for i in range(12)]
cont = 10
totalmes = [0]*12
totalsemana = [0]*12
totalvendas = 0
for i in range(12):
    print("Mês:", meses[i])
    for j in range(4):
        print("Semana:", j+1)
        repet = True
        while repet:
            matriz[i][j] = int(input())
            if matriz[i][j] < 0:
                print("Insira um numero positivo!")
            else:
                repet = False
        totalmes[i] += matriz[i][j]
        totalsemana[j] += matriz[i][j]
        totalvendas += matriz[i][j]
for i in range(12):
    print("Total de",meses[i],":",totalmes[i])
for i in range(4):
    print("Semana",i+1,":",totalsemana[i])
print("Total de vendas:", totalvendas)