tipoespec = 0
tipocomum = 0
maiorpedido = 0
qtdproduto = 0
media = 0
somatotalqtd = 0
for clientes in range(1, 4):
    qtdtotalpedido = 0
    print("<---------Cliente", clientes, "--------->")
    #<--------------TIPO DO CLIENTE------------>
    repet = True
    while repet:
        typecliente = str(input("<---Tipo de Cliente---> \nE - Especial | C - Comum\n"))
        repet = True
        if typecliente != "e" and typecliente != "c":
            print("Insira um tipo válido!")    
        else:
            if typecliente == "e":
                tipoespec += 1
            else:
                tipocomum += 1
            repet = False
    #<----------------TIPO DO PRODUTO--------------->
    precototal = 0
    confirmarproduto = "s"
    while confirmarproduto == "s":
        print("<--------Produto-------->")
        print("Escolha um tipo do produto: ") 
        repet2 = True
        while repet2:
            typeproduto = int(input("1 2 ou 3\n"))
            repet2 = True
            if typeproduto != 1 and typeproduto != 2 and typeproduto != 3:
                print("Insira um produto válido!")
            else:
                #QUANTIDADE PRODUTO
                print("Insira a quantidade do produto:")
                qtdproduto = int(input()) #QUANTIDADE DE PRODUTOS
                qtdtotalpedido += qtdproduto #TOTAL (PRA FAZER MÉDIA)
                somatotalqtd += qtdproduto #TOTAL
                if typeproduto == 1:
                    preco = qtdproduto * 3
                else:
                    if typeproduto == 2:
                        preco = qtdproduto * 9
                    else:
                        preco = qtdproduto * 10
                precototal += preco
                #OUTRO PRODUTO?
                if qtdtotalpedido > maiorpedido:
                    maiorpedido = qtdtotalpedido
                    clientemaior = clientes
                print("Você quer outro produto? S - Sim | <Qualquer> - Não")
                #confirmar = True
                #while confirmar:
                confirmarproduto = str(input())
                    #confirmar = True
                if confirmarproduto == "s":
                    #confirmar = False
                    print("OK! Insira o produto novo:")
                    repet2 = True   
                else:
                    repet2 = False
            media = qtdtotalpedido / 3
    print("Insira a comissão...(em %")
    comissao = int(input())
    print("Total do pedido: R$", precototal)
    precocomi = precototal * (comissao / 100)
    print("A comissão será de:", precocomi)
print("<-----------------FIM-------------------->\nEspeciais:", tipoespec)
print("Comuns:", tipocomum)
print("O cliente", clientemaior, "fez o maior pedido:", maiorpedido)
print("Média da quantidade dos pedidos:", media)
print("TOTAL de pedidos:", somatotalqtd)