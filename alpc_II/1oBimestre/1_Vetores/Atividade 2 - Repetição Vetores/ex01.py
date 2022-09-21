
'''
lista1 = [0] * 10
lista2 = [0] * 10
lista3 = [0] * 20
for i in range(10):
    lista1[i] = i
    lista2[i] = i * 10
cont = 0
for i in range(10):
    lista3[i + cont] = lista1[i]
    cont += 1
    lista3[i + cont] = lista2[i]
print(lista3)
'''

lista1 = [1,3,5,7,9,11,13,15,17,19]
lista2 = [2,4,6,8,10,12,14,16,18,20]
lista3 = []
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)