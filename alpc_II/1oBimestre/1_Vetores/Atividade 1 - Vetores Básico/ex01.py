lista = [0] * 10
cont = 0
for nums in range(3):
    print("Insira um número")
    lista[nums] = int(input())
    if lista[nums] > 10:
        cont += 1
lista2 = [0] * cont
proximolivre = 0
for i in range(10):
    if lista[i] > 10:   
        lista2[proximolivre] = lista[i]
        proximolivre += 1
print(lista)
print(lista2)