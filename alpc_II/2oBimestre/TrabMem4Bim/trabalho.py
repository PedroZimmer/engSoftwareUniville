import random
from tracemalloc import start

# PRIMEIRA ESCOLHA
def primeiraescolha(tamanho, letra, memoria, testememoria):
    vazios = []
    colocarmemoria = []
    for i in range(100):
        if memoria[i] == ' ': #SE A POSIÇÃO DA MEMÓRIA FOR VAZIA
            vazios.append(i) #ADICIONA A POSIÇÃO DA MEMÓRIA LIVRE NA LISTA
            if tamanho == 1: #SE O TAMANHO FOR 1
                memoria[vazios[0]] = letra #COLOCA A LETRA NA PRIMEIRA POSIÇÃO
            else:
                if i != 0: #SE A POSIÇÃO DA MEMÓRIA FOR DIFERENTE DE 0
                    if len(vazios) == tamanho: #SE O TAMANHO DA LISTA FOR IGUAL AO TAMANHO
                        for j in range(len(vazios)-1): #PERCORRE A LISTA
                            if vazios[j] - vazios[j+1] == -1: #SE A POSIÇÃO DA LISTA FOR SEGUIDA
                                colocarmemoria.append(vazios[j]) #ADICIONA A POSIÇÃO DA MEMÓRIA LIVRE NA LISTA
                                colocarmemoria.append(vazios[j+1]) #ADICIONA A POSIÇÃO DA MEMÓRIA LIVRE NA LISTA
                                if tamanho > 2:
                                    if j >= 1:
                                        del(colocarmemoria[j]) #Deleta o elemento repetido
                            else:
                                colocarmemoria = [] #LIMPA A LISTA
                                del(vazios[0]) #Deleta o elemento q n presta kkk
                                i -= 1 #Faz com que a posição da memória volte uma posição
                                break
                            if len(colocarmemoria) == tamanho:
                                for k in colocarmemoria:
                                    memoria[k] = letra
                    else:
                        pass
    if memoria == testememoria:
        print("\nNão foi possível alocar a memória")
    else:
        print("\nMemória alocada com sucesso")
        return memoria


#MELHOR ESCOLHA
def melhorescolha(tamanho, letra, memoria, testememoria):
    vazios = []
    matrizmemoria = [[]]
    cont = 0
    for i in range(100):
        if memoria[i] == ' ':
            vazios.append(i)
    #COLOCANDO NA MATRIZ 
    for j in range(len(vazios)-1):
        if vazios[j] - vazios[j+1] == -1:
            matrizmemoria[cont].append(vazios[j]) #
        else:
            matrizmemoria[cont].append(vazios[j]) 
            matrizmemoria.append([]) #CRIA UMA NOVA LINHA 
            cont += 1
    print(matrizmemoria)
    achou = False
    for k in range(len(matrizmemoria)):
        if achou == False:
            if len(matrizmemoria[k]) >= tamanho:
                omelhor = matrizmemoria[k]
                achou = True
        else:      
            if len(matrizmemoria[k]) >= tamanho:
                if len(matrizmemoria[k]) < len(omelhor):
                    omelhor = matrizmemoria[k]
    for l in omelhor:
        memoria[l] = letra
    if memoria == testememoria:
        print("\nNão foi possível alocar a memória")
    else:
        print("\nMemória alocada com sucesso")
        return memoria
        
#PIOR ESCOLHA
def piorescolha(tamanho, letra, memoria, testememoria):
    vazios = []
    matrizmemoria = [[]]
    cont = 0
    for i in range(100): 
        if memoria[i] == ' ':
            vazios.append(i)
    #COLOCANDO NA MATRIZ
    for j in range(len(vazios)-1):
        if vazios[j] - vazios[j+1] == -1:
            matrizmemoria[cont].append(vazios[j])
        else:
            matrizmemoria[cont].append(vazios[j]) 
            matrizmemoria.append([]) #CRIA UMA NOVA LINHA 
            cont += 1
    print(matrizmemoria)
    achou = False
    for k in range(len(matrizmemoria)):
        if achou == False:
            if len(matrizmemoria[k]) >= tamanho:
                opior = matrizmemoria[k]
                achou = True
        else:
            if len(matrizmemoria[k]) >= tamanho:
                if len(matrizmemoria[k]) > len(opior):
                    opior = matrizmemoria[k]
    for l in range(tamanho):
        memoria[opior[l]] = letra
    if memoria == testememoria:
        print("\nNão foi possível alocar a memória")
    else:
        print("\nMemória alocada com sucesso")
        return memoria
        

# ENTRADA DE DADOS
def entradas():
    tamanho = int(input("Tamanho: "))
    letra = input("Letra: ")
    return tamanho, letra


# IMPRIMIR MEMORIA
def imprimememoria():
    for i in range(100):
        if i % 20 == 0:  # QUEBRA A CADA 20 POSIÇÕES
            print("\n")
        print(memoria[i], end='|')


# INICIALIZAR MEMORIA
'''
memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0, 11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
'''
memoria =  ['x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ']
opcao = 0
tamanho = 0
letra = ''	



# MENU
while True:
    print("\n1 - Primeira Escolha\n2 - Melhor Escolha\n3 - Pior Escolha\n4 - Imprimir Memória\n5 - Sair")
    opcao = int(input(("\nOq deseja fazer? ")))  # OPÇÃO DO MENU

    if opcao == 5:
        print("Saindo...")
        break
    # IMPRIMIR A MEMÓRIA
    if opcao == 4:
        imprimememoria()
    if opcao != 4 and opcao != 5:
        # PRIMEIRA ESCOLA
        if(opcao == 1):
            tamanho, letra = entradas()  # ENTRADA DE DADOS
            #print("Memória antes da alocação: ", memoria)
            testememoria = memoria.copy() #CÓPIA DA MEMÓRIA
            primeiraescolha(tamanho, letra, memoria,testememoria)  # CHAMADA DA FUNÇÃO
            # print(resprimeiarescolha)
            pass
        else:
            # MELHOR ESCOLHA
            if (opcao == 2):
                tamanho, letra = entradas()  #ENTRADA DE DADOS
                testememoria = memoria.copy() #CÓPIA DA MEMÓRIA
                melhorescolha(tamanho, letra, memoria, testememoria)
            else:
                if(opcao == 3):
                    tamanho, letra = entradas()  #ENTRADA DE DADOS
                    testememoria = memoria.copy() #CÓPIA DA MEMÓRIA
                    piorescolha(tamanho, letra, memoria, testememoria)        
                else:
                    print("Opção inválida")