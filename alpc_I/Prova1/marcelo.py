linhamaior = 0
maisprodt = 0
refugost1 = 0
refugost2 = 0

for linha in range (3):
  print("> Linha", linha+1)
  acumulador = 0
  for turno in range (2):
    print("\t Turno", turno+1)
    codigo = int(input("Digite o codigo do produto produzido (1, 2 ou 3): "))
    qntprodt = int(input("Digite a quantidade de produtos produzidos: "))
    qntsuct = int(input("Digite a quantidade de sucata produzida: "))
    acumulador += qntprodt
    
    if turno == 0:
      refugost1 = refugost1 + qntsuct
    else:
      refugost2 += qntsuct
    if codigo == 2:
      if qntsuct <= 100:
        print("- Situação Normal")
      else:
        print("- Situação Irregular")
    else:
      if qntsuct >= 50:
        print("- Situação Irregular")
      else:
        print("- Situação Normal")
  if acumulador > maisprodt:
    maisprodt = acumulador
    linhamaior = linha
print("Quantidade de refugos Turno 1: ", refugost1)
print("Quantidade de refugos Turno 2: ", refugost2) 
print("Linha que mais produziu no dia: ",linhamaior, ". Produtos Produzidos: ", acumulador)