qtddezoito = 0
totalsumaltura = 0
qtdpeso = 0
for teams in range(1,7):
  print("Time", teams)
  contidade = 0
  contdezoito = 0
  sumaltura = 0
  contpeso = 0
  for players in range(1,12):
    print("Jogador", players)
    print("Insira a idade do jogador")
    idade = 10
    print("Insira o peso do jogador")
    peso = 60
    print("Insira a altura do jogador")
    altura = 30
    sumaltura += altura
    contidade += idade
    mediaidade = contidade / 11
    if idade < 18:
      qtddezoito += 1
    if peso > 80:
      qtdpeso += 1
  contpeso += qtdpeso
  contdezoito += qtddezoito
  totalsumaltura += sumaltura
  print("A média de idade dos jogadores é = ", mediaidade)    
print("\nA quantidade de jogadores abaixo de 18 anos é", contdezoito)
mediaaltura = totalsumaltura / 66
print("A média da altura do campeonato é de = ", mediaaltura)
percpeso = (contpeso / 66) * 100
print("A porcentagem de pessoas com mais de 80Kg é de:", percpeso,"%")