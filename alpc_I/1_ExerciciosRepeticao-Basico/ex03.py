#REPETIÇÃO3) Faça um programa que leia um valor N inteiro e positivo. Calcule e mostre o valor de E, conforme a fórmula a seguir: 

#E = 1 + 1/(1!) + 1/(2!) + 1/(3!) + ... + 1/(N!)



ene = 0
ee = 1

print("Insira qualquer numero inteiro positivo:")
ene = int(input())

for i in range(1,ene+1):
  print(i, end=" ")
  fat = 1
  for j in range(i,0,-1):
    #print(" ", j, end="")
    fat = fat * j
  print("! = ", fat)
  ee = ee + (1 / fat)
print("Resultado:", ee)
      

print("Fim")