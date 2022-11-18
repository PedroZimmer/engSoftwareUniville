import random

cabecinha = [' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x']
opcao = 0
tamanho = 0
letra = ''

'''
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
'''

#Aqui você deve imprimir todo o conteúdo da variável memória

def imprimir(cabecinha):
    for i in range(0,20):
        print(cabecinha[i],end="|")
    print()
    for i in range(20,40):
        print(cabecinha[i],end="|")
    print()
    for i in range(40,60):
        print(cabecinha[i],end="|")
    print()
    for i in range(60,80):
        print(cabecinha[i],end="|")
    print()
    for i in range(80,100):
        print(cabecinha[i],end="|")
    print()
    
    
while True:
    #Menu do programa
    print("1 - Primeira Escolha\n2 - Melhor Escolha\n3 - Pior Escolha\n4 - Sair\n5 - Imprimir")
    opcao = int(input("Escolha o algoritmo pelo numero\n"))
    if opcao == 4:
        print("Saindo...")
    if opcao == 5:
        imprimir(cabecinha)
    tamanho = int(input('Digite o tamanho da informacao\n'))
    letra = input('Digite a letra a ser utiliada\n')
    
    if(opcao == 1): #Primeira Escolha
        i=0
        while i < 100:
            if cabecinha[i] == " ":
                ini = i 
                j=ini+1
                while j < 100:
                    
                    if cabecinha[j] != " ":
                        fim = j
                        break
                    j += 1
                if (fim-ini) >= tamanho:
                    for cont in range(ini,ini+tamanho):
                        cabecinha[cont] = letra
                    break
                else:
                    print('Tente uma informação menor, esta não cabe em lugar nenhum!')
                    break
            i += 1

    if (opcao == 2): #Melhor Escolha
        melhor_espaco = 0
        omenor = len(cabecinha)
        i=0
        while i < 100:
            espaco = 0
            if cabecinha[i] == " ":
                inicio = i
                j = inicio + 1
                
                while j < 100:
                    if cabecinha[j] != " ":
                        fim = j
                        espaco = fim - inicio
                        
                        if espaco >= tamanho and espaco < omenor:
                            melhor_espaco = espaco
                            pos_melhor_ini = i
                            pos_melhor_fim = j
                            
                            if melhor_espaco < omenor:
                                omenor = melhor_espaco
                                omenor_ini = i
                                omenor_fim = j
                                i = j
                                break
                        else:
                            break          
                    j += 1         
            i += 1
            
            
        print("Melhor espaço: ", melhor_espaco)
        print("Posição do melhor espaço: ", omenor_ini, omenor_fim)
        #if melhor_espaco >= tamanho:
        for cont in range(0,tamanho):
            cabecinha[omenor_ini+cont] = letra


    if (opcao == 3): #Pior Escolha
        i=0
        maior_espaco = 0
        while i < 100:
            if cabecinha[i] == " ":
                ini = i
                j = ini + 1
                
                while j < 100:
                    if cabecinha[j] != " ":
                        fim = j
                        espaco = fim - ini
                        
                        if espaco > maior_espaco:
                            maior_espaco = espaco
                            pos_maior_ini = i
                            pos_maior_fim = j
                        break
                    j += 1

            i += 1
        print("Maior espaço: ", maior_espaco)
        print("Posição do maior espaço: ", pos_maior_ini, pos_maior_fim) 
        if maior_espaco >= tamanho:
            for cont in range(tamanho):
                cabecinha[pos_maior_ini+cont] = letra
            imprimir(cabecinha)
        else:
            print('Tente uma informação menor, esta não cabe em lugar nenhum!')