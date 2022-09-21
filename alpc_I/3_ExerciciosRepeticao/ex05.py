for pares in range(1,6):
  print("Par...", pares)
  num1 = int(input("Digite o 1º número..."))
  num2 = int(input("Digite o 2º número..."))
  for cont in range(num1,num2+1):
    if cont %2 == 0:
      print(cont)