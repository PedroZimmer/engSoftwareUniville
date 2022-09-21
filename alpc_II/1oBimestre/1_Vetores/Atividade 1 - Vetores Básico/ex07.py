lista = [0] * 10
for i in range(10):
    lista[i] = int(input("Insira um valor...\n"))
print("Lista Normal:", lista)
lista2 = [0] * 10
for i in range(10):
    lista2[i] = lista[-i-1]
print("Lista invertida", lista2)