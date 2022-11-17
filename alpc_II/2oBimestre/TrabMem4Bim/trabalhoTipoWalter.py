

def primeira_escolha(tamanho,letra, memoria, testememoria): # PRIMEIRA ESCOLHA
    
    while i < 100:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        i += 1





































def finalizar(memoria, testememoria): #FINALIZAR ALGORITIMO
    if memoria == testememoria:
        print("\nNão foi possível alocar a memória")
    else:
        print("\nMemória alocada com sucesso")
        return memoria    


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


imprimememoria()
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
            else:
                print("Opção inválida")           