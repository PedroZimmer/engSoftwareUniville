def abrirChamado():
    id_cracha = int(input("Digite o número do crachá: "))
    id_computador = int(input("Digite o número do computador: "))
    id_problema = int(input("Digite o código do problema: \n 1- Não liga\n 2- Lento\n 3- Sem internet\n"))
    return id_cracha, id_computador, id_problema

def colocarNaMatriz(matriz, id_cracha, id_computador, id_problema):
    matriz.append([id_cracha, id_computador, id_problema])
    return matriz

def fecharChamado(matriz, id_Fechar):
    for i in range(len(matriz)):
        if matriz[i][1] == id_Fechar:
            print("O chamado número", matriz[i][0], "foi fechado")
            matriz.pop(i)     
            return matriz
        
def listarChamados(matriz):
    if len(matriz) == 0:
        print("Não há chamados abertos")
    for lin in range(len(matriz)):
        print("Crachá: ", matriz[lin][0], "Computador: ", matriz[lin][1], "Problema: ", matriz[lin][2])

def gererEstatistica(qtd_chamados, qtd_fechados):
    emAberto = qtd_chamados - qtd_fechados
    perc = emAberto * 100 / qtd_chamados
    print("Percentual de chamados abertos: ", perc,"%")
       
qtd_fechados = 0
qtd_chamados = 0
matriz = []
while True: # MENU
    print("\nMENU\n1-Abrir chamado\n2-Fechar chamado\n3-Listar chamados abertos\n4-Gerar estatisticas dos chamados\n5-Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        if len(matriz) != 20:
            id_cracha, id_computador, id_problema = abrirChamado()
            matriz = colocarNaMatriz(matriz, id_cracha, id_computador, id_problema)
            qtd_chamados += 1
        else:
            print("Não é possível abrir mais chamados")
    if opcao == 2:
        id_Fechar = int(input("Qual chamado deseja fechar?"))
        fecharChamado(matriz, id_Fechar)
        qtd_fechados += 1
    if opcao == 3:
        listarChamados(matriz)
    if opcao == 4:
        gererEstatistica(qtd_chamados, qtd_fechados)
    if opcao == 5:
        print("Vlw professor, boas férias até uma próxima!")
        break