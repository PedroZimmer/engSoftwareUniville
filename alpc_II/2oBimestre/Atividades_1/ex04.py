'''
4)	Faça uma função que receba cinco valores inteiros, e retorne o maior valor.
Faça uma segunda função que receba também cinco valores e retorne o menor deles.

'''
lista1 = []
def funcaomaior(lista1):
    menor = lista1[0]
    maior = lista1[0]
    for i in lista1:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    return(maior,menor)

for i in range(5):
    print("Insira o numero:", i+1)
    lista1.append(int(input()))
maior,menor = funcaomaior(lista1)
print("maior:", maior, "menor:", menor)