meses = ['Janeiro', "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
maior = 0
menor = 0
omenor = 0
omaior = 0
tempmedia = []
for i in range(12):
    print("Insira a temperatura média de", meses[i])
    tempmedia.append(int(input()))
    if i == 0:
        menor = tempmedia[i]
        omenor = meses[i]
    if tempmedia[i] < menor:
        menor = tempmedia[i]
        omenor = meses[i]
    if tempmedia[i] > maior:
        maior = tempmedia[i]
        omaior = meses[i]
print("A maior média é no mês de", omaior,"com", maior,"graus.")
print("A menor média é no mês de", omenor,"com", menor,"graus.")
