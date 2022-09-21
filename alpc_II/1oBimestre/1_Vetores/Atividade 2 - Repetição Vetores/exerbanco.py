opcao = 0
listacontas = [0] * 10
listasaldos = [0] * 10

for i in range(10):
    repete = True
    while repete:
        print("Digite o numero da conta")
        numconta = int(input())
        j=0
        while j < 10:
            if listacontas[j] == numconta:
                print("Conta Duplicada")
                repete = True
                break
            j += 1
        if j == 10:
            repete = False
            listacontas[i] = numconta
            print("Digite o saldo")
            listasaldos[i] = float(input())


## CADASTRO DAS CONTAS
while(opcao !=4):
    print("Sistema Bancário")
    print("1. Efetuar depósito")
    print("2. Efetuar saque")
    print("3. Consultar ativos")
    print("4. Finalizar")
    print("Digite o número da opção desejada\n")
    print()
    opcao = int(input())
    if opcao == 1:
        print("Deposito")
        #pedir o numero da conta
        print("Digite o numero da conta")
        numcontadep = int(input())
        achei = False
        for i in range(10):
            if listacontas[i] == numcontadep:
                achei = True
                print("Digite o valor do deposito")
                valdep = float(input())
                if valdep > 0:
                    listasaldos[i] += valdep
                    print("Deposito realizado - Saldo: ", listasaldos[i])
        if not achei:
            print("Conta inválida")

        #procurar na lista de contas o numero da conta digitado
        #caso encontrar, utilizar a posição onde foi encontrado
        #para atribuir o novo saldo (tem que pedir antes o valor do deposito)
        #caso contrário apresentar mensagem de erro do numero da conta

    if opcao == 2:
        print("Saque")
        print("Digite o número da conta")
        numcontasaq = int(input())
        achei = False
        for i in range(10):
            if listacontas[i] == numcontasaq:
                achei = True
                print("Digite o valor do saque")
                valsaque = float(input())
                if valsaque > listasaldos[i]:
                    print("Saldo insuficiente...")
                else:
                    listasaldos[i] -= valsaque
                    print("Saque realizado - SALDO: ",listasaldos[i])
        if not achei:
            print("Número da conta inválido")

    if opcao == 3:
        soma = 0
        omaiorvalor = listasaldos[0]
        numcontamaior = listacontas[0]
        omenorvalor = listasaldos[0]
        numcontamenor = listacontas[0]
        contasaldozero = 0
        for i in range(10):
            print("Numero> ", listacontas[i], " SALDO> ", listasaldos[i])
            soma += listasaldos[i]
            
            if omaiorvalor < listasaldos[i]:
                omaiorvalor = listasaldos[i]
                numcontamaior = listacontas[i]
            #NUNCA MISTURAR A LOGICA DO MAIOR COM A DO MENOR
            if omenorvalor > listasaldos[i]:
                omenorvalor = listasaldos[i]
                numcontamenor = listacontas[i]
            #NAO MISTURAR
            if listasaldos[i] == 0:
                contasaldozero += 1
        print("O total do banco e ", soma)
        print("A maior conta e ", numcontamaior, " com o saldo ", omaiorvalor)
        print("A menor conta e ", numcontamenor, " com o saldo ", omenorvalor)
        print("A qtd de contas com saldo zerado e ", contasaldozero)

print("Até logo obrigado!")