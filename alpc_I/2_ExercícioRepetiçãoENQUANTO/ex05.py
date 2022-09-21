#Faça um algoritmo que calcule a média de todas as turmas de uma escola. Considere como entradas o número de turmas e o número de alunos de cada turma. A média de cada turma deve ser apresentada, além da média geral, que será o resultado da média das turmas.

mediaescola = 0
somaescola = 0

print("Insira o número de turmas...")
numturmas = int(input())

for turma in range(numturmas):
  print("Turma:", turma+1)
  print("Digite a qtd de alunos:")
  numalunos = int(input())
  somaturma = 0
  for aluno in range(numalunos):
    print("\tAluno:", aluno+1)
    print("\tDigite sua média")
    mediaaluno = float(input())
    somaturma += mediaaluno
  mediaturma = somaturma / numalunos
  print("A média da turma é", mediaturma)
  somaescola += mediaturma
mediaescola = somaescola / numturmas
print("A media da escola é", mediaescola)