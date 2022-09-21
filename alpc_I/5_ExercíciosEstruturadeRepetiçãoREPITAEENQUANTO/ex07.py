valoravista = 0
valor = 0
perc = 3
valorparcela = 0
valor = int(input("Insira o valor do veículo...\n"))
print("\tParcelas\tPorcentagem\tValor Parcela\tTotal")
for parcelas in range(6,61,6):
    valornovo = (valor * perc/100) + valor
    valorparcela = valornovo / parcelas
    print("\t|",parcelas,"\t|","\t|", perc,"%\t|","\t|",round(valorparcela,1),"|\t|",valornovo,"|")
    perc += 3
avista = valor - (valor*0.2)
print("\n\t|---------O valor a vista fica:", avista,"---------|")


