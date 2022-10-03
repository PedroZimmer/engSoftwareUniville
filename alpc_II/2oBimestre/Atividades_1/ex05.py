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
olhos = ['A', 'C', 'C', 'A', 'C']
cabelos = ['L', 'P', 'C', 'L', 'P']
idade = [20, 30, 40, 50, 60]

