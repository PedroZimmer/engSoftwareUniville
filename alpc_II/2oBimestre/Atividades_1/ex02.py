
'''
2)	Faça uma função que transforme e mostre segundos em horas, minutos e segundos.
Todas as variáveis devem ser passadas como parâmetro, não havendo variáveis globais.
a.	1h = 3600s
b.	1m = 60s

'''

def funcao(valor:int):
    horas = seg_emhoras(valor)
    minutos = seg_emmin(valor)
    segundos = seg_emseg(valor)
    return [horas,minutos,segundos]
    
def seg_emhoras(valor:int):
    return valor / 3600

def seg_emmin(valor:int):
    return valor / 60

def seg_emseg(valor:int):
    return valor / 1

valor = int(input("Insira os segundos..."))
segemhoras,segemmin,segemseg = funcao(valor)
print("Seg em hrs:", segemhoras,"\nSeg em min:", segemmin, "\nSeg em seg:", segemseg)