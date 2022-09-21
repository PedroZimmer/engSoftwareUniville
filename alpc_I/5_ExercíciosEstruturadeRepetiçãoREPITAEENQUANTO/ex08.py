aluno = 2
omaior = 0
omenor = 0
menor = 11
maior = 0
qtd1 = 0
qtd2 = 0
freq = 0
nota = 0
for alunos in range(1,aluno+1):
    somanota = 0
    print("Aluno", alunos)
    #id = int(input("Insira a matricula...\n"))
    freq = int(input("Insira a frequencia...\n"))
    if freq < 40:
        qtd2 += 1
    for notas in range(1,4):
        print("Insira a nota",notas)
        repet = True
        while repet:
            nota = int(input())
            if nota < 0 or nota > 10:
                print("Insira uma nota válida!")
                repet = True
            else:
                repet = False
        somanota += nota
        media = somanota / 3
        if notas == 1 and alunos == 1:
            menor = nota
        if nota < menor:
            menor = nota
        if nota > maior:
            maior = nota
    if media < 6 or freq < 40:
        qtd1 += 1
        print("Reprovado")
    else:
        print("Aprovado")
    print("Média:",round(media,1))
perc1 = (qtd2 / 2) * 100
print("Menor nota:", menor)
print("Maior nota:", maior)
print("Numero de reprovados:", qtd1)
print("Reprovados por falta:", perc1,"%")