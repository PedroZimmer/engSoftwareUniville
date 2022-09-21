omaior = 0
omenor = 0
altura = 0
sumaltura = 0
qtdf = 0
qtdm = 0
mediaf = 0
sexomaior = 0
sexmaior = 0
for pessoa in range(1,3):
    print("Pessoa", pessoa)
    print("Digite o sexo:")
    sexo = str(input())
    print("Digite a altura:")
    altura = float(input())
    if pessoa == 1:
      omaior = altura
      omenor = altura
    if altura > omaior:
      omaior = altura
      sexmaior = sexo
    if altura < omenor:
      omenor = altura
    #Mulher
    if sexo == "f":
      sumaltura += altura
      qtdf += 1
    #Homem
    if sexo == "m":
      qtdm += 1
if qtdf > 0:      
  mediaf = sumaltura / qtdf
if sexmaior == "m":
  type = "MASCULINO"
else:
  type = "FEMININO"
print("A maior altura é:", omaior)
print("A menor altura é:", omenor)
if mediaf > 0:
  print("A média das mulheres é de:", mediaf)
print("São ", qtdm, "homem(s)")
print("A pessoa mais alta é do sexo:", type)