maior = 0
menor = 0
maiorcity = 0
menorcity = 0
contcars = 0
contacid = 0
citymenos = 0
cidade = 0
list = ["Guaramirim",'Jaraguá do Sul','Joinville','Massaranduba','Schoereder']
for city in list:
  #cidade = str(input("Insira a cidade..."))
  print(city)
  ncars = int(input("Insira o Nº de veículos..."))
  nacid = int(input("Insira o Nº de acidentes..."))
  if city == "Guaramirim":  
    menor = nacid
  if nacid < menor:
    menor = nacid
    menorcity = city
  if nacid > maior:
    maior = nacid
    maiorcity = city
  if ncars < 2000:
    contacid += nacid
    citymenos += 1
  contcars += ncars
media = contcars / 5
media2 = contacid / citymenos
print(menorcity,"tem o menor índice de acidentes, com", menor, "acidentes")
print(maiorcity,"tem o maior índice de acidentes, com", maior, "acidentes")
print("A média de veículos é de", media)
print("A média do número de acidentes em cidades com menos de 2000 veículos é de", media2)