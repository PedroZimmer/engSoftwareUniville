maior = 0
qtd1 = 0
qtd2 = 0
for linha in range(1,4):
    print("Linha", linha)
    somaturno = 0
    for turno in range(1,3):
        print("Turno", turno)
        code = int(input("Código do produto <1, 2 ou 3>\n"))
        qtd = int(input("Quantidade produzida...\n"))
        refu = int(input("Quantidade refugada...\n"))
        somaturno += qtd
        if turno == 1:
            qtd1 += refu
        else:
            qtd2 += refu
        if code == 2:
            if refu <= 100:
                print("normal")
            else:
                print('irregular')
        else:
            if refu < 50:
                print('normal')
            else:
                print('irregular')
        if somaturno > maior:
            maior = somaturno
            maiorlinha = linha
print("A linha que mais produziu foi a", maiorlinha)
print("Refugadas turno 1:", qtd1)
print("Refugadas turno 2:", qtd2)