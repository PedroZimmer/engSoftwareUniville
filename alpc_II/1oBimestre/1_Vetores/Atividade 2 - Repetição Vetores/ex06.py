
qtdcontas = 4 #QUANTIDADE DE CONTAS
numconta = []
saldo = []
cont3 = 0




for i in range(qtdcontas):
    print("Insira o número da conta...")
    vernumconta = (int(input()))
    if i != 0:
        for j in range(len(numconta)):
            if numconta[i] == numconta[j]:
                if i != j:
                    cont3 += 1
                    if cont3 == qtdcontas:
                        print("Insira uma conta não repetida...")
            else:
                pass
    
    



'''
for i in range(qtdcontas):
    repetcontas = True
    while repetcontas:
        print("Insira o número da conta...")
        numconta.append(int(input()))
        compararconta = numconta[i]
        if i == 0:
            repetcontas = False
            pass
        else:
            comparar = True
            while comparar:
                for j in range(len(numconta)):
                    if compararconta == numconta[j]:
                        print("Digite um número de conta não duplicada!")
                        cont3 += 1
                        numconta.pop()
                        repetcontas = True
                        comparar = False
                    else:
                        if cont3 == qtdcontas:
                            repetcontas = False
    print("Insira o saldo da conta", numconta[i])
    saldo.append(float(input()))
'''




'''
repetmenu = True    
while repetmenu:
    print("<-----{MENU}----->")
    repet = True
    print("<---Digite uma ação--->")
    while repet:
        acao = int(input("1.Depósito\n2.Saque\n3.Consultar Ativo Bancário\n4.Encerrar\n"))
        if acao != 1 and acao != 2 and acao != 3 and acao != 4:
            print("Insira um valor correto...")
            repet = True
        else:
            repet = False
    #DEPOSITOOOOO
    cont2 = 0
    if acao == 1:
        codconta = int(input("Insira o código da conta..."))
        for i in range(qtdcontas+1):
            if codconta == numconta[i]:
                valordeposito = int(input("Insira o valor a ser depositado..."))
                saldo[i] += valordeposito
                print("Valor saldo atualizado: R$", saldo[i],"\n")
                break
            else:
                cont2 += 1
                if cont2 == qtdcontas:
                    print("Insira uma conta existente...")
                    repetmenu = True
    #SAQUEEEEE
    if acao == 2:
        codconta = int(input("Insira o código da conta..."))
        for i in range(qtdcontas+1):
            if codconta != numconta[i]:
                repetmenu = True
            else:
                valorsaque = int(input("Insira o valor a ser sacado..."))
                if saldo[i] < valorsaque:
                    print("Saldo insuficiente para saque! Saldo disponivel: R$", saldo[i])
                else:
                    saldo[i] -= valorsaque
                    print("Valor saldo atualizado: R$", saldo[i],"\n")
    #ATIVO_BANCARIOOOOOOOO
    if acao == 3:
        ativo = 0
        for i in range(qtdcontas+1):
            ativo += saldo[i]
        print("Ativo bancário: R$", ativo)
    #ENCERRARRRRR
    if acao == 4:
        print("Até breve!")
        repetmenu = False
'''