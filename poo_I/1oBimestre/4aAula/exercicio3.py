

print("Digite um numero para o pragama adivinhar:")
num = int(input())

numeros = [x for x in range(1,1001)]

esquerda = 0
direita = 0
for numeros in range(1,11):
    numeros = numeros / 2
    print("O numero é?", numeros)
    print("1 - Maior | 2 - Menor | 3 - Acertou")
    check = 1
    while check == 1:
        resposta = int(input())
        if resposta != 1 and resposta != 2 and resposta != 3:
            print("Digite uma opção valida")
        else:
            check = 0
    if resposta == 1:
        numeros = numeros / 2
    elif resposta == 2:
        numeros