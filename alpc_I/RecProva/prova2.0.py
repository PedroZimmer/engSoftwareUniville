somamedia = 0
qtd2 = 0 
maior = 0
for dias in range(1,9):
    valor = 0
    print("Qual sera o dia do evento...", dias)
    dia = int(input())
    qtd = int(input("Quantidade de pessoas no evento:\n"))
    if qtd <= 1000:
        valor = 4500
        qtd2 += 1
    else:
        valor = qtd * 5
    if qtd > maior:
        maior = qtd
        omaior = dia
    print("O valor da locação ficará:", valor)
    #Média
    somamedia += valor
media = somamedia / 8
print("A média do valor de locação é de:", media)
print(qtd2,"eventos não ultrapassaram 1000 pessoas.")
print("O dia com o maior número de pessoas é:", omaior, "com", maior, "pessoas.")