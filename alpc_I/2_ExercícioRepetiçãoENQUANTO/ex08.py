print("Atividade Número 8")
print("<Para finalizar o programe digite 0>")
print("\n")
num = 1
vezes = 2
while num > 0:
  print("Insira um número...")
  num = int(input())  
  for number in range(1,5):
    num *= vezes
    print(num)
  vezes += 1