#REPETIÇÃO4) Faça um programa que leia um número N que indica quantos valores inteiros e positivos devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial desse valor.

print("Digite um numero")
num = int(input())

for i in range(1,num+1):
  print(i,"! = ", end="")
  fat = 1
  for j in range(i,0,-1):
    print(j," x ", end="")
    fat = fat * j
  print("= ", fat)
  