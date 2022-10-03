'''
5)	Foi realizada uma pesquisa de algumas características físicas de cinco habitantes de uma certa região. 
De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos (A – Azuis ou C – Castanhos),
cor dos cabelos (L – Louros, P – Pretos ou C – Castanhos) e idade.

a.	Faça uma função que leia esses dados em vetores. Determine, por meio de outra função,
    a média de idade das pessoas com olhos castanhos e cabelos pretos. Mostre esse resultado no programa principal.
    
b.	Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.

c.	Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino
    cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
'''

'''
sexo = []
olhos = []
cabelo = []
idade = []
for i in range(5):
    print("Pessoa", i+1)
    sexo.append(input('Digite o sexo: '))
    olhos.append(input('Digite a cor dos olhos: '))
    cabelo.append(input('Digite a cor dos cabelos: '))
    idade.append(int(input('Digite a idade: ')))
'''

sexo = ['M', 'F', 'F', 'M', 'F']
olhos = ['C', 'C', 'C', 'A', 'C']
cabelos = ['P', 'P', 'C', 'L', 'P']
idade = [20, 30, 40, 50, 60]

def mediaidade(olhos, cabelos, idade):
    somaidade = 0
    cont = 0
    for i in range(len(olhos)):
        if olhos[i] == 'C' and cabelos[i] == 'P':
            somaidade += idade[i]
            cont += 1
    return somaidade/cont

print(mediaidade(olhos, cabelos, idade))

def maioridade(idade):
    maior = idade[0]
    for i in range(len(idade)):
        if idade[i] > maior:
            maior = idade[i]
    return maior
print("maior idade =", maioridade(idade))

def qtd_feminino(olhos, cabelos, idade, sexo):
    cont = 0
    for i in range(len(olhos)):
        if idade[i] >= 18 and idade[i] <= 35 and olhos[i] == 'A' and cabelos[i] == 'L' and sexo[i] == 'F':
            cont += 1
    return cont
print(qtd_feminino(olhos, cabelos, idade, sexo))
