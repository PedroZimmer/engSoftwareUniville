import random
from tracemalloc import start

# PRIMEIRA ESCOLHA
'''
def primeiraescolha(tamanho, letra, memoria):
    print(tamanho, letra)
    cont = 0
    listavazio = []
    terminou = False
    while terminou == False:
        if cont != tamanho: #SE O CONTADOR FOR DIFERENTE DO TAMANHO
            for i in range(100):
                verificar = memoria[i] #COLOCA A POSIÇÃO DA MEMÓRIA EM UMA VARIAVEL
                if verificar == ' ':
                    cont+=1 #CONTA SE FOIR VAZIO
                    listavazio.append(i) #ADICIONA A POSIÇÃO DA MEMÓRIA LIVRE NA LISTA
                    if tamanho > 1: #SE O TAMANHO FOR MAIOR QUE 1 CONTINUA A PESQUISA
                        for j in range(1, tamanho):
                            if memoria[i+j] == ' ': #TEM Q VER ESSA INDEXAÇÃO!!!!!!!!!!!!
                                cont+=1
                                listavazio.append(i+1) #ADICIONA A POSIÇÃO DA MEMÓRIA LIVRE NA LIST

                    else:
                        memoria[i] = letra
                        terminou = True
        else:
            for i in listavazio:
                memoria[i] = letra #COLOCA A LETRA NA POSIÇÃO DA MEMÓRIA
                terminou = True
            pass
    return memoria
'''


def primeiraescolha(tamanho, letra, memoria):
    listadosvazios = []
    vazioscolados = []
    for i in range(100):
        if memoria[i] == ' ':
            listadosvazios.append(i)
    if tamanho == 1:
        memoria[listadosvazios[0]] = letra
        return memoria
    else:
        achou = False
        for j in range(len(listadosvazios)):
            if j == listadosvazios[-1]:
                break
            if listadosvazios[j] + 1 == listadosvazios[j+1]:
                if achou == False:
                    vazioscolados.append(listadosvazios[j])
                vazioscolados.append(listadosvazios[j+1])
                achou = True
            else:
                if len(vazioscolados) == 0:
                    achou = False
                    if len(vazioscolados) > tamanho:
                        vazioscolados = []
            if len(vazioscolados) == tamanho:
                for k in vazioscolados:
                    memoria[k] = letra
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
memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0, 11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '


# MENU
while(opcao != 5):
    print("\n1 - Primeira Escolha\n2 - Melhor Escolha\n3 - Pior Escolha\n4 - Imprimir Memória\n5 - Sair")
    opcao = int(input(("\nOq deseja fazer? ")))  # OPÇÃO DO MENU

    # IMPRIMIR A MEMÓRIA
    if(opcao == 4):
        imprimememoria()
    if opcao != 4 and opcao != 5:
        # PRIMEIRA ESCOLA
        if(opcao == 1):
            tamanho, letra = entradas()  # ENTRADA DE DADOS
            print("Memória antes da alocação: ", memoria)
            primeiraescolha(tamanho, letra, memoria)  # CHAMADA DA FUNÇÃO
            # print(resprimeiarescolha)
            pass
        else:
            # MELHOR ESCOLHA
            if (opcao == 2):
                pass
            else:
                if(opcao == 3):
                    pass
                else:
                    if(opcao == 5):
                        print("Saindo...")
                        pass
                    else:
                        print("Opcao invalida")
                        pass
