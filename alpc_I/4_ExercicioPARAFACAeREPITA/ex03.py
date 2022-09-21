somaotimo = 0
qtdotimo = 0
qtdreg = 0
qtdbom = 0
for pessoa in range(1,6):
  print("Pessoa", pessoa)
  idade = int(input("Insira sua idade... "))
  opini = int(input("Insira sua opinião <ÓTIMO – 3, BOM – 2, REGULAR – 1> ... "))
  if opini == 3:
    qtdotimo += 1
    somaotimo += idade
  if opini == 1:
    qtdreg += 1
  if opini == 2:
    qtdbom += 1
mediaotimo = somaotimo / qtdotimo
percbom = (qtdbom / 5) * 100
print("Média de idaed do ótimo:", mediaotimo)
print("Qtd regular:", qtdreg)
print("Porcentagem bom:", percbom)