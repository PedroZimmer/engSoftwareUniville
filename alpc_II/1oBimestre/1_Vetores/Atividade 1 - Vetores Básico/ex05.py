

lista = [0] * 10
maior = 0
for i in range(10):
    
    lista[i] = int(input("Insira um valor..."))
    if i == 0:
        menor = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
print(lista)
print("Maior", maior, "Menor:", menor)