import random
from tracemalloc import start
        
        
def primeira_escolha(tamanho,letra, memoria, testememoria): # PRIMEIRA ESCOLHA
    listavazios = []
    for i in range(100):
        if memoria[i] == ' ':
            if tamanho == 1:
                memoria[i] = letra
                return memoria # FINALIZA O ALGORITIMO PARA TAMANHO 1
            else:
                if i < 99: # VERIFICA SE O TAMANHO É SUFICIENTE
                    if memoria[i+1] == ' ':
                        if listavazios == []:
                            listavazios.append(i)
                        listavazios.append(i+1)
                    else:
                        listavazios.clear()
                if tamanho == len(listavazios):
                    for j in range(tamanho):
                        memoria[listavazios[j]] = letra
                    finalizar(memoria, testememoria)
                    return memoria # FINALIZA O ALGORITIMO PARA TAMANHO MAIOR QUE 1  
    finalizar(memoria, testememoria)


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


memoria =  ['x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', ' ']
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
            if opcao == 1:
                tamanho, letra = entradas()
                primeira_escolha(tamanho,letra, memoria, testememoria)
            else:
                print("Opção inválida")