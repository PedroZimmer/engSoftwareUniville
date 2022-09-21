

lista1 = [0] * 10
soma = 0
for i in range(10):
    print("Insira um número...")
    lista1[i] = int(input())
    soma += lista1[i]
print(lista1)
print("Soma:",soma)
media = soma / 10
print("Média:", media)