somavista = 0
somaprazo = 0
somatotal = 0
numtransacoes = 15 #LEMBRAR DE TROCAR
for trans in range(1,numtransacoes+1):
    prest = 0
    i = True
    print("Insira o tipo da compra")
    while i:
        i - True
        type = str(input("V - A vista | P - A prazo ...\n"))
        if type != "v" and type != "p" and type != "V" and type != "P":
            print("Insira um tipo válido")
        else:
            i = False
    valor = float(input("Insira o valor da transação...\n"))
    if type == "v" or type =="V":
        somavista += valor
    if type == "p" or type =="P":
        somaprazo += valor
        prest = valor / 3
        print("Valor da 1a prestação é de", prest)
    somatotal += valor
print("\nTotal de compras a vista:", somavista)
print("Total de compras a prazo:", somaprazo)
print("Total de compras:", somatotal)