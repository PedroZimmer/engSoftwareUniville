
cont = 30
lista = [0]*30
for i in range(len(lista)):
    lista[i] = cont
    cont -= 1
print(lista)
for i in range(0,len(lista)-1):
    for j in range(i+1,len(lista)):
        #print(j)
        if lista[i] > lista[j]:
            auxi = lista[i]
            lista[i] = lista[j]
            lista[j] = auxi
print(lista)