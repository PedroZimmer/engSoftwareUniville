vetor1 = [14,15,16,17,18,19,20,21,]
disciplina = [100,2,3,4,5]
#for i in range(8):
    #print("Insira a idade do aluno", i+1)
    #etor1.append(int(input()))
#for i in range(5):
    #print("Insira o código da disciplina", i+1)
    #disciplina.append(int(input()))
matriz = [[0]*5 for i in range(8)] # COLUNA | ALUNOS
matriz2 = [[0]*5 for i in range(8)] # COLUNA | ALUNOS
cont = 1
for i in range(8):
    for j in range(5):
        matriz[i][j] = cont
        cont += 1
        if cont > 4:
            cont = 1
print("<<---MATRIZ--->>")
print(matriz)
print("<<----1---->>")
cont1 = 0
repet = True
while repet:
    codigo1 = int(input("Insira um código de uma disciplina..."))
    i = 0
    cont2 = 0
    for i in range(5):
        if codigo1 == disciplina[i]:
            pass
        else:
            cont2 += 1
    if cont2 == 5:
        print("Insira uma disciplina válida!!!")
        repet = True
    else:
        repet = False
cont4 = 0
contidade = 0
for i in range(8): #ALUNOS/LINHAS
    for j in range(5): #Nº PROVAS|COLUNAS
        if disciplina[j] == codigo1:
            if matriz[i][j] >= 2:
                if vetor1[i] >=18 and vetor1[i] <= 25:
                    cont1 += 1
        #222222
        if matriz[i][j] < 3:
            matriz2[i][j] = True
        else:
            matriz2[i][j] = False
        #33333333
        if matriz[i][j] == 0:
            contidade += vetor1[i]
            cont4 += 1
print("<< 1. =>",cont1,">>")
print("<< 2. >>")
for i in range(8):
    cont3 = 0
    print("Aluno - ",i+1)
    print("Disciplinas:")
    for j in range(5):
        if matriz2[i][j]:
            print(disciplina[j])
        else:
            cont3 += 1
    if cont3 == 5:
        print("Fez mais de 3 provas em todas as disciplinas!")
if cont4 > 0:
    print("<< 3. =>",contidade/cont4,">>")
else:
    print("Todos fizeram ao menos uma prova de cada disciplina!")
