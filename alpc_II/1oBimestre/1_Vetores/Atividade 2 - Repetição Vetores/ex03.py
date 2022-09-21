
questoes = ['a','a','a','a','a','a','a','a','a','a']
#for i in range(1,11):
    #print("Insira a resposta de questão", i)
    #questoes.append(str(input()))
print("Gabarito:", questoes)
respostas = []
numalunos = []
notas = []
cont = 0
qtdalunos = 3 #QUANTIDA DE ALUNOS
for i in range(1,qtdalunos+1):
    nota = 0
    print("Insira o número do aluno", i)
    numalunos.append(int(input()))
    for j in range(1,11):
        print("Insira a resposta do aluno da questão", j)
        respostas.append(str(input()))
    for k in range(10):
        if respostas[k] == questoes[k]:
            nota += 1
        else:
            pass
    if nota >= 6:
        cont += 1
    respostas = []
    notas.append(nota)
perc = (cont / qtdalunos) * 100
for i in range(qtdalunos):
    print("O aluno", numalunos[i],"tirou", notas[i],"na prova.")
print("A porcentagem de aprovação foi de", perc,"%")