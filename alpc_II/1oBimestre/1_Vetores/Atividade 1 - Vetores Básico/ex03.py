lista1 = [0] * 10
for num in range(10):
    print("Insira um número...")
    lista1[num] = int(input())
print(lista1)
lista2 = lista1
for i in range(10):
    if lista1[i] < 10:
        lista1[i] = 0
print(lista2)