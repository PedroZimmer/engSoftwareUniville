import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
#Aqui você deve imprimir todo o conteúdo da variável memória


while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        #Aqui você deve implementar o algoritmo de primeira escolha
        pass
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            pass
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                pass
    # Aqui você deve imprimir todo o conteúdo da variável memória
