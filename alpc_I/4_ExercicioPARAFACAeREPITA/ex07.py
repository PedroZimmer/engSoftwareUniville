somaidade = 0
pontos = 0
canal4 = 0 
canal5 = 0
canal7 = 0
canal12 = 0
menoridade = 0
maioridade = 0
idlocalmaior = 0
idlocalmenor = 0
canalmenor = 0
canalmaior = 0
age = 0
regiao = 0
quantidadedefamilias = 10
for family in range(1,quantidadedefamilias+1):
  print("\n|--------------- <<FAMÍLIA", family,">> ---------------|") 
  repet = True
  while repet:    
    #CANAL
    canal = int(input("\nQual canal vocês mais assistem: 4, 5, 7 ou 12? "))
    repet = True
    if canal != 4 and canal != 5 and canal != 7 and canal != 12:
      print("Insira um dado válido!")
    else:      
      if canal == 4:
        canal4 += 1
      else:
        if canal == 5:
          canal5 += 1
        else:
          if canal == 7:
            canal7 +=1
          else:
            canal12 += 1
      repet = False
      print("\n|----------------- <<IDADE>> ------------------|")
      #PESSOAS DA CASA      
      numpessoas = int(input("\nInsira o número de pessoas da casa... "))
      somaidade = 0
      for idade in range(1,numpessoas+1):
        print("\nInsira a idade da pessoa", idade)
        age = int(input())
        somaidade += age
        mediaidade = somaidade / numpessoas     
      print("\n A média da idade da casa é:", mediaidade)      
      #REGIÃO
      repet2 = True
      while repet2:
        print("\n|----------------- <<REGIÃO>> ------------------|")
        regiao = str(input("\nInsira a sua região... \n\nN -> Norte | S -> Sul | L -> Leste | O -> Oeste "))
        repet2 = True
        if regiao != "n" and regiao != "s" and regiao != "l" and regiao != "o":    
          print("Insira uma região válida!")
        else:
          repet2 = False        
      #PONTOS
      if mediaidade <= 30:
        if regiao == "n" or regiao == "l":
          pontos += 20
        else:
          pontos += 35
      else:
        if mediaidade > 30 and mediaidade <= 50:
          if regiao == "n":
            pontos += 40
          else:
            if regiao == "s":
              pontos += 50
            else:
              pontos += 60    
        else:
          pontos += 30
    if family == 1:
      menoridade = age
      idlocalmenor = regiao
      canalmenor = canal  
    if age < menoridade:
      menoridade = age
      idlocalmenor = regiao
      canalmenor = canal
    if age > maioridade:
      maioridade = age    
      idlocalmaior = regiao
      canalmaior = canal
    mediapontos = pontos / quantidadedefamilias #Nº de FAMILIAS
    per4 = (canal4 / quantidadedefamilias) * 100
    per5 = (canal5 / quantidadedefamilias) * 100
    per7 = (canal7 / quantidadedefamilias) * 100
    per12 = (canal12 / quantidadedefamilias) * 100   
print("\n<----------------<<FIM>>-------------------->")   
print("\n\nMédia de pontos:", mediapontos)
print("\nCanal 4: ", per4, "%")
print("Canal 5: ", per5, "%")
print("Canal 7: ", per7, "%")
print("Canal 12: ", per12, "%")
print("\n<--------------------->\nMenor idade:", menoridade,"\nRegião: ", idlocalmenor, "\nCanal mais assistido:", canalmenor)
print("<--------------------->\nMaior idade:", maioridade,"\nRegião: ", idlocalmaior, "\nCanal mais assistido:", canalmaior,"\n<------------------------>")#TA FUNCIONANDO