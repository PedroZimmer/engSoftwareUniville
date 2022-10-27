'''
4)	Faça uma função que receba cinco valores inteiros, e retorne o maior valor.
Faça uma segunda função que receba também cinco valores e retorne o menor deles.

'''
def funcao_menor(lista1):
    menor = lista1[0]
    for i in lista1:
        if i < menor:
            menor = i
    return(menor)

def funcao_maior(lista1):
    maior = lista1[0]
    for i in lista1:
        if i > maior:
            maior = i
    return(maior)

def criar_lista():
    lista1 = []    
    for i in range(5):
        lista1.append(int(input("Digite um numero: ")))
    return lista1
lista = criar_lista()
resposta = "Maior:", funcao_maior(lista), "Menor:", funcao_menor(lista)
print(resposta)