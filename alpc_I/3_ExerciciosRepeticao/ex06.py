menor = 0
maior = 0
nmaior = 0
nmenor = 0
for alunos in range(1,11):
  print("Aluno...", alunos)
  num = alunos#int(input("Insira o número do aluno..."))
  altura = float(input("Insira a altura do aluno..."))
  if alunos == 1:
    menor = altura
  if altura > maior:
    maior = altura
    nmaior = num
  if altura < menor:
    menor = altura
    nmenor = num   
print("O aluno", nmenor, "é o mais baixo com", menor, "de altura")
print("O aluno", nmaior, "é o mais alto com", maior, "de altura")