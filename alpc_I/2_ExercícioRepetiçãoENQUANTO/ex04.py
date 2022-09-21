#REPENQ4) Faça um programa que apresente os resultados de uma tabuada de um número qualquer, a qual deve ser impressa no seguinte formato: Considerando como exemplo o fornecimento do número 2 para o número qualquer, ter-se-ia a seguinte situação:


print("Insira o número...")
num = int(input())
tabu = 0
while (tabu < 11):
  print ("1 x", tabu ,"=", num * tabu)
  tabu += 1
#else:
 # print("Aqui está a tabuada do", num,"!")