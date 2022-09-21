#REPETIÇÃO7) Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final o total do somatório, a média e o total de valores lidos. O programa deve fazer as leituras dos valores enquanto o usuário estiver fornecedor valores positivos. Ou seja, o programa deve parar quando o usuário fornecer um valor negativo.



media = 0
total = 0
soma = 0
cont = 0


while True:
    print("Insira valores:")
    i = int(input())
    soma = soma + i
    cont = cont + 1
    if i < 0:
      break
  
media = soma / 2

print("Média", media)
print("Total:",soma)
print("Qtd de valores:",cont-1)