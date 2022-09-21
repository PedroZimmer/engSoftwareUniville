#REPENQ6) Faça um programa que receba o valor do salário mínimo e uma lista contendo a quantidade de quilowatts gasta por consumidor e o tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial).
#Calcule e mostre:
# O valor de cada quilowatt, sabendo que o quilowatt custa 1/8 do salário mínimo;
#- O valor a ser pago por cada consumidor (conta final mais acréscimos), considerando que o acréscimo é o mesmo da tabela a seguir:

consumo = 1
contaconsumidor = 0
fatura = 0

while consumo  != 0:
  sal = int(input("\nInsira o valor do salário do consumidor:"))
  type = int(input("Insira o tipo de consumidor..."))
  consumo = float(input("Insira a quantidade de quilowatt consumida..."))
  custwatt = (sal / 8) 
  print("O quilowatt custa:", custwatt)
  if type == 1:
    wattpagar = ((custwatt * consumo) * 0.05) + (custwatt * consumo)
    print("O valor a ser pago pelo consumidor será de...", wattpagar)
  else:
    if type == 2:
      wattpagar = ((custwatt * consumo) * 0.1) + (custwatt * consumo)
      print("O valor a ser pago pelo consumidor será de...", wattpagar)
    else:
      if type == 3:
        wattpagar = ((custwatt * consumo) * 0.15) + (custwatt * consumo)
        print("O valor a ser pago pelo consumidor será de...", wattpagar)
  if wattpagar > 500 and wattpagar < 1000:
    contaconsumidor += 1
  fatura += wattpagar 
print("\nO faturamente total da empresa é...", fatura)
print("A quantidade de consumidores que pagam entre R$500 e R$1000 é de...", contaconsumidor)