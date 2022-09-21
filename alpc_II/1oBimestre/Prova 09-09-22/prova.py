'''
cep = [2,2,1,4,5,6,7,8,456,10,11,12]
orca = [2,2,1,4,5,6,7,8,789,10,11,12]
status = [1,1,0,0,1,1,1,0,0,1,1,1]
'''
cep = []
orca = []
stat = []
for i in range(12):
    print("Cliente", i+1)
    print("Insira o CEP...")
    cep.append(int(input()))
    print("Insira o orçamento...")
    orca.append(int(input()))
    print("Insira o status... 1- SIM | 2 - NÃO")
    stat.append(int(input()))
menu = True
while menu:
    print("<<--{MENU}-->>")
    opcao = int(input("1-Listar atendimentos agendados...\n2-Calcular a soma dos orçamentos...\n3-CEP do orçamento mais caro e mais barato\n4-Sair\n"))
    if opcao == 1:
        for i in range(12):
            print("CEP:", cep[i], "Valor do orçamento:", orca[i])    
    somaorca =  0
    if opcao == 2:
        for i in range(12):
            if stat[i] == 1:
                somaorca += orca[i]
        print("Soma do dinheiro:", somaorca)
    maiororca = 0
    idmaiororca = 0
    menororca = orca[0]
    idmenororca = 0
    if opcao == 3:
        for i in range(12):
            if orca[i] > maiororca:
                maiororca = orca[i]
                idmaiororca = i
            if orca[i] < menororca:
                menororca = orca[i]
                idmenororca = i
        print("Maior orçamento:", maiororca,"CEP:", cep[idmaiororca])
        print("Menor orçamento:", menororca, "CEP:", cep[idmenororca])
    if opcao == 4:
        print("Até a próxima!")
        menu = False