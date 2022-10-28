import random
from tracemalloc import start


'''def algoritimo(tamanho, letra, memoria, testememoria, opcao): #ALGORITIMO
    matrizmemoria = colocando_na_matriz(procurando_vazios(memoria))
    colocando_na_memoria(tamanho, memoria,achando_o_local(matrizmemoria,tamanho,opcao), letra, opcao)
    print(matrizmemoria)
    finalizar(memoria, testememoria)

def procurando_vazios(memoria): #PROCURANDO VAZIOS
    vazios = []
    for i in range(100): 
        if memoria[i] == ' ':
            vazios.append(i) 
    return vazios   

def colocando_na_matriz(vazios): #ALOCANDO VAZIOS NA MATRIZ
    matrizmemoria = [[]]
    cont = 0
    for j in range(1,len(vazios)):
        if j == len(vazios)-1:
            matrizmemoria[cont].append(vazios[j])
            break
        else:  
            if vazios[j-1] - vazios[j] == -1:
                matrizmemoria[cont].append(vazios[j-1])
            else:
                matrizmemoria[cont].append(vazios[j-1])
                if j != len(vazios):
                    matrizmemoria.append([])
                    cont += 1
    return matrizmemoria

def achando_o_local(matrizmemoria,tamanho,opcao): #ACHANDO O LOCAL PARA ARMAZENAR A MEMÓRIA
    achou = False
    for k in range(len(matrizmemoria)):
        if achou == False:
            if len(matrizmemoria[k]) >= tamanho:
                asposicoes = matrizmemoria[k]
                achou = True
                if opcao == 1: #PRIMEIRA ESCOLHA
                    return asposicoes
        else:
            if opcao == 3: #PIOR ESCOLHA
                if len(matrizmemoria[k]) >= tamanho:
                    if len(matrizmemoria[k]) > len(asposicoes):
                        asposicoes = matrizmemoria[k]
            else: #MELHOR ESCOLHA
                if len(matrizmemoria[k]) >= tamanho:
                    if len(matrizmemoria[k]) < len(asposicoes):
                        asposicoes = matrizmemoria[k]
    return asposicoes

def colocando_na_memoria(tamanho,memoria,asposicoes,letra,opcao): #COLOCANDO NA MEMÓRIA
    if opcao == 2: #MELHOR ESCOLHA
        for p in asposicoes:
            memoria[p] = letra
        return memoria
    else: #PRIMEIRA ESCOLHA E PIOR ESCOLHA
        for l in range(tamanho):
            memoria[asposicoes[l]] = letra
        return memoria'''
        
        
def primeira_escolha():
    

def finalizar(memoria, testememoria): #FINALIZAR ALGORITIMO
    if memoria == testememoria:
        print("\nNão foi possível alocar a memória")
    else:
        print("\nMemória alocada com sucesso")
        return memoria    

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
memoria =  ['x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ']
opcao = 0
tamanho = 0
letra = ''	

def imprimememoria(): # IMPRIMIR MEMORIA
    for i in range(100):
        if i % 20 == 0:  # QUEBRA A CADA 20 POSIÇÕES
            print("\n")
        print(memoria[i], end='|')
        
def entradas(): # ENTRADA DE DADOS
    tamanho = int(input("Tamanho: "))
    letra = input("Letra: ")
    return tamanho, letra     

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
            if opcao == 1 or opcao == 2 or opcao == 3:
                tamanho, letra = entradas()
                algoritimo(tamanho,letra, memoria, testememoria, opcao)
            else:
                print("Opção inválida")