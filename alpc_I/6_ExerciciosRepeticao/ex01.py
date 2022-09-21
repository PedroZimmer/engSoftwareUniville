totalalunos = 0
menor = 0
maior = 0
amenor = 0
amaior = 0

turmas = int(input("Insira o número de turmas...\n"))
for turma in range(1, turmas+1):
    num = int(input("Número da sala...\n"))
    alunos = int(input("Insira o número de alunos...\n"))
    homem = 0
    mulher = 0
    for sexo in range(1, alunos+1):
        print("Insira o sexo da criança", sexo)
        sex = str(input())
        if sex == "m":
            homem += 1
        if sex == "f":
            mulher += 1
        if turma == 1 and sexo == 1:
            menor = mulher
            amenor = num
    if mulher < menor:
        menor = mulher
        amenor = num
    if homem > maior:
        maior = homem
        amaior = num
    totalalunos += alunos
    media = totalalunos / turmas
print("Total crianças:", totalalunos)
print("Média de alunos por sala:", media)
print("Sala com mais meninos:", amaior, "com", maior, "meninos")
print("Sala com menos meninas:", amenor, "com", menor, "meninas")