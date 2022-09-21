


lista = [0] * 10

for i in range(10):
    lista[i] = int(input("Insira um número...\n"))
print("Lista Normal:\n", lista)
multi = int(input("Insira um multiplicador...\n"))
lista2 = lista
for i in range(10):
    lista2[i] = lista[i] * multi
print("Lista multiplicada:\n", lista2)