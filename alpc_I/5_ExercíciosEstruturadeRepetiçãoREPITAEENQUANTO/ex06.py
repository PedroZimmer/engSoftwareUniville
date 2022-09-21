pessoas = 2
qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd4 = 0
somamedia1 = 0
for pessoa in range(1,pessoas+1):
    print("Pessoa", pessoa)
    idade = int(input("Insira a idade...\n"))
    peso = int(input("Insira o peso...\n"))
    altura = int(input("Insira a altura...\n"))
    repet1 = True
    while repet1:
        olhos = str(input("Insira a cor dos olhos \n<A – Azul | P – Preto | V – Verde | C – Castanho>\n"))
        repet1 = True
        if olhos != "a" and olhos != "p" and olhos != "v" and olhos != "c":
            print("Insira uma cor válida!")
        else:
            repet1 = False
    cabelo = str(input("Insira a cor do cabelo\n<P – preto | C – castanho | L – Louro | R – Ruivo>\n"))
    repet2 = True
    while repet2:
        if cabelo != "p" and cabelo != "c" and cabelo != "l" and cabelo != "r":
            print("Insira uma cor válida!")
            repet2 = True
        else:
            repet2 = False
    if idade > 50 and peso < 60:
        qtd1 += 1
    if altura < 150:
        qtd2 += 1   
        somamedia1 += idade
    if olhos == "a":
        qtd3 += 1
    if cabelo == "r" and olhos != "a":
        qtd4 += 1
media1 = somamedia1 / qtd2
perc1 = (qtd3 / pessoas) * 100
print("Pessoas acima de 50 anos e menos de 60Kg:", qtd1)
print("Média idade das pessoas com menos de 150cm:", media1)
print("Porcentagem de pessoas com olhos azuis:", perc1,"%")
print("Pessoas ruivas sem olhos azuis:", qtd4)