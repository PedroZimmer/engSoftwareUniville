import random
from tracemalloc import start
        
def primeira_escolha(tamanho,letra, memoria, testememoria): # PRIMEIRA ESCOLHA
    listavazios = []
    for i in range(100):
        #aqui se o tamanho for 1 ele vai alocar a primeira posição vazia
        if memoria[i] == ' ':
            if tamanho == 1:
                memoria[i] = letra
                finalizar(memoria, testememoria) # FINALIZA O ALGORITIMO PARA TAMANHO 1
            else:
                if i < 99: # VERIFICA SE O TAMANHO É SUFICIENTE
                    #vai ver se a casa esta vazia
                    if memoria[i+1] == ' ':
                        #vai ver até quantas casas vazias tem
                        if listavazios == []:
                            listavazios.append(i)
                        listavazios.append(i+1)
                    else:
                        listavazios.clear()
                #se o tamanho atingir o necessario para alocar ele vai alocar a memoria
                if tamanho == len(listavazios):
                    for j in range(tamanho):
                        memoria[listavazios[j]] = letra
                    #finalizar(memoria, testememoria) #chama a funcao q testa a memoria e mostra uma mensagem 
                    #break
    finalizar(memoria, testememoria) #isso é caso n tenha conseguido alocar a memoria
    
def pior_melhor_escolha(tamanho, letra, memoria, testememoria, opcao): # PIOR ESCOLHA e MELHOR ESCOLHA
    listavazios = []
    asposicoes = []
    cont = 1
    for i in range(100):
        if memoria[i] == ' ': #ve se a posicao ta vazia, em seguinte se a lista dos vazios estive vazia ele vai adicionar a posicao
            if listavazios == []:
                listavazios.append(i)   
            if i < 99: #verifica se a posicao é a ultima, se nao for ele vai ver se a proxima posicao esta vazia, no caso n tem posicao 100
                if memoria[i+1] == ' ': #se a proxima posicao estiver vazia ele vai adicionar a lista dos vazios
                    listavazios.append(i+1)
                else:
                    if len(listavazios) >= tamanho: #se a lista dos espaços vazios foir >= ele vai pra proxima etapa
                        if cont == 1:
                            asposicoes = listavazios.copy() #isso é pra ter uma base para o algoritimo de menor espaco
                            cont = 0
                        if opcao == 3: # PIOR ESCOLHA
                            if len(asposicoes) < len(listavazios): #se a lista dos espaços vazios for maior que a lista das posicoes ele vai substituir
                                asposicoes = listavazios.copy()
                                listavazios.clear() #limpa a lista dos espaços vazios, para a proxima verificação
                            else:
                                listavazios.clear()
                        if opcao == 2: # MELHOR ESCOLHA
                            asposicoes = listavazios.copy()
                            if len(asposicoes) == tamanho:
                                asposicoes = listavazios.copy() #se for igual ele vai alocar, e quebrar o 'for' direto pois ja achou o melhor espaco
                                break 
                            if len(asposicoes) > len(listavazios): #se a lista for menor do q a q ja esta ela salva na 'as posicoes'
                                asposicoes = listavazios.copy()
                                listavazios.clear() #limpa a lista dos espaços vazios, para a proxima verificação
                            else:
                                listavazios.clear()
                    else:
                        listavazios.clear()   
    for j in range(tamanho):
        memoria[asposicoes[j]] = letra
    finalizar(memoria, testememoria)
    
def finalizar(memoria, testememoria): #FINALIZAR ALGORITIMO
    #pega a memoria inicial e testa pra ver se teve alteração
    if memoria == testememoria:
        print("\nNão foi possível alocar a memória")
    else:
        print("\nMemória alocada com sucesso")
        return memoria #retorna a memoria

'''
memoria =  ['x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ']
opcao = 0
tamanho = 0
letra = ''	
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

def imprimememoria(): # IMPRIMIR MEMORIA
    for i in range(100):
        if i % 20 == 0:  # QUEBRA A CADA 20 POSIÇÕES
            print("\n")
        print(memoria[i], end='|')
        
def entradas(): # ENTRADA DE DADOS
    tamanho = int(input("Tamanho: "))
    letra = input("Letra: ")
    return tamanho, letra     

imprimememoria() # IMPRIME A MEMORIA

while True: # MENU
    print("\n\n1 - Primeira Escolha\n2 - Melhor Escolha\n3 - Pior Escolha\n4 - Imprimir Memória\n5 - Sair")
    opcao = int(input(("\nOq deseja fazer? ")))  # OPÇÃO DO MENU
    testememoria = memoria.copy()
    if opcao == 5:
        print("Saindo...")
        break
    else:
        if opcao == 4:
            imprimememoria()
        else:
            if opcao == 1:
                tamanho, letra = entradas()
                primeira_escolha(tamanho,letra, memoria, testememoria)
            if opcao == 3 or opcao == 2:
                tamanho, letra = entradas()
                pior_melhor_escolha(tamanho,letra, memoria, testememoria, opcao)
            #else:
                #print("Opção inválida")           