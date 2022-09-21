#1)	Faça um programa que carregue uma matriz 10x3 com as notas de dez alunos em três provas.
#Mostre um relatório com o número do aluno (número da linha) e a prova em que cada aluno...
#obteve menor nota.
#Ao final do relatório, mostre quantos alunos tiveram menor nota na prova 1
#Quantos alunos tiveram menor nota na prova 2 e quantos alunos tiveram menor nota na prova 3.


matriz = [[0] * 3 for i in range(10)]
cont = 1
for i in range(10):
    for j in range(3):
        matriz[i][j] = cont
        cont += 1
        if cont > 10:
            cont = 1        
asmenores = [0] * 10
menornota = 0
provamenor = [0] * 10
qtdmenor = [0,0,0]   
for i in range(10):
    for j in range(3):
        if j == 0:
            menornota = matriz[i][j]
            provamenor[i] = j            
        if matriz[i][j] < menornota:
            menornota = matriz[i][j]
            provamenor[i] = j
    if provamenor[i] == 0:
        qtdmenor[0] += 1
    else:
        if provamenor[i] == 1:
            qtdmenor[1] += 1
        else:
            qtdmenor[2] += 1
    asmenores[i] = menornota
print(matriz)
for i in range(10):
    print("Aluno", i+1)
    print("A menor nota foi na prova",provamenor[i]+1,"com:", asmenores[i])
for i in range(3):
    print("Menor nota na prova",i+1,":",qtdmenor[i])