#REPETIÇÃO8) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final deve ser apresentados o maior e o menor número informado pelo usuário.

maior = 0
menor = 0
conta = 0

while True:
    print("Insira valores:")
    num = float(input())
    if num < 0:
      break
    else:
      if conta == 0:
        maior = num
        menor = num
      if num > maior:
        maior = num
      if num < menor:
        menor = num

      conta += 1

print("O maior valor é:", maior)
print("O menor valor é:", menor)