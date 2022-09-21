numh = 0
somaaltura = 0
qtdm = 0
maior = 0
menor = 0
for pessoas in range(1,11):
    print("Pessoa", pessoas)
    altura = int(input("Insira a altura..."))
    repet = True
    while repet:
        sexo = str(input("Insira o sexo... (M ou F)"))
        if sexo != "f" and sexo != "m":
            print("N deu")
            repet = True
        else:
            repet = False
    if pessoas == 1:
        menor = altura
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura
        sexmaior = sexo
    if sexo == "m":
        numh += 1
    if sexo == "f":
        somaaltura += altura
        qtdm += 1
print("Maior altura:", maior)
print("Menor altura:", menor)
media = somaaltura / qtdm
print("Média", media)
print("Homens:", numh)
if sexmaior == "f":
    sexmaior = "Mulher"
else:
    sexmaior = "Homem"
print("A pessoa mais alta é:", sexmaior)