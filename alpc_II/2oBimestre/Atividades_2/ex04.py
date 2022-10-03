'''
4.	Um determinado estabelecimento fará uma venda com descontos nos produtos A e B.
Se forem comprados apenas os produtos A ou apenas os produtos B, o desconto será de 10%.
Caso sejam comprados os produtos A e B, o desconto será de 15%.
O custo da unidade de cada produto é dado respectivamente para os produtos A e B como sendo de R$ 10 e R$ 20.
Elaborar um programa que por meio de sub-rotina calcule e apresente o valor da despesa do freguês na compra dos produtos. 
Lembre-se que o freguês poderá levar mais de uma unidade de um determinado produto. 
'''


def funcao():
    
    produto = []	
    qtdproduto = []
    
    
    menus = True
    while menus:
        produto.append(str(input('Digite o produto: ').upper()))
        if produto[0] != "A" and produto[0] != "B":
            print('Produto inválido')
            produto.pop()
        menus = input('Deseja adicionar outro? [S/N] ').upper()
        if menus == 'S':
            if len(produto) < 2:
                if produto.count('A') == 0 and produto.count('B') == 0:
                    print("Você não comprou nenhum produto!")
                    menus = True
            else:
                print("Você só pode comprar 2 produtos!")
                menus = False
        else:
            print("Você comprou os produtos: ", produto)
            menus = False
    
    for i in range(len(produto)):
        print("Quantidade de", produto[i], ":")
        qtdproduto.append(int(input()))
        
    if len(produto) == 1:
        if produto.count('A') == 1:
            print("Você comprou",qtdproduto[0]," do produto A, o valor total é: R$", (qtdproduto[0]*10)*0.9)
        else:
            print("Você comprou",qtdproduto[0]," do produto B, o valor total é: R$", (qtdproduto[0]*20)*0.9)
    else:
        print("Você comprou",qtdproduto[0]," do produto",produto[0],"e",qtdproduto[1]," do produto",produto[1], "o valor total é: R$", (qtdproduto[0]*10 + qtdproduto[1]*20)*0.85)
            
funcao()