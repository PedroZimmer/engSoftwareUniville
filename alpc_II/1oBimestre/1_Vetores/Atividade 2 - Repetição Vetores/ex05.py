qtdvendedor = 5 #QTD DE VENDEDORES
qtdpecas = []
valorpeca = []
totalpecas = 0
for i in range(1,qtdvendedor+1):
    print("Insira a quantidade de peças vendidas pelo vendendor", i,"...")
    qtdpecas.append(int(input()))
    print("Insira o valor da peça vendida...")
    valorpeca.append(int(input()))
    totalpecas += qtdpecas[i-1]
print("Total de peças vendidas:", totalpecas)
for j in range(1,qtdvendedor+1):
    valorvenda = qtdpecas[j-1] * valorpeca[j-1]
    print("O vendedor", j, "teve faturamento de", valorvenda,"$")