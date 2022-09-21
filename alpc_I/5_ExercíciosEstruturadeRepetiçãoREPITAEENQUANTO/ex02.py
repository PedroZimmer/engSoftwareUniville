times = 1
menordeidade = 0
mediacamp = 0
somaaltura = 0 
mediaaltura= 0
jogadores = 2
qtdpeso = 0
for times in range(1,times+1):
    print("Time", times)
    somaidade =  0
    for players in range(1,jogadores+1):
        print("Jogador", players)
        repetidade = True
        while repetidade:
            idade = int(input("Insira a idade...\n"))
            repetidade = True
            if idade >= 200: 
                print("Insira uma idade válida!")
            else:
                if idade < 18:
                    menordeidade += 1
                    repetidade = False
            media = somaidade / jogadores         
        peso = int(input("Insira o peso...\n"))
        if peso > 80:
            qtdpeso += 1
        altura = int(input("Insira a altura...(cm)"))
        somaaltura += altura
    mediaaltura = somaaltura / (times * jogadores)
    print("\nMédia idade:", media)
    mediacamp += media
    percpeso = (qtdpeso / (times * jogadores)) * 100
print("\n<-----------FIM------------>")        
print("Menores de 18:", menordeidade)
print("Média altura campeonato:", mediaaltura)
print("Porcetegem acima 80Kg", percpeso, "%")