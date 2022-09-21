matriz = [[" "] * 3 for i in range(3)]
jogador = ['X','O']
print("<<<Jogo da Velha>>>")
jogo = True
while jogo:
    for b in range(2):
        for lin in range(3):
            for col in range(3):
                if col < 2:
                    print(matriz[lin][col], end="|")
                else:
                    print(matriz[lin][col], end="")
            print()   
        print('Insira a posição! Jogador',jogador[b])
        repet = True
        while repet:
            ondelin = int(input("Linha:"))
            ondecol = int(input("Coluna:"))
            if matriz[ondelin-1][ondecol-1] == " ":
                matriz[ondelin-1][ondecol-1] = jogador[b]
                repet = False
            else:
                print("Esta preenchido! Tente outra casa!")
                repet = True
        