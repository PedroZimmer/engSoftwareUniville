maior = 0
menor = 0
conta = 0
soma = 0
cont = 0
resto = 0
par = 0
somapar = 0
contpar = 0
contimpar = 0
while True:
    print("Insira valores:")
    num = int(input())
    if num == 30000:
      break
    else:
      soma = soma + num
      cont = cont + 1
      média = soma / cont
      if conta == 0:
        maior = num
        menor = num
      if num > maior:
        maior = num
      if num < menor:
        menor = num
      conta += 1
      if num %2 == 0:
        contpar = contpar + 1
        somapar = somapar + num
        mediapar = somapar / contpar
      if num %2 != 0:
        contimpar = contimpar + 1
        percentimpar = (contimpar / cont) * 100
              
print("Quantidade de par:", contpar)
print("Soma de par:", somapar)
print("Soma:", soma)
print("Quantidade:", cont)
print("Maior:", maior)
print("Menor:", menor)
print("Média dos pares:", mediapar)
print("Percentual impar:", percentimpar)