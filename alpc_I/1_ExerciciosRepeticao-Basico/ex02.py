#REPETIÇÃO2) Elabore um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.


soma = 1
total = 0


while soma <= 500:
  if soma % 2 == 0:
    print(soma)
    total = total + soma
  soma += 1
  

print("A soma é:", total)



total = 0


while soma <= 500:
  print(soma)
  total = total + soma
  soma += 2
  

print("A soma é:", total)
