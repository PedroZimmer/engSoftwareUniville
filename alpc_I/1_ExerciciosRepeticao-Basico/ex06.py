#print("Insira 10 valores:")
#numero = input()
#for i in numero.split(" "):

num = 0
soma = 0

for i in range(10):
  print("Insira 10 números:")
  num = int(input())
  soma += num
  media = soma / 10

print("Total:",soma)
print("Média:", media)