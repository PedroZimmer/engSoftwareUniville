#Faça um algoritmo que calcule a soma de todos os números ímpares dentro de uma faixa de valores determinada pelo usuário. Um número é ímpar quando sua divisão por 2 não é exata, ou seja, o resto resultante da divisão inteira pelo número 2 tem valor 1. Utilize a palavra resto como operador que calcula o resto da divisão de um numero por outro.

print("Digite 1º numero:")
num1 = int(input())

print("Digite 2º numero:")
num2 = int(input())

somaimpar = 0

for i in range(num1,num2+1):
  #print(i)
  if i % 2 == 1:
    somaimpar += i
print(somaimpar)