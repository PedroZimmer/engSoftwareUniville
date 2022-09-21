cont = 1
lista = [0]*10000000
for i in range(len(lista)):
    lista[i] = cont
    cont += 1
valproc = int(input("Insira o valor procurado..\n"))
cont = 0
for i in range(len(lista)):
    if valproc == lista[i]:
        print("Valor foi encontrado!")
    else:
        cont += 1
    if cont == len(lista):
        print("Valor não encontrado!")