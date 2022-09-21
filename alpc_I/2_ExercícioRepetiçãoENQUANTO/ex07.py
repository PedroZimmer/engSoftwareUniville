#REPENQ7) Faça um programa que receba a idade de 15 pessoas e que calcule e mostre: - A quantidade de pessoas em cada faixa etária - A percentagem de pessoas em cada uma das faixas etárias, com relação ao total de pessoas, de acordo com a tabela abaixo:
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
for idades in range(1,16):
  print("Insira a idade da pessoa nº...", idades)
  age = int(input())
  if age <= 15:
    faixa1 += 1
  else:
    if age >= 16 and age <= 30:
      faixa2 += 1
    else:
      if age >= 31 and age <= 45:
        faixa3 += 1
      else:
        if age >= 46 and age <= 60:
          faixa4 += 1
        else:
          faixa5 += 1
per1 = (faixa1 / 15) * 100
per2 = (faixa2 / 15) * 100
per3 = (faixa3 / 15) * 100
per4 = (faixa4 / 15) * 100
per5 = (faixa5 / 15) * 100
print("\nPessoas até 15 anos -->", faixa1, ".", per1, "% do total.")
print("Pessoas de 16 até 30 anos -->", faixa2, ".", per2, "% do total.")
print("Pessoas de 31 até 45 anos -->", faixa3, ".", per3, "% do total.")
print("Pessoas de 46 até 60 anos -->", faixa4, ".", per4, "% do total.")
print("Pessoas acima da 61 anos -->", faixa5, ".", per5, "% do total.") 