
'''
2)	Faça uma função que transforme e mostre segundos em horas, minutos e segundos. Todas as variáveis devem ser passadas como parâmetro, não havendo variáveis globais.
a.	1h = 3600s
b.	1m = 60s

'''

def funcao(valor:int):
    segemhoras = valor / 3600
    segemmin = valor / 60
    segemseg = valor / 1
    return(segemhoras,segemmin,segemseg)

valor = int(input("Insira os segundos..."))
segemhoras,segemmin,segemseg = funcao(valor)
print("Seg em hrs:", segemhoras,"\nSeg em min:", segemmin, "\nSeg em seg:", segemseg)