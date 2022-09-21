lista = [0] * 10
contpar = 0
contimpar = 0
for nums in range(10):
    print("Insira um número...")
    lista[nums] = int(input())
    if lista[nums] % 2 == 0:
        contpar += 1
    if lista[nums] % 2 != 0:
        contimpar += 1
listapar = [0] * contpar
prox1 =0
for i in range(10):
    if lista[i] % 2 == 0:
        listapar[prox1] = lista[i]
        prox1 += 1
listaimpar = [0] * contimpar
prox2 = 0
for i in range(10):
    if lista[i] % 2 != 0:
        listaimpar[prox2] = lista[i]
        prox2 += 1
print(lista)
print("Pares:", contpar)
print(listapar)
print("Impar:", contimpar)
print(listaimpar)