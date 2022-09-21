qtdrep = 0
qtdap = 0
qtdexam = 0
média = 0
summedia = 0
for aluno in range(1,7):
  print("Aluno", aluno)
  print("Insira a primeira nota...")
  nota1 = float(input())
  print("Insira a segunda nota...")
  nota2 = float(input())
  media = (nota1 + nota2) / 2
  summedia += media
  if media < 3:
    print("<REPROVADO>")
    qtdrep += 1
  else:
    if media >= 3 and media <= 7:
      print("<EXAME>")
      qtdexam += 1
    else:
      print("<APROVADO>")
      qtdap += 1
mediaturma = summedia / 6
print("Aprovados = ", qtdap)
print("Exames = ", qtdexam)
print("Reprovados = ", qtdrep)
print("\nA média da sala é de = ", mediaturma)