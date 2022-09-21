totalalunos = 0
maiormasc = 0
menor = 0
numturmas = int(input("Insira o Nº de turmas... "))
for turmas in range(1,numturmas+1):
  numsala = int(input("Insira o número da sala... "))
  numalunos = int(input("Insira o número de alunos... "))
  qtdmasc = int(input("Insira o numero de meninos... "))
  qtdfem = numalunos - qtdmasc
  if turmas == 1:
    menor = qtdfem
  if numalunos > 0:
    totalalunos += numalunos
  if qtdmasc > maiormasc:
    maiormasc = qtdmasc
    idsalamasc = turmas
  if qtdfem < menor:
    menor = qtdfem
    idsalafem = turmas
media = totalalunos / numturmas
print("O total de crianças é de", totalalunos)
print("A média de alunos por sala é de", media)
print("A sala", idsalamasc, "tem o maior numero de meninos")
print("A sala", idsalafem, "tem o menor numero de meninas")