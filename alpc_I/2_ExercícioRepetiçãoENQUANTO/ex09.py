#REPENQ9) Elaborar um programa que efetue o cálculo e no final apresente o somatório do número de grãos de trigo que se pode obter num tabuleiro de xadrez, obedecendo a seguinte regra: colocar um grão de trigo no primeiro quadro e nos quadros seguintes o dobro do quadro anterior. Ou seja, no primeiro quadro coloca-se 1 grão, no segundo quadro colocam-se 2 grãos (neste momento têm-se 3 grãos), no terceiro quadro colocam-se 4 grãos (tendo neste momento 7 grãos), no quarto quadro colocam-se 8 grãos (tendo-se então 15 grãos) até atingir o sexagésimo quarto quadrado.
soma = 0
contador = 1
start = 1
for total in range(1,61):
  contador *= 2
  soma += contador
  print(contador) 
print("A soma é de...", soma)