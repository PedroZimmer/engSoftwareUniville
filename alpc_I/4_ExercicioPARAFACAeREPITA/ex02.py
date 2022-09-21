qtd50 = 0
qtdaltura = 0
mediaaltura = 0
quilos40 = 0
qtdpeso = 0
for pessoas in range(1,6):
  print("Pessoa", pessoas)
  idade = int(input("Insira a idade..."))
  altura = int(input("Insira a altura..."))
  peso = int(input("Insira o peso..."))
  if idade > 50:
    qtd50 += 1
  if idade > 10 and idade < 20:
    mediaaltura += altura
    qtdaltura += 1
  if peso < 40:
    qtdpeso += 1    
if qtdaltura != 0:    
  media = mediaaltura / qtdaltura
  print("A média das alturas das pessoas entre 10 e 20 anos é de:", media)
else:
  print("Não tem pessoas entre 10 e 20 anos!")
quilos40 = (qtdpeso / 5) * 100
print("Pessoas com mais de 50 anos:", qtd50)
print("A porcentagem das pessoas com peso inferior a 40 quilos é de:", quilos40)